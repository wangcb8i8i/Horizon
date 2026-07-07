import { useApp } from "../App"
import { cn } from "@/lib/utils"

export function TopBar() {
  const { state, dispatch } = useApp()

  return (
    <div className="flex-shrink-0 border-b border-horizon-border">
      <div className="flex items-center gap-3 px-4 h-11">
        <div className="flex items-center gap-2 flex-shrink-0">
          <span className="font-display font-semibold text-sm tracking-tight text-horizon-text">
            Horizon
          </span>
        </div>

        <div className="flex items-center gap-0.5 bg-horizon-surface rounded-lg p-0.5">
          <button
            onClick={() => dispatch({ type: "SET_SIDEBAR_TAB", sidebarTab: "run" })}
            className={cn(
              "px-3 py-1 text-xs font-medium rounded-md transition-all duration-200",
              state.sidebarTab === "run"
                ? "bg-horizon-card text-horizon-text"
                : "text-horizon-muted hover:text-horizon-text"
            )}
          >
            Run
          </button>
          <button
            onClick={() => {
              dispatch({ type: "SET_SIDEBAR_TAB", sidebarTab: "history" })
              if (state.sidebarTab !== "history") {
                fetch("/api/history")
                  .then((r) => r.json())
                  .then((data) => dispatch({ type: "SET_HISTORY", history: Array.isArray(data) ? data : [] }))
                  .catch(() => {})
              }
            }}
            className={cn(
              "px-3 py-1 text-xs font-medium rounded-md transition-all duration-200",
              state.sidebarTab === "history"
                ? "bg-horizon-card text-horizon-text"
                : "text-horizon-muted hover:text-horizon-text"
            )}
          >
            History
          </button>
        </div>

        <div className="flex-1" />
      </div>
    </div>
  )
}
