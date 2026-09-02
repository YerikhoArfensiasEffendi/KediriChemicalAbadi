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
    <header className="fixed top-3.5 sm:top-4 inset-x-0 z-50 pointer-events-none select-none transition-all duration-300">
      <div className="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-10 w-full flex items-center justify-between gap-4">
        
        {/* ═══════════════════════════════════════════════════════ */}
        {/* SISI KIRI: Kapsul Identitas Legal & Pabrik (Brand Dock) */}
        {/* ═══════════════════════════════════════════════════════ */}
        <Link
          to="/"
          className={cn(
            "pointer-events-auto flex items-center gap-3 px-3.5 sm:px-4 py-2 rounded-2xl transition-all duration-300 group",
            isScrolled
              ? "bg-white/95 backdrop-blur-xl border border-slate-200/90 shadow-md shadow-slate-900/5"
              : "bg-white/85 backdrop-blur-lg border border-slate-200/70 shadow-xs"
          )}
        >
          {/* Logo Resmi PT Kediri Chemical Abadi */}
          <img
            src="/images/kca_logo.png"
            alt="Logo Resmi PT Kediri Chemical Abadi"
            className="h-9 sm:h-10 w-auto object-contain transition-transform group-hover:scale-105 duration-300"
          />

          {/* Micro Typography Identitas Pabrik */}
          <div className="hidden sm:flex flex-col text-left pr-1">
            <span className="text-[12px] font-heading font-extrabold text-slate-900 tracking-tight leading-tight group-hover:text-[#0F58A8] transition-colors">
              PT KEDIRI CHEMICAL ABADI
            </span>
            <span className="text-[10px] font-medium text-slate-500 tracking-normal flex items-center gap-1.5 mt-0.5">
              <span className="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
              Pabrik Kimia B2B • Est. 2004
            </span>
          </div>
        </Link>

        {/* ═══════════════════════════════════════════════════════ */}
        {/* SISI KANAN: Floating Action & Navigation Dock          */}
        {/* ═══════════════════════════════════════════════════════ */}
        <div className="pointer-events-auto flex items-center gap-2.5 sm:gap-3">
          
          {/* Desktop Navigation Glass Dock */}
          <nav
            className={cn(
              "hidden lg:flex items-center gap-1 p-1.5 rounded-full transition-all duration-300",
              isScrolled
                ? "bg-white/95 backdrop-blur-xl border border-slate-200/90 shadow-md shadow-slate-900/5"
                : "bg-white/85 backdrop-blur-lg border border-slate-200/70 shadow-xs"
            )}
          >
            {NAVIGATION_DATA.navLinks.map((link) => (
              <NavLink
                key={link.to}
                to={link.to}
                end={link.to === '/'}
                className={({ isActive }) =>
                  cn(
                    'px-3.5 xl:px-4 py-2 rounded-full text-xs font-heading font-bold uppercase tracking-wider transition-all duration-300 cursor-pointer',
                    isActive
                      ? 'text-white bg-gradient-to-r from-[#0F58A8] to-[#0284C7] shadow-xs shadow-blue-600/30 font-extrabold'
                      : 'text-slate-700 hover:text-[#0F58A8] hover:bg-slate-100/80'
                  )
                }
              >
                {link.label}
              </NavLink>
            ))}

            {/* Quick CTA inside dock for Desktop */}
            <div className="pl-1">
              <Link
                to="/contact"
                className="btn-fluid-primary text-xs py-2 px-4.5 rounded-full shadow-xs"
              >
                <span>Hubungi Lab</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          </nav>

          {/* Quick Contact Pill for Tablet/Mobile */}
          <div className="hidden sm:flex lg:hidden">
            <Link
              to="/contact"
              className="btn-fluid-primary text-xs py-2 px-4 rounded-full shadow-xs"
            >
              <span>Hubungi Lab</span>
              <ArrowUpRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          {/* Mobile Hamburger Toggle Glass Pill */}
          <div className="flex items-center lg:hidden">
            <button
              onClick={() => setMobileOpen(!mobileOpen)}
              className={cn(
                "p-2.5 rounded-2xl transition-all duration-300 cursor-pointer text-slate-700 hover:text-[#0F58A8]",
                isScrolled
                  ? "bg-white/95 backdrop-blur-xl border border-slate-200 shadow-md"
                  : "bg-white/85 backdrop-blur-lg border border-slate-200/70 shadow-xs"
              )}
              aria-label="Toggle Mobile Menu"
            >
              {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>

        </div>

      </div>

      {/* ═══════════════════════════════════════════════════════ */}
      {/* MOBILE DROPDOWN DOCK                                    */}
      {/* ═══════════════════════════════════════════════════════ */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -8, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -8, scale: 0.98 }}
            transition={{ duration: 0.2 }}
            className="max-w-[1700px] mx-auto px-4 sm:px-6 mt-2 pointer-events-auto lg:hidden"
          >
            <div className="bg-white/95 backdrop-blur-2xl border border-slate-200 rounded-3xl shadow-xl p-4 sm:p-5">
              <nav className="flex flex-col gap-1.5">
                {NAVIGATION_DATA.navLinks.map((link) => (
                  <NavLink
                    key={link.to}
                    to={link.to}
                    end={link.to === '/'}
                    onClick={() => setMobileOpen(false)}
                    className={({ isActive }) =>
                      cn(
                        'px-4 py-3 rounded-2xl text-xs font-heading font-extrabold uppercase tracking-wider transition-all',
                        isActive
                          ? 'text-white bg-gradient-to-r from-[#0F58A8] to-[#0284C7] shadow-xs'
                          : 'text-slate-700 hover:bg-slate-100/80 hover:text-[#0F58A8]'
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
                    className="btn-fluid-primary w-full text-xs py-3 rounded-2xl text-center flex items-center justify-center gap-2"
                  >
                    <span>Hubungi Lab & Konsultasi B2B</span>
                    <ArrowUpRight className="w-4 h-4" />
                  </Link>
                </div>
              </nav>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  )
}
