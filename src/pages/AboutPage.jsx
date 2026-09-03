import { useState, useEffect, useRef, useCallback } from 'react'
import { Helmet } from 'react-helmet-async'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  Building2, 
  Award, 
  ShieldCheck, 
  CheckCircle2, 
  Factory, 
  FlaskConical, 
  Droplets, 
  Leaf, 
  MousePointer2,
  ChevronDown,
  ArrowRight
} from 'lucide-react'
import { Link } from 'react-router-dom'
import { COMPANY_DATA } from '@/data/companyData'

const SLIDES = [
  // SLIDE 0: HERO BANNER SEJARAH KAMI
  {
    type: 'hero',
    id: 'hero',
    label: 'Pembuka',
    title: 'SEJARAH KAMI',
    subtitle: 'Fasilitas Reaktor Pencampur & Pusat Riset Formulasi • Mojoroto, Kediri',
    image: '/images/kca_factory_reactors.jpg'
  },
  // SLIDE 1: NARASI PENGANTAR (PROLOG / LATAR BELAKANG)
  {
    type: 'prologue',
    id: 'prologue',
    label: 'Latar Belakang',
    title: 'PERJALANAN PANJANG DARI SEBUAH REAKTOR PEMBERSIH KONSENTRAT',
    subtitle: 'INDUSTRI KIMIA YANG BERMANFAAT BAGI MITRA BISNIS DAN LINGKUNGAN',
    desc1: 'Mengawali usaha dari sebuah unit reaktor pencampur sederhana di Mojoroto, Kota Kediri, Jawa Timur, di sinilah titik awal perjalanan usaha manufaktur kimia pembersih didirikan oleh Bapak Yan Effendi pada tahun 2004.',
    desc2: 'Berangkat dari keprihatinan mendalam terhadap tingginya kesadahan air tanah lokal (>350 ppm CaCO₃) yang kerap mematikan daya pembersih deterjen dan merusak mesin cuci laundry lokal, beliau mendedikasikan riset formulasi konsentrat murni yang stabil terhadap ion sadah.',
    desc3: 'Komitmen mutu ini dilanjutkan dan diperkuat oleh Bapak Yerikho Arfensias Effendi melalui sertifikasi Sistem Manajemen Mutu ISO 9001:2015, izin edar PKRT Kemenkes RI, dan kapasitas produksi massal melampaui 500+ Ton per bulan.'
  },
  // SLIDE 2: TAHUN 2004
  {
    type: 'timeline',
    id: '2004',
    label: '2004',
    year: '2004',
    badge: 'Fase 01 • Pendirian & Riset Air Sadah',
    title: 'Titik Mula di Mojoroto: Menaklukkan Kesadahan Air Jawa Timur',
    desc: 'Didirikan oleh Yan Effendi di Mojoroto, Kota Kediri dengan modal 1 unit reaktor manual 500 Liter. Menjawab kendala busa mati dan serat kain menguning akibat tingginya kesadahan air tanah Jawa Timur (>350 ppm CaCO₃).',
    details: 'Yan Effendi berhasil merekayasa formula agen pengkhelat murni (sequestering agent) pertama di Kediri yang mengikat ion kalsium & magnesium secara stabil tanpa merusak serat kain.',
    highlights: [
      'Operasional reaktor perdana 500L dengan kontrol pemanasan terukur',
      'Riset adaptasi formula terhadap kesadahan air lokal 300–450 ppm',
      'Penyaluran perdana ke puluhan sentra laundry komersial Karesidenan Kediri'
    ],
    breakthrough: 'Formulasi surfaktan stabil air sadah pertama yang menekan pemborosan dosis hingga 40%.',
    image: '/images/kca_factory_reactors.jpg',
    imageCaption: 'Reaktor Pencampur Perdana KCA di Mojoroto, Kediri (Est. 2004)',
    align: 'left'
  },
  // SLIDE 3: TAHUN 2008
  {
    type: 'timeline',
    id: '2008',
    label: '2008',
    year: '2008',
    badge: 'Fase 02 • Inovasi Hijau & Reaktor Stainless',
    title: 'Terobosan Formula 100% Bebas Fosfat & Tangki SS 316L Pertama',
    desc: 'Di tengah maraknya deterjen industri murah berbasis STPP (senyawa fosfat perusak ekosistem perairan), KCA mengambil komitmen tegas menghentikan total penggunaan bahan fosfat dan mengoperasikan reaktor Stainless Steel 316L pertama.',
    details: 'Sinergi surfaktan non-ionik murni dan enzim pembersih ramah lingkungan menghasilkan daya angkat noda minyak berat yang tinggi namun sepenuhnya aman terhadap biofilter IPAL.',
    highlights: [
      'Instalasi reaktor Stainless Steel 316L tahan korosi asam dan basa pekat',
      'Standarisasi formula 100% bebas STPP (mencegah pencemaran perairan)',
      'Konsistensi efisiensi dosis stabil pada 10–15 ml per kilogram cucian'
    ],
    breakthrough: 'Pelopor formula deterjen ramah ekosistem air di Kediri dengan efisiensi dosis tinggi.',
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Lini Manufaktur Formulasi Ramah Lingkungan Bebas Fosfat Berstandar Mutu',
    align: 'right'
  },
  // SLIDE 4: TAHUN 2014
  {
    type: 'timeline',
    id: '2014',
    label: '2014',
    year: '2014',
    badge: 'Fase 03 • Standarisasi Medis & Kelayakan IPAL',
    title: 'Penetrasi Rumah Sakit Rujukan & Kelayakan Biofilter IPAL KARS',
    desc: 'KCA memasuki sektor higienitas medis dengan memformulasi deterjen disinfektan dan alkali builder khusus pencucian linen ruang isolasi, bedah, dan rawat inap rumah sakit.',
    details: 'Menggunakan biosurfaktan yang terurai secara alami (>90% biodegradasi OECD 301D) dipadukan dengan senyawa oksigen aktif untuk disinfeksi termokimia tanpa merusak serat kain linen medis.',
    highlights: [
      'Lolos uji baku mutu limbah cair pada sistem IPAL biofilter rumah sakit',
      'Penyediaan formula Alkali Booster, Emulsifier Noda Darah, dan Oxy Bleach',
      'Kemitraan resmi dengan puluhan RSUD dan RS swasta se-Jawa Timur'
    ],
    breakthrough: 'Standar mutu linen medis lolos uji akreditasi KARS dengan nol risiko kerusakan IPAL.',
    image: '/images/product_jerigen5l.jpg',
    imageCaption: 'Produk Kimia Higienitas Medis & Pembersih Konsentrat Ramah Biofilter IPAL RS',
    align: 'left'
  },
  // SLIDE 5: TAHUN 2019
  {
    type: 'timeline',
    id: '2019',
    label: '2019',
    year: '2019',
    badge: 'Fase 04 • Modernisasi Demin RO & Dedicated Line VIP',
    title: 'Instalasi Demin RO 50.000 L/Hari & Skema Reaktor Dedikasi',
    desc: 'Menjawab lonjakan kebutuhan maklon private label brand nasional, KCA membangun fasilitas pengolahan air Reverse Osmosis (RO) dan demineralisasi berkapasitas 50.000 Liter/hari (<5 ppm TDS).',
    details: 'Penggunaan air demineralisasi murni memastikan kemurnian reaktif bahan aktif surfaktan mencapai tingkat optimal dan memperpanjang masa simpan produk jadi hingga lebih dari 24 bulan tanpa degradasi.',
    highlights: [
      'Pembangunan instalasi Double-Stage RO & Mixed-Bed Resin (<5 ppm TDS)',
      'Peningkatan kapasitas total pabrik melampaui 500+ Ton konsentrat per bulan',
      'Peluncuran skema Dedicated Line maklon dengan jaminan kerahasiaan NDA'
    ],
    breakthrough: 'Pabrik kimia di Jawa Timur dengan fasilitas air demin mandiri dan kapasitas skala besar.',
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Instalasi Pengolahan Air Demineralisasi RO 50.000 L/Hari & Reaktor Kapasitas 500+ Ton/Bln',
    align: 'right'
  },
  // SLIDE 6: TAHUN 2024-2026 (SLIDE TAHUN TERAKHIR)
  {
    type: 'timeline',
    id: '2026',
    label: '2026',
    year: '2024–2026',
    badge: 'Fase 05 • Era Manajemen Modern & ISO 9001',
    title: 'Kepemimpinan Generasi Kedua, Standar ISO 9001 & Izin Edar PKRT',
    desc: 'Estafet kepemimpinan di bawah Yerikho Arfensias Effendi mempercepat transformasi tata kelola korporat, sertifikasi Sistem Manajemen Mutu ISO 9001:2015, dan integrasi rantai pasok digital.',
    details: 'Penerapan standar titrasi digital QC laboratorium, kepatuhan perpajakan e-Faktur PPN 11%, dan kesiapan pengadaan tender pemerintah di platform e-Katalog LKPP RI.',
    highlights: [
      'Sertifikasi Sistem Manajemen Mutu ISO 9001:2015 untuk konsistensi batch',
      'Kelengkapan izin edar PKRT Kemenkes RI untuk seluruh lini sabun & pembersih',
      'Kesiapan tender nasional e-Katalog LKPP RI dan ekspansi distribusi logistik antarpulau'
    ],
    breakthrough: 'Produsen kimia konsentrat terpercaya dengan legalitas lengkap dan kapasitas industri 500+ Ton.',
    image: '/images/kca_packaging_lineup.png',
    imageCaption: 'Lini Produk Resmi & Fasilitas Lab PT Kediri Chemical Abadi Standar ISO 9001:2015',
    align: 'left'
  },
  // SLIDE 7: DEWAN DIREKSI & TATA KELOLA KORPORAT
  {
    type: 'directors',
    id: 'directors',
    label: 'Direksi'
  },
  // SLIDE 8: KOMITMEN ESG & PENUTUP
  {
    type: 'esg',
    id: 'esg',
    label: 'Prinsip'
  }
]

