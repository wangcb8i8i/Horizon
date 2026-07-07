import { useMemo } from "react"
import { useApp } from "../App"
import { Button } from "@/components/ui/button"
import { Switch } from "@/components/ui/switch"
import { cn } from "@/lib/utils"
import { useSounds } from "@/hooks/useSounds"

export function SourcePill({
  label,
  checked,
  disabled,
  onChange,
}: {
  label: string
  checked: boolean
  disabled: boolean
  onChange: (v: boolean) => void
}) {
  return (
    <button
      onClick={() => onChange(!checked)}
      disabled={disabled}
      className={cn(
        "text-[11px] leading-none px-2 py-1 rounded-md border transition-all duration-150 whitespace-nowrap font-mono uppercase tracking-wider",
        checked
          ? "bg-horizon-signal-soft border-horizon-signal-line text-horizon-signal"
          : "bg-transparent border-horizon-border text-horizon-muted hover:text-horizon-text hover:border-horizon-dim"
      )}
    >
      {label}
    </button>
  )
}

export function RunButton({ className }: { className?: string }) {
  const { state, startRun } = useApp()
  const { playRun } = useSounds()
  const isLoading = state.runState === "running"

  const handleRun = () => {
    console.log("[RunButton] clicked, isLoading=", isLoading)
    playRun()
    startRun()
  }

  return (
    <Button
      onClick={handleRun}
      disabled={isLoading}
      size="sm"
      className={cn("h-7 px-4 text-xs font-semibold", className)}
    >
      {isLoading ? (
        <span className="flex items-center gap-1.5">
          <svg className="w-3 h-3 animate-spin" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3" opacity="0.25" />
            <path d="M12 2a10 10 0 0 1 10 10" stroke="currentColor" strokeWidth="3" strokeLinecap="round" />
          </svg>
          扫描中
        </span>
      ) : (
        "扫描"
      )}
    </Button>
  )
}

export function ControlsPanel() {
  const { state, dispatch } = useApp()
  const isLoading = state.runState === "running"

  const plugins = state.config?.plugins ?? {}
  const sortedPlugins = useMemo(
    () => Object.entries(plugins).sort(([a], [b]) => a.localeCompare(b)),
    [plugins]
  )

  return (
    <div className="flex items-center gap-4 flex-wrap">
      {/* Sources */}
      <div className="flex items-center gap-1.5">
        <span className="text-[11px] text-horizon-muted font-mono uppercase tracking-wider flex-shrink-0">
          源
        </span>
        <button
          className="text-[10px] text-horizon-signal/70 hover:text-horizon-signal transition-colors font-mono uppercase tracking-wider"
          disabled={isLoading}
          onClick={() => {
            const allEnabled: Record<string, boolean> = {}
            for (const [k] of sortedPlugins) allEnabled[k] = true
            dispatch({ type: "SET_CONTROL", key: "enabledSources", value: allEnabled })
          }}
        >
          all
        </button>
        <span className="text-[10px] text-horizon-dim font-mono">/</span>
        <button
          className="text-[10px] text-horizon-signal/70 hover:text-horizon-signal transition-colors font-mono uppercase tracking-wider"
          disabled={isLoading}
          onClick={() => {
            const inverted: Record<string, boolean> = {}
            for (const [k] of sortedPlugins) inverted[k] = !(state.enabledSources[k] ?? true)
            dispatch({ type: "SET_CONTROL", key: "enabledSources", value: inverted })
          }}
        >
          inv
        </button>
        <div className="flex gap-1 flex-wrap">
          {sortedPlugins.map(([key, plugin]) => (
            <SourcePill
              key={key}
              label={plugin.name ?? key}
              checked={state.enabledSources[key] ?? true}
              disabled={isLoading}
              onChange={(v) =>
                dispatch({
                  type: "SET_CONTROL",
                  key: "enabledSources",
                  value: { ...state.enabledSources, [key]: v },
                })
              }
            />
          ))}
        </div>
      </div>

      <div className="h-4 w-px bg-horizon-border flex-shrink-0" />

      {/* Time */}
      <div className="flex items-center gap-1.5">
        <span className="text-[11px] text-horizon-muted font-mono uppercase tracking-wider">time</span>
        <select
          className="h-7 rounded-md border border-horizon-border bg-horizon-surface px-2 text-xs text-horizon-text focus:outline-none focus:ring-2 focus:ring-horizon-signal/30 font-mono cursor-pointer"
          value={state.since}
          onChange={(e) => dispatch({ type: "SET_CONTROL", key: "since", value: e.target.value })}
          disabled={isLoading}
        >
          <option value="1h">1h</option>
          <option value="6h">6h</option>
          <option value="24h">24h</option>
          <option value="7d">7d</option>
          <option value="14d">14d</option>
          <option value="30d">30d</option>
        </select>
      </div>

      <div className="h-4 w-px bg-horizon-border flex-shrink-0" />

      {/* AI */}
      <div className="flex items-center gap-1.5">
        <span className="text-[11px] text-horizon-muted font-mono uppercase tracking-wider">ai</span>
        <Switch
          checked={state.useAi}
          onCheckedChange={(v) => dispatch({ type: "SET_CONTROL", key: "useAi", value: v })}
          disabled={isLoading}
          className="scale-75 origin-left"
        />
        {state.useAi && (
          <select
            className="h-7 rounded-md border border-horizon-border bg-horizon-surface px-2 text-xs text-horizon-text focus:outline-none focus:ring-2 focus:ring-horizon-signal/30 font-mono cursor-pointer"
            value={state.scorer}
            onChange={(e) => dispatch({ type: "SET_CONTROL", key: "scorer", value: e.target.value })}
            disabled={isLoading}
          >
            {(state.config?.scorers ?? []).map((s) => (
              <option key={s} value={s}>{s}</option>
            ))}
          </select>
        )}
      </div>

      <div className="h-4 w-px bg-horizon-border flex-shrink-0" />

      {/* Profile */}
      <div className="flex items-center gap-1.5">
        <span className="text-[11px] text-horizon-muted font-mono uppercase tracking-wider">cfg</span>
        <select
          className="h-7 rounded-md border border-horizon-border bg-horizon-surface px-2 text-xs text-horizon-text focus:outline-none focus:ring-2 focus:ring-horizon-signal/30 font-mono cursor-pointer"
          value={state.profile}
          onChange={(e) => dispatch({ type: "SET_CONTROL", key: "profile", value: e.target.value })}
          disabled={isLoading}
        >
          <option value="">default</option>
          {Object.keys(state.config?.profiles ?? {}).map((p) => (
            <option key={p} value={p}>{p}</option>
          ))}
        </select>
      </div>
    </div>
  )
}
