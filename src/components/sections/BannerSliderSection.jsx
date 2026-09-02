import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  ChevronLeft, 
  ChevronRight, 
  ArrowRight, 
  Building2, 
  Hotel, 
  HeartPulse, 
  Factory, 
  UtensilsCrossed, 
  ShieldCheck, 
  Award, 
  Landmark 
} from 'lucide-react'
import { Link } from 'react-router-dom'
import { BANNER_SLIDES } from '@/data/bannerData'

const CLIENT_LOGOS = [
  {
    name: 'RSUD & Fasilitas Medis',
    tag: 'Standar KARS',
    icon: HeartPulse,
  },
  {
    name: 'Santika & Hotel Chains',
    tag: 'Hospitality 5-Star',
    icon: Hotel,
  },
  {
    name: 'Asosiasi Laundry Indonesia',
    tag: 'Sentra B2B',
    icon: Building2,
  },
  {
    name: 'Pabrik Tekstil & Garmen',
    tag: 'Industrial Mill',
    icon: Factory,
  },
  {
    name: 'Food Processing HACCP',
    tag: 'Food Grade Safe',
    icon: UtensilsCrossed,
  },
  {
    name: 'e-Katalog LKPP RI',
    tag: 'Pengadaan Resmi',
    icon: Landmark,
  },
  {
    name: 'ISO 9001:2015 Certified',
    tag: 'Mutu Internasional',
    icon: ShieldCheck,
  },
  {
    name: 'Kemenkes RI PKRT',
    tag: 'Izin Edar Resmi',
    icon: Award,
  },
]

