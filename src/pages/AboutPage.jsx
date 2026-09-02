import { useRef } from 'react'
import { Helmet } from 'react-helmet-async'
import { motion, useScroll, useSpring, useTransform, useMotionValue } from 'framer-motion'
import { 
  Building2, 
  Award, 
  ShieldCheck, 
  CheckCircle2, 
  Factory, 
  FlaskConical, 
  Scale, 
  Droplets, 
  Leaf, 
  FileText, 
  Check, 
  ArrowRight, 
  Clock, 
  Users, 
  MapPin, 
  FileCheck2, 
  Layers, 
  Sparkles, 
  Milestone,
  ChevronDown
} from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import CTASection from '@/components/sections/CTASection'

// Interactive 3D Perspective Photo Card with Physics Tilt & Parallax Floating Layer
function Tilt3DPhotoCard({ image, title, caption, phaseNumber }) {
  const cardRef = useRef(null)
  const x = useMotionValue(0)
  const y = useMotionValue(0)

  const mouseXSpring = useSpring(x, { stiffness: 240, damping: 22 })
  const mouseYSpring = useSpring(y, { stiffness: 240, damping: 22 })

  const rotateX = useTransform(mouseYSpring, [-0.5, 0.5], ['8deg', '-8deg'])
  const rotateY = useTransform(mouseXSpring, [-0.5, 0.5], ['-8deg', '8deg'])

  const handleMouseMove = (e) => {
    if (!cardRef.current) return
    const rect = cardRef.current.getBoundingClientRect()
    const mouseX = e.clientX - rect.left
    const mouseY = e.clientY - rect.top
    const xPct = mouseX / rect.width - 0.5
    const yPct = mouseY / rect.height - 0.5
    x.set(xPct)
    y.set(yPct)
  }

  const handleMouseLeave = () => {
    x.set(0)
    y.set(0)
  }

  return (
    <div style={{ perspective: 1000 }} className="w-full">
      <motion.div
        ref={cardRef}
        onMouseMove={handleMouseMove}
        onMouseLeave={handleMouseLeave}
        style={{
          rotateX,
          rotateY,
          transformStyle: 'preserve-3d',
        }}
        whileHover={{ scale: 1.02 }}
        transition={{ duration: 0.3 }}
        className="relative overflow-hidden rounded-3xl border border-sky-100 shadow-xl hover:shadow-2xl hover:shadow-[#0F58A8]/15 bg-white group aspect-[16/11] cursor-pointer will-change-transform transform-gpu"
      >
        {/* 3D Base Image Layer (100% Pure Clean Photo - No Overlapping Text) */}
        <img
          src={image}
          alt={title}
          style={{ transform: 'translateZ(0px)' }}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out select-none"
        />

        {/* Subtle Natural Vignette */}
        <div 
          style={{ transform: 'translateZ(10px)' }}
          className="absolute inset-0 bg-gradient-to-t from-slate-900/20 via-transparent to-transparent pointer-events-none" 
        />
      </motion.div>
    </div>
  )
}

// 3D Isometric / Perspective Journey Graphic Line with Depth Conduit, 3D Milestone Orbs & Traveling Energy Core
function Timeline3DGraphicTrack({ progressHeight, activeOpacity }) {
  const milestones = [
    { year: '2004', topPct: 2, label: '01' },
    { year: '2008', topPct: 26, label: '02' },
    { year: '2014', topPct: 50, label: '03' },
    { year: '2019', topPct: 74, label: '04' },
    { year: '2026', topPct: 98, label: '05' },
  ]

  return (
    <motion.div
      style={{ opacity: activeOpacity }}
      className="hidden lg:block absolute top-28 bottom-24 left-6 xl:left-12 w-24 z-20 pointer-events-none select-none"
    >
      <div 
        style={{ perspective: 800, transformStyle: 'preserve-3d' }}
        className="relative h-full w-full flex items-center justify-start"
      >
        {/* 3D Tilted Perspective Axis Container */}
        <div 
          style={{ 
            transform: 'rotateY(-20deg) rotateX(6deg)',
            transformStyle: 'preserve-3d'
          }}
          className="relative h-full w-14 flex flex-col items-center justify-between"
        >
          {/* 3D Outer Glass Tubular Conduit */}
          <div className="absolute inset-y-0 w-3.5 rounded-full bg-gradient-to-r from-slate-200/90 via-white to-slate-300/90 border border-slate-300/80 shadow-[0_0_15px_rgba(15,88,168,0.15),inset_0_0_6px_rgba(255,255,255,0.9)] backdrop-blur-xs overflow-hidden">
            {/* 3D Internal Fluid Energy Stream */}
            <motion.div
              style={{ height: progressHeight }}
              className="w-full bg-gradient-to-b from-[#0F58A8] via-[#38BDF8] to-[#0F58A8] rounded-full origin-top shadow-[0_0_12px_#38BDF8,0_0_20px_rgba(15,88,168,0.8)]"
            />
          </div>

          {/* 3D Traveling Energy Core Capsule (Rides along the tube in real-time) */}
          <motion.div
            style={{ 
              top: progressHeight,
              transform: 'translate(-50%, -50%) translateZ(16px)',
              transformStyle: 'preserve-3d'
            }}
            className="absolute left-1/2 w-6 h-6 rounded-full bg-gradient-to-tr from-[#0F58A8] to-[#38BDF8] border-2 border-white shadow-[0_0_16px_#38BDF8,0_6px_14px_rgba(15,88,168,0.5)] flex items-center justify-center will-change-transform z-30"
          >
            {/* Inner Core Pulse Ring */}
            <div className="w-2.5 h-2.5 rounded-full bg-white animate-ping" />
            <div className="absolute inset-0 rounded-full border border-white/80 animate-spin" style={{ animationDuration: '3s' }} />
          </motion.div>

          {/* 3D Milestone Checkpoint Nodes (2004, 2008, 2014, 2019, 2026) */}
          {milestones.map((m, idx) => (
            <div
              key={idx}
              style={{
                top: `${m.topPct}%`,
                transform: 'translateY(-50%) translateZ(12px)',
                transformStyle: 'preserve-3d'
              }}
              className="absolute left-1/2 -translate-x-1/2 flex items-center gap-2"
            >
              {/* 3D Metallic Ring / Node Sphere */}
              <div className="w-5 h-5 rounded-full bg-white border-2 border-[#0F58A8] shadow-[0_2px_8px_rgba(15,88,168,0.25)] flex items-center justify-center">
                <div className="w-2 h-2 rounded-full bg-[#0F58A8]" />
              </div>

              {/* 3D Floating Year Tag Badge */}
              <div 
                style={{ transform: 'translateZ(14px)' }}
                className="px-1.5 py-0.5 rounded-md bg-white/95 border border-slate-200 shadow-2xs text-[9px] font-mono font-black text-[#0F58A8] whitespace-nowrap drop-shadow-xs"
              >
                {m.year}
              </div>
            </div>
          ))}

        </div>
      </div>
    </motion.div>
  )
}

