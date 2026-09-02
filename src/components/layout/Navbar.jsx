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
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 15)
    }
    window.addEventListener('scroll', handleScroll, { passive: true })
    handleScroll()
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <header className={cn(
      "sticky top-0 z-50 h-20 flex items-center transition-all duration-300 relative overflow-hidden",
      isScrolled
        ? "bg-white/85 backdrop-blur-lg border-b border-sky-100 shadow-sm shadow-blue-900/5"
        : "bg-white border-b border-slate-100"
    )}>
      {/* Subtle Liquid Flow & Water Wave Motif Spanning Across Navigation Bar */}
      <div className="absolute inset-0 pointer-events-none opacity-30 select-none overflow-hidden">
        <svg 
          className="absolute -bottom-1 left-0 w-full h-8 text-sky-200/60 preserve-3d" 
          viewBox="0 0 1440 48" 
          fill="none" 
          xmlns="http://www.w3.org/2000/svg"
        >
          <path 
            d="M0 24C240 40 480 8 720 24C960 40 1200 8 1440 24V48H0V24Z" 
            fill="currentColor" 
            fillOpacity="0.4"
          />
          <path 
            d="M0 32C320 16 640 44 960 28C1280 12 1360 36 1440 32V48H0V32Z" 
            fill="currentColor" 
            fillOpacity="0.25"
          />
        </svg>

        {/* Delicate Water Droplet Accents */}
        <div className="absolute top-3 left-[15%] w-1.5 h-1.5 rounded-full bg-sky-400/40 blur-[0.5px]" />
        <div className="absolute top-7 left-[45%] w-2 h-2 rounded-full bg-blue-400/30 blur-[0.5px]" />
        <div className="absolute top-4 right-[25%] w-1.5 h-1.5 rounded-full bg-sky-300/40 blur-[0.5px]" />
      </div>

      <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full flex items-center justify-between gap-6 relative z-10">
        
        {/* Logo Resmi PT Kediri Chemical Abadi */}
        <Link to="/" className="flex items-center shrink-0 group py-1">
          <img
            src="/images/kca_logo.png"
            alt="Logo Resmi PT Kediri Chemical Abadi"
            className="h-11 sm:h-12 w-auto object-contain transition-transform group-hover:scale-105 duration-300"
          />
        </Link>

        {/* Desktop Navigation Pill Menu (Manis, Estetik, Tema Air) */}
        <nav className="hidden lg:flex items-center gap-1.5 xl:gap-2 ml-auto bg-slate-50/80 p-1.5 rounded-full border border-sky-100 shadow-2xs">
          {NAVIGATION_DATA.navLinks.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.to === '/'}
              className={({ isActive }) =>
                cn(
                  'px-4 py-2 rounded-full text-xs font-heading font-extrabold uppercase tracking-wider transition-all duration-300 cursor-pointer relative',
                  isActive
                    ? 'text-white bg-gradient-to-r from-[#0F58A8] to-[#0284C7] shadow-sm shadow-blue-600/30'
                    : 'text-slate-700 hover:text-[#0F58A8] hover:bg-white/80'
                )
              }
            >
              {link.label}
            </NavLink>
          ))}
        </nav>

        {/* Desktop Quick CTA Pill Button */}
        <div className="hidden lg:flex items-center pl-2">
          <Link
            to="/contact"
            className="btn-fluid-primary text-xs py-2 px-5"
          >
            <span>Hubungi Lab</span>
            <ArrowUpRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        {/* Mobile Hamburger Toggle */}
        <div className="flex items-center lg:hidden ml-auto">
          <button
            onClick={() => setMobileOpen(!mobileOpen)}
            className="p-2.5 rounded-full text-slate-700 hover:text-[#0F58A8] hover:bg-blue-50 border border-slate-200 cursor-pointer transition-colors"
            aria-label="Toggle Mobile Menu"
          >
            {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>

      </div>

      {/* Mobile Dropdown Menu */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.2 }}
            className="absolute top-20 inset-x-0 bg-white/95 backdrop-blur-xl border-b border-sky-100 shadow-xl p-6 lg:hidden z-50"
          >
            <nav className="flex flex-col gap-2">
              {NAVIGATION_DATA.navLinks.map((link) => (
                <NavLink
                  key={link.to}
                  to={link.to}
                  end={link.to === '/'}
                  onClick={() => setMobileOpen(false)}
                  className={({ isActive }) =>
                    cn(
                      'px-4 py-3 rounded-xl text-xs font-heading font-extrabold uppercase tracking-wider transition-all',
                      isActive
                        ? 'text-white bg-gradient-to-r from-[#0F58A8] to-[#0284C7] shadow-sm'
                        : 'text-slate-700 hover:bg-blue-50/60'
                    )
                  }
                >
                  {link.label}
                </NavLink>
              ))}
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  )
}

