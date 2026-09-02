import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  ArrowRight, 
  CheckCircle2, 
  ShieldCheck,
  Award,
  Layers,
  Calculator,
  FileCheck2,
  FileText
} from 'lucide-react'
import { PRODUCTS_DATA } from '@/data/productsData'
import RFQModal from '@/components/ui/RFQModal'

// Professional Corporate Category Color Themes & Volumetric Styles
const SATELLITE_THEMES = {
  'laundry': {
    topBar: 'bg-[#0F58A8]',
    border: 'border-blue-300 hover:border-[#0F58A8]',
    badge: 'bg-[#0F58A8] text-white',
    skuBadge: 'bg-blue-100 text-[#0F58A8] border-blue-300',
    topTint: 'bg-gradient-to-b from-blue-50/80 via-white to-white',
    specBg: 'bg-blue-50/50 border-blue-100',
    btnBg: 'bg-[#0F58A8] hover:bg-blue-800 text-white',
    shadow: 'shadow-md shadow-blue-900/10 hover:shadow-2xl hover:shadow-blue-900/20 hover:-translate-y-1',
  },
  'housekeeping': {
    topBar: 'bg-[#4338CA]',
    border: 'border-indigo-300 hover:border-[#4338CA]',
    badge: 'bg-[#4338CA] text-white',
    skuBadge: 'bg-indigo-100 text-[#4338CA] border-indigo-300',
    topTint: 'bg-gradient-to-b from-indigo-50/80 via-white to-white',
    specBg: 'bg-indigo-50/50 border-indigo-100',
    btnBg: 'bg-[#4338CA] hover:bg-indigo-800 text-white',
    shadow: 'shadow-md shadow-indigo-900/10 hover:shadow-2xl hover:shadow-indigo-900/20 hover:-translate-y-1',
  },
  'fnb': {
    topBar: 'bg-[#B45309]',
    border: 'border-amber-300 hover:border-[#B45309]',
    badge: 'bg-[#B45309] text-white',
    skuBadge: 'bg-amber-100 text-[#B45309] border-amber-300',
    topTint: 'bg-gradient-to-b from-amber-50/80 via-white to-white',
    specBg: 'bg-amber-50/50 border-amber-100',
    btnBg: 'bg-[#B45309] hover:bg-amber-800 text-white',
    shadow: 'shadow-md shadow-amber-900/10 hover:shadow-2xl hover:shadow-amber-900/20 hover:-translate-y-1',
  },
  'medis': {
    topBar: 'bg-[#059669]',
    border: 'border-emerald-300 hover:border-[#059669]',
    badge: 'bg-[#059669] text-white',
    skuBadge: 'bg-emerald-100 text-[#059669] border-emerald-300',
    topTint: 'bg-gradient-to-b from-emerald-50/80 via-white to-white',
    specBg: 'bg-emerald-50/50 border-emerald-100',
    btnBg: 'bg-[#059669] hover:bg-emerald-800 text-white',
    shadow: 'shadow-md shadow-emerald-900/10 hover:shadow-2xl hover:shadow-emerald-900/20 hover:-translate-y-1',
  },
  'otomotif': {
    topBar: 'bg-[#0A192F]',
    border: 'border-slate-400 hover:border-[#0A192F]',
    badge: 'bg-[#0A192F] text-white',
    skuBadge: 'bg-slate-200 text-slate-900 border-slate-400',
    topTint: 'bg-gradient-to-b from-slate-100 via-white to-white',
    specBg: 'bg-slate-100/70 border-slate-200',
    btnBg: 'bg-[#0A192F] hover:bg-slate-800 text-white',
    shadow: 'shadow-md shadow-slate-900/15 hover:shadow-2xl hover:shadow-slate-900/25 hover:-translate-y-1',
  },
}

