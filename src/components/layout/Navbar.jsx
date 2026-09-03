import { useState, useEffect } from 'react'
import { Link, NavLink, useLocation } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { Menu, X, ArrowUpRight } from 'lucide-react'
import { cn } from '@/utils/cn'
import { NAVIGATION_DATA } from '@/data/navigationData'

export default function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)
  const location = useLocation()

  useEffect(() => {
    setMobileOpen(false)
    window.scrollTo(0, 0)
  }, [location.pathname])

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 20)
    window.addEventListener('scroll', handleScroll, { passive: true })
    handleScroll()
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <header
      className={cn(
        "fixed top-0 inset-x-0 z-50 w-full transition-all duration-300 select-none",
        isScrolled
          ? "bg-white/95 backdrop-blur-xl border-b border-slate-200/90 shadow-xs h-18 sm:h-20"
          : "bg-white/90 backdrop-blur-lg border-b border-slate-200/60 h-20"
      )}
    >
      <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 h-full w-full flex items-center justify-between gap-6">
        
        {/* ═══════════════════════════════════════════════════════════ */}
        {/* SISI KIRI: Logo Resmi PT Kediri Chemical Abadi              */}
        {/* ═══════════════════════════════════════════════════════════ */}
        <Link to="/" className="flex items-center py-1 group shrink-0">
          <img
            src="/images/kca_logo.png"
            alt="Logo Resmi PT Kediri Chemical Abadi"
            className="h-11 sm:h-13 lg:h-14 w-auto object-contain transition-transform group-hover:scale-105 duration-300"
          />
        </Link>

        {/* ═══════════════════════════════════════════════════════════ */}
        {/* SISI KANAN: Navigasi Tegas & Hubungi Lab Button             */}
        {/* ═══════════════════════════════════════════════════════════ */}
        <div className="flex items-center gap-2 lg:gap-3">
          
          {/* Desktop Navigation Links (Sido Muncul Style: Montserrat, Uppercase, Active Underline) */}
          <nav className="hidden lg:flex items-center gap-1.5 xl:gap-2">
            {NAVIGATION_DATA.navLinks.map((link) => (
              <NavLink
                key={link.to}
                to={link.to}
                end={link.to === '/'}
                className={({ isActive }) =>
                  cn(
                    'px-3.5 py-2 text-[12px] xl:text-[12.5px] font-heading uppercase tracking-wider transition-all duration-200 cursor-pointer relative font-bold',
                    isActive
                      ? 'text-[#0F58A8] font-black after:content-[\'\'] after:absolute after:bottom-[-2px] after:inset-x-3 after:h-[2.5px] after:bg-[#0F58A8] after:rounded-full'
                      : 'text-slate-800 hover:text-[#0F58A8] hover:bg-slate-50 rounded-md'
                  )
                }
              >
                {link.label}
              </NavLink>
            ))}
          </nav>

          {/* Divider */}
          <div className="hidden lg:block h-4 w-px bg-slate-200 mx-1" />

          {/* CTA Hubungi Lab (Sido Muncul Style: Bold Royal Blue Button) */}
          <Link
            to="/contact"
            className="h-10 px-5.5 bg-[#0F58A8] hover:bg-blue-700 active:bg-blue-800 text-white rounded-md text-xs font-heading font-extrabold uppercase tracking-wider inline-flex items-center gap-2 transition-all shadow-xs cursor-pointer"
          >
            <span>Hubungi Lab</span>
            <ArrowUpRight className="w-4 h-4" />
          </Link>

          {/* Mobile Hamburger Toggle */}
          <div className="flex items-center lg:hidden">
            <button
              onClick={() => setMobileOpen(!mobileOpen)}
              className="p-2 rounded-md border border-slate-200 text-slate-700 hover:text-[#0F58A8] hover:bg-slate-100 cursor-pointer transition-colors"
              aria-label="Toggle Mobile Menu"
            >
              {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>

        </div>

      </div>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* MOBILE DROPDOWN DOCK                                    */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -6 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -6 }}
            transition={{ duration: 0.15 }}
            className="absolute top-full inset-x-0 bg-white/95 backdrop-blur-2xl border-b border-slate-200 shadow-xl p-4 lg:hidden"
          >
            <nav className="flex flex-col gap-1 max-w-[1700px] mx-auto px-2">
              {NAVIGATION_DATA.navLinks.map((link) => (
                <NavLink
                  key={link.to}
                  to={link.to}
                  end={link.to === '/'}
                  onClick={() => setMobileOpen(false)}
                  className={({ isActive }) =>
                    cn(
                      'px-4 py-2.5 rounded-lg text-xs font-heading uppercase tracking-wider transition-all font-bold',
                      isActive
                        ? 'text-white bg-[#0F58A8] font-extrabold'
                        : 'text-slate-700 hover:bg-slate-100 hover:text-[#0F58A8]'
                    )
                  }
                >
                  {link.label}
                </NavLink>
              ))}

              <div className="pt-2 border-t border-slate-100 mt-1">
                <Link
                  to="/contact"
                  onClick={() => setMobileOpen(false)}
                  className="w-full h-11 bg-[#0F58A8] hover:bg-blue-700 text-white rounded-lg text-xs font-heading font-extrabold uppercase tracking-wider flex items-center justify-center gap-2 shadow-2xs"
                >
                  <span>Hubungi Lab &amp; Konsultasi B2B</span>
                  <ArrowUpRight className="w-4 h-4" />
                </Link>
              </div>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  )
}
