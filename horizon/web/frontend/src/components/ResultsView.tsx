import { useState, useMemo, useRef, useEffect, useCallback, useLayoutEffect } from "react"
import type { ContentItem } from "../types"
import { cn } from "@/lib/utils"

// --- URL linkification ---

/** Converts bare URLs in text to clickable `<a>` tags. */
function linkifyText(text: string): React.ReactNode {
  const urlRe = /https?:\/\/[^\s<>"']+/g
  const parts: React.ReactNode[] = []
  let lastIndex = 0
  let match: RegExpExecArray | null
  const re = new RegExp(urlRe.source, "g")

  while ((match = re.exec(text)) !== null) {
    if (match.index > lastIndex) {
      parts.push(text.slice(lastIndex, match.index))
    }
    const url = match[0]
    const display = url.length > 55 ? url.slice(0, 55) + "…" : url
    parts.push(
      <a key={match.index} href={url} target="_blank" rel="noopener noreferrer"
        className="text-horizon-echo/70 hover:text-horizon-echo underline underline-offset-2 decoration-1 decoration-horizon-echo/20 transition-colors"
      >{display}</a>
    )
    lastIndex = match.index + url.length
  }
  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex))
  }
  return parts.length > 0 ? parts : text
}

// --- Source navigation helpers ---

const SOURCE_ABBR: Record<string, string> = {
  hackernews: "HN",
  reddit: "RD",
  github: "GH",
  twitter: "TW",
  v2ex: "V2",
  bilibili: "BL",
  telegram: "TG",
  youtube: "YT",
  rss: "RS",
  xiaohongshu: "XH",
  ossinsight: "OI",
  openbb: "OB",
}

function sourceHue(name: string): number {
  let hash = 0
  for (const c of name) hash = c.charCodeAt(0) + ((hash << 5) - hash)
  return Math.abs(hash) % 360
}

// --- Comment parsing ---

interface ParsedComment {
  author: string
  body: string
  score?: string
}

interface ParsedContent {
  body: string
  comments: ParsedComment[]
}

function parseContent(raw: string): ParsedContent {
  // Match the marker and everything after it
  const markerRe = /\n--- Top Comments ---\n*/
  const match = markerRe.exec(raw)
  if (!match) return { body: raw, comments: [] }

  const body = raw.slice(0, match.index).trim()
  const commentBlock = raw.slice(match.index + match[0].length)

  // Find each [author] or [author (score)]: prefix — works with or without newlines
  const itemRe = /\[([^\]]+)\]:\s*/g
  const entries: { rawAuthor: string; start: number }[] = []
  let m: RegExpExecArray | null
  while ((m = itemRe.exec(commentBlock)) !== null) {
    entries.push({ rawAuthor: m[1].trim(), start: m.index + m[0].length })
  }

  const comments: ParsedComment[] = []
  for (let i = 0; i < entries.length; i++) {
    const { rawAuthor, start } = entries[i]
    // End at the next '[' that starts a new author entry, or end of string
    const nextBracket = commentBlock.indexOf('[', start)
    const bodyEnd = (nextBracket !== -1 && i < entries.length - 1) ? nextBracket : commentBlock.length
    let rawBody = commentBlock.slice(start, bodyEnd).trim().replace(/\s+$/, "")

    // Extract score if present, e.g. "username (42 pts)"
    const scoreMatch = rawAuthor.match(/^(.+?)\s*\(([^)]+)\)$/)
    const author = scoreMatch ? scoreMatch[1].trim() : rawAuthor
    const score = scoreMatch ? scoreMatch[2].trim() : undefined

    if (rawBody) {
      comments.push({ author, body: rawBody, score })
    }
  }

  return { body, comments }
}

// --- Sub-components ---

function SourceTag({ source }: { source: string }) {
  return (
    <span className="text-[10px] font-mono uppercase tracking-wider text-horizon-muted bg-horizon-surface px-1.5 py-0.5 rounded border border-horizon-border/30 leading-none flex-shrink-0">
      {source}
    </span>
  )
}

function CommentCard({ comment }: { comment: ParsedComment }) {
  return (
    <div className="group/comment flex gap-3 py-2 first:pt-0 last:pb-0">
      {/* Left gutter bar — subtle vertical connector */}
      <div className="w-px flex-shrink-0 bg-horizon-border/40 group-hover/comment:bg-horizon-signal/60 transition-colors rounded-full" />
      <div className="min-w-0 flex-1 space-y-0.5">
        {/* Author + score */}
        <div className="flex items-baseline gap-2">
          <span className="text-[11px] font-medium text-horizon-text/80 font-mono">@{comment.author}</span>
          {comment.score && (
            <span className="text-[10px] text-horizon-dim font-mono tabular-nums">{comment.score}</span>
          )}
        </div>
        {/* Body */}
        <p className="text-sm text-horizon-text/70 leading-relaxed font-body [overflow-wrap:anywhere]">
          {linkifyText(comment.body)}
        </p>
      </div>
    </div>
  )
}

function TimeAgo({ dateStr }: { dateStr?: string }) {
  if (!dateStr) return null
  try {
    const now = Date.now()
    const date = new Date(dateStr).getTime()
    const diff = now - date
    const mins = Math.floor(diff / 60000)
    if (mins < 1) return <span className="text-xs text-horizon-dim font-mono tabular-nums">now</span>
    if (mins < 60) return <span className="text-xs text-horizon-dim font-mono tabular-nums">{mins}m</span>
    const hours = Math.floor(mins / 60)
    if (hours < 24) return <span className="text-xs text-horizon-dim font-mono tabular-nums">{hours}h</span>
    const days = Math.floor(hours / 24)
    return <span className="text-xs text-horizon-dim font-mono tabular-nums">{days}d</span>
  } catch {
    return null
  }
}

function StrengthBar({ score }: { score: number }) {
  const pct = Math.min(Math.round((score / 10) * 100), 100)
  const color =
    score >= 7 ? "bg-horizon-signal" :
    score >= 4 ? "bg-horizon-echo" :
    "bg-horizon-dim"
  return (
    <div className="signal-strength min-w-[56px]">
      <div className={`signal-strength-fill ${color}`} style={{ width: `${pct}%` }} />
    </div>
  )
}