// Professional Vector Corporate Logos & Monograms
const CorporateLogos = {
  Laundry: () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z" />
      <path d="M8 14a4 4 0 0 0 8 0" strokeDasharray="2 2" />
      <circle cx="12" cy="12" r="1.5" fill="currentColor" />
    </svg>
  ),
  Hospitality: () => (
    <svg className="w-5 h-5 text-[#4338CA]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 9h1M14 9h1M9 13h1M14 13h1M9 17h1M14 17h1" />
      <path d="M12 3v3" strokeWidth="2" />
    </svg>
  ),
  Healthcare: () => (
    <svg className="w-5 h-5 text-[#059669]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 4v16m-8-8h16" strokeWidth="2.5" strokeLinecap="round" />
      <circle cx="12" cy="12" r="9" strokeWidth="1.5" />
    </svg>
  ),
  Industrial: () => (
    <svg className="w-5 h-5 text-slate-800" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M2 20h20M6 20V8l6 4V8l6 4V4l4 4v12" />
      <circle cx="6" cy="14" r="1.5" fill="currentColor" />
      <circle cx="12" cy="16" r="1.5" fill="currentColor" />
    </svg>
  ),
  FnB: () => (
    <svg className="w-5 h-5 text-[#B45309]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M18 2v6a3 3 0 0 1-3 3 3 3 0 0 1-3-3V2M15 11v11M5 2v8a2 2 0 0 0 2 2h0a2 2 0 0 0 2-2V2M7 12v10" />
    </svg>
  ),
  Reactor: () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <rect x="5" y="4" width="14" height="16" rx="1" />
      <path d="M9 2h6M12 2v2M8 12h8M9 20v2M15 20v2" />
      <circle cx="12" cy="12" r="2" fill="currentColor" fillOpacity="0.2" />
    </svg>
  ),
}

const CATEGORY_LOGOS = {
  'laundry': CorporateLogos.Laundry,
  'Commercial & Hospital Laundry': CorporateLogos.Laundry,
  'Commercial Laundry': CorporateLogos.Laundry,
  'housekeeping': CorporateLogos.Hospitality,
  'Hospitality & Hotel': CorporateLogos.Hospitality,
  'Hotel, Resort & Garmen': CorporateLogos.Hospitality,
  'fnb': CorporateLogos.FnB,
  'Food & Beverage': CorporateLogos.FnB,
  'Restoran & Food Processing': CorporateLogos.FnB,
  'otomotif': CorporateLogos.Industrial,
  'Industrial & Heavy Duty': CorporateLogos.Industrial,
  'Otomotif & Bengkel Pabrik': CorporateLogos.Industrial,
  'medis': CorporateLogos.Healthcare,
  'Medical & Hospital': CorporateLogos.Healthcare,
}

const PACKAGING_VARIANTS = [
  { id: '5l', label: 'Jerigen 5L', subtitle: 'Klinik & Laundry Komersial', image: '/images/product_jerigen5l.jpg' },
  { id: '20l', label: 'Jerigen 20L', subtitle: 'Hotel & RS Rujukan', image: '/images/product_jerigen20l.jpg' },
  { id: '200l', label: 'Drum 200L', subtitle: 'Sentra Pabrik & Industri', image: '/images/product_drum200l.jpg' },
  { id: 'lineup', label: 'Lini Lengkap PKRT', subtitle: 'Standar Izin Edar Kemenkes RI', image: '/images/kca_packaging_lineup.png' },
]