const TIMELINE_MILESTONES = [
  {
    year: '2004',
    badge: 'Fase 01 • Pendirian & Riset Kesadahan Air',
    title: 'Titik Mula di Mojoroto: Menaklukkan Kesadahan Air Tanah',
    desc: 'Didirikan oleh Yan Effendi di Mojoroto, Kota Kediri dengan modal 1 unit reaktor manual 500 Liter. Pada masa awal ini, industri laundry komersial dan tekstil lokal menghadapi kendala busa mati dan serat kain menguning akibat tingginya kesadahan air tanah Jawa Timur (>350 ppm CaCO₃).',
    challenge: 'Surfaktan pasar cepat menggumpal, memicu kerak pada drum mesin cuci, dan boros dosis pada air sadah lokal.',
    solution: 'Rekayasa agen chelating murni (sequestering agent) berdaya ikat ion kalsium & magnesium tinggi tanpa merusak serat kain.',
    points: [
      'Operasional 1 unit reaktor manual 500L dengan kontrol pemanasan terukur',
      'Riset adaptasi formulasi spesifik terhadap air sadah lokal 300–450 ppm',
      'Penyaluran perdana ke puluhan sentra laundry komersial Karesidenan Kediri'
    ],
    breakthrough: 'Formulasi surfaktan stabil air sadah pertama yang menekan pemborosan dosis hingga 40%.',
    image: '/images/kca_factory_reactors.jpg',
    imageCaption: 'Reaktor Pencampur Perdana PT Kediri Chemical Abadi di Mojoroto, Kediri (Est. 2004)'
  },
  {
    year: '2008',
    badge: 'Fase 02 • Inovasi Hijau Anti-Fosfat',
    title: 'Terobosan Formula 100% Bebas Fosfat & Reaktor SS 316L Pertama',
    desc: 'Di tengah maraknya deterjen industri berbasis STPP (fosfat murah perusak lingkungan perairan), KCA mengambil langkah berani menghentikan total penggunaan fosfat dan menginvestasikan tangki reaktor Stainless Steel 316L anti-korosi asam/basa pekat pertama.',
    challenge: 'Menghilangkan bahan fosfat tanpa menurunkan daya angkat noda lemak & minyak berat industri.',
    solution: 'Sinergi surfaktan non-ionik murni dan enzim protease ramah lingkungan yang aman terhadap ekosistem perairan.',
    points: [
      'Instalasi reaktor pencampur Stainless Steel 316L berjaket pemanas terpadu',
      'Standarisasi formula 100% bebas STPP (mencegah eutrofikasi & ledakan alga)',
      'Konsistensi efisiensi dosis stabil pada 10–15 ml per kilogram pakaian kering'
    ],
    breakthrough: 'Formula ramah ekosistem air pertama di Kediri dengan daya cuci setara standar internasional.',
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Lini Manufaktur Formulasi Ramah Lingkungan Bebas Fosfat Berstandar Mutu'
  },
  {
    year: '2014',
    badge: 'Fase 03 • Standarisasi Medis & IPAL KARS',
    title: 'Penetrasi Rumah Sakit & Kelayakan IPAL KARS',
    desc: 'KCA memasuki sektor higienitas medis dengan memformulasi deterjen disinfektan dan alkali builder khusus pencucian linen ruang isolasi, bedah, dan rawat inap. Formula KCA lolos uji ketat IPAL rumah sakit karena tidak mematikan bakteri pengurai biofilter.',
    challenge: 'Kimia medis wajib membunuh bakteri patogen nosokomial namun air buangannya tidak boleh merusak biofilter IPAL rumah sakit.',
    solution: 'Formulasi biosurfaktan terurai cepat (>90% biodegradasi OECD 301D) dipadukan dengan senyawa oksigen aktif.',
    points: [
      'Lolos uji baku mutu limbah cair pada sistem IPAL biofilter RS rujukan daerah',
      'Penyediaan formula Alkali Booster, Emulsifier Noda Darah, dan Oxy Bleach Medis',
      'Kemitraan resmi dengan puluhan RSUD, RS Swasta, dan klinik spesialis se-Jawa Timur'
    ],
    breakthrough: 'Standar higienitas KARS (Komisi Akreditasi Rumah Sakit) dengan nol risiko kerusakan IPAL.',
    image: '/images/product_jerigen5l.jpg',
    imageCaption: 'Produk Kimia Higienitas Medis & Pembersih Konsentrat Ramah Biofilter IPAL RS'
  },
  {
    year: '2019',
    badge: 'Fase 04 • Modernisasi Demin RO & Maklon VIP',
    title: 'Instalasi Demin RO 50.000 L/Hari & Skema Dedicated Line VIP',
    desc: 'Menjawab lonjakan permintaan maklon private label nasional, KCA membangun fasilitas pemurnian air Reverse Osmosis (RO) dan Demineralisasi berkapasitas 50.000 Liter/hari (<5 ppm TDS). Pada fase ini, skema kemitraan Capex Dedicated Line VIP resmi diluncurkan.',
    challenge: 'Permintaan private label brand nasional melonjak melampaui kapasitas antrean batch standar pabrik.',
    solution: 'Membuka skema investasi mesin reaktor khusus yang didedikasikan 100% untuk satu mitra dengan pengembalian via diskon faktur.',
    points: [
      'Pembangunan instalasi Double-Stage RO & Mixed-Bed Resin (<5 ppm TDS)',
      'Ekspansi kapasitas total pabrik melampaui 500+ Ton konsentrat murni per bulan',
      'Peluncuran skema Dedicated Production Line VIP dengan jaminan kerahasiaan NDA'
    ],
    breakthrough: 'Pabrik kimia lokal pertama di Jawa Timur dengan skema reaktor dedicated tanpa antrean batch.',
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Instalasi Pengolahan Air Demineralisasi RO 50.000 L/Hari & Reaktor Kapasitas 500+ Ton/Bulan'
  },
  {
    year: '2024–2026',
    badge: 'Fase 05 • Era Manajemen Modern & LKPP RI',
    title: 'Kepemimpinan Generasi Kedua, Mutu ISO 9001 & e-Katalog LKPP RI',
    desc: 'Estafet kepemimpinan di bawah Yerikho Arfensias Effendi mempercepat transformasi tata kelola korporat, sertifikasi Sistem Manajemen Mutu ISO 9001:2015, dan integrasi rantai pasok digital. KCA melengkapi izin edar PKRT Kemenkes RI dan bersiap memenuhi pengadaan tender pemerintah di platform e-Katalog LKPP RI.',
    challenge: 'Standarisasi birokrasi pengadaan nasional dan integrasi rantai pasok multi-sektor skala besar.',
    solution: 'Audit kepatuhan legalitas menyeluruh (NIB OSS-RBA, e-Faktur PPN 11%, COA per batch bertandatangan Direktur).',
    points: [
      'Manajemen operasional berbasis standar Sistem Manajemen Mutu ISO 9001:2015',
      'Kelengkapan izin edar PKRT Kementerian Kesehatan RI untuk seluruh lini produk',
      'Kesiapan tender nasional e-Katalog LKPP RI dan ekspansi distribusi logistik antarpulau'
    ],
    breakthrough: 'Produsen kimia konsentrat terpercaya dengan kepatuhan hukum penuh dan kapasitas skala industri.',
    image: '/images/kca_packaging_lineup.png',
    imageCaption: 'Standarisasi Lini Produk Kemasan Jerigen & Drum Berizin Edar Resmi PKRT Kemenkes RI'
  },
]

