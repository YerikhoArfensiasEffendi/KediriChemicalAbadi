import { cn } from '@/utils/cn'

export function Badge({ children, className }) {
  return (
    <p
      className={cn(
        'text-xs font-bold tracking-widest uppercase text-[#0F58A8]',
        className
      )}
    >
      {children}
    </p>
  )
}
