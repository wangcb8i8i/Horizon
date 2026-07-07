import { useCallback, useRef } from "react"

let audioCtx: AudioContext | null = null

function getCtx() {
  if (!audioCtx) {
    audioCtx = new AudioContext()
  }
  return audioCtx
}

function playTone(freq: number, duration: number, type: OscillatorType = "sine", gain = 0.08) {
  try {
    const ctx = getCtx()
    const osc = ctx.createOscillator()
    const g = ctx.createGain()
    osc.type = type
    osc.frequency.setValueAtTime(freq, ctx.currentTime)
    g.gain.setValueAtTime(gain, ctx.currentTime)
    g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration)
    osc.connect(g)
    g.connect(ctx.destination)
    osc.start()
    osc.stop(ctx.currentTime + duration)
  } catch { /* audio not available */ }
}

export function useSounds() {
  const lastItemRef = useRef(0)

  const playRun = useCallback(() => {
    playTone(440, 0.15, "sine", 0.06)
    setTimeout(() => playTone(660, 0.12, "sine", 0.05), 60)
  }, [])

  const playItem = useCallback(() => {
    const now = Date.now()
    if (now - lastItemRef.current < 200) return
    lastItemRef.current = now
    playTone(880 + Math.random() * 440, 0.08, "sine", 0.03)
  }, [])

  const playDone = useCallback(() => {
    playTone(523, 0.12, "sine", 0.06)
    setTimeout(() => playTone(659, 0.12, "sine", 0.06), 100)
    setTimeout(() => playTone(784, 0.2, "sine", 0.06), 200)
  }, [])

  const playError = useCallback(() => {
    playTone(220, 0.3, "sawtooth", 0.04)
  }, [])

  return { playRun, playItem, playDone, playError }
}
