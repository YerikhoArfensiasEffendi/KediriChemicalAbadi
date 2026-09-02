import { useState, useRef } from 'react'
import { motion, useScroll, useTransform, useSpring } from 'framer-motion'
import { ArrowRight, FileDown, ChevronDown, CheckCircle2 } from 'lucide-react'
import { HERO_DATA } from '@/data/heroData'
import RFQModal from '@/components/ui/RFQModal'

export default function HeroSection() {
  const [rfqOpen, setRfqOpen] = useState(false)
  const containerRef = useRef(null)

  // Track scroll progress along the 280vh scroll track
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end'],
  })

  // Physics-based spring momentum for ultra-smooth, organic 60 FPS interpolation
  const smoothProgress = useSpring(scrollYProgress, {
    stiffness: 90,
    damping: 26,
    mass: 0.6,
    restDelta: 0.0001
  })

  // =========================================================================
  // PARALLAX BACKGROUND & AMBIENT GLOW (Terkunci stabil, bebas celah atas)
  // =========================================================================
  const bgY = useTransform(smoothProgress, [0, 1], ['0px', '0px'])
  const bgScale = useTransform(smoothProgress, [0, 1], [1.04, 1.08])
  const glowScale = useTransform(smoothProgress, [0, 1], [1, 1.2])

  // =========================================================================
  // FASE 1: INTRO PEMBUKA "PT KEDIRI CHEMICAL ABADI" (Scroll 0.0 -> 0.20)
  // Hilang total & display: none setelah lewat 0.20 (Tidak akan muncul lagi)
  // =========================================================================
  const introOpacity = useTransform(smoothProgress, [0, 0.12, 0.20], [1, 0.8, 0], { clamp: true })
  const introScale = useTransform(smoothProgress, [0, 0.20], [1, 0.94], { clamp: true })
  const introY = useTransform(smoothProgress, [0, 0.20], [0, -25], { clamp: true })
  const introDisplay = useTransform(smoothProgress, (v) => (v > 0.20 ? 'none' : 'flex'))
  const introPointerEvents = useTransform(smoothProgress, (v) => (v > 0.20 ? 'none' : 'auto'))
  const scrollIndicatorOpacity = useTransform(smoothProgress, [0, 0.08], [1, 0], { clamp: true })

  // =========================================================================
  // FASE 2 & 3: 3D PACKAGING LINEUP (Scroll 0.16 -> 0.48 -> 0.70 -> 1.0)
  // Muncul di tengah (Fase 2) -> Meluncur ke kanan (Fase 3) & Terkunci (Locked)
  // =========================================================================
  const packagingOpacity = useTransform(
    smoothProgress,
    [0, 0.16, 0.26, 1.0],
    [0, 0, 1, 1],
    { clamp: true }
  )

  const packagingScale = useTransform(
    smoothProgress,
    [0, 0.16, 0.28, 0.48, 0.68, 1.0],
    [0.55, 0.55, 0.88, 1.16, 1.0, 1.0],
    { clamp: true }
  )

  const packagingXDesktop = useTransform(
    smoothProgress,
    [0, 0.16, 0.46, 0.68, 1.0],
    ['0vw', '0vw', '0vw', '26vw', '26vw'],
    { clamp: true }
  )

  const packagingRotateY = useTransform(
    smoothProgress,
    [0, 0.16, 0.28, 0.48, 0.68, 1.0],
    [12, 12, 0, 0, -4, -4],
    { clamp: true }
  )

  const packagingRotateZ = useTransform(
    smoothProgress,
    [0, 0.16, 0.28, 0.48, 0.68, 1.0],
    [-3, -3, 0, 0, 1, 1],
    { clamp: true }
  )

  const packagingY = useTransform(
    smoothProgress,
    [0, 0.16, 0.28, 0.48, 0.68, 1.0],
    [40, 40, 0, 0, 0, 0],
    { clamp: true }
  )

  // =========================================================================
  // FASE 3: TEKS UTAMA KIRI (Scroll 0.46 -> 0.68 -> 1.0)
  // =========================================================================
  const contentOpacity = useTransform(
    smoothProgress,
    [0, 0.46, 0.68, 1.0],
    [0, 0, 1, 1],
    { clamp: true }
  )

  const contentX = useTransform(
    smoothProgress,
    [0, 0.46, 0.68, 1.0],
    [-35, -35, 0, 0],
    { clamp: true }
  )

  const contentPointerEvents = useTransform(smoothProgress, (v) => (v > 0.52 ? 'auto' : 'none'))

  return (
    <>
      {/* Scroll Track Container (280vh) */}
      <div ref={containerRef} className="relative w-full h-[280vh] bg-white -mt-20">
        
        {/* Sticky Viewport Stage */}
        <section className="sticky top-0 h-screen w-full pt-20 bg-white text-slate-900 overflow-hidden flex flex-col justify-center select-none border-b border-slate-200">
          
          {/* Real Factory Plant Floor Background (Terkunci Penuh, Zero Gap Atas) */}
          <motion.div 
            style={{ y: bgY, scale: bgScale }}
            className="absolute -top-12 -bottom-12 -left-6 -right-6 w-[calc(100%+48px)] h-[calc(100%+96px)] z-0 pointer-events-none overflow-hidden origin-center will-change-transform"
          >
            <img
              src="/images/kca_factory_floor.jpg"
              alt="Fasilitas Reaktor & Lini Produksi Pabrik PT Kediri Chemical Abadi"
              className="w-full h-full object-cover object-center opacity-75"
            />
            {/* Gradasi Lembut Bersih */}
            <div className="absolute inset-0 bg-gradient-to-r from-white/85 via-white/50 to-white/20" />
            <div className="absolute inset-0 bg-white/15" />
          </motion.div>

          {/* Soft Royal Blue Ambient Glow dengan Parallax Scaling */}
          <motion.div 
            style={{ scale: glowScale }}
            className="absolute -top-32 right-0 w-[600px] h-[600px] bg-blue-100/50 rounded-full blur-3xl pointer-events-none z-0" 
          />

          {/* Ambient 4K Liquid Water Caustics & Ripple Texture (Tema Air Higienis & Segar) */}
          <div className="absolute -top-12 -bottom-12 -left-6 -right-6 w-[calc(100%+48px)] h-[calc(100%+96px)] z-0 pointer-events-none overflow-hidden select-none opacity-35 mix-blend-multiply">
            <img
              src="/images/bg_liquid_caustics_4k.png"
              alt="Liquid Water Caustics Texture"
              className="w-full h-full object-cover object-top filter contrast-105"
            />
          </div>

          {/* ========================================================= */}
          {/* FASE 1: INTRO PEMBUKA "PT KEDIRI CHEMICAL ABADI"          */}
          {/* (Aktif HANYA di awal scroll 0 -> 0.20, lalu lenyap total)  */}
          {/* ========================================================= */}
          <motion.div
            style={{
              opacity: introOpacity,
              scale: introScale,
              y: introY,
              display: introDisplay,
              pointerEvents: introPointerEvents,
            }}
            className="absolute inset-0 z-20 flex flex-col items-center justify-center text-center px-4 pt-16"
          >
            <div className="max-w-3xl mx-auto space-y-4">
              <h2 className="text-2xl sm:text-4xl lg:text-5xl font-extrabold font-heading tracking-tight leading-tight">
                <span className="text-[#0F58A8]">PT KEDIRI</span>{' '}
                <span className="text-red-600">CHEMICAL ABADI</span>
              </h2>
              <p className="text-xs sm:text-sm lg:text-base text-slate-600 max-w-xl mx-auto font-normal leading-relaxed">
                Pusat riset &amp; manufaktur kimia pembersih industri konsentrat 100% non-fosfat terpercaya sejak 2004 di Mojoroto, Kediri.
              </p>

              {/* Scroll Indicator Prompt (Clean Typography & Chevron Tanpa Kotak Card) */}
              <motion.div
                style={{ opacity: scrollIndicatorOpacity }}
                className="pt-5 flex flex-col items-center justify-center gap-1.5 pointer-events-none"
              >
                <span className="text-xs font-heading font-extrabold uppercase tracking-widest text-slate-700">
                  Scroll Ke Bawah Untuk Eksplorasi
                </span>
                <ChevronDown className="w-4 h-4 text-[#0F58A8] animate-bounce stroke-[2.5]" />
              </motion.div>
            </div>
          </motion.div>

          {/* ========================================================= */}
          {/* FASE 2 & FASE 3: STAGE UTAMA (TEKS KIRI & PACKAGING 3D)   */}
          {/* ========================================================= */}
          <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-30 h-full flex items-center pt-8 sm:pt-0">
            
            {/* Grid Konten Kiri (FASE 3: Muncul saat scroll > 0.46) */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 xl:gap-16 items-center w-full relative">
              
              <motion.div
                style={{
                  opacity: contentOpacity,
                  x: contentX,
                  pointerEvents: contentPointerEvents,
                }}
                className="lg:col-span-6 xl:col-span-6 flex flex-col justify-center space-y-6"
              >
                <h1 className="text-2xl sm:text-3xl lg:text-4xl xl:text-5xl font-extrabold font-heading text-slate-900 tracking-tight leading-[1.15]">
                  Mitra Terpercaya Manufaktur &amp;{' '}
                  <span className="text-[#0F58A8]">
                    Formulasi Kimia Industri
                  </span>
                </h1>

                <p className="text-slate-700 text-xs sm:text-sm lg:text-base leading-relaxed max-w-xl font-normal">
                  {HERO_DATA.subtitle || 'Pusat riset dan manufaktur kimia pembersih konsentrat 100% non-fosfat berkapasitas 500+ Ton/bulan di Mojoroto, Kediri. Solusi pasokan massal B2B dan layanan maklon private label terpercaya.'}
                </p>

                {/* Fluid Pill Action Buttons (Water Sheen Theme) */}
                <div className="pt-2 flex items-center gap-3 flex-wrap">
                  <button
                    onClick={() => setRfqOpen(true)}
                    className="btn-fluid-primary"
                  >
                    <span>Minta Penawaran Resmi</span>
                    <ArrowRight className="w-4 h-4" />
                  </button>

                  <a
                    href="#makloon"
                    className="btn-fluid-secondary"
                  >
                    <span>Layanan Maklon</span>
                  </a>
                </div>
              </motion.div>

              <div className="hidden lg:block lg:col-span-6 xl:col-span-6" />
            </div>

            {/* ======================================================= */}
            {/* 3D PACKAGING ACTOR DENGAN AMBIENT FLOAT                 */}
            {/* ======================================================= */}
            <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-40 px-4">
              <motion.div
                style={{
                  opacity: packagingOpacity,
                  scale: packagingScale,
                  x: packagingXDesktop,
                  y: packagingY,
                  rotateY: packagingRotateY,
                  rotateZ: packagingRotateZ,
                  transformPerspective: 1200,
                }}
                className="relative w-full max-w-[420px] sm:max-w-[540px] lg:max-w-[620px] xl:max-w-[680px] origin-center will-change-transform"
              >
                <motion.div
                  animate={{ y: [0, -7, 0] }}
                  transition={{ repeat: Infinity, duration: 4.5, ease: 'easeInOut' }}
                >
                  <img
                    src="/images/kca_packaging_lineup.png"
                    alt="Lini Kemasan Produk PT Kediri Chemical Abadi"
                    className="w-full h-auto object-contain drop-shadow-2xl select-none"
                  />
                </motion.div>
              </motion.div>
            </div>

          </div>

          {/* ========================================================= */}
          {/* SEAMLESS GRADIENT & S-CURVE TRANSITION INTO NEXT SECTION */}
          {/* ========================================================= */}
          <div className="absolute bottom-0 inset-x-0 z-20 pointer-events-none leading-none">
            <div className="h-28 sm:h-36 w-full bg-gradient-to-t from-white via-white/80 to-transparent" />
            
            <svg
              className="relative block w-full h-8 sm:h-12 lg:h-14 text-white -mt-6 sm:-mt-8 lg:-mt-10"
              viewBox="0 0 1440 120"
              preserveAspectRatio="none"
            >
              <path
                d="M0,32 C360,95 620,10 980,60 C1200,90 1360,45 1440,55 L1440,120 L0,120 Z"
                fill="currentColor"
              />
            </svg>
          </div>

        </section>
      </div>

      {/* RFQ Modal */}
      <RFQModal isOpen={rfqOpen} onClose={() => setRfqOpen(false)} />
    </>
  )
}
