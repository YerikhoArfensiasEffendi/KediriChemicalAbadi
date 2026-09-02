import { useState, useEffect, useRef, useCallback } from 'react'
import { Link, NavLink, useLocation } from 'react-router-dom'
import { motion, AnimatePresence, useMotionValue, useSpring, useTransform } from 'framer-motion'
import { Menu, X, ArrowUpRight } from 'lucide-react'
import { cn } from '@/utils/cn'
import { NAVIGATION_DATA } from '@/data/navigationData'

export default function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)
  const location = useLocation()
  const headerRef = useRef(null)

  // Mouse parallax for subtle 3D depth on the liquid shape
  const rawMouseX = useMotionValue(0)
  const mouseX = useSpring(rawMouseX, { stiffness: 40, damping: 20 })
  const waveShiftX = useTransform(mouseX, [-1, 1], [-6, 6])

  const handleMouseMove = useCallback((e) => {
    if (!headerRef.current) return
    const rect = headerRef.current.getBoundingClientRect()
    const nx = ((e.clientX - rect.left) / rect.width - 0.5) * 2
    rawMouseX.set(nx)
  }, [rawMouseX])

  const handleMouseLeave = useCallback(() => {
    rawMouseX.set(0)
  }, [rawMouseX])

  useEffect(() => {
    setMobileOpen(false)
    window.scrollTo(0, 0)
  }, [location.pathname])

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 15)
    window.addEventListener('scroll', handleScroll, { passive: true })
    handleScroll()
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <header
      ref={headerRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      className="fixed top-0 left-0 right-0 z-50 w-full select-none"
    >
      {/* ═══════════════════════════════════════════════════════════════ */}
      {/* LIQUID WAVE NAVBAR SHAPE — The wave IS the navbar background  */}
      {/* Stretches edge-to-edge, forming a unique organic nav shape    */}
      {/* ═══════════════════════════════════════════════════════════════ */}
      <div className="relative w-full">
        
        {/* The Liquid Wave Shape — Full-bleed from corner to corner */}
        <motion.div
          style={{ x: waveShiftX }}
          className="absolute top-0 left-[-3%] w-[106%] h-[140px] sm:h-[160px] lg:h-[180px] pointer-events-none select-none animate-liquid-flow"
        >
          <img
            src="/images/navbar_liquid_final_4k.png"
            alt=""
            aria-hidden="true"
            className={cn(
              "w-full h-full object-fill transition-all duration-500",
              isScrolled ? "opacity-60" : "opacity-70"
            )}
            draggable={false}
          />
        </motion.div>

        {/* Caustic light shimmer moving across the wave */}
        <div 
          className="absolute top-0 left-0 right-0 h-[120px] sm:h-[140px] lg:h-[150px] pointer-events-none animate-caustic-shimmer"
          style={{
            background: 'linear-gradient(110deg, transparent 25%, rgba(255,255,255,0.15) 45%, rgba(186,230,253,0.1) 55%, transparent 75%)',
            backgroundSize: '200% 100%',
          }}
        />

        {/* Scroll blur frost overlay — fades in on scroll */}
        <div className={cn(
          "absolute top-0 left-0 right-0 h-20 transition-all duration-500 pointer-events-none",
          isScrolled 
            ? "bg-white/50 backdrop-blur-md" 
            : "bg-transparent backdrop-blur-none"
        )} />

        {/* ════════════════════════════════════════════════ */}
        {/* NAV CONTENT — Sits on top of the liquid shape   */}
        {/* ════════════════════════════════════════════════ */}
        <div className="relative z-10 h-20 w-full flex items-center pointer-events-auto">
          <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full flex items-center justify-between gap-6">
            
            {/* Logo */}
            <Link to="/" className="flex items-center shrink-0 group py-1">
              <img
                src="/images/kca_logo.png"
                alt="Logo Resmi PT Kediri Chemical Abadi"
                className="h-11 sm:h-12 w-auto object-contain transition-transform group-hover:scale-105 duration-300 filter drop-shadow-sm"
              />
            </Link>

            {/* Desktop Navigation Pill Menu */}
            <nav className="hidden lg:flex items-center gap-1.5 xl:gap-2 ml-auto bg-white/50 backdrop-blur-lg p-1.5 rounded-full border border-white/40 shadow-sm">
              {NAVIGATION_DATA.navLinks.map((link) => (
                <NavLink
                  key={link.to}
                  to={link.to}
                  end={link.to === '/'}
                  className={({ isActive }) =>
                    cn(
                      'px-4 py-2 rounded-full text-xs font-heading font-extrabold uppercase tracking-wider transition-all duration-300 cursor-pointer',
                      isActive
                        ? 'text-white bg-gradient-to-r from-[#0F58A8] to-[#0284C7] shadow-sm shadow-blue-600/30'
                        : 'text-slate-700 hover:text-[#0F58A8] hover:bg-white/70'
                    )
                  }
                >
                  {link.label}
                </NavLink>
              ))}
            </nav>

            {/* Desktop CTA */}
            <div className="hidden lg:flex items-center pl-2">
              <Link to="/contact" className="btn-fluid-primary text-xs py-2 px-5">
                <span>Hubungi Lab</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </Link>
            </div>

            {/* Mobile Hamburger */}
            <div className="flex items-center lg:hidden ml-auto">
              <button
                onClick={() => setMobileOpen(!mobileOpen)}
                className="p-2.5 rounded-full text-slate-700 hover:text-[#0F58A8] hover:bg-blue-50 border border-white/40 bg-white/50 backdrop-blur-md cursor-pointer transition-colors shadow-xs"
                aria-label="Toggle Mobile Menu"
              >
                {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Mobile Dropdown */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.2 }}
            className="absolute top-20 inset-x-0 bg-white/95 backdrop-blur-xl border-b border-sky-100 shadow-xl p-6 lg:hidden z-50 pointer-events-auto"
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
