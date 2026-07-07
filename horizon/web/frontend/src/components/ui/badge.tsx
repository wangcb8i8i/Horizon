import { cn } from "@/lib/utils"
import { cva, type VariantProps } from "class-variance-authority"

const badgeVariants = cva(
  "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium transition-colors",
  {
    variants: {
      variant: {
        default: "bg-horizon-signal-soft text-horizon-signal border border-horizon-signal-line",
        secondary: "bg-horizon-card text-horizon-muted border border-horizon-border",
        destructive: "bg-red-500/15 text-red-300 border border-red-500/20",
        outline: "text-horizon-muted border border-horizon-border",
        success: "bg-emerald-500/15 text-emerald-300 border border-emerald-500/20",
        amber: "bg-amber-500/15 text-amber-300 border border-amber-500/20",
        sky: "bg-sky-500/15 text-sky-300 border border-sky-500/20",
        rose: "bg-rose-500/15 text-rose-300 border border-rose-500/20",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return <div className={cn(badgeVariants({ variant }), className)} {...props} />
}

export { Badge, badgeVariants }
