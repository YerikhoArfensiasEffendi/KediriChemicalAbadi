import { useState } from 'react'
import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { 
  ArrowRight, 
  CheckCircle2,
  FileText
} from 'lucide-react'
import { INDUSTRIES_DATA } from '@/data/industriesData'
import RFQModal from '@/components/ui/RFQModal'

// Professional Corporate Vector Logos for Industries
const SectorLogos = {
  'laundry-textile': () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z" />
      <path d="M8 14a4 4 0 0 0 8 0" strokeDasharray="2 2" />
      <circle cx="12" cy="12" r="1.5" fill="currentColor" />
    </svg>
  ),
  'hospitality': () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 9h1M14 9h1M9 13h1M14 13h1M9 17h1M14 17h1" />
      <path d="M12 3v3" strokeWidth="2" />
    </svg>
  ),
  'healthcare': () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 4v16m-8-8h16" strokeWidth="2.5" strokeLinecap="round" />
      <circle cx="12" cy="12" r="9" strokeWidth="1.5" />
    </svg>
  ),
  'manufacturing-automotive': () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M2 20h20M6 20V8l6 4V8l6 4V4l4 4v12" />
      <circle cx="6" cy="14" r="1.5" fill="currentColor" />
      <circle cx="12" cy="16" r="1.5" fill="currentColor" />
    </svg>
  ),
  'fnb-food-processing': () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M18 2v6a3 3 0 0 1-3 3 3 3 0 0 1-3-3V2M15 11v11M5 2v8a2 2 0 0 0 2 2h0a2 2 0 0 0 2-2V2M7 12v10" />
    </svg>
  ),
}

const SECTOR_DETAILS = [
  {
    id: 'laundry-textile',
    title: 'Commercial Laundry & Tekstil',
    badge: 'SENTRA LAUNDRY & INDUSTRI GARMEN',
    tagline: 'Efisiensi Dosis Tinggi & Perlindungan Serat Kain',
    image: '/images/kca_factory_floor.jpg',
    description: 'Formulasi deterjen konsentrat bebas fosfat berdaya cuci tinggi untuk industri garmen dan sentra laundry komersial. Efektif mengangkat noda berat minyak, lemak, dan keringat tanpa merapuhkan serat kain linen atau memudarkan warna pakaian.',
    features: [
      'Deterjen Non-Fosfat Konsentrat (Dosis hemat 10–15 ml/kg cucian)',
      'Alkali Booster & Emulsifier Pelarut Noda Minyak Berat',
      'Sour Neutralizer Penstabil pH Linen & Pencegah Iritasi Kulit',
      'Parfum Micro-Capsule Tahan Suhu Pengering Rotary Tinggi',
    ],
    packaging: 'Jerigen 5L, 20L, Drum 200L, IBC 1.000L',
    ctaLabel: 'Minta Penawaran Sektor Laundry',
  },
  {
    id: 'hospitality',
    title: 'Perhotelan & Hospitality Chains',
    badge: 'STANDAR RESORT & HOTEL BINTANG 4-5',
    tagline: 'Kemewahan Linen Putih & Sanitasi Ruang Tamu',
    image: '/images/kca_factory_reactors.jpg',
    description: 'Standar kebersihan premium untuk resort bintang 4-5 dan hotel chain nasional. Menjaga sprei, handuk, dan duvet cover tetap putih cemerlang tanpa klorin keras yang merapuhkan katun, dilengkapi pembersih multi-permukaan beraroma mewah aromaterapi.',
    features: [
      'Oxygen Bleach Non-Klorin Pencerah Linen Putih & Katun Berwarna',
      'Fabric Softener Ekstra Lembut Tanpa Residu Lilin (Bebas Lengket)',
      'Floor & Surface Multi-Cleaner Beraroma Segar Tahan Lama',
      'Glass Cleaner Cepat Kering Bebas Goresan (Streak-Free Shine)',
    ],
    packaging: 'Jerigen 5L, 20L, Drum 200L',
    ctaLabel: 'Minta Penawaran Sektor Hotel',
  },
  {
    id: 'healthcare',
    title: 'Rumah Sakit & Fasilitas Medis',
    badge: 'STANDAR SANITASI AKREDITASI KARS',
    tagline: 'Dekontaminasi Linen Infeksius & 100% Ramah IPAL',
    image: '/images/kca_factory_floor.jpg',
    description: 'Disinfeksi dan sanitasi linen medis sesuai standar KARS & Kemenkes RI. Menginaktivasi bakteri patogen nosokomial, virus, serta spora darah secara tuntas tanpa membunuh bakteri pengurai pada instalasi pengolahan air limbah (IPAL) rumah sakit.',
    features: [
      'Medical Disinfectant Linen Infeksius & Ruang Operasi',
      'Formula 100% Ramah Bakteri IPAL Rumah Sakit (>90% Biodegradable)',
      'Enzymatic Detergent Pengurai Noda Darah & Protein Medis',
      'Dokumentasi Lengkap TDS, MSDS, & COA Siap Audit Akreditasi RS',
    ],
    packaging: 'Jerigen 5L, 20L, Drum 200L, Kontrak Rutin LKPP',
    ctaLabel: 'Minta Penawaran Sektor Medis',
  },
  {
    id: 'manufacturing-automotive',
    title: 'Pabrik Manufaktur & Otomotif',
    badge: 'HEAVY DUTY INDUSTRIAL DEGREASING',
    tagline: 'Pelarut Kerak Oli Berat & Gemuk Permesinan',
    image: '/images/kca_factory_reactors.jpg',
    description: 'Pembersih dan pelarut kerak oli berat, gemuk industri, dan sisa coolant permesinan CNC. Sangat aman diaplikasikan pada permukaan baja, besi tempa, dan lantai workshop tanpa memicu korosi dini pada komponen mesin presisi.',
    features: [
      'Heavy Duty Water-Based Alkaline Degreaser Konsentrat',
      'Solvent Fast-Dry Penetrasi Rantai, Gearbox, & Komponen Mesin',
      'Floor Degreaser Anti-Licin Area Forklift & Jalur Produksi Pabrik',
      'Pasokan Massal Kontinu Skala Drum 200L & Tangki IBC 1.000L',
    ],
    packaging: 'Drum Besi/Plastik 200L, Tangki IBC 1.000L',
    ctaLabel: 'Minta Penawaran Sektor Manufaktur',
  },
  {
    id: 'fnb-food-processing',
    title: 'Restoran, Katering, & Food Processing',
    badge: 'FOOD GRADE & HACCP SAFE SANITATION',
    tagline: 'Sanitasi Bebas Residu Bau & Pengurai Lemak Dapur',
    image: '/images/kca_factory_floor.jpg',
    description: 'Formula sanitasi food-grade ramah lingkungan untuk dapur restoran komersial, katering skala besar, dan industri pengolahan makanan. Efektif melarutkan lemak hewani pekat pada grease trap dan peralatan masak tanpa meninggalkan residu aroma berbahaya.',
    features: [
      'Dishwashing Liquid Konsentrat Busa Cepat Bilas (Hemat Air)',
      'Grease Trap & Exhaust Hood Bio-Enzyme Degreaser Pengurai Lemak',
      'Surface Sanitizer Food Contact Safe Tanpa Perlu Dibilas',
      'Descaler Mesin Pencuci Piring Otomatis & Boiler Pemanas Air',
    ],
    packaging: 'Jerigen 5L, 20L, Drum 200L',
    ctaLabel: 'Minta Penawaran Sektor F&B',
  },
]

