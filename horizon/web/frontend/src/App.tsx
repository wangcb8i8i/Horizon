import { useReducer, createContext, useContext, useEffect, useCallback } from "react"
import type { AppState, AppAction, ContentItem, PluginStatus } from "./types"
import { TopBar } from "./components/TopBar"
import { LeftPanel } from "./components/LeftPanel"
import { MainView } from "./components/MainView"

const initialProgress = {
  plugins: [],
  pluginNames: {},
  statuses: {},
  counts: {},
  errors: {},
  current: null,
  aiPhase: false,
  aiDone: false,
  liveItems: [] as ContentItem[],
}

const initialState: AppState = {
  config: null,
  runState: "idle",
  runId: null,
  progress: initialProgress,
  results: null,
  error: null,
  sidebarTab: "run",
  history: [],
  currentHistoryId: null,
  historyResults: null,
  since: "24h",
  enabledSources: {},
  useAi: false,
  scorer: "default",
  threshold: 5,
  profile: "",
}

function reducer(state: AppState, action: AppAction): AppState {
  switch (action.type) {
    case "SET_CONFIG":
      return {
        ...state,
        config: action.config,
        enabledSources: Object.fromEntries(
          Object.entries(action.config.plugins).map(([k]) => [k, true])
        ),
      }
    case "START_RUN": {
      const statuses: Record<string, PluginStatus> = {}
      for (const p of action.plugins) statuses[p] = "pending"
      return {
        ...state,
        runState: "running",
        runId: action.runId,
        results: null,
        error: null,
        progress: {
          plugins: action.plugins,
          pluginNames: action.pluginNames,
          statuses,
          counts: {},
          errors: {},
          current: null,
          aiPhase: false,
          aiDone: false,
          liveItems: [],
        },
      }
    }
    case "SET_RUN_STATE":
      return { ...state, runState: action.runState }
    case "SET_PLUGIN_STATUS": {
      const statuses = { ...state.progress.statuses, [action.plugin]: action.status }
      const counts = { ...state.progress.counts }
      const errors = { ...state.progress.errors }
      if (action.count !== undefined) counts[action.plugin] = action.count
      if (action.error !== undefined) {
        errors[action.plugin] = action.error
      } else if (action.status !== "error") {
        delete errors[action.plugin]
      }
      return {
        ...state,
        progress: { ...state.progress, statuses, counts, errors },
      }
    }
    case "SET_CURRENT_PLUGIN":
      return { ...state, progress: { ...state.progress, current: action.plugin } }
    case "SET_AI_PHASE":
      return { ...state, progress: { ...state.progress, aiPhase: action.active } }
    case "RUN_COMPLETED":
      return { ...state, progress: { ...state.progress, aiDone: true }, runState: "done" }
    case "SET_RESULTS":
      return { ...state, results: action.results }
    case "SET_ERROR":
      return { ...state, error: action.error, runState: "error" }
    case "SET_SIDEBAR_TAB":
      return { ...state, sidebarTab: action.sidebarTab }
    case "SET_HISTORY":
      return { ...state, history: action.history }
    case "SET_CURRENT_HISTORY_ID":
      return { ...state, currentHistoryId: action.currentHistoryId }
    case "SET_HISTORY_RESULTS":
      return { ...state, historyResults: action.historyResults }
    case "SET_CONTROL":
      return { ...state, [action.key]: action.value }
    case "ITEM_ARRIVED":
      return {
        ...state,
        progress: {
          ...state.progress,
          liveItems: [...state.progress.liveItems, action.item],
        },
      }
    case "RESET":
      return { ...initialState, config: state.config, history: state.history }
    default:
      return state
  }
}

interface AppContextValue {
  state: AppState
  dispatch: React.Dispatch<AppAction>
  startRun: () => Promise<void>
}

export const AppContext = createContext<AppContextValue | null>(null)
export const useApp = () => useContext(AppContext)!

export default function App() {
  const [state, dispatch] = useReducer(reducer, initialState)

  // Fetch config on mount
  useEffect(() => {
    fetch("/api/config")
      .then((r) => r.json())
      .then((config) => dispatch({ type: "SET_CONFIG", config }))
      .catch(() => {})
    fetch("/api/history")
      .then(async (r) => {
        const data = await r.json()
        const history = Array.isArray(data) ? data : []
        dispatch({ type: "SET_HISTORY", history })
        if (history.length > 0) {
          try {
            const res = await fetch(`/api/history/${history[0].run_id}`)
            if (res.ok) {
              const results = await res.json()
              if (Array.isArray(results) && results.length > 0) {
                dispatch({ type: "SET_RESULTS", results })
              }
            }
          } catch {}
        }
      })
      .catch(() => {})
  }, [])

  const startRun = useCallback(async () => {
    console.log("[startRun] beginning, runState=", state.runState)
    dispatch({ type: "SET_ERROR", error: "" })

    // Determine which plugins to run
    const allPlugins = state.config?.plugins ?? {}
    const enabledEntries = Object.entries(state.enabledSources).filter(([, v]) => v)
    // If all enabled, just use the config order; otherwise use explicitly enabled
    const pluginKeys =
      enabledEntries.length === Object.keys(allPlugins).length
        ? Object.keys(allPlugins)
        : enabledEntries.map(([k]) => k)
    console.log("[startRun] plugins=", pluginKeys)

    const pluginNames: Record<string, string> = {}
    for (const k of pluginKeys) {
      pluginNames[k] = allPlugins[k]?.name ?? k
    }

    dispatch({
      type: "START_RUN",
      plugins: pluginKeys,
      pluginNames,
      runId: "__connecting__",
    })

    try {
      const body: Record<string, unknown> = { since: state.since }

      if (enabledEntries.length > 0 && enabledEntries.length < Object.keys(allPlugins).length) {
        body.sources = pluginKeys
      }

      if (state.useAi) {
        body.ai = true
        if (state.scorer) body.scorer = state.scorer
        // threshold is read from horizon.yaml config (keep_pct)
      }
      if (state.profile) body.profile = state.profile
      const res = await fetch("/api/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      })

      if (!res.ok) {
        const err = await res.text()
        dispatch({ type: "SET_ERROR", error: err })
        return
      }

      const { run_id } = await res.json()
      dispatch({ type: "START_RUN", plugins: pluginKeys, pluginNames, runId: run_id })

      // SSE in ProgressView handles the rest
    } catch (e) {
      dispatch({
        type: "SET_ERROR",
        error: e instanceof Error ? e.message : "Failed to start run",
      })
    }
  }, [state.since, state.enabledSources, state.useAi, state.scorer, state.profile, state.config])

  return (
    <AppContext.Provider value={{ state, dispatch, startRun }}>
      <div className="h-screen w-screen flex flex-col overflow-hidden" style={{ background: "#0B0B0E" }}>
        <TopBar />
        <div className="flex-1 flex overflow-hidden">
          {state.sidebarTab === "run" && <LeftPanel />}
          <MainView />
        </div>
      </div>
    </AppContext.Provider>
  )
}
