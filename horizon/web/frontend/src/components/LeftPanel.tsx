import { useMemo } from "react"
import { useApp } from "../App"
import { RunButton } from "./ControlsPanel"
import { Switch } from "@/components/ui/switch"
import { cn } from "@/lib/utils"

function SectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <span className="text-[10px] text-horizon-dim font-mono uppercase tracking-widest">{children}</span>
  )
}

function SourceRow({
  name,
  checked,
  disabled,
  onChange,
}: {
  name: string
  checked: boolean
  disabled: boolean
  onChange: (v: boolean) => void
}) {
  return (
    <button
      onClick={() => onChange(!checked)}
      disabled={disabled}
      className={cn(
        "w-full flex items-center gap-2 px-2 py-1 rounded-md transition-all duration-150 text-left",
        checked
          ? "text-horizon-text"
          : "text-horizon-muted hover:text-horizon-text"
      )}
    >
      <span className={cn(
        "flex-1 text-[11px] font-mono uppercase tracking-wider min-w-0 truncate",
        checked ? "text-horizon-text" : "text-horizon-muted"
      )}>
        {name}
      </span>
      <span className={cn(
        "w-[6px] h-[6px] rounded-full flex-shrink-0 transition-colors duration-150",
        checked ? "bg-horizon-signal" : "bg-horizon-dim"
      )} />
    </button>
  )
}

export function LeftPanel() {
  const { state, dispatch } = useApp()
  const isLoading = state.runState === "running"

  const plugins = state.config?.plugins ?? {}
  const sortedPlugins = useMemo(
    () => Object.entries(plugins).sort(([a], [b]) => a.localeCompare(b)),
    [plugins]
  )

  return (
    <div className="flex-shrink-0 w-56 border-r border-horizon-border bg-horizon-surface/20 flex flex-col overflow-hidden">
      <div className="flex-1 overflow-y-auto scrollbar-custom px-3 py-4 space-y-5">
        {/* Sources */}
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <SectionLabel>源</SectionLabel>
            <button
              className="text-[10px] text-horizon-signal/70 hover:text-horizon-signal transition-colors font-mono uppercase tracking-wider"
              disabled={isLoading}
              onClick={() => {
                const allEnabled: Record<string, boolean> = {}
                for (const [k] of sortedPlugins) allEnabled[k] = true
                dispatch({ type: "SET_CONTROL", key: "enabledSources", value: allEnabled })
              }}
            >全选</button>
            <span className="text-[10px] text-horizon-dim font-mono">/</span>
            <button
              className="text-[10px] text-horizon-signal/70 hover:text-horizon-signal transition-colors font-mono uppercase tracking-wider"
              disabled={isLoading}
              onClick={() => {
                const inverted: Record<string, boolean> = {}
                for (const [k] of sortedPlugins) inverted[k] = !(state.enabledSources[k] ?? true)
                dispatch({ type: "SET_CONTROL", key: "enabledSources", value: inverted })
              }}
            >反选</button>
          </div>
          <div className="space-y-0.5">
            {sortedPlugins.map(([key, plugin]) => (
              <SourceRow
                key={key}
                name={plugin.name ?? key}
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

        {/* Controls */}
        <div className="space-y-3">
          {/* Time */}
          <div className="flex items-center gap-2">
            <SectionLabel>时段</SectionLabel>
            <select
              className="flex-1 h-7 rounded-md border border-horizon-border bg-horizon-surface px-2 text-xs text-horizon-text focus:outline-none focus:ring-2 focus:ring-horizon-signal/30 font-mono cursor-pointer"
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

          {/* AI */}
          <div className="flex items-center gap-2">
            <SectionLabel>智能</SectionLabel>
            <Switch
              checked={state.useAi}
              onCheckedChange={(v) => dispatch({ type: "SET_CONTROL", key: "useAi", value: v })}
              disabled={isLoading}
              className="scale-75 origin-left"
            />
            {state.useAi && (
              <select
                className="flex-1 h-7 rounded-md border border-horizon-border bg-horizon-surface px-2 text-xs text-horizon-text focus:outline-none focus:ring-2 focus:ring-horizon-signal/30 font-mono cursor-pointer"
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

          {/* Profile */}
          <div className="flex items-center gap-2">
            <SectionLabel>配置</SectionLabel>
            <select
              className="flex-1 h-7 rounded-md border border-horizon-border bg-horizon-surface px-2 text-xs text-horizon-text focus:outline-none focus:ring-2 focus:ring-horizon-signal/30 font-mono cursor-pointer"
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
      </div>

      {/* Run button at bottom */}
      <div className="flex-shrink-0 border-t border-horizon-border px-3 py-3">
        <RunButton className="w-full justify-center" />
      </div>
    </div>
  )
}
