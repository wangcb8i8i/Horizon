import { cn } from "@/lib/utils"
import { cva, type VariantProps } from "class-variance-authority"
import { forwardRef } from "react"

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-lg text-sm font-medium transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-horizon-signal focus-visible:ring-offset-2 focus-visible:ring-offset-[#0B0B0E] disabled:pointer-events-none disabled:opacity-50 select-none",
  {
    variants: {
      variant: {
        default: "bg-horizon-signal text-[#0B0B0E] hover:brightness-110 active:scale-[0.98]",
        destructive: "bg-red-600 text-white hover:bg-red-500",
        outline:
          "border border-horizon-border bg-transparent hover:bg-horizon-card text-horizon-muted hover:text-horizon-text",
        secondary:
          "bg-horizon-card text-horizon-text hover:bg-horizon-surface border border-horizon-border",
        ghost: "text-horizon-muted hover:text-horizon-text hover:bg-horizon-card",
        link: "text-horizon-signal underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-5 py-2",
        sm: "h-7 rounded-md px-3 text-xs",
        lg: "h-11 rounded-xl px-8 text-base",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {}

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, ...props }, ref) => {
    return (
      <button
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