export default function ProductShowcaseSection() {
  const [rfqOpen, setRfqOpen] = useState(false)
  const [activeTab, setActiveTab] = useState('features')
  const [selectedPackaging, setSelectedPackaging] = useState(PACKAGING_VARIANTS[0])
  const [laundryKg, setLaundryKg] = useState(300)

  const productsArray = Array.isArray(PRODUCTS_DATA) ? PRODUCTS_DATA : []
  const heroProduct = productsArray.find((p) => p.isHero) || productsArray[0] || {}
  const satelliteProducts = productsArray.filter((p) => !p.isHero)

  // Dynamic dosage calculations
  const kcaLitersPerDay = ((laundryKg * 12.5) / 1000).toFixed(1)
  const competitorLitersPerDay = ((laundryKg * 40) / 1000).toFixed(1)
  const savingsPct = Math.round((1 - 12.5 / 40) * 100)

  return (
    <>
      <section id="products" className="py-16 sm:py-24 bg-white text-slate-900 relative overflow-hidden">
        
        {/* Ambient 4K Liquid Water Caustic & Ripple Texture */}
        <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden select-none opacity-30 mix-blend-multiply">
          <img
            src="/images/bg_liquid_caustics_4k.png"
            alt="Liquid Water Caustics Texture"
            className="w-full h-full object-cover object-top"
          />
        </div>

        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-14 relative z-10">
          
          {/* Section Header: Direct Title & Subline (No Eyebrow Tag) */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 pb-6 border-b border-sky-100">
            <div className="space-y-2 max-w-3xl">
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                Lini Produk Kimia Pembersih Industri Konsentrat Murni
              </h2>
            </div>
            <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
              Diformulasikan dari bahan aktif surfaktan murni tanpa bahan pengisi (*filler*), 100% bebas fosfat, hemat dosis per siklus pencucian, dan teruji ramah biofilter IPAL rumah sakit.
            </p>
          </div>

          {/* ========================================================================= */}
          {/* 1. HERO PRODUCT: OPEN EDITORIAL SHOWCASE (FLUID WATER THEME)             */}
          {/* ========================================================================= */}
          {heroProduct.id && (
            <div className="pb-16 border-b border-sky-100">
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-start">
                
                {/* Sisi Kiri: Galeri Visual Kemasan Bersih (5 Kolom) */}
                <div className="lg:col-span-5 space-y-4">
                  
                  {/* Foto Produk Murni & Bersih Tanpa Background Card */}
                  <div className="relative flex flex-col items-center justify-center p-2 aspect-[4/3] group">
                    
                    {/* Dynamic Image with Crossfade & Clean Blend */}
                    <AnimatePresence mode="wait">
                      <motion.img
                        key={selectedPackaging.id}
                        src={selectedPackaging.image}
                        alt={`${heroProduct.title} - ${selectedPackaging.label}`}
                        initial={{ opacity: 0, scale: 0.95 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0.95 }}
                        transition={{ duration: 0.3 }}
                        className="w-full h-60 sm:h-72 object-contain relative z-10 mix-blend-multiply group-hover:scale-105 transition-transform duration-500 select-none"
                      />
                    </AnimatePresence>
                  </div>

                  {/* Packaging Variant Switcher (Fluid Pill Buttons) */}
                  <div className="space-y-1.5">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 block font-heading">
                      Pilihan Kemasan Pabrik:
                    </span>
                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                      {PACKAGING_VARIANTS.map((v) => (
                        <button
                          key={v.id}
                          onClick={() => setSelectedPackaging(v)}
                          className={`px-3 py-2 text-center rounded-xl border transition-all cursor-pointer ${
                            selectedPackaging.id === v.id
                              ? 'bg-gradient-to-r from-[#0F58A8] to-[#0284C7] text-white border-transparent shadow-sm'
                              : 'bg-white text-slate-700 border-sky-100 hover:border-sky-300 hover:bg-sky-50/50'
                          }`}
                        >
                          <strong className="text-[11px] font-bold block font-heading truncate">
                            {v.label}
                          </strong>
                          <span className={`text-[9px] block truncate ${selectedPackaging.id === v.id ? 'text-blue-100' : 'text-slate-500'}`}>
                            {v.subtitle.split('&')[0]}
                          </span>
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Highlights Bullet Badges (Open Inline) */}
                  <div className="grid grid-cols-2 gap-2.5 pt-1">
                    <div className="flex items-center gap-2 text-xs text-slate-700 font-medium">
                      <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                      </div>
                      <span>100% Bebas Fosfat STPP</span>
                    </div>
                    <div className="flex items-center gap-2 text-xs text-slate-700 font-medium">
                      <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                      </div>
                      <span>OECD 301D &gt;90% IPAL</span>
                    </div>
                    <div className="flex items-center gap-2 text-xs text-slate-700 font-medium">
                      <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                      </div>
                      <span>Dosis Hemat 10–15 ml/kg</span>
                    </div>
                    <div className="flex items-center gap-2 text-xs text-slate-700 font-medium">
                      <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                      </div>
                      <span>Optical Brightener Anti-Pudar</span>
                    </div>
                  </div>

                </div>

                {/* Sisi Kanan: Tab Interaktif Detail Formulasi & TDS (7 Kolom) */}
                <div className="lg:col-span-7 space-y-5">
                  
                  {/* Title & Narrative Overview (Direct Title - No Eyebrow Tag) */}
                  <div className="space-y-2">
                    <h3 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                      {heroProduct.title || heroProduct.name}
                    </h3>
                    <p className="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal">
                      Deterjen cair konsentrat rendah busa (*low-foam*) dengan rekayasa agen pengkhelat murni (*sequestering agent*) yang menaklukkan kesadahan air tanah tinggi Jawa Timur (&gt;350 ppm CaCO₃). Mencegah pengapuran elemen pemanas mesin cuci industri dan menjaga kelembutan serat linen hingga 50x siklus cuci.
                    </p>
                  </div>

                  {/* Interactive Tab Switcher (Minimalist Underline Style) */}
                  <div className="border-b border-slate-200 flex items-center gap-4 overflow-x-auto pb-px">
                    <button
                      onClick={() => setActiveTab('features')}
                      className={`pb-2 text-xs font-bold font-heading uppercase tracking-wider transition-all border-b-2 cursor-pointer flex items-center gap-1.5 whitespace-nowrap ${
                        activeTab === 'features'
                          ? 'border-[#0F58A8] text-[#0F58A8]'
                          : 'border-transparent text-slate-500 hover:text-slate-900'
                      }`}
                    >
                      <Layers className="w-3.5 h-3.5" />
                      <span>Rekayasa &amp; Mekanisme Formulasi</span>
                    </button>

                    <button
                      onClick={() => setActiveTab('specs')}
                      className={`pb-2 text-xs font-bold font-heading uppercase tracking-wider transition-all border-b-2 cursor-pointer flex items-center gap-1.5 whitespace-nowrap ${
                        activeTab === 'specs'
                          ? 'border-[#0F58A8] text-[#0F58A8]'
                          : 'border-transparent text-slate-500 hover:text-slate-900'
                      }`}
                    >
                      <FileCheck2 className="w-3.5 h-3.5" />
                      <span>Lembar Data Teknis (TDS Matrix)</span>
                    </button>

                    <button
                      onClick={() => setActiveTab('calculator')}
                      className={`pb-2 text-xs font-bold font-heading uppercase tracking-wider transition-all border-b-2 cursor-pointer flex items-center gap-1.5 whitespace-nowrap ${
                        activeTab === 'calculator'
                          ? 'border-[#0F58A8] text-[#0F58A8]'
                          : 'border-transparent text-slate-500 hover:text-slate-900'
                      }`}
                    >
                      <Calculator className="w-3.5 h-3.5" />
                      <span>Kalkulator Dosis &amp; ROI Biaya</span>
                    </button>
                  </div>

                  {/* Tab Content Display (Open Editorial Layout) */}
                  <div className="min-h-[200px]">
                    {/* TAB 1: Rekayasa Formulasi */}
                    {activeTab === 'features' && (
                      <motion.div
                        initial={{ opacity: 0, y: 6 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.25 }}
                        className="grid grid-cols-1 sm:grid-cols-2 gap-4"
                      >
                        <div className="border-l-2 border-[#0F58A8] pl-3.5 space-y-0.5">
                          <strong className="text-xs font-bold text-slate-900 block font-heading">
                            1. Sequestering Agent Murni
                          </strong>
                          <p className="text-xs text-slate-600 leading-relaxed font-normal">
                            Mengikat ion Ca²⁺ &amp; Mg²⁺ air tanah sadah agar molekul surfaktan aktif bekerja 100% tanpa pengendapan kerak.
                          </p>
                        </div>

                        <div className="border-l-2 border-emerald-600 pl-3.5 space-y-0.5">
                          <strong className="text-xs font-bold text-slate-900 block font-heading">
                            2. Dual Surfactant Non-Ionic &amp; Anionic
                          </strong>
                          <p className="text-xs text-slate-600 leading-relaxed font-normal">
                            Penetrasi serat mikro ganda memecah noda protein darah, lemak dapur, dan partikulat debu secara tuntas.
                          </p>
                        </div>

                        <div className="border-l-2 border-amber-600 pl-3.5 space-y-0.5">
                          <strong className="text-xs font-bold text-slate-900 block font-heading">
                            3. Low-Foam Formula (Hemat Air)
                          </strong>
                          <p className="text-xs text-slate-600 leading-relaxed font-normal">
                            Busa rendah menjaga bantalan drum mesin cuci dan memotong 1 siklus bilas, menghemat air bersih hingga 25%.
                          </p>
                        </div>

                        <div className="border-l-2 border-purple-600 pl-3.5 space-y-0.5">
                          <strong className="text-xs font-bold text-slate-900 block font-heading">
                            4. Anti-Redeposition Polymer
                          </strong>
                          <p className="text-xs text-slate-600 leading-relaxed font-normal">
                            Mengunci kotoran terlepas dalam air buangan agar tidak menempel kembali pada kain putih selama putaran ekstraksi.
                          </p>
                        </div>
                      </motion.div>
                    )}

                    {/* TAB 2: TDS Matrix Spesifikasi Laboratorium */}
                    {activeTab === 'specs' && (
                      <motion.div
                        initial={{ opacity: 0, y: 6 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.25 }}
                        className="space-y-2 text-xs text-slate-700"
                      >
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-1.5 divide-y sm:divide-y-0 divide-slate-100">
                          <div className="flex justify-between py-1 border-b border-slate-100">
                            <span className="text-slate-500">Bahan Aktif Total:</span>
                            <strong className="text-slate-900 font-bold">18% – 22% Active Matter</strong>
                          </div>
                          <div className="flex justify-between py-1 border-b border-slate-100">
                            <span className="text-slate-500">Nilai pH Digital (1% Sol):</span>
                            <strong className="text-slate-900 font-bold">7.5 – 8.5 (Netral Serat)</strong>
                          </div>
                          <div className="flex justify-between py-1 border-b border-slate-100">
                            <span className="text-slate-500">Berat Jenis (25°C):</span>
                            <strong className="text-slate-900 font-bold">1.02 – 1.05 g/cm³</strong>
                          </div>
                          <div className="flex justify-between py-1 border-b border-slate-100">
                            <span className="text-slate-500">Standar IPAL (OECD 301D):</span>
                            <strong className="text-emerald-700 font-bold">&gt;90% Biodegradable</strong>
                          </div>
                          <div className="flex justify-between py-1 border-b border-slate-100">
                            <span className="text-slate-500">Kandungan Fosfat (STPP):</span>
                            <strong className="text-emerald-700 font-bold">0.0% (100% Bebas Fosfat)</strong>
                          </div>
                          <div className="flex justify-between py-1 border-b border-slate-100">
                            <span className="text-slate-500">Kelarutan Air Murni:</span>
                            <strong className="text-slate-900 font-bold">100% Sempurna (Bebas Endapan)</strong>
                          </div>
                        </div>

                        <div className="pt-2 text-[11px] text-slate-500 flex items-center gap-1.5">
                          <Award className="w-3.5 h-3.5 text-[#0F58A8]" />
                          <span>Setiap pengiriman batch disertai Certificate of Analysis (COA) resmi bertandatangan QC Manager KCA.</span>
                        </div>
                      </motion.div>
                    )}

                    {/* TAB 3: Interactive Dosage Calculator */}
                    {activeTab === 'calculator' && (
                      <motion.div
                        initial={{ opacity: 0, y: 6 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.25 }}
                        className="space-y-4"
                      >
                        <div className="space-y-2">
                          <div className="flex justify-between items-center text-xs">
                            <span className="font-bold text-slate-800">
                              Kapasitas Cuci Harian Fasilitas Anda:
                            </span>
                            <span className="font-mono font-extrabold text-[#0F58A8] text-sm bg-blue-50 px-2.5 py-0.5 border border-blue-200">
                              {laundryKg} kg kain kering / hari
                            </span>
                          </div>
                          <input
                            type="range"
                            min="50"
                            max="2000"
                            step="50"
                            value={laundryKg}
                            onChange={(e) => setLaundryKg(Number(e.target.value))}
                            className="w-full accent-[#0F58A8] cursor-pointer h-1.5 bg-slate-200 rounded-none"
                          />
                        </div>

                        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-1">
                          <div className="border-l-2 border-[#0F58A8] pl-3 space-y-0.5">
                            <span className="text-[10px] text-slate-500 block uppercase font-bold">Kebutuhan Cairan KCA:</span>
                            <strong className="text-base font-extrabold text-[#0F58A8] block font-heading">{kcaLitersPerDay} Liter / Hari</strong>
                            <span className="text-[10px] text-slate-500">Dosis 12.5 ml / kg</span>
                          </div>

                          <div className="border-l-2 border-slate-300 pl-3 space-y-0.5">
                            <span className="text-[10px] text-slate-500 block uppercase font-bold">Deterjen Pasar Biasa:</span>
                            <strong className="text-base font-extrabold text-slate-500 block font-heading">{competitorLitersPerDay} Liter / Hari</strong>
                            <span className="text-[10px] text-slate-500">Dosis rata-rata 40 ml / kg</span>
                          </div>

                          <div className="border-l-2 border-emerald-600 pl-3 space-y-0.5">
                            <span className="text-[10px] text-emerald-700 block uppercase font-bold">Efisiensi Kimia Bersih:</span>
                            <strong className="text-base font-extrabold text-emerald-700 block font-heading">Hemat {savingsPct}% Volume</strong>
                            <span className="text-[10px] text-emerald-600 font-medium">Bebas Limbah Kerak</span>
                          </div>
                        </div>
                      </motion.div>
                    )}
                  </div>

                  {/* Action Buttons (Sharp Square Direct Styling) */}
                  <div className="pt-3 border-t border-slate-200 flex items-center gap-4 flex-wrap">
                    <button
                      onClick={() => setRfqOpen(true)}
                      className="btn-fluid-primary"
                    >
                      <span>Minta Sampel Gratis &amp; Penawaran</span>
                      <ArrowRight className="w-4 h-4" />
                    </button>
                    <a
                      href="/contact"
                      className="btn-fluid-secondary"
                    >
                      <span>Konsultasi Formulasi</span>
                    </a>
                  </div>

                </div>

              </div>
            </div>
          )}

          {/* ========================================================================= */}
          {/* 2. SATELLITE PRODUCTS: FLUID CARDS & CLEAN WATER THEME                   */}
          {/* ========================================================================= */}
          <div>
            <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8 pb-3 border-b border-sky-100">
              <div className="space-y-1">
                <h3 className="text-xl sm:text-2xl font-extrabold font-heading text-slate-900 tracking-tight">
                  Formulasi Kimia Khusus Berdasarkan Sektor Industri
                </h3>
              </div>
              <a
                href="/products"
                className="text-xs font-bold text-[#0F58A8] uppercase tracking-wider hover:underline flex items-center gap-1.5 shrink-0"
              >
                <span>Lihat Seluruh Katalog Sektoral</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </a>
            </div>

            {/* Satellite Catalog Cards (Rounded-2xl, Fluid Water Accent) */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {satelliteProducts.slice(0, 4).map((p, idx) => {
                const LogoComp = CATEGORY_LOGOS[p.category] || CorporateLogos.Reactor
                const theme = SATELLITE_THEMES[p.category] || SATELLITE_THEMES['laundry']

                return (
                  <motion.div
                    key={p.id || idx}
                    initial={{ opacity: 0, y: 15 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.35, delay: idx * 0.05 }}
                    className={`bg-white border rounded-3xl transition-all duration-300 flex flex-col justify-between group relative overflow-hidden ${theme.border} shadow-lg shadow-blue-900/5 hover:shadow-xl hover:-translate-y-1`}
                  >
                    {/* Top Color Accent Bar */}
                    <div className={`h-1.5 w-full ${theme.topBar}`} />

                    <div className="p-5 space-y-4 bg-gradient-to-b from-sky-50/40 via-white to-white">
                      
                      {/* Logo Icon Mark & SKU Tag */}
                      <div className="flex items-center justify-between">
                        <div className="w-8 h-8 rounded-full bg-white border border-sky-100 flex items-center justify-center shadow-2xs">
                          <LogoComp />
                        </div>
                        <span className={`text-[10px] font-mono font-bold px-2 py-0.5 rounded-full border ${theme.skuBadge}`}>
                          {p.sku || 'SKU'}
                        </span>
                      </div>

                      {/* Photo Thumbnail Stage */}
                      <div className="w-full h-36 bg-white/80 border border-sky-100 rounded-2xl p-2.5 flex items-center justify-center overflow-hidden shadow-2xs group-hover:scale-102 transition-transform duration-500">
                        <img
                          src={p.image || '/images/product_jerigen5l.jpg'}
                          alt={p.title || p.name}
                          className="w-full h-full object-contain filter drop-shadow-sm select-none"
                          loading="lazy"
                        />
                      </div>

                      {/* Product Name & Description */}
                      <div className="space-y-1">
                        <h4 className="text-sm sm:text-base font-extrabold font-heading text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug">
                          {p.title || p.name}
                        </h4>
                        <p className="text-xs text-slate-600 leading-relaxed line-clamp-2 font-normal">
                          {p.description}
                        </p>
                      </div>

                      {/* Spec Matrix */}
                      <div className="grid grid-cols-2 gap-2 p-2.5 rounded-xl bg-sky-50/50 border border-sky-100 text-[11px]">
                        <div>
                          <span className="text-[9px] text-slate-500 block uppercase font-bold">Dosis:</span>
                          <span className="font-bold text-slate-900 truncate block font-heading">{p.dosage || '10 ml/kg'}</span>
                        </div>
                        <div>
                          <span className="text-[9px] text-slate-500 block uppercase font-bold">pH Range:</span>
                          <span className="font-bold text-slate-900 truncate block font-heading">{p.phRange || 'Netral'}</span>
                        </div>
                      </div>
                    </div>

                    {/* Bottom Action (Fluid Pill Button) */}
                    <div className="p-3.5 bg-white border-t border-sky-100 flex items-center justify-between text-xs">
                      <span className="text-slate-500 text-[11px] font-medium truncate max-w-[110px]">
                        {p.packaging || 'Jerigen 5L - 200L'}
                      </span>
                      <button
                        onClick={() => setRfqOpen(true)}
                        className={`px-4 py-1.5 rounded-full text-xs font-bold font-heading uppercase tracking-wider transition-all flex items-center gap-1 cursor-pointer shadow-xs ${theme.btnBg}`}
                      >
                        <FileText className="w-3 h-3" />
                        <span>Minta RFQ</span>
                      </button>
                    </div>
                  </motion.div>
                )
              })}
            </div>
          </div>

        </div>
      </section>

      <RFQModal isOpen={rfqOpen} onClose={() => setRfqOpen(false)} />
    </>
  )
}



