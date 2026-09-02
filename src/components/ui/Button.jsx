import { forwardRef } from 'react'
import { cn } from '@/utils/cn'

export const Button = forwardRef(function Button(
  {
    children,
    className,
    variant = 'primary', // 'primary' | 'outline' | 'secondary' | 'ghost'
    size = 'default', // 'sm' | 'default' | 'lg'
    as: Component = 'button',
    ...props
  },
  ref
) {
  const baseStyles =
    'inline-flex items-center justify-center gap-2 font-heading font-bold text-xs uppercase tracking-wider transition-all duration-200 cursor-pointer disabled:opacity-50 disabled:pointer-events-none rounded-xl'

  const sizeStyles = {
    sm: 'h-9 px-4 text-[11px]',
    default: 'h-11 px-6',
    lg: 'h-12 px-8',
  }

  const variantStyles = {
    primary:
      'bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white shadow-md shadow-blue-600/20 hover:shadow-lg',
    outline:
      'bg-white/10 hover:bg-white/20 text-white border border-white/30 hover:border-white/50 backdrop-blur-xs',
    secondary:
      'bg-slate-800 hover:bg-slate-700 text-white border border-slate-700',
    ghost:
      'bg-transparent hover:bg-slate-800/60 text-slate-300 hover:text-white',
  }

  return (
    <Component
      ref={ref}
      className={cn(baseStyles, sizeStyles[size], variantStyles[variant], className)}
      {...props}
    >
      {children}
    </Component>
  )
})