export default function BannerSliderSection() {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isHovered, setIsHovered] = useState(false)
  const timerRef = useRef(null)

  const slides = Array.isArray(BANNER_SLIDES) ? BANNER_SLIDES : []

  // Auto slide every 5 seconds for the main hero banner
  useEffect(() => {
    if (slides.length <= 1 || isHovered) return

    timerRef.current = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % slides.length)
    }, 5000)

    return () => clearInterval(timerRef.current)
  }, [slides.length, isHovered])

  if (slides.length === 0) return null

  const handlePrev = () => {
    setCurrentIndex((prev) => (prev - 1 + slides.length) % slides.length)
  }

  const handleNext = () => {
    setCurrentIndex((prev) => (prev + 1) % slides.length)
  }

  const currentSlide = slides[currentIndex]

  // Double the logos array for seamless infinite marquee loop
  const marqueeLogos = [...CLIENT_LOGOS, ...CLIENT_LOGOS]

  return (
    <section className="w-full bg-white relative">
      
      {/* ========================================================================= */}
      {/* 1. INFINITE SLIDING CLIENT LOGO MARQUEE (Pure Logos, Slow & Ultra-Stable)  */}
      {/* ========================================================================= */}
      <div className="w-full border-y border-slate-200/80 bg-slate-50/50 py-5 sm:py-6 overflow-hidden relative">
        
        {/* Section Label */}
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full mb-3">
          <span className="text-[10px] sm:text-[11px] font-extrabold uppercase tracking-widest text-slate-400 font-heading block">
            Mitra Industri & Sertifikasi Terpercaya
          </span>
        </div>

        {/* Left & Right Gradient Fog Masks */}
        <div className="absolute left-0 top-0 bottom-0 w-20 sm:w-32 bg-gradient-to-r from-slate-50 via-slate-50/80 to-transparent z-10 pointer-events-none" />
        <div className="absolute right-0 top-0 bottom-0 w-20 sm:w-32 bg-gradient-to-l from-slate-50 via-slate-50/80 to-transparent z-10 pointer-events-none" />

        {/* Continuous Smooth & Slow Infinite Marquee Track */}
        <motion.div
          className="flex items-center gap-10 sm:gap-16 w-max will-change-transform"
          animate={{ x: ['0%', '-50%'] }}
          transition={{
            duration: 42,
            ease: 'linear',
            repeat: Infinity,
            repeatType: 'loop',
          }}
        >
          {marqueeLogos.map((item, idx) => {
            const IconComp = item.icon

            return (
              <div
                key={idx}
                className="flex items-center gap-3 opacity-70 hover:opacity-100 transition-opacity shrink-0 cursor-default group select-none"
              >
                <div className="w-9 h-9 rounded-xl bg-slate-200/60 group-hover:bg-[#0F58A8] text-slate-700 group-hover:text-white flex items-center justify-center transition-colors shadow-2xs">
                  <IconComp className="w-5 h-5" />
                </div>
                <div className="flex flex-col leading-tight">
                  <span className="text-xs sm:text-sm font-extrabold font-heading text-slate-800 group-hover:text-[#0F58A8] transition-colors whitespace-nowrap">
                    {item.name}
                  </span>
                  <span className="text-[10px] sm:text-[11px] font-medium text-slate-400 whitespace-nowrap">
                    {item.tag}
                  </span>
                </div>
              </div>
            )
          })}
        </motion.div>

      </div>

      {/* ========================================================================= */}
      {/* 2. FULL-WIDTH EDGE-TO-EDGE BANNER SLIDER (Menempel Penuh Kiri-Kanan)       */}
      {/* ========================================================================= */}
      <div
        className="relative w-full h-64 sm:h-80 lg:h-96 xl:h-[420px] bg-slate-950 overflow-hidden group select-none"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        {/* Animated Slide Background & Content */}
        <AnimatePresence mode="wait">
          <motion.div
            key={currentSlide.id || currentIndex}
            initial={{ opacity: 0, scale: 1.05 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.98 }}
            transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
            className="absolute inset-0 w-full h-full"
          >
            {/* Edge-to-Edge Factory/Product Image */}
            <img
              src={currentSlide.image}
              alt={currentSlide.title}
              className="w-full h-full object-cover object-center opacity-45 select-none pointer-events-none"
            />

            {/* Industrial Gradient Overlays */}
            <div className="absolute inset-0 bg-gradient-to-r from-slate-950/95 via-slate-950/70 to-slate-950/20" />
            <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent" />

            {/* Text & Content Layer (Aligned to Site Container Grid) */}
            <div className="absolute inset-0 flex items-center">
              <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
                <div className="max-w-3xl space-y-3 sm:space-y-4">
                  
                  {/* Title */}
                  <h3 className="text-xl sm:text-2xl lg:text-3xl xl:text-4xl font-extrabold font-heading text-white tracking-tight leading-[1.15]">
                    {currentSlide.title}
                  </h3>

                  {/* Subtitle */}
                  <p className="text-slate-300 text-xs sm:text-sm lg:text-base leading-relaxed max-w-2xl font-normal line-clamp-2 sm:line-clamp-none">
                    {currentSlide.subtitle}
                  </p>

                  {/* Action CTA */}
                  <div className="pt-2">
                    <Link
                      to={currentSlide.ctaLink || '/products'}
                      className="inline-flex items-center gap-2 px-6 py-3 bg-[#0F58A8] hover:bg-blue-600 text-white rounded-xl text-xs font-bold font-heading uppercase tracking-wider transition-all shadow-md hover:shadow-lg w-fit cursor-pointer"
                    >
                      <span>{currentSlide.ctaText || 'Pelajari Selengkapnya'}</span>
                      <ArrowRight className="w-4 h-4" />
                    </Link>
                  </div>

                </div>
              </div>
            </div>
          </motion.div>
        </AnimatePresence>

        {/* Navigation Arrows */}
        <button
          onClick={handlePrev}
          aria-label="Slide Sebelumnya"
          className="absolute left-4 sm:left-8 top-1/2 -translate-y-1/2 w-11 h-11 rounded-full bg-slate-900/80 hover:bg-[#0F58A8] text-white/80 hover:text-white border border-white/20 flex items-center justify-center transition-all z-20 backdrop-blur-xs cursor-pointer opacity-0 group-hover:opacity-100 shadow-lg"
        >
          <ChevronLeft className="w-6 h-6" />
        </button>

        <button
          onClick={handleNext}
          aria-label="Slide Selanjutnya"
          className="absolute right-4 sm:right-8 top-1/2 -translate-y-1/2 w-11 h-11 rounded-full bg-slate-900/80 hover:bg-[#0F58A8] text-white/80 hover:text-white border border-white/20 flex items-center justify-center transition-all z-20 backdrop-blur-xs cursor-pointer opacity-0 group-hover:opacity-100 shadow-lg"
        >
          <ChevronRight className="w-6 h-6" />
        </button>

        {/* Dot Pagination */}
        <div className="absolute bottom-6 right-6 sm:right-12 lg:right-20 z-20 flex items-center gap-2">
          {slides.map((_, idx) => (
            <button
              key={idx}
              onClick={() => setCurrentIndex(idx)}
              aria-label={`Pindah ke Slide ${idx + 1}`}
              className={`h-2.5 rounded-full transition-all cursor-pointer ${
                currentIndex === idx
                  ? 'w-8 bg-[#0F58A8]'
                  : 'w-2.5 bg-white/40 hover:bg-white/80'
              }`}
            />
          ))}
        </div>

      </div>

    </section>
  )
}
