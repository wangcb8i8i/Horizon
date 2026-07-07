import { useMemo } from "react"

function RadarBlip({ delay, x, y }: { delay: number; x: number; y: number }) {
  return (
    <div
      className="absolute w-1.5 h-1.5 rounded-full bg-horizon-signal"
      style={{
        left: `${50 + x}%`,
        top: `${50 + y}%`,
        animation: `radar-blip ${2 + Math.random() * 2}s ease-out ${delay}s infinite`,
        opacity: 0,
      }}
    />
  )
}

export function EmptyView() {
  const blips = useMemo(() => {
    return Array.from({ length: 8 }, (_, i) => ({
      delay: i * 0.8 + Math.random() * 0.5,
      x: (Math.random() - 0.5) * 60,
      y: (Math.random() - 0.5) * 60,
      key: i,
    }))
  }, [])

  return (
    <div className="h-full flex flex-col items-center justify-center select-none">
      {/* Radar display */}
      <div className="relative mb-10">
        {/* Outer ring */}
        <div className="w-56 h-56 rounded-full border border-horizon-border/50 relative">
          {/* Inner rings */}
          <div className="absolute inset-[25%] rounded-full border border-horizon-border/30" />
          <div className="absolute inset-[50%] rounded-full border border-horizon-border/20" />
          <div className="absolute inset-[75%] rounded-full border border-horizon-border/10" />

          {/* Crosshairs */}
          <div className="absolute left-1/2 top-0 bottom-0 w-px bg-horizon-border/15" />
          <div className="absolute top-1/2 left-0 right-0 h-px bg-horizon-border/15" />

          {/* Sweep line */}
          <div className="absolute inset-0 rounded-full overflow-hidden">
            <div
              className="absolute inset-0 animate-radar-spin"
              style={{
                background: `conic-gradient(
                  from 0deg,
                  transparent 0%,
                  rgba(212, 135, 90, 0.08) 30%,
                  rgba(212, 135, 90, 0.15) 50%,
                  rgba(212, 135, 90, 0.08) 70%,
                  transparent 100%
                )`,
                maskImage: `linear-gradient(
                  to right,
                  transparent 0%,
                  black 40%,
                  black 60%,
                  transparent 100%
                )`,
                WebkitMaskImage: `linear-gradient(
                  to right,
                  transparent 0%,
                  black 40%,
                  black 60%,
                  transparent 100%
                )`,
              }}
            />
          </div>

          {/* Sweep line indicator */}
          <div className="absolute inset-0 rounded-full overflow-hidden">
            <div
              className="absolute top-1/2 left-1/2 h-px w-1/2 origin-left animate-radar-spin"
              style={{
                background: `linear-gradient(90deg, rgba(212, 135, 90, 0.6), rgba(212, 135, 90, 0.05))`,
              }}
            />
          </div>

          {/* Blips */}
          {blips.map((b) => (
            <RadarBlip key={b.key} delay={b.delay} x={b.x} y={b.y} />
          ))}

          {/* Center dot */}
          <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-horizon-signal/60" />
        </div>
      </div>

      {/* Text */}
      <h1 className="font-display text-lg font-semibold text-horizon-text mb-2 tracking-tight">
        信号扫描仪
      </h1>
      <p className="text-sm text-horizon-muted text-center max-w-xs leading-relaxed font-body">
        在左侧配置数据源，点击 <span className="text-horizon-signal font-medium">扫描</span> 开始采集信号。
      </p>
    </div>
  )
}