export default function AboutPage() {
  const historyContainerRef = useRef(null)

  // Track scroll progression across the pinned history section
  const { scrollYProgress } = useScroll({
    target: historyContainerRef,
    offset: ['start start', 'end end']
  })

  // Physics-based spring progress for silky smooth locked storytelling
  const smoothP = useSpring(scrollYProgress, {
    stiffness: 90,
    damping: 24,
    restDelta: 0.0005
  })

  // 1. Fase 1: Intro Section Lock (0.00 - 0.13)
  const introOpacity = useTransform(smoothP, [0, 0.08, 0.13], [1, 0.85, 0])
  const introScale = useTransform(smoothP, [0, 0.13], [1, 1.35])
  const introFilter = useTransform(smoothP, [0, 0.06, 0.13], ['blur(0px)', 'blur(4px)', 'blur(16px)'])
  const introPointerEvents = useTransform(smoothP, (v) => (v < 0.13 ? 'auto' : 'none'))

  // 2. Timeline 3D Track & Top Bar (0.13 - 1.00)
  const centerLineHeight = useTransform(smoothP, [0.13, 0.98], ['0%', '100%'])
  const activeTimelineOpacity = useTransform(smoothP, [0.11, 0.15], [0, 1])

  // ========================================================
  // FASE 01: 2004 (Scroll Window: 0.13 -> 0.30)
  // ========================================================
  const p1Opacity = useTransform(smoothP, [0.12, 0.15, 0.27, 0.30], [0, 1, 1, 0])
  const p1Y = useTransform(smoothP, [0.12, 0.15, 0.27, 0.30], [25, 0, 0, -25])
  const p1Scale = useTransform(smoothP, [0.12, 0.15, 0.27, 0.30], [0.96, 1, 1, 0.96])
  const p1PointerEvents = useTransform(smoothP, (v) => (v >= 0.13 && v < 0.30 ? 'auto' : 'none'))
  const p1ProgressWidth = useTransform(smoothP, [0.14, 0.28], ['0%', '100%'])
  // Step 1: Title & Story
  const p1Step1Opacity = useTransform(smoothP, [0.13, 0.16], [0, 1])
  const p1Step1Y = useTransform(smoothP, [0.13, 0.16], [12, 0])
  // Step 2: Tantangan vs Solusi
  const p1Step2Opacity = useTransform(smoothP, [0.16, 0.21], [0.2, 1])
  const p1Step2Y = useTransform(smoothP, [0.16, 0.21], [14, 0])
  const p1ChallengeBorder = useTransform(smoothP, [0.16, 0.21], ['#cbd5e1', '#ef4444'])
  const p1SolutionBorder = useTransform(smoothP, [0.19, 0.24], ['#cbd5e1', '#059669'])
  // Step 3: Lab Points & Breakthrough
  const p1Step3Opacity = useTransform(smoothP, [0.21, 0.26], [0.15, 1])
  const p1Step3Y = useTransform(smoothP, [0.21, 0.26], [14, 0])
  const p1PhotoScale = useTransform(smoothP, [0.14, 0.28], [1, 1.08])

  // ========================================================
  // FASE 02: 2008 (Scroll Window: 0.30 -> 0.47)
  // ========================================================
  const p2Opacity = useTransform(smoothP, [0.29, 0.32, 0.44, 0.47], [0, 1, 1, 0])
  const p2Y = useTransform(smoothP, [0.29, 0.32, 0.44, 0.47], [25, 0, 0, -25])
  const p2Scale = useTransform(smoothP, [0.29, 0.32, 0.44, 0.47], [0.96, 1, 1, 0.96])
  const p2PointerEvents = useTransform(smoothP, (v) => (v >= 0.30 && v < 0.47 ? 'auto' : 'none'))
  const p2ProgressWidth = useTransform(smoothP, [0.31, 0.45], ['0%', '100%'])
  // Step 1: Title & Story
  const p2Step1Opacity = useTransform(smoothP, [0.30, 0.33], [0, 1])
  const p2Step1Y = useTransform(smoothP, [0.30, 0.33], [12, 0])
  // Step 2: Tantangan vs Solusi
  const p2Step2Opacity = useTransform(smoothP, [0.33, 0.38], [0.2, 1])
  const p2Step2Y = useTransform(smoothP, [0.33, 0.38], [14, 0])
  const p2ChallengeBorder = useTransform(smoothP, [0.33, 0.38], ['#cbd5e1', '#ef4444'])
  const p2SolutionBorder = useTransform(smoothP, [0.36, 0.41], ['#cbd5e1', '#059669'])
  // Step 3: Lab Points & Breakthrough
  const p2Step3Opacity = useTransform(smoothP, [0.38, 0.43], [0.15, 1])
  const p2Step3Y = useTransform(smoothP, [0.38, 0.43], [14, 0])
  const p2PhotoScale = useTransform(smoothP, [0.31, 0.45], [1, 1.08])

  // ========================================================
  // FASE 03: 2014 (Scroll Window: 0.47 -> 0.64)
  // ========================================================
  const p3Opacity = useTransform(smoothP, [0.46, 0.49, 0.61, 0.64], [0, 1, 1, 0])
  const p3Y = useTransform(smoothP, [0.46, 0.49, 0.61, 0.64], [25, 0, 0, -25])
  const p3Scale = useTransform(smoothP, [0.46, 0.49, 0.61, 0.64], [0.96, 1, 1, 0.96])
  const p3PointerEvents = useTransform(smoothP, (v) => (v >= 0.47 && v < 0.64 ? 'auto' : 'none'))
  const p3ProgressWidth = useTransform(smoothP, [0.48, 0.62], ['0%', '100%'])
  // Step 1: Title & Story
  const p3Step1Opacity = useTransform(smoothP, [0.47, 0.50], [0, 1])
  const p3Step1Y = useTransform(smoothP, [0.47, 0.50], [12, 0])
  // Step 2: Tantangan vs Solusi
  const p3Step2Opacity = useTransform(smoothP, [0.50, 0.55], [0.2, 1])
  const p3Step2Y = useTransform(smoothP, [0.50, 0.55], [14, 0])
  const p3ChallengeBorder = useTransform(smoothP, [0.50, 0.55], ['#cbd5e1', '#ef4444'])
  const p3SolutionBorder = useTransform(smoothP, [0.53, 0.58], ['#cbd5e1', '#059669'])
  // Step 3: Lab Points & Breakthrough
  const p3Step3Opacity = useTransform(smoothP, [0.55, 0.60], [0.15, 1])
  const p3Step3Y = useTransform(smoothP, [0.55, 0.60], [14, 0])
  const p3PhotoScale = useTransform(smoothP, [0.48, 0.62], [1, 1.08])

  // ========================================================
  // FASE 04: 2019 (Scroll Window: 0.64 -> 0.82)
  // ========================================================
  const p4Opacity = useTransform(smoothP, [0.63, 0.66, 0.79, 0.82], [0, 1, 1, 0])
  const p4Y = useTransform(smoothP, [0.63, 0.66, 0.79, 0.82], [25, 0, 0, -25])
  const p4Scale = useTransform(smoothP, [0.63, 0.66, 0.79, 0.82], [0.96, 1, 1, 0.96])
  const p4PointerEvents = useTransform(smoothP, (v) => (v >= 0.64 && v < 0.82 ? 'auto' : 'none'))
  const p4ProgressWidth = useTransform(smoothP, [0.65, 0.80], ['0%', '100%'])
  // Step 1: Title & Story
  const p4Step1Opacity = useTransform(smoothP, [0.64, 0.67], [0, 1])
  const p4Step1Y = useTransform(smoothP, [0.64, 0.67], [12, 0])
  // Step 2: Tantangan vs Solusi
  const p4Step2Opacity = useTransform(smoothP, [0.67, 0.72], [0.2, 1])
  const p4Step2Y = useTransform(smoothP, [0.67, 0.72], [14, 0])
  const p4ChallengeBorder = useTransform(smoothP, [0.67, 0.72], ['#cbd5e1', '#ef4444'])
  const p4SolutionBorder = useTransform(smoothP, [0.70, 0.75], ['#cbd5e1', '#059669'])
  // Step 3: Lab Points & Breakthrough
  const p4Step3Opacity = useTransform(smoothP, [0.72, 0.77], [0.15, 1])
  const p4Step3Y = useTransform(smoothP, [0.72, 0.77], [14, 0])
  const p4PhotoScale = useTransform(smoothP, [0.65, 0.80], [1, 1.08])

  // ========================================================
  // FASE 05: 2024–2026 (Scroll Window: 0.82 -> 1.00)
  // ========================================================
  const p5Opacity = useTransform(smoothP, [0.81, 0.84, 1.0], [0, 1, 1])
  const p5Y = useTransform(smoothP, [0.81, 0.84, 1.0], [25, 0, 0])
  const p5Scale = useTransform(smoothP, [0.81, 0.84, 1.0], [0.96, 1, 1])
  const p5PointerEvents = useTransform(smoothP, (v) => (v >= 0.82 ? 'auto' : 'none'))
  const p5ProgressWidth = useTransform(smoothP, [0.83, 0.98], ['0%', '100%'])
  // Step 1: Title & Story
  const p5Step1Opacity = useTransform(smoothP, [0.82, 0.85], [0, 1])
  const p5Step1Y = useTransform(smoothP, [0.82, 0.85], [12, 0])
  // Step 2: Tantangan vs Solusi
  const p5Step2Opacity = useTransform(smoothP, [0.85, 0.90], [0.2, 1])
  const p5Step2Y = useTransform(smoothP, [0.85, 0.90], [14, 0])
  const p5ChallengeBorder = useTransform(smoothP, [0.85, 0.90], ['#cbd5e1', '#ef4444'])
  const p5SolutionBorder = useTransform(smoothP, [0.88, 0.93], ['#cbd5e1', '#059669'])
  // Step 3: Lab Points & Breakthrough
  const p5Step3Opacity = useTransform(smoothP, [0.90, 0.96], [0.15, 1])
  const p5Step3Y = useTransform(smoothP, [0.90, 0.96], [14, 0])
  const p5PhotoScale = useTransform(smoothP, [0.83, 0.98], [1, 1.08])

  const phaseAnimStates = [
    { 
      opacity: p1Opacity, 
      y: p1Y, 
      scale: p1Scale, 
      pointerEvents: p1PointerEvents,
      progressWidth: p1ProgressWidth,
      step1Opacity: p1Step1Opacity,
      step1Y: p1Step1Y,
      step2Opacity: p1Step2Opacity,
      step2Y: p1Step2Y,
      challengeBorder: p1ChallengeBorder,
      solutionBorder: p1SolutionBorder,
      step3Opacity: p1Step3Opacity,
      step3Y: p1Step3Y,
      photoScale: p1PhotoScale,
    },
    { 
      opacity: p2Opacity, 
      y: p2Y, 
      scale: p2Scale, 
      pointerEvents: p2PointerEvents,
      progressWidth: p2ProgressWidth,
      step1Opacity: p2Step1Opacity,
      step1Y: p2Step1Y,
      step2Opacity: p2Step2Opacity,
      step2Y: p2Step2Y,
      challengeBorder: p2ChallengeBorder,
      solutionBorder: p2SolutionBorder,
      step3Opacity: p2Step3Opacity,
      step3Y: p2Step3Y,
      photoScale: p2PhotoScale,
    },
    { 
      opacity: p3Opacity, 
      y: p3Y, 
      scale: p3Scale, 
      pointerEvents: p3PointerEvents,
      progressWidth: p3ProgressWidth,
      step1Opacity: p3Step1Opacity,
      step1Y: p3Step1Y,
      step2Opacity: p3Step2Opacity,
      step2Y: p3Step2Y,
      challengeBorder: p3ChallengeBorder,
      solutionBorder: p3SolutionBorder,
      step3Opacity: p3Step3Opacity,
      step3Y: p3Step3Y,
      photoScale: p3PhotoScale,
    },
    { 
      opacity: p4Opacity, 
      y: p4Y, 
      scale: p4Scale, 
      pointerEvents: p4PointerEvents,
      progressWidth: p4ProgressWidth,
      step1Opacity: p4Step1Opacity,
      step1Y: p4Step1Y,
      step2Opacity: p4Step2Opacity,
      step2Y: p4Step2Y,
      challengeBorder: p4ChallengeBorder,
      solutionBorder: p4SolutionBorder,
      step3Opacity: p4Step3Opacity,
      step3Y: p4Step3Y,
      photoScale: p4PhotoScale,
    },
    { 
      opacity: p5Opacity, 
      y: p5Y, 
      scale: p5Scale, 
      pointerEvents: p5PointerEvents,
      progressWidth: p5ProgressWidth,
      step1Opacity: p5Step1Opacity,
      step1Y: p5Step1Y,
      step2Opacity: p5Step2Opacity,
      step2Y: p5Step2Y,
      challengeBorder: p5ChallengeBorder,
      solutionBorder: p5SolutionBorder,
      step3Opacity: p5Step3Opacity,
      step3Y: p5Step3Y,
      photoScale: p5PhotoScale,
    },
  ]

  return (
    <main className="bg-white text-slate-900 pt-6">
      <Helmet>
        <title>Profil Perusahaan, Sejarah & Fasilitas Pabrik — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Sejarah perjalanan 2 dekade, latar belakang berdirinya pabrik di Mojoroto Kediri, fasilitas reaktor SS 316L 500+ Ton/bulan, dan dewan direksi PT Kediri Chemical Abadi."
        />
      </Helmet>

      {/* ========================================================================= */}
      {/* 1. HERO BANNER: PROFIL & DEDIKASI MANUFAKTUR                              */}
      {/* ========================================================================= */}
      <section className="py-12 sm:py-16 bg-slate-50/70 border-b border-slate-200 text-center relative overflow-hidden">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-10">
          <div className="max-w-4xl mx-auto space-y-3">
            <h1 className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Dedikasi Formulasi Presisi &amp; Manufaktur Kimia Berkelanjutan
            </h1>

            <p className="text-xs sm:text-[13px] text-slate-600 leading-relaxed max-w-3xl mx-auto font-normal pt-0.5">
              Didirikan sejak tahun 2004 di Mojoroto, Kota Kediri, PT Kediri Chemical Abadi hadir sebagai produsen kimia pembersih industri murni konsentrat tinggi yang mengutamakan efisiensi biaya nyata, kepatuhan baku mutu lingkungan IPAL, dan integritas mutu tanpa kompromi.
            </p>

            {/* Quick Metrics (Clean Inline Typography - No Boxed Cards) */}
            <div className="pt-3 flex items-center justify-center flex-wrap gap-x-6 gap-y-2 text-xs font-bold text-slate-700">
              <span className="flex items-center gap-2">
                <Factory className="w-4 h-4 text-[#0F58A8]" />
                <span>Reaktor Stainless Steel 316L</span>
              </span>
              <span className="text-slate-300 hidden sm:inline">•</span>
              <span className="flex items-center gap-2">
                <Award className="w-4 h-4 text-emerald-600" />
                <span>Kapasitas 500+ Ton / Bulan</span>
              </span>
              <span className="text-slate-300 hidden sm:inline">•</span>
              <span className="flex items-center gap-2">
                <Building2 className="w-4 h-4 text-blue-600" />
                <span>Area Pabrik 2.500+ m²</span>
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 2. LATAR BELAKANG & SEJARAH PENDIRIAN (ORIGIN STORY & FILOSOFI BISNIS)     */}
      {/* ========================================================================= */}
      <section className="py-12 sm:py-16 bg-white text-slate-900 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-start">
            
            {/* Sisi Kiri: Narasi Sejarah & Filosofi Integritas (7 Kolom) */}
            <div className="lg:col-span-7 space-y-4">
              <div className="space-y-1.5">
                <h2 className="text-lg sm:text-xl lg:text-2xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                  Latar Belakang &amp; Filosofi Berdirinya PT Kediri Chemical Abadi
                </h2>
              </div>

              <div className="space-y-3 text-xs text-slate-700 leading-relaxed font-normal">
                <p>
                  Perjalanan PT Kediri Chemical Abadi berawal pada tahun 2004 dari pengamatan langsung sang pendiri, <strong>Yan Effendi</strong>, terhadap industri kimia pembersih komersial di Jawa Timur. Saat itu, pasar dibanjiri oleh produk-produk deterjen berkadar air tinggi yang diencerkan secara berlebihan atau menggunakan bahan pengisi (*filler*) garam natrium sulfat murah untuk sekadar menambah bobot volume.
                </p>
                <p>
                  Dampaknya sangat merugikan para pelaku usaha: mesin cuci industri cepat berkarat, kain linen rumah sakit menjadi kaku dan cepat rusak, limbah cucian merusak bakteri pada instalasi IPAL, serta biaya operasional membengkak karena dosis pemakaian yang sangat boros (mencapai 30–50 ml per kilogram pakaian).
                </p>
                <p>
                  Didorong oleh komitmen untuk menyediakan alternatif kimia pembersih yang jujur dan berdaya guna tinggi, PT Kediri Chemical Abadi didirikan dengan satu filosofi dasar: <strong>"Konsentrat Murni Tanpa Oplosan, Efisiensi Dosis Maksimal, dan Ramah Terhadap Lingkungan."</strong> Kami membuktikan bahwa formula berkualitas tinggi dengan dosis hemat (hanya 10–15 ml/kg) mampu menekan total biaya operasional (*Total Cost of Ownership*) pelaku bisnis hingga 40%.
                </p>
              </div>

              {/* 3 Pilar Fondasi Pendirian */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-3 border-t border-slate-200">
                <div className="space-y-1">
                  <strong className="text-xs font-bold text-slate-900 block font-heading">
                    1. Formula Murni Konsentrat
                  </strong>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    Kandungan bahan aktif surfaktan tinggi tanpa penambahan garam pengisi atau pengental buatan perusak serat kain.
                  </p>
                </div>
                <div className="space-y-1">
                  <strong className="text-xs font-bold text-slate-900 block font-heading">
                    2. Perlindungan Aset Mesin
                  </strong>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    Menggunakan agen anti-korosi khusus yang memperpanjang umur drum pencuci dan pompa dosing otomatis mitra.
                  </p>
                </div>
                <div className="space-y-1">
                  <strong className="text-xs font-bold text-slate-900 block font-heading">
                    3. Kepatuhan Baku Mutu IPAL
                  </strong>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    100% bebas fosfat (STPP-free) agar aman bagi biofilter pengolahan limbah cair rumah sakit dan industri.
                  </p>
                </div>
              </div>
            </div>

            {/* Sisi Kanan: Foto Fasilitas & Data Ringkas Pabrik (5 Kolom) */}
            <div className="lg:col-span-5 space-y-4">
              <div className="relative rounded-3xl overflow-hidden border border-sky-100 shadow-xl shadow-blue-900/5 aspect-[16/11] group bg-sky-50">
                <img
                  src="/images/kca_factory_floor.jpg"
                  alt="Lantai Fasilitas Produksi PT Kediri Chemical Abadi Mojoroto"
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 select-none"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-900/20 via-transparent to-transparent pointer-events-none" />
              </div>

              {/* Data Identitas Resmi Pabrik */}
              <div className="space-y-1.5 text-xs divide-y divide-sky-100 border-t border-sky-100 pt-1">
                <div className="flex justify-between py-1">
                  <span className="text-slate-500">Tahun Berdiri:</span>
                  <strong className="text-slate-900 font-bold">2004 (22 Tahun Dedikasi Manufaktur)</strong>
                </div>
                <div className="flex justify-between py-1">
                  <span className="text-slate-500">Lokasi Pabrik:</span>
                  <strong className="text-slate-900 font-bold">Mojoroto, Kota Kediri, Jawa Timur</strong>
                </div>
                <div className="flex justify-between py-1">
                  <span className="text-slate-500">Kapasitas Produksi:</span>
                  <strong className="text-slate-900 font-bold">500+ Ton Konsentrat / Bulan</strong>
                </div>
                <div className="flex justify-between py-1">
                  <span className="text-slate-500">Standarisasi Mutu:</span>
                  <strong className="text-[#0F58A8] font-bold">ISO 9001:2015 QMS Standard</strong>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. ALUR SEJARAH PINNED MULTI-PHASE (LOCKED SECTION WITH ZOOM & BLUR)      */}
      {/* ========================================================================= */}
      <section 
        ref={historyContainerRef} 
        className="relative h-[620vh] bg-slate-50/70 border-b border-slate-200"
      >
        {/* Sticky Pinned Viewport Container */}
        <div className="sticky top-0 h-screen w-full overflow-hidden flex items-center justify-center">
          
          {/* Top Floating Milestone Phase Tracker Bar */}
          <motion.div 
            style={{ opacity: activeTimelineOpacity }}
            className="absolute top-5 inset-x-0 z-40 max-w-2xl mx-auto px-4 pointer-events-none"
          >
            <div className="bg-white/90 backdrop-blur-md border border-slate-200/90 rounded-full px-5 py-2 shadow-xs flex items-center justify-between text-xs font-mono">
              <span className="text-[10px] text-[#0F58A8] font-black uppercase tracking-wider font-heading">
                Garis Sejarah 2 Dekade KCA
              </span>
              <div className="flex items-center gap-2 text-[11px] font-bold text-slate-400">
                {TIMELINE_MILESTONES.map((m, idx) => (
                  <div key={idx} className="flex items-center gap-2">
                    <span className="text-slate-700 font-heading">
                      {m.year.split('–')[0]}
                    </span>
                    {idx < TIMELINE_MILESTONES.length - 1 && <span>•</span>}
                  </div>
                ))}
              </div>
            </div>
          </motion.div>

          {/* 3D Graphic Journey Track (Isometric Depth Conduit, 3D Nodes & Traveling Energy Capsule) */}
          <Timeline3DGraphicTrack 
            progressHeight={centerLineHeight} 
            activeOpacity={activeTimelineOpacity} 
          />

          {/* ======================================================================= */}
          {/* FASE 1: INTRO SECTION LOCK (FULL SCREEN TITLE + SCROLL BLUR ZOOM EFFECT)*/}
          {/* ======================================================================= */}
          <motion.div
            style={{
              opacity: introOpacity,
              scale: introScale,
              filter: introFilter,
              pointerEvents: introPointerEvents,
            }}
            className="absolute inset-0 flex flex-col items-center justify-center text-center px-4 sm:px-8 z-30 will-change-transform bg-slate-50/95"
          >
            <div className="max-w-3xl space-y-4">
              <h2 className="text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-slate-900 tracking-tight leading-tight">
                Alur Perjalanan &amp; Lika-Liku 2 Dekade (2004 – 2026)
              </h2>
              <p className="text-xs sm:text-sm text-slate-600 font-normal leading-relaxed max-w-2xl mx-auto">
                Menelusuri rintangan formulasi, inovasi reaktor Stainless Steel 316L, dan modernisasi tata kelola pabrik PT Kediri Chemical Abadi.
              </p>
              <div className="pt-6 flex flex-col items-center gap-2 text-slate-400">
                <span className="text-[11px] font-bold font-heading uppercase tracking-widest text-[#0F58A8]">
                  Gulir ke bawah untuk masuk ke garis sejarah
                </span>
                <div className="w-7 h-7 rounded-full bg-blue-50 border border-blue-200 text-[#0F58A8] flex items-center justify-center">
                  <ChevronDown className="w-3.5 h-3.5 animate-bounce" />
                </div>
              </div>
            </div>
          </motion.div>

          {/* ======================================================================= */}
          {/* FASE 2 TO FASE 6: 5 HISTORICAL CHAPTERS STAGES (2004, 2008, 2014...)    */}
          {/* ======================================================================= */}
          {TIMELINE_MILESTONES.map((m, idx) => {
            const isEven = idx % 2 === 1
            const anim = phaseAnimStates[idx]

            return (
              <motion.div
                key={idx}
                style={{
                  opacity: anim.opacity,
                  y: anim.y,
                  scale: anim.scale,
                  pointerEvents: anim.pointerEvents,
                }}
                className="absolute inset-0 flex items-center justify-center px-4 sm:px-8 lg:px-14 xl:px-20 lg:pl-20 xl:pl-28 z-20 will-change-transform"
              >
                <div className="max-w-[1700px] w-full">
                  <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
                    
                    {/* Editorial Content (7 Kolom - 3D Parallax Typography & Progressive Scroll Details) */}
                    <div className={`space-y-3.5 lg:col-span-7 ${isEven ? 'lg:order-2' : 'lg:order-1'}`}>
                      
                      {/* STEP 1: Phase Badge, 3D Metallic Year, Title & Narrative Story (Reveals First) */}
                      <motion.div 
                        style={{ opacity: anim.step1Opacity, y: anim.step1Y }}
                        className="space-y-1.5"
                      >
                        <div className="flex items-center justify-between">
                          <span className="text-[11px] font-mono font-bold text-[#0F58A8] tracking-wider uppercase">
                            Fase 0{idx + 1} dari 05
                          </span>
                          <span className="text-[10px] font-mono font-bold text-slate-400">
                            {m.badge.split('•')[1] || ''}
                          </span>
                        </div>

                        {/* Continuous Phase Progression Fill Beam */}
                        <div className="w-full h-1 bg-slate-200/80 rounded-full overflow-hidden my-1">
                          <motion.div
                            style={{ width: anim.progressWidth }}
                            className="h-full bg-gradient-to-r from-[#0F58A8] via-[#38BDF8] to-[#0F58A8] rounded-full shadow-[0_0_8px_#38BDF8]"
                          />
                        </div>

                        <div className="flex items-baseline gap-3 pt-0.5">
                          <span className="text-3xl sm:text-4xl lg:text-5xl font-black font-heading tracking-tight text-slate-900 drop-shadow-[0_6px_14px_rgba(15,88,168,0.15)] select-none">
                            {m.year}
                          </span>
                        </div>

                        <h3 className="text-base sm:text-lg lg:text-xl font-extrabold font-heading text-slate-900 leading-snug">
                          {m.title}
                        </h3>

                        <p className="text-xs sm:text-[13px] text-slate-700 leading-relaxed font-normal pt-1">
                          {m.desc}
                        </p>
                      </motion.div>

                      {/* STEP 2: Tantangan vs Solusi Rekayasa (Revealed on Scroll Lanjutan) */}
                      <motion.div 
                        style={{ opacity: anim.step2Opacity, y: anim.step2Y }}
                        className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-1"
                      >
                        <motion.div 
                          style={{ borderLeftColor: anim.challengeBorder }}
                          className="border-l-2 pl-3 space-y-0.5 transition-colors duration-300"
                        >
                          <span className="text-[10px] font-bold uppercase tracking-wider text-red-600 block font-heading">
                            Tantangan Lapangan:
                          </span>
                          <p className="text-xs text-slate-700 leading-relaxed">
                            {m.challenge}
                          </p>
                        </motion.div>

                        <motion.div 
                          style={{ borderLeftColor: anim.solutionBorder }}
                          className="border-l-2 pl-3 space-y-0.5 transition-colors duration-300"
                        >
                          <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-700 block font-heading">
                            Solusi Rekayasa KCA:
                          </span>
                          <p className="text-xs text-slate-700 leading-relaxed">
                            {m.solution}
                          </p>
                        </motion.div>
                      </motion.div>

                      {/* STEP 3: Rincian Operasional & Terobosan Utama (Revealed on Scroll Mendalam) */}
                      <motion.div 
                        style={{ opacity: anim.step3Opacity, y: anim.step3Y }}
                        className="space-y-2.5 pt-1.5 border-t border-slate-200"
                      >
                        <div className="space-y-1.5">
                          <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-900 block font-heading">
                            Rincian Operasional &amp; Standarisasi Lab:
                          </span>
                          <div className="space-y-1">
                            {m.points.map((pt, pIdx) => (
                              <div key={pIdx} className="flex items-start gap-2 text-xs text-slate-700">
                                <CheckCircle2 className="w-3.5 h-3.5 text-[#0F58A8] shrink-0 mt-0.5" />
                                <span className="leading-snug font-medium">{pt}</span>
                              </div>
                            ))}
                          </div>
                        </div>

                        {/* Terobosan Utama */}
                        <div className="border-l-2 border-[#0F58A8] pl-3 py-0.5 space-y-0.5">
                          <span className="text-[10px] font-bold text-[#0F58A8] uppercase tracking-wider block font-heading">
                            Dampak &amp; Terobosan Utama:
                          </span>
                          <p className="text-xs text-slate-800 font-semibold italic">
                            "{m.breakthrough}"
                          </p>
                        </div>
                      </motion.div>

                    </div>

                    {/* High-Resolution Real Factory Photo with 3D Physics Tilt & Scroll Scale Push (5 Kolom) */}
                    <div className={`lg:col-span-5 ${isEven ? 'lg:order-1' : 'lg:order-2'}`}>
                      <motion.div style={{ scale: anim.photoScale }}>
                        <Tilt3DPhotoCard
                          image={m.image}
                          title={m.title}
                          caption={m.imageCaption}
                          phaseNumber={idx + 1}
                        />
                      </motion.div>
                    </div>

                  </div>
                </div>
              </motion.div>
            )
          })}

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 4. BEDAH FASILITAS & INFRASTRUKTUR MANUFAKTUR PABRIK (DEDICATED SECTION)   */}
      {/* ========================================================================= */}
      <section className="py-12 sm:py-16 bg-white text-slate-900 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-10">
          
          <div className="max-w-3xl space-y-1.5">
            <h2 className="text-lg sm:text-xl lg:text-2xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Infrastruktur Manufaktur &amp; Kapabilitas Rekayasa Reaktor SS 316L
            </h2>
            <p className="text-xs text-slate-600 leading-relaxed font-normal">
              Fasilitas produksi PT Kediri Chemical Abadi di Mojoroto, Kediri didesain khusus untuk stabilitas kimia konsentrat tinggi dengan toleransi nol terhadap kontaminasi logam atau partikulat.
            </p>
          </div>

          {/* Deep Dive 1: Lini Reaktor Stainless Steel 316L */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
            <div className="lg:col-span-6 space-y-3">
              <div className="space-y-1">
                <h3 className="text-base sm:text-lg font-extrabold font-heading text-slate-900">
                  Lini Reaktor Pencampur Stainless Steel 316L (500+ Ton / Bulan)
                </h3>
                <p className="text-xs text-slate-700 leading-relaxed">
                  Fasilitas reaktor utama kami dibangun menggunakan material Stainless Steel 316L berkemurnian tinggi (*Food &amp; Chemical Grade*) yang memiliki resistensi absolut terhadap korosi bahan asam kuat maupun alkali pekat. Dilengkapi sistem pengadukan agitator variabel (*Variable Frequency Drive*) dan jaket pengatur temperatur untuk memastikan reaksi pelarutan surfaktan homogen sempurna tanpa risiko penggumpalan (*lump-free*).
                </p>
              </div>

              <div className="space-y-1 pt-1.5 border-t border-slate-200 text-xs">
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Standar Material Tangki:</span>
                  <strong className="text-slate-900 font-bold">Stainless Steel 316L Anti-Korosi</strong>
                </div>
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Kapasitas Output Pabrik:</span>
                  <strong className="text-slate-900 font-bold">500+ Ton Konsentrat / Bulan</strong>
                </div>
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Sistem Pengadukan:</span>
                  <strong className="text-slate-900 font-bold">Multi-Blade Agitator Variable RPM</strong>
                </div>
                <div className="flex justify-between py-0.5">
                  <span className="text-slate-500">Kontrol Suhu Reaksi:</span>
                  <strong className="text-slate-900 font-bold">Jacketed Thermal Cooling &amp; Heating</strong>
                </div>
              </div>
            </div>

            <div className="lg:col-span-6">
              <div className="relative rounded-3xl overflow-hidden border border-sky-100 shadow-xl shadow-blue-900/5 aspect-[16/10] bg-sky-50">
                <img
                  src="/images/kca_factory_reactors.jpg"
                  alt="Fasilitas Reaktor Stainless Steel 316L PT Kediri Chemical Abadi"
                  className="w-full h-full object-cover select-none"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-900/20 via-transparent to-transparent pointer-events-none" />
              </div>
            </div>
          </div>

          {/* Deep Dive 2: Sistem Pemurnian Air Demineralisasi (Demin & RO) */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center pt-6 border-t border-slate-200">
            <div className="lg:col-span-6 space-y-3 lg:order-2 order-1">
              <div className="space-y-1">
                <h3 className="text-base sm:text-lg font-extrabold font-heading text-slate-900">
                  Sistem Pemurnian Air Demineralisasi &amp; Reverse Osmosis (RO)
                </h3>
                <p className="text-xs text-slate-700 leading-relaxed">
                  Kualitas air merupakan 80% fondasi dari kestabilan cairan kimia pembersih. Air sumur atau PDAM dengan kadar kesadahan tinggi dapat mengikat surfaktan aktif sehingga daya cuci menurun drastis. Pabrik KCA mengoperasikan sistem Reverse Osmosis (RO) multi-tahap dan deionisasi resin khusus untuk menghasilkan air ultra-murni dengan Total Dissolved Solids (TDS) di bawah 5 PPM.
                </p>
              </div>

              <div className="space-y-1 pt-1.5 border-t border-slate-200 text-xs">
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Kadar Padatan Terlarut (TDS):</span>
                  <strong className="text-emerald-700 font-bold">&lt; 5 PPM (Ultra-Pure Deionized Water)</strong>
                </div>
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Teknologi Filtrasi:</span>
                  <strong className="text-slate-900 font-bold">Double-Stage RO &amp; Mixed-Bed Resin</strong>
                </div>
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Kapasitas Pasokan Air:</span>
                  <strong className="text-slate-900 font-bold">50.000 Liter Air Murni / Hari</strong>
                </div>
                <div className="flex justify-between py-0.5">
                  <span className="text-slate-500">Manfaat Utama:</span>
                  <strong className="text-slate-900 font-bold">Bebas Endapan &amp; Busa Surfaktan Optimal</strong>
                </div>
              </div>
            </div>

            <div className="lg:col-span-6 lg:order-1 order-2 space-y-3">
              <div className="border-l-2 border-emerald-600 pl-4 py-1 space-y-1.5">
                <div className="flex items-center gap-2 text-emerald-600">
                  <Droplets className="w-4 h-4" />
                  <strong className="text-xs sm:text-sm font-bold font-heading text-slate-900">
                    Standar Mutu Pelarut Murni KCA vs Air Baku Biasa
                  </strong>
                </div>
                <p className="text-xs text-slate-600 leading-relaxed">
                  Penggunaan air demineralisasi murni mencegah terbentuknya kerak mineral kalsium karbonat pada elemen pemanas mesin cuci mitra, menjaga kejernihan larutan kimia selama 24 bulan masa simpan, serta menjamin formula tidak memisah saat disimpan di gudang suhu ruang tropis.
                </p>
              </div>
            </div>
          </div>

          {/* Deep Dive 3: Pengemasan & Induksi Segel Hermetis */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center pt-6 border-t border-slate-200">
            <div className="lg:col-span-6 space-y-3">
              <div className="space-y-1">
                <h3 className="text-base sm:text-lg font-extrabold font-heading text-slate-900">
                  Lini Pengemasan Semi-Otomatis &amp; Induksi Segel Anti-Bocor
                </h3>
                <p className="text-xs text-slate-700 leading-relaxed">
                  Seluruh produk dialirkan melalui penyaringan mikro 5-mikron sebelum proses pengisian jerigen 5L, 20L, drum 200L, atau tangki IBC 1.000L. Dilengkapi teknologi induksi segel aluminium foil hermetis kedap udara untuk menjamin tidak ada kebocoran cairan kimia maupun penguapan aroma selama pengiriman ekspedisi logistik antarpulau.
                </p>
              </div>

              <div className="space-y-1 pt-1.5 border-t border-slate-200 text-xs">
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Varian Kemasan Resmi:</span>
                  <strong className="text-slate-900 font-bold">Jerigen 5L, 20L, Drum 200L, IBC 1.000L</strong>
                </div>
                <div className="flex justify-between py-0.5 border-b border-slate-100">
                  <span className="text-slate-500">Teknologi Penyegelan:</span>
                  <strong className="text-slate-900 font-bold">Induction Cap Sealer (Segel Kedap Udara)</strong>
                </div>
                <div className="flex justify-between py-0.5">
                  <span className="text-slate-500">Standar Pengiriman:</span>
                  <strong className="text-slate-900 font-bold">Palet Kayu Kokoh + Wrapping Plastik Tebal</strong>
                </div>
              </div>
            </div>

            <div className="lg:col-span-6">
              <div className="relative overflow-hidden border border-slate-300 shadow-sm aspect-[16/10] bg-slate-50 flex items-center justify-center p-4">
                <img
                  src="/images/kca_packaging_lineup.png"
                  alt="Lini Kemasan Produk Kimia PT Kediri Chemical Abadi"
                  className="max-h-full object-contain"
                />
              </div>
            </div>
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 5. DEWAN DIREKSI & KEPEMIMPINAN 2 GENERASI (YAN EFFENDI & YERIKHO ARFENSIAS)*/}
      {/* ========================================================================= */}
      <section className="py-12 sm:py-16 bg-slate-50/70 text-slate-900 border-b border-slate-200 relative overflow-hidden">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-10">
          
          <div className="text-center max-w-3xl mx-auto space-y-1.5">
            <h2 className="text-lg sm:text-xl lg:text-2xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Dewan Direksi &amp; Kepemimpinan 2 Generasi
            </h2>
            <p className="text-xs text-slate-600 font-normal max-w-2xl mx-auto">
              Sinergi pengalaman lebih dari 20 tahun dalam rekayasa formula kimia industri dengan manajemen operasional modern untuk memastikan kepuasan dan keberlanjutan bisnis mitra.
            </p>
          </div>

          {/* Open Direct Editorial Grid (Tanpa Box Card) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-14 max-w-6xl mx-auto divide-y md:divide-y-0 md:divide-x divide-slate-200/90 items-start">
            {COMPANY_DATA.boardOfDirectors.map((person, idx) => (
              <div
                key={idx}
                className={`space-y-4 ${idx === 1 ? 'md:pl-10 lg:pl-14 pt-8 md:pt-0' : 'md:pr-10 lg:pr-14'}`}
              >
                {/* Monogram & Title Stack */}
                <div className="flex items-start gap-3.5">
                  <div className="w-12 h-12 bg-white border border-slate-300 text-[#0F58A8] flex items-center justify-center font-heading font-black text-base shadow-2xs shrink-0 mt-0.5">
                    {person.name.split(' ').map((n) => n[0]).join('')}
                  </div>
                  <div>
                    <h3 className="text-base sm:text-lg font-extrabold font-heading text-slate-900 leading-snug">
                      {person.name}
                    </h3>
                    <span className="text-xs font-bold text-[#0F58A8] block">
                      {person.role}
                    </span>
                    <span className="text-[11px] text-slate-500 block pt-0.5 font-medium">
                      Pengalaman: {person.experience}
                    </span>
                  </div>
                </div>

                <p className="text-xs text-slate-700 leading-relaxed font-normal">
                  {person.bio}
                </p>

                {/* Tanggung Jawab Operasional */}
                <div className="space-y-1.5 pt-1.5 border-t border-slate-200/80">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 block">
                    Fokus Tanggung Jawab Operasional:
                  </span>
                  <div className="space-y-1 text-xs text-slate-800">
                    {(person.responsibilities || [person.focus]).map((resp, rIdx) => (
                      <div key={rIdx} className="flex items-start gap-2">
                        <CheckCircle2 className="w-3.5 h-3.5 text-[#0F58A8] shrink-0 mt-0.5" />
                        <span className="leading-snug">{resp}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 6. 4 NILAI UTAMA & KOMITMEN TATA KELOLA KORPORAT (ESG)                     */}
      {/* ========================================================================= */}
      <section className="py-12 sm:py-16 bg-white text-slate-900 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-10">
          
          <div className="max-w-3xl space-y-1.5">
            <h2 className="text-lg sm:text-xl lg:text-2xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              4 Nilai Fundamental &amp; Komitmen Keberlanjutan (ESG)
            </h2>
            <p className="text-xs text-slate-600 leading-relaxed font-normal">
              Prinsip operasional yang menjadi pegangan seluruh tim produksi, formulator lab, dan manajemen PT Kediri Chemical Abadi.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-2 border-t border-slate-200">
            <div className="space-y-1.5 border-l-2 border-[#0F58A8] pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                1. Kejujuran Formulasi Murni
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Menolak penambahan bahan pengisi (*filler*) garam murah atau pengencer berlebih yang merusak mesin dan memboroskan biaya pelanggan.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-emerald-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                2. Tanggung Jawab Lingkungan (IPAL)
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Komitmen 100% bebas fosfat (STPP-free) dan surfaktan biodegradasi &gt;90% (OECD 301D) menjaga keselamatan ekosistem air.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-amber-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                3. Akuntabilitas Legalitas &amp; Pajak
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Beroperasi dengan perizinan OSS-RBA resmi, SPPKP dengan e-Faktur PPN 11%, serta siap pengadaan tender pemerintah LKPP RI.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-indigo-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                4. Jaminan Pasokan Kontinu
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Kapasitas produksi 500+ Ton/bulan dan armada logistik menjamin kelancaran pasokan bahan kimia rutin tanpa jeda operasional.
              </p>
            </div>
          </div>

        </div>
      </section>

      {/* Full Width CTA Section */}
      <CTASection />
    </main>
  )
}
