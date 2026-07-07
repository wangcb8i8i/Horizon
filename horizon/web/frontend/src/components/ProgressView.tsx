import { useState, useMemo, useRef, useEffect } from "react"
import { useApp } from "../App"
import { useSSE } from "../hooks/useSSE"
import { useSounds } from "@/hooks/useSounds"
import { cn } from "@/lib/utils"
import type { PluginStatus } from "../types"

function PluginStatusDot({ status }: { status: PluginStatus; isCurrent?: boolean }) {
  if (status === "done") {
    return (
      <div className="w-4 h-4 rounded-full bg-horizon-signal-soft border border-horizon-signal-line flex items-center justify-center flex-shrink-0">
        <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#D4875A" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
          <polyline points="20 6 9 17 4 12" />
        </svg>
      </div>
    )
  }
  if (status === "error") {
    return (
      <div className="w-4 h-4 rounded-full bg-red-500/15 border border-red-500/30 flex items-center justify-center flex-shrink-0">
        <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#f87171" strokeWidth="3" strokeLinecap="round">
          <line x1="18" y1="6" x2="6" y2="18" />
          <line x1="6" y1="6" x2="18" y2="18" />
        </svg>
      </div>
    )
  }
  if (status === "running") {
    return (
      <div className="w-4 h-4 rounded-full border border-horizon-signal flex items-center justify-center flex-shrink-0">
        <div className="w-1.5 h-1.5 rounded-full bg-horizon-signal animate-pulse" />
      </div>
    )
  }
  return (
    <div className="w-4 h-4 rounded-full border border-horizon-border flex items-center justify-center flex-shrink-0">
      <div className="w-1 h-1 rounded-full bg-horizon-dim" />
    </div>
  )
}

function PluginRow({
  name,
  status,
  count,
  isCurrent,
  isLast,
}: {
  name: string
  status: PluginStatus
  count?: number
  isCurrent: boolean
  isLast: boolean
}) {
  return (
    <div className="flex gap-3">
      <div className="flex flex-col items-center w-4 flex-shrink-0">
        <PluginStatusDot status={status} isCurrent={isCurrent} />
        {!isLast && <div className="w-px flex-1 bg-horizon-border/50 mt-1" />}
      </div>
      <div className={cn(
        "flex-1 flex items-center gap-2 pb-4 min-w-0",
        status === "done" && "animate-fade-away"
      )}>
        <span className={cn(
          "text-sm flex-1 min-w-0 truncate font-body",
          isCurrent ? "text-horizon-text font-medium" :
          status === "done" ? "text-horizon-muted" :
          status === "error" ? "text-red-300" :
          "text-horizon-dim"
        )}>
          {name}
        </span>
        {status === "done" && count !== undefined && (
          <span className="text-xs text-horizon-dim font-mono tabular-nums flex-shrink-0">{count} 条</span>
        )}
        {status === "error" && (
          <span className="text-xs text-red-400 font-mono flex-shrink-0">失败</span>
        )}
        {status === "running" && (
          <span className="status-label text-horizon-signal flex-shrink-0 animate-pulse">扫描中</span>
        )}
        {isCurrent && (
          <span className="w-1 h-1 rounded-full bg-horizon-signal animate-signal-pulse flex-shrink-0" />
        )}
      </div>
    </div>
  )
}

