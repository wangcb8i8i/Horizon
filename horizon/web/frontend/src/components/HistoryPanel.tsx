import { useEffect } from "react"
import { useApp } from "../App"
import { cn } from "@/lib/utils"

export function HistoryPanel() {
  const { state, dispatch } = useApp()

  useEffect(() => {
    fetch("/api/history")
      .then((r) => r.json())
      .then((data) => dispatch({ type: "SET_HISTORY", history: Array.isArray(data) ? data : [] }))
      .catch(() => {})
  }, [state.runState])

  const selectHistory = async (runId: string) => {
    dispatch({ type: "SET_CURRENT_HISTORY_ID", currentHistoryId: runId })
    try {
      const res = await fetch(`/api/history/${runId}`)
      if (!res.ok) throw new Error("Failed to load")
      const data = await res.json()
      dispatch({ type: "SET_HISTORY_RESULTS", historyResults: Array.isArray(data) ? data : null })
    } catch {
      dispatch({ type: "SET_HISTORY_RESULTS", historyResults: null })
    }
  }

  return (
    <div className="space-y-1 px-4 py-6 max-w-md mx-auto">
      <p className="text-xs text-horizon-muted px-1 pb-3 font-mono uppercase tracking-wider">
        Recent runs
      </p>
      {state.history.length === 0 ? (
        <p className="text-sm text-horizon-dim px-1 font-body">No runs yet</p>
      ) : (
        state.history.map((entry) => (
          <button
            key={entry.run_id}
            onClick={() => selectHistory(entry.run_id)}
            className={cn(
              "w-full text-left px-3 py-2.5 rounded-lg transition-all duration-150 border",
              state.currentHistoryId === entry.run_id
                ? "bg-horizon-card border-horizon-border"
                : "hover:bg-horizon-surface/50 border-transparent"
            )}
          >
            <div className="flex items-center justify-between">
              <span className="text-sm text-horizon-text font-body">
                {formatTimestamp(entry.timestamp)}
              </span>
              <span className="text-xs text-horizon-muted font-mono tabular-nums">{entry.item_count} items</span>
            </div>
            {entry.has_ai && (
              <span className="text-xs text-horizon-echo font-mono mt-1 block">ai filtered</span>
            )}
          </button>
        ))
      )}
    </div>
  )
}

function formatTimestamp(ts: string) {
  try {
    const d = new Date(ts)
    const month = (d.getMonth() + 1).toString().padStart(2, "0")
    const day = d.getDate().toString().padStart(2, "0")
    const hours = d.getHours().toString().padStart(2, "0")
    const mins = d.getMinutes().toString().padStart(2, "0")
    return `${month}-${day} ${hours}:${mins}`
  } catch {
    return ts
  }
}
