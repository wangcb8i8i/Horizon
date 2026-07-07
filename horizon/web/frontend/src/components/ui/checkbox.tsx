import { cn } from "@/lib/utils"
import { forwardRef } from "react"

const Checkbox = forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  ({ className, ...props }, ref) => (
    <input
      type="checkbox"
      ref={ref}
      className={cn(
        "h-4 w-4 rounded border-horizon-border bg-horizon-surface text-horizon-signal focus:ring-2 focus:ring-horizon-signal/30 focus:ring-offset-0 cursor-pointer accent-horizon-signal",
        className
      )}
      {...props}
    />
  )
)
Checkbox.displayName = "Checkbox"

export { Checkbox }