function ItemRow({ item, index, live }: { item: ContentItem; index: number; live?: boolean }) {
  const [showFullContent, setShowFullContent] = useState(false)
  const [isClamped, setIsClamped] = useState(false)
  const contentRef = useRef<HTMLParagraphElement>(null)
  const hasScore = item.ai_score !== undefined && item.ai_score !== null
  const displayContent = item.ai_summary || item.content || ""
  const parsed = parseContent(displayContent)
  const hnScore = item.metadata?.score
  const hnComments = item.metadata?.descendants
  const discussionUrl = item.metadata?.discussion_url
  const hasBodyContent = !!parsed.body

  useLayoutEffect(() => {
    if (contentRef.current) {
      setIsClamped(contentRef.current.scrollHeight > contentRef.current.clientHeight)
    }
  }, [displayContent, showFullContent])

  return (
    <div className={cn("group flex", live ? "animate-item-arrive" : "animate-blip-enter")}
      style={{ animationDelay: `${index * 20}ms` }}>
      {/* Timeline dot + connector */}
      <div className="flex flex-col items-center w-5 flex-shrink-0 pt-[5px]">
        <div className="w-[5px] h-[5px] rounded-full bg-horizon-border group-hover:bg-horizon-signal transition-colors duration-200 flex-shrink-0" />
        <div className="w-px flex-1 bg-horizon-border/30 mt-[5px]" />
      </div>

      {/* Main content */}
      <div className="flex-1 min-w-0 pb-8 pt-0.5">
        {/* Title + source badge */}
        <div className="flex items-start gap-2">
          <div className="min-w-0 flex-1">
            <h3 className="text-sm font-bold leading-snug truncate font-body text-horizon-text">
              {item.title}
            </h3>
          </div>
          <SourceTag source={item.source_type} />
        </div>

        {/* Metadata row: author · score · comments · time */}
        <div className="flex items-center gap-2.5 mt-1 flex-wrap">
          {item.author && (
            <span className="text-[11px] text-horizon-muted font-mono truncate max-w-[160px]">
              {item.author}
            </span>
          )}
          {hnScore !== undefined && (
            <span className="text-[11px] text-horizon-muted font-mono tabular-nums flex items-center gap-1 flex-shrink-0">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" className="text-horizon-dim">
                <polyline points="14 9 9 14 12 17 17 12" />
              </svg>
              {hnScore}
            </span>
          )}
          {hnComments !== undefined && (
            <span className="text-[11px] text-horizon-muted font-mono tabular-nums flex items-center gap-1 flex-shrink-0">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" className="text-horizon-dim">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
              </svg>
              {hnComments}
            </span>
          )}
          <TimeAgo dateStr={item.published_at} />
          {hasScore && (
            <div className="flex items-center gap-1.5 ml-auto flex-shrink-0">
              <StrengthBar score={item.ai_score!} />
              <span className="text-[11px] text-horizon-muted font-mono tabular-nums w-6 text-right flex-shrink-0">
                {item.ai_score!.toFixed(1)}
              </span>
            </div>
          )}
        </div>

        {/* Body content */}
        {hasBodyContent && (
          <div className="mt-2">
            <p ref={contentRef} className={cn("text-sm text-horizon-text/85 leading-relaxed font-body [overflow-wrap:anywhere]", !showFullContent && "line-clamp-4")}>
              {linkifyText(parsed.body)}
            </p>
            {(isClamped || showFullContent) && (
              <button onClick={(e) => { e.stopPropagation(); setShowFullContent(!showFullContent) }}
                className="mt-1 text-[11px] text-horizon-signal/60 hover:text-horizon-signal transition-colors font-mono uppercase tracking-wider">
                {showFullContent ? "收起" : "展开"}
              </button>
            )}
          </div>
        )}

        {/* Comments section */}
        {parsed.comments.length > 0 && (
          <div className="mt-3 rounded-md bg-horizon-surface/40 px-3 py-2.5 border border-horizon-border/30">
            <div className="flex items-center gap-2 mb-1.5 pb-1.5 border-b border-horizon-border/20">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" className="text-horizon-muted">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
              </svg>
              <span className="text-[10px] text-horizon-muted font-mono uppercase tracking-wider">
                Top Comments
              </span>
              <span className="text-[10px] text-horizon-dim font-mono tabular-nums">{parsed.comments.length}</span>
            </div>
            <div className="space-y-0">
              {parsed.comments.map((c, i) => <CommentCard key={i} comment={c} />)}
            </div>
          </div>
        )}

        {/* Action links */}
        <div className="mt-2 flex items-center gap-3">
          {item.url && (
            <a href={item.url} target="_blank" rel="noopener noreferrer"
              onClick={(e) => e.stopPropagation()}
              className="inline-flex items-center gap-1 text-[11px] text-horizon-signal/60 hover:text-horizon-signal transition-colors font-mono">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                <polyline points="15 3 21 3 21 9" />
                <line x1="10" y1="14" x2="21" y2="3" />
              </svg>
              打开链接
            </a>
          )}
          {discussionUrl && (
            <a href={discussionUrl} target="_blank" rel="noopener noreferrer"
              onClick={(e) => e.stopPropagation()}
              className="inline-flex items-center gap-1 text-[11px] text-horizon-echo/60 hover:text-horizon-echo transition-colors font-mono">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
              </svg>
              HN讨论
            </a>
          )}
        </div>
      </div>
    </div>
  )
}

// --- Source navigation ---

interface SourceGroup {
  name: string
  count: number
  hue: number
}

function SourceNav({
  groups,
  activeSource,
  onNavigate,
  sidebarLeft,
}: {
  groups: SourceGroup[]
  activeSource: string | null
  onNavigate: (name: string) => void
  sidebarLeft: number
}) {
  return (
    <nav className="hidden md:flex flex-col gap-1 fixed top-11 bottom-0 w-28 z-20 bg-horizon-surface border-r border-horizon-border/20 justify-center px-1"
      style={{ left: `${sidebarLeft}px` }}>
      {groups.map((g) => {
        const active = g.name === activeSource
        return (
          <button key={g.name} onClick={() => onNavigate(g.name)}
            className={cn(
              "relative flex flex-col items-stretch gap-0.5 py-2 rounded-md transition-all duration-200",
              active
                ? "bg-horizon-card/60 text-horizon-text"
                : "text-horizon-muted hover:bg-horizon-surface/60 hover:text-horizon-text"
            )}>
            {active && (
              <div className="absolute left-0 top-1/2 -translate-y-1/2 w-0.5 h-4 rounded-full"
                style={{ background: `hsl(${g.hue}, 55%, 60%)` }} />
            )}
            <span className="self-center w-2 h-2 rounded-full" style={{ background: `hsl(${g.hue}, 55%, 60%)` }} />
            <div className="flex items-center justify-center gap-1 w-full">
              <span className="text-[10px] font-mono leading-tight truncate max-w-[64px]">{g.name}</span>
              <span className="text-[9px] font-mono tabular-nums text-horizon-dim flex-shrink-0">{g.count}</span>
            </div>
          </button>
        )
      })}
    </nav>
  )
}