export default function AboutPage() {
  const [currentIdx, setCurrentIdx] = useState(0)
  const [isTransitioning, setIsTransitioning] = useState(false)
  const [direction, setDirection] = useState(1) // 1 = scroll down, -1 = scroll up
  const [isPushingPrologue, setIsPushingPrologue] = useState(false)
  const [isLeavingTimeline, setIsLeavingTimeline] = useState(false)
  const containerRef = useRef(null)

  const changeSlide = useCallback((newIdx, dir = 1) => {
    if (newIdx < 0 || newIdx >= SLIDES.length || isTransitioning || isPushingPrologue || isLeavingTimeline) return

    // JEMBATAN MASUK SINEMATIK: Dari Latar Belakang (1) ke Tahun 2004 (2)
    if (currentIdx === 1 && newIdx === 2 && dir === 1) {
      setIsTransitioning(true)
      setIsPushingPrologue(true)
      setDirection(1)

      setTimeout(() => {
        setIsPushingPrologue(false)
        setCurrentIdx(2)
        setTimeout(() => {
          setIsTransitioning(false)
        }, 800)
      }, 700)
      return
    }

    // JEMBATAN KELUAR SINEMATIK: Dari Tahun Terakhir 2026 (6) ke Direksi (7)
    // Garis terakhir dan konten 2026 melayang naik meninggalkan linimasa sebelum masuk Direksi
    if (currentIdx === 6 && newIdx === 7 && dir === 1) {
      setIsTransitioning(true)
      setIsLeavingTimeline(true)
      setDirection(1)

      setTimeout(() => {
        setIsLeavingTimeline(false)
        setCurrentIdx(7)
        setTimeout(() => {
          setIsTransitioning(false)
        }, 850)
      }, 700)
      return
    }

    // Pergantian Slide Standar
    setIsTransitioning(true)
    setDirection(dir)
    setCurrentIdx(newIdx)
    setTimeout(() => {
      setIsTransitioning(false)
    }, 950)
  }, [currentIdx, isTransitioning, isPushingPrologue, isLeavingTimeline])

  const nextSlide = useCallback(() => {
    if (currentIdx < SLIDES.length - 1) {
      changeSlide(currentIdx + 1, 1)
    }
  }, [currentIdx, changeSlide])

  const prevSlide = useCallback(() => {
    if (currentIdx > 0) {
      changeSlide(currentIdx - 1, -1)
    }
  }, [currentIdx, changeSlide])

  // Pause Lenis while on Section-Locked AboutPage
  useEffect(() => {
    window.__lenis?.stop()
    return () => {
      window.__lenis?.start()
    }
  }, [])

  // Responsif & Ringan: 1 Sentuhan Scroll Langsung Berpindah Halus
  useEffect(() => {
    let lastScrollTime = 0

    const handleWheel = (e) => {
      e.preventDefault()
      const now = Date.now()
      if (now - lastScrollTime < 850) return
      
      if (Math.abs(e.deltaY) > 10) {
        lastScrollTime = now
        if (e.deltaY > 0) {
          nextSlide()
        } else {
          prevSlide()
        }
      }
    }

    const handleKeyDown = (e) => {
      if (e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ') {
        e.preventDefault()
        nextSlide()
      } else if (e.key === 'ArrowUp' || e.key === 'PageUp') {
        e.preventDefault()
        prevSlide()
      }
    }

    let touchStartY = 0
    const handleTouchStart = (e) => {
      touchStartY = e.touches[0].clientY
    }
    const handleTouchEnd = (e) => {
      const touchEndY = e.changedTouches[0].clientY
      const diff = touchStartY - touchEndY
      if (Math.abs(diff) > 25) {
        if (diff > 0) {
          nextSlide()
        } else {
          prevSlide()
        }
      }
    }

    const container = containerRef.current
    if (container) {
      container.addEventListener('wheel', handleWheel, { passive: false })
      container.addEventListener('touchstart', handleTouchStart, { passive: true })
      container.addEventListener('touchend', handleTouchEnd, { passive: true })
    }
    window.addEventListener('keydown', handleKeyDown)

    return () => {
      if (container) {
        container.removeEventListener('wheel', handleWheel)
        container.removeEventListener('touchstart', handleTouchStart)
        container.removeEventListener('touchend', handleTouchEnd)
      }
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [nextSlide, prevSlide])

  const currentSlide = SLIDES[currentIdx]
  const isTimeline = currentSlide.type === 'timeline'
  const isLastTimelineYear = currentSlide.id === '2026'

  return (
    <main 
      ref={containerRef} 
      className="h-screen w-screen overflow-hidden bg-white text-slate-900 pt-20 relative select-none flex flex-col justify-between"
    >
      <Helmet>
        <title>Sejarah & Profil Perusahaan — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Perjalanan sejarah PT Kediri Chemical Abadi sejak 2004 dari pabrik reaktor di Mojoroto, Kediri hingga menjadi pusat manufaktur kimia pembersih berkapasitas 500+ Ton/bulan berstandar ISO 9001:2015."
        />
        <meta name="author" content="Yerikho Arfensias Effendi" />
      </Helmet>

      {/* ═════════════════════════════════════════════════════════════════════ */}
      {/* GARIS TENGAH PERMANEN (HANYA DI BAGIAN TIMELINE)                     */}
      {/* PADA 2026: BERHENTI DI TENGAH (h-1/2) SEBAGAI GARIS TERAKHIR!         */}
      {/* ═════════════════════════════════════════════════════════════════════ */}
      {isTimeline && (
        <motion.div 
          animate={isLeavingTimeline ? { y: -160, opacity: 0 } : { y: 0, opacity: 1 }}
          transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          className="hidden lg:block absolute left-1/2 -translate-x-1/2 top-0 bottom-0 w-[2px] pointer-events-none z-0"
        >
          {/* Garis Dasar Abu-abu Halus: Jika slide terakhir 2026, berhenti di tengah (h-1/2)! */}
          <div className={`w-full ${isLastTimelineYear ? 'h-1/2' : 'h-full'} bg-slate-200 transition-all duration-500`} />
          {/* Garis Aksen Biru Korporat Halus */}
          <div className={`absolute inset-0 w-full ${isLastTimelineYear ? 'h-1/2' : 'h-full'} bg-[#0F58A8]/60 transition-all duration-500`} />
        </motion.div>
      )}

      {/* ═════════════════════════════════════════════════════════════════════ */}
      {/* TITIK PEMBERHENTIAN (NODE BULLET) TEPAT DI TENGAH LAYAR (DEAD-CENTER) */}
      {/* MELUNCUR NAIK TINGGI KE ATAS (-80PX) & MUNCUL DARI BAWAH (+80PX)     */}
      {/* ═════════════════════════════════════════════════════════════════════ */}
      {isTimeline && (
        <motion.div 
          animate={isLeavingTimeline ? { y: -160, opacity: 0 } : { y: 0, opacity: 1 }}
          transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          className="hidden lg:flex absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 z-0 pointer-events-none items-center justify-center"
        >
          <AnimatePresence mode="wait">
            <motion.div
              key={`node-${currentSlide.id}`}
              initial={{ 
                opacity: 0, 
                y: direction > 0 ? 80 : -80,
                scale: 0.75
              }}
              animate={{ 
                opacity: 1, 
                y: 0, 
                scale: 1 
              }}
              exit={{ 
                opacity: 0, 
                y: direction > 0 ? -80 : 80,
                scale: 0.75
              }}
              transition={{ 
                duration: 0.85, 
                ease: [0.16, 1, 0.3, 1] 
              }}
              className={`w-5 h-5 rounded-full border-2 border-[#0F58A8] bg-white flex items-center justify-center shadow-xs ${
                isLastTimelineYear ? 'ring-4 ring-blue-100/90' : ''
              }`}
            >
              <div className="w-2 h-2 rounded-full bg-[#0F58A8]" />
            </motion.div>
          </AnimatePresence>
        </motion.div>
      )}

      {/* ═════════════════════════════════════════════════════════════════════ */}
      {/* PANGGUNG PRESENTASI: FADE OUT LEBIH PELAN & LEBIH JAUH KE ATAS (-120PX)*/}
      {/* ═════════════════════════════════════════════════════════════════════ */}
      <div className="flex-1 w-full h-full relative overflow-hidden flex items-center justify-center">
        <AnimatePresence mode="wait" custom={direction}>
          <motion.div
            key={currentSlide.id}
            custom={direction}
            initial={{ 
              opacity: 0, 
              y: direction > 0 ? 90 : -90,
              scale: 0.985
            }}
            animate={{ 
              opacity: 1, 
              y: 0, 
              scale: 1 
            }}
            exit={{ 
              opacity: 0, 
              y: direction > 0 ? -120 : 120,
              scale: 0.985
            }}
            transition={{ 
              duration: 0.88, 
              ease: [0.16, 1, 0.3, 1] 
            }}
            className="w-full h-full flex items-center justify-center px-4 sm:px-8 lg:px-16 relative"
          >
            <motion.div 
              animate={isLeavingTimeline ? { y: -160, opacity: 0 } : {}}
              transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
              className="max-w-6xl mx-auto w-full relative z-10"
            >

              {/* 1. HERO SLIDE */}
              {currentSlide.type === 'hero' && (
                <div className="max-w-5xl mx-auto w-full text-center space-y-6 sm:space-y-8">
                  {/* Judul Muncul Halus & Tenang */}
                  <motion.div 
                    initial={{ opacity: 0, y: 40 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -80 }}
                    transition={{ duration: 0.85, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                    className="flex items-center justify-center gap-4 sm:gap-8"
                  >
                    <div className="h-[1.5px] bg-slate-300 w-16 sm:w-32 lg:w-48" />
                    <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold font-heading tracking-[0.18em] text-[#0F58A8] uppercase">
                      {currentSlide.title}
                    </h1>
                    <div className="h-[1.5px] bg-slate-300 w-16 sm:w-32 lg:w-48" />
                  </motion.div>

                  {/* Foto Mosaik Muncul Paralaks dari Bawah */}
                  <motion.div 
                    initial={{ opacity: 0, y: 60, scale: 0.97 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -100, scale: 0.97 }}
                    transition={{ duration: 0.9, delay: 0.25, ease: [0.16, 1, 0.3, 1] }}
                    className="relative overflow-hidden rounded-xl border border-slate-200/90 shadow-md bg-slate-100 aspect-[21/9]"
                  >
                    <img
                      src={currentSlide.image}
                      alt={currentSlide.title}
                      className="w-full h-full object-cover filter brightness-[0.98] contrast-[1.03]"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-slate-900/40 via-transparent to-transparent pointer-events-none" />
                    <div className="absolute bottom-3 left-4 sm:left-6 text-white text-xs sm:text-sm font-heading font-medium drop-shadow-sm">
                      {currentSlide.subtitle}
                    </div>
                  </motion.div>
                </div>
              )}

              {/* 2. PROLOGUE / LATAR BELAKANG */}
              {currentSlide.type === 'prologue' && (
                <div className="max-w-4xl mx-auto w-full text-center space-y-6 relative">
                  {/* GARIS PENDORONG YANG MUNCUL TERLEBIH DAHULU MENUJU TAHUN 2004 */}
                  {isPushingPrologue && (
                    <div className="hidden lg:block fixed left-1/2 -translate-x-1/2 top-0 bottom-0 w-[2px] pointer-events-none z-0">
                      <div className="w-full h-full bg-slate-200" />
                      <motion.div
                        initial={{ scaleY: 0, originY: 1 }}
                        animate={{ scaleY: 1, originY: 1 }}
                        transition={{ duration: 0.65, ease: [0.16, 1, 0.3, 1] }}
                        className="absolute inset-0 w-full bg-[#0F58A8] origin-bottom shadow-xs"
                      />
                    </div>
                  )}

                  {/* KONTEN LATAR BELAKANG TERDORONG NAIK HINGGA FADE OUT */}
                  <motion.div
                    animate={isPushingPrologue ? { y: -180, opacity: 0 } : { y: 0, opacity: 1 }}
                    transition={{ duration: 0.65, ease: [0.16, 1, 0.3, 1] }}
                    className="space-y-6 relative z-10"
                  >
                    {/* Judul */}
                    <div className="space-y-2.5">
                      <h2 className="text-base sm:text-lg lg:text-xl font-bold font-heading uppercase tracking-wider text-[#0F58A8]">
                        {currentSlide.title}
                      </h2>
                      <h3 className="text-sm sm:text-base font-bold font-heading uppercase tracking-wide text-slate-900">
                        {currentSlide.subtitle}
                      </h3>
                    </div>

                    {/* Paragraf Latar Belakang */}
                    <div className="text-sm sm:text-[15.5px] text-slate-800 leading-[1.85] font-normal text-justify sm:text-center space-y-4 max-w-3xl mx-auto">
                      <p>{currentSlide.desc1}</p>
                      <p>{currentSlide.desc2}</p>
                      <p>{currentSlide.desc3}</p>
                    </div>
                  </motion.div>
                </div>
              )}

              {/* 3. TIMELINE TAHUN: MASUK BERGANTIAN (FOTO -> TULISAN) SECARA KALEM */}
              {currentSlide.type === 'timeline' && (
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-center relative z-20">
                  
                  {/* GANJIL: FOTO KIRI, TULISAN KANAN */}
                  {currentSlide.align === 'left' && (
                    <>
                      {/* LANGKAH 1: FOTO MUNCUL PARALAKS PERLAHAN DARI BAWAH, KELUAR NAIK KE ATAS (-100PX) */}
                      <motion.div 
                        initial={{ opacity: 0, y: 60, scale: 0.97 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -100, scale: 0.97 }}
                        transition={{ duration: 0.9, delay: 0.25, ease: [0.16, 1, 0.3, 1] }}
                        className="lg:col-span-6 order-2 lg:order-1 flex justify-center lg:justify-end relative z-20"
                      >
                        <div className="relative p-2.5 sm:p-3 bg-white border border-slate-200/90 shadow-md rounded-lg max-w-md w-full group">
                          <div className="overflow-hidden rounded aspect-[16/11] bg-slate-100">
                            <img
                              src={currentSlide.image}
                              alt={currentSlide.year}
                              className="w-full h-full object-cover select-none group-hover:scale-103 transition-transform duration-700 ease-out"
                            />
                          </div>
                          <div className="pt-2 text-center text-xs font-heading font-medium text-slate-600">
                            {currentSlide.imageCaption}
                          </div>
                        </div>
                      </motion.div>

                      {/* LANGKAH 2: TULISAN MUNCUL BERGANTIAN SECARA TENANG, KELUAR NAIK KE ATAS (-90PX) */}
                      <motion.div 
                        initial={{ opacity: 0, y: 50 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -90 }}
                        transition={{ duration: 0.9, delay: 0.45, ease: [0.16, 1, 0.3, 1] }}
                        className="lg:col-span-6 order-1 lg:order-2 space-y-3.5 lg:pl-6 text-left relative z-20"
                      >
                        {/* Tahun & Badge */}
                        <div className="space-y-1">
                          <span className="text-[11px] font-bold font-heading uppercase tracking-widest text-slate-500 block">
                            {currentSlide.badge}
                          </span>
                          <h3 className="text-3xl sm:text-4xl lg:text-[44px] font-bold font-heading text-[#0F58A8] tracking-tight leading-none flex items-center gap-3">
                            <span>{currentSlide.year}</span>
                            <span className="text-xs font-mono font-normal px-2.5 py-0.5 rounded-full bg-blue-50 text-[#0F58A8] border border-blue-200">
                              {isLastTimelineYear ? 'Masa Kini & Masa Depan' : 'Tonggak Sejarah'}
                            </span>
                          </h3>
                        </div>

                        {/* Judul & Narasi */}
                        <div className="space-y-2">
                          <h4 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                            {currentSlide.title}
                          </h4>
                          <p className="text-sm sm:text-[15px] text-slate-800 leading-[1.8] font-normal">
                            {currentSlide.desc}
                          </p>
                          <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                            {currentSlide.details}
                          </p>
                        </div>

                        {/* Poin Pencapaian */}
                        <div className="pt-2 border-t border-slate-100 space-y-1.5">
                          {currentSlide.highlights.map((h, hIdx) => (
                            <div key={hIdx} className="flex items-start gap-2 text-xs sm:text-sm text-slate-700">
                              <CheckCircle2 className="w-4 h-4 text-[#0F58A8] shrink-0 mt-0.5" />
                              <span className="leading-snug">{h}</span>
                            </div>
                          ))}
                        </div>

                        {/* Box Terobosan */}
                        <div className="p-3 bg-blue-50/70 border-l-2 border-[#0F58A8] rounded-r text-xs sm:text-sm text-slate-800 font-medium leading-relaxed">
                          <strong className="text-slate-900">Pencapaian:</strong> {currentSlide.breakthrough}
                        </div>
                      </motion.div>
                    </>
                  )}

                  {/* GENAP: TULISAN KIRI, FOTO KANAN */}
                  {currentSlide.align === 'right' && (
                    <>
                      {/* LANGKAH 2: TULISAN MUNCUL BERGANTIAN SECARA TENANG (RATA KANAN), KELUAR NAIK KE ATAS (-90PX) */}
                      <motion.div 
                        initial={{ opacity: 0, y: 50 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -90 }}
                        transition={{ duration: 0.9, delay: 0.45, ease: [0.16, 1, 0.3, 1] }}
                        className="lg:col-span-6 order-1 lg:order-1 space-y-3.5 lg:pr-6 text-left lg:text-right flex flex-col lg:items-end relative z-20"
                      >
                        {/* Tahun & Badge */}
                        <div className="space-y-1">
                          <span className="text-[11px] font-bold font-heading uppercase tracking-widest text-slate-500 block">
                            {currentSlide.badge}
                          </span>
                          <h3 className="text-3xl sm:text-4xl lg:text-[44px] font-bold font-heading text-[#0F58A8] tracking-tight leading-none flex items-center gap-3 lg:flex-row-reverse">
                            <span>{currentSlide.year}</span>
                            <span className="text-xs font-mono font-normal px-2.5 py-0.5 rounded-full bg-blue-50 text-[#0F58A8] border border-blue-200">
                              Tonggak Sejarah
                            </span>
                          </h3>
                        </div>

                        {/* Judul & Narasi */}
                        <div className="space-y-2">
                          <h4 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                            {currentSlide.title}
                          </h4>
                          <p className="text-sm sm:text-[15px] text-slate-800 leading-[1.8] font-normal">
                            {currentSlide.desc}
                          </p>
                          <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                            {currentSlide.details}
                          </p>
                        </div>

                        {/* Poin Pencapaian */}
                        <div className="pt-2 border-t border-slate-100 space-y-1.5 flex flex-col lg:items-end">
                          {currentSlide.highlights.map((h, hIdx) => (
                            <div key={hIdx} className="flex items-start gap-2 text-xs sm:text-sm text-slate-700 lg:flex-row-reverse text-left lg:text-right">
                              <CheckCircle2 className="w-4 h-4 text-[#0F58A8] shrink-0 mt-0.5" />
                              <span className="leading-snug">{h}</span>
                            </div>
                          ))}
                        </div>

                        {/* Box Terobosan */}
                        <div className="p-3 bg-blue-50/70 border-l-2 lg:border-l-0 lg:border-r-2 border-[#0F58A8] rounded-r lg:rounded-r-none lg:rounded-l text-xs sm:text-sm text-slate-800 font-medium leading-relaxed text-left lg:text-right">
                          <strong className="text-slate-900">Pencapaian:</strong> {currentSlide.breakthrough}
                        </div>
                      </motion.div>

                      {/* LANGKAH 1: FOTO MUNCUL PARALAKS PERLAHAN DARI BAWAH, KELUAR NAIK KE ATAS (-100PX) */}
                      <motion.div 
                        initial={{ opacity: 0, y: 60, scale: 0.97 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -100, scale: 0.97 }}
                        transition={{ duration: 0.9, delay: 0.25, ease: [0.16, 1, 0.3, 1] }}
                        className="lg:col-span-6 order-2 lg:order-2 flex justify-center lg:justify-start relative z-20"
                      >
                        <div className="relative p-2.5 sm:p-3 bg-white border border-slate-200/90 shadow-md rounded-lg max-w-md w-full group">
                          <div className="overflow-hidden rounded aspect-[16/11] bg-slate-100">
                            <img
                              src={currentSlide.image}
                              alt={currentSlide.year}
                              className="w-full h-full object-cover select-none group-hover:scale-103 transition-transform duration-700 ease-out"
                            />
                          </div>
                          <div className="pt-2 text-center text-xs font-heading font-medium text-slate-600">
                            {currentSlide.imageCaption}
                          </div>
                        </div>
                      </motion.div>
                    </>
                  )}

                </div>
              )}

              {/* 4. DIREKSI */}
              {currentSlide.type === 'directors' && (
                <div className="max-w-[1200px] mx-auto w-full space-y-8">
                  <motion.div 
                    initial={{ opacity: 0, y: 40 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -80 }}
                    transition={{ duration: 0.85, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                    className="text-center max-w-3xl mx-auto space-y-2"
                  >
                    <span className="text-xs font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
                      TATA KELOLA PERUSAHAAN & KEPEMIMPINAN
                    </span>
                    <h2 className="text-xl sm:text-2xl font-bold font-heading text-slate-900 tracking-tight leading-tight uppercase">
                      Dewan Direksi & Kepemimpinan 2 Generasi
                    </h2>
                    <p className="text-sm text-slate-600 font-normal max-w-2xl mx-auto">
                      Sinergi pengalaman lebih dari 20 tahun dalam riset kimia industri dengan manajemen modern berstandar ISO 9001:2015.
                    </p>
                  </motion.div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12 max-w-4xl mx-auto divide-y md:divide-y-0 md:divide-x divide-slate-200 items-start">
                    {COMPANY_DATA.boardOfDirectors.map((person, pIdx) => (
                      <motion.div
                        key={pIdx}
                        initial={{ opacity: 0, y: 40 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -80 }}
                        transition={{ duration: 0.85, delay: 0.25 + pIdx * 0.15, ease: [0.16, 1, 0.3, 1] }}
                        className={`space-y-4 ${pIdx === 1 ? 'md:pl-8 lg:pl-10 pt-6 md:pt-0' : 'md:pr-8 lg:pr-10'}`}
                      >
                        <div className="flex items-start gap-3.5">
                          <div className="w-11 h-11 bg-white border border-slate-300 text-[#0F58A8] flex items-center justify-center font-heading font-bold text-base shadow-2xs shrink-0 rounded-md">
                            {person.name.split(' ').map((n) => n[0]).join('')}
                          </div>
                          <div>
                            <h3 className="text-base font-bold font-heading text-slate-900 leading-snug">
                              {person.name}
                            </h3>
                            <span className="text-xs font-semibold text-[#0F58A8] block">
                              {person.role}
                            </span>
                            <span className="text-xs text-slate-500 block pt-0.5 font-medium">
                              Rekam Jejak: {person.experience}
                            </span>
                          </div>
                        </div>

                        <p className="text-xs sm:text-sm text-slate-700 leading-relaxed font-normal">
                          {person.bio}
                        </p>

                        <div className="space-y-1 pt-2 border-t border-slate-200">
                          <span className="text-xs font-bold uppercase tracking-wider text-slate-500 block font-heading">
                            Fokus Tanggung Jawab:
                          </span>
                          <div className="space-y-1 text-xs text-slate-700">
                            {(person.responsibilities || [person.focus]).map((resp, rIdx) => (
                              <div key={rIdx} className="flex items-start gap-2">
                                <CheckCircle2 className="w-3.5 h-3.5 text-[#0F58A8] shrink-0 mt-0.5" />
                                <span className="leading-snug">{resp}</span>
                              </div>
                            ))}
                          </div>
                        </div>
                      </motion.div>
                    ))}
                  </div>
                </div>
              )}

              {/* 5. ESG & PENUTUP */}
              {currentSlide.type === 'esg' && (
                <div className="max-w-[1250px] mx-auto w-full space-y-8 text-center">
                  <motion.div 
                    initial={{ opacity: 0, y: 40 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -80 }}
                    transition={{ duration: 0.85, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                    className="max-w-2xl mx-auto space-y-1.5"
                  >
                    <span className="text-xs font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
                      PRINSIP INTEGRITAS & KEBERLANJUTAN
                    </span>
                    <h2 className="text-xl sm:text-2xl font-bold font-heading text-slate-900 tracking-tight leading-tight uppercase">
                      4 Komitmen Fundamental Perusahaan
                    </h2>
                  </motion.div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 text-left pt-2">
                    <motion.div 
                      initial={{ opacity: 0, y: 35 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -70 }}
                      transition={{ duration: 0.8, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                      className="p-4 rounded-lg bg-slate-50 border border-slate-200/80 space-y-1.5"
                    >
                      <strong className="text-xs sm:text-sm font-bold text-slate-900 block font-heading">
                        1. Kejujuran Formulasi
                      </strong>
                      <p className="text-xs text-slate-600 leading-relaxed">
                        Menolak filler garam murah atau pengencer air berlebih demi menjaga daya kerja mesin mitra.
                      </p>
                    </motion.div>

                    <motion.div 
                      initial={{ opacity: 0, y: 35 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -70 }}
                      transition={{ duration: 0.8, delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
                      className="p-4 rounded-lg bg-emerald-50/60 border border-emerald-200/80 space-y-1.5"
                    >
                      <strong className="text-xs sm:text-sm font-bold text-slate-900 block font-heading">
                        2. Tanggung Jawab IPAL
                      </strong>
                      <p className="text-xs text-slate-600 leading-relaxed">
                        100% bebas fosfat (STPP-free) dan surfaktan biodegradasi &gt;90% aman biofilter perairan.
                      </p>
                    </motion.div>

                    <motion.div 
                      initial={{ opacity: 0, y: 35 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -70 }}
                      transition={{ duration: 0.8, delay: 0.4, ease: [0.16, 1, 0.3, 1] }}
                      className="p-4 rounded-lg bg-amber-50/60 border border-amber-200/80 space-y-1.5"
                    >
                      <strong className="text-xs sm:text-sm font-bold text-slate-900 block font-heading">
                        3. Legalitas & Pajak
                      </strong>
                      <p className="text-xs text-slate-600 leading-relaxed">
                        Izin OSS-RBA resmi, PKRT Kemenkes RI, faktur PPN 11%, dan kesiapan tender e-Katalog LKPP RI.
                      </p>
                    </motion.div>

                    <motion.div 
                      initial={{ opacity: 0, y: 35 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -70 }}
                      transition={{ duration: 0.8, delay: 0.5, ease: [0.16, 1, 0.3, 1] }}
                      className="p-4 rounded-lg bg-blue-50/60 border border-blue-200/80 space-y-1.5"
                    >
                      <strong className="text-xs sm:text-sm font-bold text-slate-900 block font-heading">
                        4. Kontinuitas Pasokan
                      </strong>
                      <p className="text-xs text-slate-600 leading-relaxed">
                        Kapasitas 500+ Ton/bulan menjamin kepastian pasokan rutin tanpa jeda operasional.
                      </p>
                    </motion.div>
                  </div>

                  {/* Call to Action Bar */}
                  <motion.div 
                    initial={{ opacity: 0, scale: 0.97 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.97 }}
                    transition={{ duration: 0.8, delay: 0.6, ease: [0.16, 1, 0.3, 1] }}
                    className="pt-4 flex items-center justify-center gap-4 flex-wrap"
                  >
                    <Link
                      to="/contact"
                      className="btn-fluid-primary text-xs sm:text-sm py-3 px-8 font-semibold"
                    >
                      <span>Mulai Kemitraan Formulasi</span>
                      <ArrowRight className="w-4 h-4" />
                    </Link>

                    <Link
                      to="/products"
                      className="btn-fluid-secondary text-xs sm:text-sm py-3 px-8 font-semibold"
                    >
                      <span>Lihat Katalog Produk</span>
                    </Link>
                  </motion.div>
                </div>
              )}

            </motion.div>
          </motion.div>
        </AnimatePresence>
      </div>
    </main>
  )
}
