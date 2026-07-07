import { useEffect, useRef } from "react"

type EventHandler = (data: Record<string, unknown>) => void

export function useSSE(url: string | null, handlers: Record<string, EventHandler>) {
  const handlersRef = useRef(handlers)
  handlersRef.current = handlers

  useEffect(() => {
    if (!url) return

    const eventSource = new EventSource(url)
    let closed = false

    eventSource.addEventListener("message", (e) => {
      try {
        const data = JSON.parse(e.data)
        const eventType = (e as MessageEvent & { type?: string }).type || "message"
        handlersRef.current[eventType]?.(data)
      } catch { /* skip */ }
    })

    const eventTypes = Object.keys(handlers)
    for (const eventType of eventTypes) {
      eventSource.addEventListener(eventType, (e: Event) => {
        if (closed) return
        const messageEvent = e as MessageEvent
        try {
          const data = JSON.parse(messageEvent.data)
          handlersRef.current[eventType]?.(data)
        } catch { /* skip */ }
      })
    }

    eventSource.onerror = () => {
      if (!closed) {
        handlersRef.current["error"]?.({})
      }
    }

    return () => {
      closed = true
      eventSource.close()
    }
  }, [url])
}
