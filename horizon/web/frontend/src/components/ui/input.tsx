import { cn } from "@/lib/utils"
import { forwardRef } from "react"

const Input = forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-9 w-full rounded-lg border border-horizon-border bg-horizon-surface px-3 py-2 text-sm text-horizon-text placeholder:text-horizon-dim focus:outline-none focus:ring-2 focus:ring-horizon-signal/30 focus:border-horizon-signal/40 disabled:cursor-not-allowed disabled:opacity-50 transition-all font-body",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }
