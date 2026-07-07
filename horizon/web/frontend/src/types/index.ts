export interface ContentItem {
  id?: string
  title: string
  content?: string
  ai_summary?: string
  ai_score?: number
  url?: string
  source_type: string
  source_name: string
  published_at?: string
  author?: string
  metadata?: {
    score?: number
    descendants?: number
    discussion_url?: string
  }
}

export interface HistoryEntry {
  run_id: string
  timestamp: string
  item_count: number
  has_ai: boolean
}

export interface AppConfig {
  plugins: Record<string, { name: string; enabled: boolean }>
  profiles: Record<string, string[]>
  scorers: string[]
}

export type RunState = "idle" | "running" | "done" | "error"

export type PluginStatus = "pending" | "running" | "done" | "error"

export interface ProgressState {
  plugins: string[]
  pluginNames: Record<string, string>
  statuses: Record<string, PluginStatus>
  counts: Record<string, number>
  errors: Record<string, string>
  current: string | null
  aiPhase: boolean
  aiDone: boolean
  liveItems: ContentItem[]
}

export interface AppState {
  config: AppConfig | null
  runState: RunState
  runId: string | null
  progress: ProgressState
  results: ContentItem[] | null
  error: string | null
  sidebarTab: "run" | "history"
  history: HistoryEntry[]
  currentHistoryId: string | null
  historyResults: ContentItem[] | null
  // controls
  since: string
  enabledSources: Record<string, boolean>
  useAi: boolean
  scorer: string
  threshold: number
  profile: string
}

export type AppAction =
  | { type: "SET_CONFIG"; config: AppConfig }
  | { type: "START_RUN"; plugins: string[]; pluginNames: Record<string, string>; runId: string }
  | { type: "SET_RUN_STATE"; runState: RunState }
  | { type: "SET_PLUGIN_STATUS"; plugin: string; status: PluginStatus; count?: number; error?: string }
  | { type: "SET_CURRENT_PLUGIN"; plugin: string | null }
  | { type: "SET_AI_PHASE"; active: boolean }
  | { type: "RUN_COMPLETED" }
  | { type: "SET_RESULTS"; results: ContentItem[] | null }
  | { type: "SET_ERROR"; error: string }
  | { type: "SET_SIDEBAR_TAB"; sidebarTab: "run" | "history" }
  | { type: "SET_HISTORY"; history: HistoryEntry[] }
  | { type: "SET_CURRENT_HISTORY_ID"; currentHistoryId: string | null }
  | { type: "SET_HISTORY_RESULTS"; historyResults: ContentItem[] | null }
  | { type: "SET_CONTROL"; key: string; value: unknown }
  | { type: "ITEM_ARRIVED"; item: ContentItem }
  | { type: "RESET" }