export function ProgressView() {
  const { state, dispatch } = useApp()
  const [expanded, setExpanded] = useState(false)
  const { playItem, playDone, playError } = useSounds()
  const runIdRef = useRef(state.runId)
  runIdRef.current = state.runId
  const doneRef = useRef(false)

  const [itemFlash, setItemFlash] = useState(false)
  const prevItemCountRef = useRef(0)
  const liveCount = state.progress.liveItems.length

  useEffect(() => {
    if (liveCount > prevItemCountRef.current) {
      setItemFlash(true)
      const t = setTimeout(() => setItemFlash(false), 500)
      prevItemCountRef.current = liveCount
      return () => clearTimeout(t)
    }
  }, [liveCount])

  useSSE(
    state.runId && state.runId !== "__connecting__" ? `/api/run/${state.runId}/sse` : null,
    {
      "run:start": () => {
        dispatch({ type: "SET_AI_PHASE", active: false })
      },
      "item": (d) => {
        playItem()
        dispatch({
          type: "ITEM_ARRIVED",
          item: {
            title: (d.title as string) ?? "",
            url: (d.url as string) ?? "",
            source_type: (d.source_type as string) ?? "",
            source_name: (d.plugin as string) ?? "",
            published_at: (d.timestamp as string) ?? undefined,
          },
        })
      },
      "plugin:start": (d) => {
        const plugin = d.plugin as string
        dispatch({ type: "SET_PLUGIN_STATUS", plugin, status: "running" })
        dispatch({ type: "SET_CURRENT_PLUGIN", plugin })
      },
      "plugin:done": (d) => {
        const plugin = d.plugin as string
        const count = (d.count as number) ?? 0
        dispatch({ type: "SET_PLUGIN_STATUS", plugin, status: "done", count })
        dispatch({ type: "SET_CURRENT_PLUGIN", plugin: null })
      },
      "plugin:error": (d) => {
        const plugin = d.plugin as string
        const error = (d.error as string) ?? "Unknown error"
        dispatch({ type: "SET_PLUGIN_STATUS", plugin, status: "error", error })
        dispatch({ type: "SET_CURRENT_PLUGIN", plugin: null })
      },
      "ai:start": () => {
        dispatch({ type: "SET_AI_PHASE", active: true })
      },
      "ai:done": () => {
        dispatch({ type: "SET_AI_PHASE", active: false })
      },
      "run:done": () => {
        doneRef.current = true
        playDone()
        dispatch({ type: "RUN_COMPLETED" })
        const rid = runIdRef.current
        fetch(`/api/run/${rid}/results`)
          .then((r) => r.json())
          .then((data) => dispatch({ type: "SET_RESULTS", results: Array.isArray(data) ? data : [] }))
          .catch(() => {})
        fetch("/api/history")
          .then((r) => r.json())
          .then((data) => dispatch({ type: "SET_HISTORY", history: Array.isArray(data) ? data : [] }))
          .catch(() => {})
      },
      error: () => {
        if (!doneRef.current) {
          dispatch({ type: "SET_ERROR", error: "Connection lost" })
        }
      },
    }
  )

  const { plugins, pluginNames, statuses, counts, current, aiPhase, aiDone } = state.progress
  const isConnecting = state.runId === "__connecting__"

  const completedCount = useMemo(
    () => plugins.filter((p) => statuses[p] === "done" || statuses[p] === "error").length,
    [plugins, statuses]
  )
  const total = plugins.length
  const percent = total > 0 ? Math.round((completedCount / total) * 100) : 0

  const isRunning = state.runState === "running"
  const isDone = state.runState === "done"
  const hasError = plugins.some((p) => statuses[p] === "error")
  const currentName = current ? (pluginNames[current] ?? current) : null

  const statusText = isConnecting ? "连接中..." :
    isRunning && currentName ? `扫描 ${currentName}` :
    isRunning ? "扫描中..." :
    isDone && hasError ? `扫描完成 (${completedCount}/${total})` :
    isDone ? "扫描完成" : ""

  return (
    <>
      {/* Status bar */}
      <div
        className={cn("flex-shrink-0 border-b cursor-pointer px-4 py-2 transition-colors", isRunning ? "border-b-horizon-signal/15 animate-spectrum-bar-glow" : "border-b-horizon-border hover:bg-horizon-surface/30")}
        onClick={() => setExpanded(!expanded)}
      >
        <div className="flex items-center gap-3">
          {isRunning ? (
            <div className="w-2 h-2 rounded-full bg-horizon-signal animate-signal-pulse flex-shrink-0" />
          ) : isDone ? (
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D4875A" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" className="flex-shrink-0">
              <polyline points="20 6 9 17 4 12" />
            </svg>
          ) : null}

          <span className="text-sm font-medium text-horizon-text font-body flex-1 min-w-0 truncate">
            {statusText}
          </span>

          <span className="text-xs text-horizon-muted font-mono tabular-nums flex-shrink-0">
            {completedCount}/{total}
          </span>

          <span className="text-xs text-horizon-muted font-mono flex-shrink-0">
              items: {liveCount}
            </span>

          <div className={cn("spectrum-bar w-24 flex-shrink-0", isRunning && "animate-spectrum-bar-glow", itemFlash && "animate-spectrum-flash")}>
            <div
              className="spectrum-bar-fill"
              style={{ width: `${percent}%` }}
            />
            {isRunning && (
              <div className="absolute inset-0 overflow-hidden rounded-[2px]">
                <div
                  className="absolute inset-y-0 w-20 animate-spectrum-scan rounded-[2px]"
                  style={{
                    background: "linear-gradient(90deg, transparent 0%, rgba(212,135,90,0.35) 30%, rgba(212,135,90,0.6) 50%, rgba(212,135,90,0.35) 70%, transparent 100%)",
                  }}
                />
              </div>
            )}
          </div>

          <svg
            className={cn(
              "w-3 h-3 text-horizon-muted transition-transform flex-shrink-0",
              expanded && "rotate-180"
            )}
            viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"
          >
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </div>
      </div>

      {/* Expanded Source Chain */}
      {expanded && (
        <div className="flex-shrink-0 border-b border-horizon-border bg-horizon-surface/30 px-6 py-4 max-h-80 overflow-y-auto">
          <div className="max-w-md">
            {plugins.map((pluginKey, i) => {
              const status = statuses[pluginKey] ?? "pending"
              const isCurrentPlugin = pluginKey === current && status === "running"
              return (
                <PluginRow
                  key={pluginKey}
                  name={pluginNames[pluginKey] ?? pluginKey}
                  status={status}
                  count={counts[pluginKey]}
                  isCurrent={isCurrentPlugin}
                  isLast={i === plugins.length - 1 && !aiPhase && !aiDone}
                />
              )
            })}

            {(state.config?.scorers?.length ?? 0) > 0 && (
              <div className="flex gap-3">
                <div className="flex flex-col items-center w-4 flex-shrink-0">
                  {aiDone ? (
                    <div className="w-4 h-4 rounded-full bg-horizon-echo-soft border border-horizon-echo-line flex items-center justify-center flex-shrink-0">
                      <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#3D7A8E" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                    </div>
                  ) : aiPhase ? (
                    <div className="w-4 h-4 rounded-full border border-horizon-echo flex items-center justify-center flex-shrink-0">
                      <div className="w-1.5 h-1.5 rounded-full bg-horizon-echo animate-pulse" />
                    </div>
                  ) : (
                    <div className="w-4 h-4 rounded-full border border-horizon-border flex items-center justify-center flex-shrink-0">
                      <div className="w-1 h-1 rounded-full bg-horizon-dim" />
                    </div>
                  )}
                </div>
                <div className={cn(
                  "flex-1 flex items-center gap-2 pb-4 min-w-0",
                  aiDone && "animate-fade-away"
                )}>
                  <span className={cn(
                    "text-sm flex-1 min-w-0 truncate font-body",
                    aiPhase ? "text-horizon-text font-medium" :
                    aiDone ? "text-horizon-muted" : "text-horizon-dim"
                  )}>
                    AI 过滤
                  </span>
                  {aiPhase && (
                    <span className="status-label text-horizon-echo animate-pulse flex-shrink-0">评分中</span>
                  )}
                  {aiDone && (
                    <span className="text-xs text-horizon-dim font-mono flex-shrink-0">完成</span>
                  )}
                  {aiPhase && (
                    <span className="w-1 h-1 rounded-full bg-horizon-echo animate-signal-pulse flex-shrink-0" />
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Error banner */}
      {state.error && (
        <div className="flex-shrink-0 border-b border-red-500/20 bg-red-500/5 px-4 py-2 text-xs text-red-300/80 font-mono">
          {state.error}
        </div>
      )}
    </>
  )
}
