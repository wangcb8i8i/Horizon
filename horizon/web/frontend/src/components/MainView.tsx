import { useApp } from "../App"
import { EmptyView } from "./EmptyView"
import { ProgressView } from "./ProgressView"
import ResultsView from "./ResultsView"
import { HistoryPanel } from "./HistoryPanel"

function HistoryBackButton() {
  const { dispatch } = useApp()
  return (
    <button
      onClick={() => {
        dispatch({ type: "SET_CURRENT_HISTORY_ID", currentHistoryId: null })
        dispatch({ type: "SET_HISTORY_RESULTS", historyResults: null })
      }}
      className="text-xs text-horizon-signal hover:text-horizon-signal/80 transition-colors mb-3 inline-flex items-center gap-1 font-mono"
    >
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
        <line x1="19" y1="12" x2="5" y2="12" />
        <polyline points="12 19 5 12 12 5" />
      </svg>
      back to list
    </button>
  )
}

export function MainView() {
  const { state } = useApp()

  const isHistoryTab = state.sidebarTab === "history"
  const showProgress = state.runState === "running" || (state.runState === "done" && state.results === null && state.progress.plugins.length > 0)
  const showEmpty = state.runState === "idle" && !isHistoryTab && state.results === null

  const showFeed = !isHistoryTab && (state.runState === "running" || state.runState === "done" || state.results !== null)
  const feedItems = state.results ?? state.progress.liveItems
  const isLive = state.runState === "running"

  return (
    <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
      {/* Progress/status bar */}
      {showProgress && <ProgressView />}

      {/* Error banner */}
      {state.error && !showProgress && (
        <div className="flex-shrink-0 border-b border-red-500/20 bg-red-500/5 px-4 py-2 text-xs text-red-300/80 font-mono">
          {state.error}
        </div>
      )}

      {/* Main content */}
      <div className="flex-1 overflow-y-auto scrollbar-none">
        {!isHistoryTab && showEmpty && <EmptyView />}

        {showFeed && (
          <ResultsView items={feedItems} live={isLive} sidebarLeft={224} />
        )}

        {/* History mode */}
        {isHistoryTab && !state.currentHistoryId && (
          <HistoryPanel />
        )}
        {isHistoryTab && state.currentHistoryId && state.historyResults && (
          <div className="h-full">
            <div className="sticky top-0 z-10 bg-horizon-bg px-4 pt-6 pb-2">
              <HistoryBackButton />
            </div>
            <div className="px-4">
              <ResultsView items={state.historyResults} sidebarLeft={0} />
            </div>
          </div>
        )}
        {isHistoryTab && state.currentHistoryId && !state.historyResults && (
          <div className="h-full flex items-center justify-center">
            <p className="text-sm text-horizon-dim font-mono">Loading…</p>
          </div>
        )}
      </div>
    </div>
  )
}
