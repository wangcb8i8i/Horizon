import { cn } from "@/lib/utils"
import { forwardRef } from "react"

const ScrollArea = forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn("overflow-auto scrollbar-thin", className)}
        {...props}
      >
        <style>{`
          .scrollbar-thin::-webkit-scrollbar { width: 6px; }
          .scrollbar-thin::-webkit-scrollbar-track { background: transparent; }
          .scrollbar-thin::-webkit-scrollbar-thumb { background: #272730; border-radius: 3px; }
          .scrollbar-thin::-webkit-scrollbar-thumb:hover { background: #3B3B45; }
        `}</style>
        {children}
      </div>
    )
  }
)
ScrollArea.displayName = "ScrollArea"

export { ScrollArea }
