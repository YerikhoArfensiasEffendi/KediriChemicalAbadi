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
    <header className="fixed top-3 sm:top-4 inset-x-0 z-50 pointer-events-none select-none transition-all duration-300">
      <div className="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-10 w-full flex items-center justify-between gap-4">
        
        {/* ═══════════════════════════════════════════════════════════ */}
        {/* SISI KIRI: Identitas Pabrik Tegas & Minimalis (Brand Box)   */}
        {/* ═══════════════════════════════════════════════════════════ */}
        <Link
          to="/"
          className={cn(
            "pointer-events-auto flex items-center gap-3 px-3.5 sm:px-4 py-2 rounded-lg transition-all duration-300 group border",
            isScrolled
              ? "bg-white/95 backdrop-blur-xl border-slate-300/90 shadow-sm"
              : "bg-white/90 backdrop-blur-lg border-slate-200/80 shadow-2xs"
          )}
        >
          {/* Logo Resmi PT Kediri Chemical Abadi */}
          <img
            src="/images/kca_logo.png"
            alt="Logo Resmi PT Kediri Chemical Abadi"
            className="h-8 sm:h-9 w-auto object-contain transition-transform group-hover:scale-102 duration-300"
          />

          {/* Micro Typography Identitas Pabrik Tegas */}
          <div className="hidden sm:flex flex-col text-left pr-1">
            <span className="text-xs font-heading font-extrabold text-slate-900 tracking-tight leading-tight group-hover:text-[#0F58A8] transition-colors">
              PT KEDIRI CHEMICAL ABADI
            </span>
            <span className="text-[9.5px] font-semibold text-slate-500 tracking-wider uppercase flex items-center gap-1.5 mt-0.5 font-mono">
              <span className="inline-block w-1.5 h-1.5 rounded-xs bg-emerald-500" />
              Pabrik Kimia B2B • Est. 2004
            </span>
          </div>
        </Link>

        {/* ═══════════════════════════════════════════════════════════ */}
        {/* SISI KANAN: Navigasi Tegas, Simpel & Presisi (Action Bar)   */}
        {/* ═══════════════════════════════════════════════════════════ */}
        <div className="pointer-events-auto flex items-center gap-2.5 sm:gap-3">
          
          {/* Desktop Navigation Crisp Dock */}
          <nav
            className={cn(
              "hidden lg:flex items-center gap-1 p-1.5 rounded-lg border transition-all duration-300",
              isScrolled
                ? "bg-white/95 backdrop-blur-xl border-slate-300/90 shadow-sm"
                : "bg-white/90 backdrop-blur-lg border-slate-200/80 shadow-2xs"
            )}
          >
            {NAVIGATION_DATA.navLinks.map((link) => (
              <NavLink
                key={link.to}
                to={link.to}
                end={link.to === '/'}
                className={({ isActive }) =>
                  cn(
                    'px-3.5 py-1.5 rounded-md text-xs font-heading uppercase tracking-wider transition-all duration-200 cursor-pointer font-bold',
                    isActive
                      ? 'text-white bg-[#0F58A8] shadow-2xs font-extrabold'
                      : 'text-slate-700 hover:text-[#0F58A8] hover:bg-slate-100/90'
                  )
                }
              >
                {link.label}
              </NavLink>
            ))}

            {/* Subtle Vertical Divider */}
            <div className="h-4 w-px bg-slate-200 mx-1" />

            {/* Quick CTA inside dock for Desktop (Tegas, Kotak Presisi) */}
            <Link
              to="/contact"
              className="h-8 px-4 bg-[#0F58A8] hover:bg-blue-700 active:bg-blue-800 text-white rounded-md text-xs font-heading font-extrabold uppercase tracking-wider inline-flex items-center gap-1.5 transition-all shadow-2xs cursor-pointer"
            >
              <span>Hubungi Lab</span>
              <ArrowUpRight className="w-3.5 h-3.5" />
            </Link>
          </nav>

          {/* Quick Contact for Tablet */}
          <div className="hidden sm:flex lg:hidden">
            <Link
              to="/contact"
              className="h-9 px-4 bg-[#0F58A8] hover:bg-blue-700 text-white rounded-lg text-xs font-heading font-extrabold uppercase tracking-wider inline-flex items-center gap-1.5 shadow-2xs"
            >
              <span>Hubungi Lab</span>
              <ArrowUpRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          {/* Mobile Hamburger Toggle (Tegas rounded-lg) */}
          <div className="flex items-center lg:hidden">
            <button
              onClick={() => setMobileOpen(!mobileOpen)}
              className={cn(
                "p-2.5 rounded-lg border transition-all duration-300 cursor-pointer text-slate-700 hover:text-[#0F58A8]",
                isScrolled
                  ? "bg-white/95 backdrop-blur-xl border-slate-300 shadow-sm"
                  : "bg-white/90 backdrop-blur-lg border-slate-200/80 shadow-2xs"
              )}
              aria-label="Toggle Mobile Menu"
            >
              {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>

        </div>

      </div>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* MOBILE DROPDOWN DOCK (Tegas & Rapi)                         */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -6 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -6 }}
            transition={{ duration: 0.15 }}
            className="max-w-[1700px] mx-auto px-4 sm:px-6 mt-2 pointer-events-auto lg:hidden"
          >
            <div className="bg-white/95 backdrop-blur-2xl border border-slate-300/80 rounded-xl shadow-lg p-4">
              <nav className="flex flex-col gap-1">
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
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  )
}
