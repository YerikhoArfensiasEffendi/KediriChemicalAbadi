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

  // Mouse parallax for interactive 3D depth
  const rawMouseX = useMotionValue(0)
  const rawMouseY = useMotionValue(0)
  const mouseX = useSpring(rawMouseX, { stiffness: 50, damping: 18 })
  const mouseY = useSpring(rawMouseY, { stiffness: 50, damping: 18 })

  // Transform mouse position into parallax offsets for each layer
  const layer1X = useTransform(mouseX, [-1, 1], [-12, 12])
  const layer1Y = useTransform(mouseY, [-1, 1], [-4, 4])
  const layer2X = useTransform(mouseX, [-1, 1], [8, -8])
  const layer2Y = useTransform(mouseY, [-1, 1], [3, -3])
  const shimmerX = useTransform(mouseX, [-1, 1], [-20, 20])

  const handleMouseMove = useCallback((e) => {
    if (!headerRef.current) return
    const rect = headerRef.current.getBoundingClientRect()
    const nx = ((e.clientX - rect.left) / rect.width - 0.5) * 2
    const ny = ((e.clientY - rect.top) / rect.height - 0.5) * 2
    rawMouseX.set(nx)
    rawMouseY.set(ny)
  }, [rawMouseX, rawMouseY])

  const handleMouseLeave = useCallback(() => {
    rawMouseX.set(0)
    rawMouseY.set(0)
  }, [rawMouseX, rawMouseY])

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
      className="fixed top-0 left-0 right-0 z-50 w-full pointer-events-none select-none"
    >
      
      {/* ── LAYER 1: Soft White Depth Gradient Base ── */}
      <div className="absolute top-0 left-0 right-0 w-full h-24 sm:h-28 lg:h-32 pointer-events-none overflow-visible">
        <div className={cn(
          "w-full h-full transition-all duration-500",
          isScrolled 
            ? "bg-gradient-to-b from-white/90 via-white/60 to-transparent"
            : "bg-gradient-to-b from-white/60 via-white/25 to-transparent"
        )} />
      </div>

      {/* ── LAYER 2: Primary 3D Liquid Wave (Mouse Parallax + Flow Anim) ── */}
      <motion.div
        style={{ x: layer1X, y: layer1Y }}
        className={cn(
          "absolute -top-1 -left-4 -right-4 w-[calc(100%+32px)] h-24 sm:h-28 lg:h-32 pointer-events-none select-none overflow-visible animate-liquid-flow",
          isScrolled ? "opacity-100" : "opacity-95"
        )}
      >
        <img
          src="/images/navbar_liquid_final_4k.png"
          alt="3D Liquid Water Wave Ribbon PT Kediri Chemical Abadi"
          className="w-full h-full object-cover object-top filter drop-shadow-md"
          draggable={false}
        />
      </motion.div>

      {/* ── LAYER 3: Shadow Echo Wave (Reverse Parallax for 3D Depth) ── */}
      <motion.div
        style={{ x: layer2X, y: layer2Y }}
        className="absolute top-1 -left-2 -right-2 w-[calc(100%+16px)] h-20 sm:h-24 lg:h-28 pointer-events-none select-none overflow-visible animate-liquid-flow-reverse opacity-20 mix-blend-multiply"
      >
        <img
          src="/images/navbar_liquid_final_4k.png"
          alt=""
          aria-hidden="true"
          className="w-full h-full object-cover object-top filter blur-[1px] contrast-110"
          draggable={false}
        />
      </motion.div>

      {/* ── LAYER 4: Caustic Light Shimmer (Moving Refraction) ── */}
      <motion.div 
        style={{ x: shimmerX }}
        className="absolute top-0 left-0 right-0 w-full h-20 sm:h-24 lg:h-28 pointer-events-none overflow-visible animate-caustic-shimmer"
      >
        <div 
          className="w-full h-full"
          style={{
            background: 'linear-gradient(115deg, transparent 20%, rgba(56,189,248,0.1) 35%, rgba(255,255,255,0.18) 50%, rgba(56,189,248,0.07) 65%, transparent 80%)',
            backgroundSize: '200% 100%',
          }}
        />
      </motion.div>

      {/* ── LAYER 5: Glassmorphic Scroll Wash ── */}
      <div className={cn(
        "absolute top-0 left-0 right-0 w-full h-20 transition-all duration-400 pointer-events-none",
        isScrolled ? "bg-white/20 backdrop-blur-sm" : "bg-transparent"
      )} />

      {/* ══════════════════════════════════════════════ */}
      {/* INTERACTIVE NAVIGATION CONTENT BAR            */}
      {/* ══════════════════════════════════════════════ */}
      <div className="h-20 w-full flex items-center pointer-events-auto relative z-10">
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
          <nav className="hidden lg:flex items-center gap-1.5 xl:gap-2 ml-auto bg-white/65 backdrop-blur-lg p-1.5 rounded-full border border-white/50 shadow-sm shadow-blue-900/8">
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

          {/* Desktop CTA Button */}
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
              className="p-2.5 rounded-full text-slate-700 hover:text-[#0F58A8] hover:bg-blue-50 border border-white/50 bg-white/60 backdrop-blur-md cursor-pointer transition-colors shadow-xs"
              aria-label="Toggle Mobile Menu"
            >
              {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
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