export default function IndustriesSection() {
  const [rfqOpen, setRfqOpen] = useState(false)
  const { customFormulation, sectionTitle, sectionSubtitle } = INDUSTRIES_DATA

  return (
    <>
      <section id="industries" className="py-16 sm:py-24 bg-white text-slate-900 relative w-full overflow-hidden">
        
        {/* Ambient 4K Liquid Water Texture Background */}
        <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden select-none opacity-25 mix-blend-multiply">
          <img
            src="/images/bg_liquid_caustics_4k.png"
            alt="Liquid Water Caustics Texture"
            className="w-full h-full object-cover object-top"
          />
        </div>

        {/* Section Header (Sido Muncul Corporate Standard) */}
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full mb-10 sm:mb-14 relative z-10">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6 border-b border-slate-200">
            <div className="space-y-2 max-w-2xl">
              <span className="text-xs font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
                PENETRASI PASAR &amp; SEKTOR BISNIS
              </span>
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-black font-heading text-slate-900 tracking-tight leading-tight uppercase">
                {sectionTitle || 'Sektor Industri yang Kami Layani'}
              </h2>
            </div>
            <p className="text-xs sm:text-sm text-slate-700 max-w-lg font-normal leading-relaxed">
              {sectionSubtitle || 'Formulasi kimia pembersih khusus yang dirancang presisi untuk spesifikasi teknis, kepatuhan IPAL, dan efisiensi operasional setiap sektor bisnis.'}
            </p>
          </div>
        </div>

        {/* Fluid Editorial Zig-Zag Layout (Smooth Rounded-3xl Curves) */}
        <div className="w-full space-y-8 sm:space-y-10 mb-14 sm:mb-20">
          {SECTOR_DETAILS.map((sec, idx) => {
            const isRightAligned = idx % 2 === 1
            const LogoComp = SectorLogos[sec.id] || SectorLogos['laundry-textile']

            return (
              <motion.div
                key={sec.id}
                initial={{ opacity: 0, y: 15 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.35, delay: idx * 0.04 }}
                className={`w-full max-w-[96%] sm:max-w-[92%] lg:max-w-[88%] xl:max-w-[84%] bg-gradient-to-r from-sky-50/40 via-white to-sky-50/20 border border-sky-100 rounded-3xl shadow-lg shadow-blue-900/5 transition-all flex flex-col lg:flex-row items-stretch overflow-hidden ${
                  isRightAligned ? 'ml-auto' : 'mr-auto'
                }`}
              >
                {/* 1. Foto Sektor Bersih */}
                <div
                  className={`w-full lg:w-80 xl:w-96 min-h-[200px] lg:min-h-full shrink-0 relative overflow-hidden bg-slate-100 ${
                    isRightAligned ? 'lg:order-2' : 'lg:order-1'
                  }`}
                >
                  <img
                    src={sec.image}
                    alt={sec.title}
                    className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700 select-none"
                  />
                </div>

                {/* 2. Informasi Konten Open Editorial */}
                <div
                  className={`flex-1 p-6 sm:p-8 flex flex-col justify-between space-y-5 ${
                    isRightAligned ? 'lg:order-1' : 'lg:order-2'
                  }`}
                >
                  {/* Header Sektor with Vector Logo */}
                  <div className="space-y-1.5">
                    <div className="flex items-center gap-2">
                      <div className="w-8 h-8 rounded-full bg-sky-50 border border-sky-100 flex items-center justify-center shrink-0 text-[#0F58A8]">
                        <LogoComp />
                      </div>
                      <span className="text-[10px] font-mono font-bold text-[#0F58A8] uppercase tracking-wider bg-blue-50 px-2.5 py-0.5 rounded-full border border-blue-100">
                        {sec.badge}
                      </span>
                    </div>

                    <h3 className="text-lg sm:text-xl lg:text-2xl font-extrabold font-heading text-slate-900 leading-snug">
                      {sec.title}
                    </h3>

                    <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal pt-1">
                      {sec.description}
                    </p>
                  </div>

                  {/* 4 Poin Keunggulan Formula */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-2 border-t border-sky-100 text-xs">
                    {sec.features.map((feat, fIdx) => (
                      <div key={fIdx} className="flex items-start gap-2 text-slate-700">
                        <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 mt-0.5">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                        </div>
                        <span className="font-medium">{feat}</span>
                      </div>
                    ))}
                  </div>

                  {/* Footer: Kemasan & Tombol Aksi (Fluid Pill) */}
                  <div className="pt-3 border-t border-sky-100 flex flex-col sm:flex-row sm:items-center justify-between gap-3 flex-wrap">
                    <div className="text-[11px] text-slate-500 font-medium">
                      <span className="text-slate-400">Kemasan Distribusi:</span>{' '}
                      <strong className="text-slate-800 font-bold">{sec.packaging}</strong>
                    </div>

                    <div className="flex items-center gap-3 shrink-0">
                      <button
                        onClick={() => setRfqOpen(true)}
                        className="btn-fluid-primary text-xs py-2 px-4"
                      >
                        <span>{sec.ctaLabel}</span>
                        <ArrowRight className="w-3.5 h-3.5" />
                      </button>

                      <Link
                        to="/industries"
                        className="text-xs font-bold text-slate-500 hover:text-[#0F58A8] transition-colors uppercase tracking-wider hidden sm:inline"
                      >
                        Detail Sektor →
                      </Link>
                    </div>
                  </div>

                </div>
              </motion.div>
            )
          })}
        </div>

        {/* Custom Formulation Banner (Fluid Styling) */}
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          <div className="bg-gradient-to-r from-sky-50 via-blue-50/60 to-white rounded-3xl border border-sky-100 p-8 sm:p-12 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center shadow-lg shadow-blue-900/5">
            
            <div className="lg:col-span-8 space-y-3">
              <h3 className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                {customFormulation?.title || 'Butuh Formula Kimia Khusus untuk Kebutuhan Spesifik Anda?'}
              </h3>

              <p className="text-slate-600 text-xs sm:text-sm leading-relaxed max-w-2xl font-normal pt-1">
                {customFormulation?.description || 'Laboratorium PT Kediri Chemical Abadi siap merekayasa formulasi pembersih khusus dengan spesifikasi viskositas, konsentrasi aktif, aroma, dan warna sesuai standar mutu industri Anda.'}
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2 text-xs text-slate-700">
                <div className="flex items-center gap-2">
                  <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                  </div>
                  <span>Uji Titrasi Lab Presisi</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                  </div>
                  <span>Penyesuaian pH &amp; Surfaktan</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                  </div>
                  <span>Dukungan Izin PKRT Kemenkes</span>
                </div>
              </div>
            </div>

            <div className="lg:col-span-4 flex flex-col sm:flex-row lg:flex-col gap-3 justify-center">
              <button
                onClick={() => setRfqOpen(true)}
                className="btn-fluid-primary w-full text-center"
              >
                <span>Minta Penawaran Resmi (RFQ)</span>
                <ArrowRight className="w-4 h-4" />
              </button>

              <Link
                to="/contact"
                className="btn-fluid-secondary w-full text-center"
              >
                <span>Konsultasi Formulator Lab</span>
              </Link>
            </div>

          </div>
        </div>

      </section>

      {/* RFQ Modal */}
      <RFQModal isOpen={rfqOpen} onClose={() => setRfqOpen(false)} />
    </>
  )
}