// --- Group header ---

function GroupHeader({ source, count }: { source: string; count: number }) {
  return (
    <div data-source-group={source} className="flex items-center gap-3 pl-7 py-3">
      <div className="h-px flex-1 bg-horizon-border/30" />
      <span className="text-[11px] text-horizon-muted font-mono uppercase tracking-wider flex-shrink-0">
        {source}
      </span>
      <span className="text-[10px] text-horizon-dim font-mono tabular-nums flex-shrink-0">
        {count}
      </span>
      <div className="h-px flex-1 bg-horizon-border/30" />
    </div>
  )
}

// --- Main ResultsView ---

export default function ResultsView({
  items,
  live = false,
  sources = [],
  sourceFilter: initialSourceFilter,
  sidebarLeft,
}: {
  items: ContentItem[]
  live?: boolean
  sources?: string[]
  sourceFilter?: string | null
  sidebarLeft?: number
}) {
  const [sourceFilter, setSourceFilter] = useState<string | null>(initialSourceFilter ?? null)
  const [activeSource, setActiveSource] = useState<string | null>(null)
  const scrollContainerRef = useRef<HTMLDivElement>(null)

  const filtered = useMemo(() => {
    let result = sourceFilter ? items.filter((i) => i.source_type === sourceFilter) : items
    const groups: Record<string, ContentItem[]> = {}
    for (const item of result) {
      const key = item.source_type
      if (!groups[key]) groups[key] = []
      groups[key].push(item)
    }
    for (const g of Object.values(groups)) {
      g.sort((a, b) => {
        const sa = a.ai_score ?? 0
        const sb = b.ai_score ?? 0
        if (sb !== sa) return sb - sa
        const ta = a.published_at ? new Date(a.published_at).getTime() : 0
        const tb = b.published_at ? new Date(b.published_at).getTime() : 0
        return tb - ta
      })
    }
    const sourceOrder = Object.entries(groups)
      .sort(([, a], [, b]) => {
        const sa = a[0]?.ai_score ?? 0
        const sb = b[0]?.ai_score ?? 0
        if (sb !== sa) return sb - sa
        const ta = a[0]?.published_at ? new Date(a[0].published_at).getTime() : 0
        const tb = b[0]?.published_at ? new Date(b[0].published_at).getTime() : 0
        return tb - ta
      })
      .map(([s]) => s)
    return sourceOrder.flatMap((s) => groups[s])
  }, [items, sourceFilter])

  // Compute source groups for nav sidebar
  const sourceGroups = useMemo(() => {
    const map = new Map<string, number>()
    for (const item of filtered) {
      map.set(item.source_type, (map.get(item.source_type) ?? 0) + 1)
    }
    return Array.from(map.entries()).map(([name, count]) => ({ name, count, hue: sourceHue(name) }))
  }, [filtered])

  // Scroll-spy: auto-highlight current source
  useEffect(() => {
    const elements = document.querySelectorAll("[data-source-group]")
    if (elements.length === 0) return
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)
        if (visible.length > 0) {
          setActiveSource(visible[0].getAttribute("data-source-group"))
        }
      },
      { threshold: 0.2, rootMargin: "-80px 0px -25% 0px" }
    )
    elements.forEach((el) => observer.observe(el))
    return () => observer.disconnect()
  }, [filtered])

  const scrollToSource = useCallback((name: string) => {
    const el = document.querySelector(`[data-source-group="${name}"]`)
    el?.scrollIntoView({ behavior: "smooth" })
  }, [])

  return (
    <div className="max-w-5xl mx-auto px-6 py-4">
      {/* Source filter chips */}
      <div className="flex gap-1 flex-wrap mb-6">
        <button onClick={() => setSourceFilter(null)}
          className={cn("text-[11px] px-2.5 py-1 rounded-md border transition-all font-mono uppercase tracking-wider",
            !sourceFilter
              ? "bg-horizon-card text-horizon-text border-horizon-border"
              : "text-horizon-muted border-horizon-border hover:text-horizon-text hover:border-horizon-dim bg-transparent"
          )}>全部</button>
        {sources.map((s) => (
          <button key={s}
            onClick={() => setSourceFilter(s === sourceFilter ? null : s)}
            className={cn("text-[11px] px-2.5 py-1 rounded-md border transition-all font-mono uppercase tracking-wider",
              sourceFilter === s
                ? "bg-horizon-card text-horizon-text border-horizon-border"
                : "text-horizon-muted border-horizon-border hover:text-horizon-text hover:border-horizon-dim bg-transparent"
            )}>{s}</button>
        ))}
      </div>

      {/* Content area with source navigation */}
      <div className="relative">
        {sourceGroups.length > 1 && (
          <SourceNav groups={sourceGroups} activeSource={activeSource} onNavigate={scrollToSource} sidebarLeft={sidebarLeft ?? 0} />
        )}

        {/* Results list */}
        <div ref={scrollContainerRef}>
          {items.length === 0 && live ? (
            <div className="flex flex-col items-center justify-center py-32 select-none">
              <div className="relative w-40 h-40 mb-8">
                {/* Outer ring */}
                  <div className="absolute inset-0 rounded-full border border-horizon-border/25" />
                  {/* Inner ring */}
                  <div className="absolute inset-[30%] rounded-full border border-horizon-border/15" />
                  {/* Crosshairs */}
                  <div className="absolute left-1/2 top-0 bottom-0 w-px bg-horizon-border/10" />
                  <div className="absolute top-1/2 left-0 right-0 h-px bg-horizon-border/10" />
                  {/* Sweep glow */}
                  <div className="absolute inset-0 rounded-full overflow-hidden">
                    <div className="absolute inset-0 animate-radar-spin"
                      style={{
                        background: "conic-gradient(from 0deg, transparent 0%, rgba(212,135,90,0.08) 35%, rgba(212,135,90,0.18) 50%, rgba(212,135,90,0.08) 65%, transparent 100%)",
                        maskImage: "linear-gradient(to right, transparent 0%, black 35%, black 65%, transparent 100%)",
                        WebkitMaskImage: "linear-gradient(to right, transparent 0%, black 35%, black 65%, transparent 100%)",
                      }} />
                  </div>
                  {/* Sweep line */}
                  <div className="absolute inset-0 rounded-full overflow-hidden">
                    <div className="absolute top-1/2 left-1/2 h-px w-1/2 origin-left animate-radar-spin"
                      style={{ background: "linear-gradient(90deg, rgba(212,135,90,0.5), rgba(212,135,90,0.03))" }} />
                  </div>
                  {/* Center dot */}
                  <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-horizon-signal/30" />
                  {/* Tick marks */}
                  <div className="absolute top-0 left-1/2 -translate-x-1/2 w-px h-2 bg-horizon-border/20" />
                  <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-px h-2 bg-horizon-border/10" />
                  <div className="absolute left-0 top-1/2 -translate-y-1/2 w-2 h-px bg-horizon-border/20" />
                  <div className="absolute right-0 top-1/2 -translate-y-1/2 w-2 h-px bg-horizon-border/10" />
                </div>
                <p className="text-xs text-horizon-muted font-mono tracking-[0.15em] animate-pulse">
                  信号搜索中
                </p>
              </div>
          ) : filtered.length === 0 ? (
            <p className="text-sm text-horizon-dim py-12 text-center font-body">暂无结果</p>
          ) : (
            <div>
              {(() => {
                const out: React.ReactNode[] = []
                let currentSource = ""
                for (let i = 0; i < filtered.length; i++) {
                  const item = filtered[i]
                  if (item.source_type !== currentSource) {
                    currentSource = item.source_type
                    const count = filtered.filter((x) => x.source_type === currentSource).length
                    out.push(<GroupHeader key={`hdr-${currentSource}`} source={currentSource} count={count} />)
                  }
                  out.push(<ItemRow key={`${item.source_type}-${i}-${item.title}`} item={item} index={i} live={live} />)
                }
                return out
              })()}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
