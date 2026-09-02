import { useState } from 'react'
import { Link } from 'react-router-dom'
import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { 
  FileCheck2, 
  FileSignature,
  FlaskConical, 
  ShieldCheck, 
  Factory, 
  Truck, 
  CheckCircle2, 
  ArrowRight, 
  HelpCircle, 
  Award,
  Clock,
  Layers,
  FileText,
  Package,
  Handshake
} from 'lucide-react'
import CTASection from '@/components/sections/CTASection'
import RFQModal from '@/components/ui/RFQModal'

const WORKFLOW_STEPS = [
  {
    step: '01',
    phase: 'LEGALITAS & HKI',
    title: 'Penandatanganan NDA',
    icon: FileSignature,
    color: '#0F58A8',
    borderColor: 'border-b-[#0F58A8]',
    badgeBg: 'bg-[#0F58A8]',
    textColor: 'text-[#0F58A8]',
    checkColor: 'text-[#0F58A8]',
    desc: 'Perlindungan hukum untuk formula, merek, dan kekayaan intelektual sebelum memulai proses kerja sama.',
    points: [
      'Perjanjian kerahasiaan (NDA)',
      'Perlindungan formula & resep',
      'Klausul anti-replikasi',
      'Kerahasiaan target pasar & volume bisnis'
    ],
    deliverable: 'Dokumen NDA Sah Bertandatangan',
    deliverableIcon: FileSignature
  },
  {
    step: '02',
    phase: 'R&D & SAMPLE LAB',
    title: 'Riset & Formulasi Lab',
    icon: FlaskConical,
    color: '#D97706',
    borderColor: 'border-b-[#D97706]',
    badgeBg: 'bg-[#D97706]',
    textColor: 'text-[#D97706]',
    checkColor: 'text-[#D97706]',
    desc: 'Pengembangan dan uji coba formula sesuai target performa, stabilitas, aroma, viskositas, dan efektivitas.',
    points: [
      'Penyesuaian kadar surfaktan aktif & pH',
      'Uji stabilitas suhu & kesadahan air',
      'Pengiriman sampel uji 500ml ke mitra'
    ],
    deliverable: 'Sampel Formula Teruji & Lolos QC',
    deliverableIcon: FlaskConical
  },
  {
    step: '03',
    phase: 'REGULASI & STANDAR',
    title: 'Standarisasi & Izin Edar',
    icon: ShieldCheck,
    color: '#059669',
    borderColor: 'border-b-[#059669]',
    badgeBg: 'bg-[#059669]',
    textColor: 'text-[#059669]',
    checkColor: 'text-[#059669]',
    desc: 'Penyusunan dokumen teknis & legalitas sesuai regulasi Kemenkes untuk keamanan dan peredaran produk.',
    points: [
      'Penerbitan dokumen TDS & MSDS',
      'Pendampingan izin edar PKRT Kemenkes RI',
      'Standarisasi label & kemasan regulasi'
    ],
    deliverable: 'Berkas TDS, MSDS & Legalitas PKRT',
    deliverableIcon: FileCheck2
  },
  {
    step: '04',
    phase: 'MANUFAKTUR REAKTOR',
    title: 'Produksi Reaktor 316L',
    icon: Factory,
    color: '#7C3AED',
    borderColor: 'border-b-[#7C3AED]',
    badgeBg: 'bg-[#7C3AED]',
    textColor: 'text-[#7C3AED]',
    checkColor: 'text-[#7C3AED]',
    desc: 'Proses pencampuran & produksi di tangki reaktor Stainless Steel 316L dengan kontrol mutu ketat.',
    points: [
      'Reaktor Stainless Steel 316L anti-korosi',
      'Kapasitas batch hingga 500+ ton/bulan',
      'Pengemasan otomatis Jerigen 5L - IBC Tank'
    ],
    deliverable: 'Produk Massal Terkemas Sempurna',
    deliverableIcon: Package
  },
  {
    step: '05',
    phase: 'QC & LOGISTIK',
    title: 'QC, COA & Pengiriman',
    icon: Truck,
    color: '#0F172A',
    borderColor: 'border-b-[#0F172A]',
    badgeBg: 'bg-[#0F172A]',
    textColor: 'text-[#0F172A]',
    checkColor: 'text-[#0F172A]',
    desc: 'Uji laboratorium akhir, penerbitan COA, dan pengiriman via armada terintegrasi ke gudang mitra.',
    points: [
      'Uji titrasi akhir pH & berat jenis',
      'Penerbitan Certificate of Analysis (COA)',
      'Pengiriman armada logistik tepat waktu'
    ],
    deliverable: 'COA Resmi & Serah Terima Barang',
    deliverableIcon: FileCheck2
  },
]

const PRINCIPLES = [
  {
    icon: ShieldCheck,
    title: 'KEAMANAN & KERAHASIAAN',
    desc: 'Perlindungan data, formula, dan mitra secara mutlak.',
    iconColor: 'text-[#0F58A8]'
  },
  {
    icon: Award,
    title: 'KUALITAS TERJAMIN',
    desc: 'Standar mutu tinggi di setiap proses & pengujian.',
    iconColor: 'text-[#D97706]'
  },
  {
    icon: FileCheck2,
    title: 'KEPATUHAN REGULASI',
    desc: 'Sesuai regulasi Kemenkes RI dan standar industri.',
    iconColor: 'text-[#059669]'
  },
  {
    icon: Factory,
    title: 'EFISIENSI & KONSISTENSI',
    desc: 'Proses terintegrasi untuk hasil stabil dan berkelanjutan.',
    iconColor: 'text-[#7C3AED]'
  },
  {
    icon: Handshake,
    title: 'KEMITRAAN BERKELANJUTAN',
    desc: 'Fokus pada pertumbuhan mitra dan nilai jangka panjang.',
    iconColor: 'text-[#0F172A]'
  },
]

const FAQS = [
  { 
    q: 'Apakah formula khusus mitra dijamin kerahasiaannya?', 
    a: 'Ya, seluruh kerjasama dilindungi klausul Non-Disclosure Agreement (NDA) yang mengikat secara hukum. Resep formula mitra tidak akan direplikasi atau dijual kepada pihak ketiga.' 
  },
  { 
    q: 'Bagaimana mekanisme potongan invoice pada Skema Dedicated Line?', 
    a: 'Mitra mendanai pengadaan unit mesin/reaktor khusus. Nilai investasi tersebut akan dikembalikan secara bertahap dalam bentuk diskon khusus pada setiap faktur pesanan hingga seluruh modal mitra impas (BEP).' 
  },
  { 
    q: 'Berapa Minimum Order Quantity (MOQ) untuk maklon reguler?', 
    a: 'MOQ sangat fleksibel, disesuaikan dengan kapasitas batch minimal reaktor pencampur pabrik kami (mulai dari 1.000 Liter / 1 Ton).' 
  },
  { 
    q: 'Berapa lama estimasi waktu dari riset sampel hingga produksi massal?', 
    a: 'Proses formulasi dan sampel uji lab memakan waktu sekitar 3–7 hari kerja. Setelah sampel disetujui, jadwal produksi massal di reaktor dapat diselesaikan dalam 5–10 hari kerja.' 
  },
]

export default function ServicesPage() {
  const [rfqOpen, setRfqOpen] = useState(false)

  return (
    <main className="bg-white text-slate-900 pt-20">
      <Helmet>
        <title>Layanan Maklon & Dedicated Production Line — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Jasa maklon toll compounding formula kimia pembersih private label dan skema kemitraan Dedicated Production Line VIP mesin khusus di Kediri."
        />
        <link rel="canonical" href="https://kedirichemical.id/services" />
        <meta property="og:title" content="Layanan Maklon & Dedicated Production Line — PT Kediri Chemical Abadi" />
        <meta property="og:description" content="Jasa maklon toll compounding formula kimia pembersih private label dan skema kemitraan Dedicated Production Line VIP di Kediri." />
        <meta property="og:url" content="https://kedirichemical.id/services" />
      </Helmet>

      {/* Header Banner (Direct Title & Subline) */}
      <section className="py-16 sm:py-20 bg-slate-50/70 border-b border-slate-200 text-center">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          <div className="max-w-3xl mx-auto space-y-3">
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight">
              Kemitraan Manufaktur Kimia Private Label
            </h1>

            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl mx-auto font-normal">
              Solusi terpadu memproduksi formula kimia merek Anda sendiri tanpa beban biaya pembangunan pabrik dan pengelolaan IPAL mandiri dengan kapasitas 500+ Ton/bulan di Mojoroto, Kediri.
            </p>
          </div>
        </div>
      </section>

      {/* Makloon Information & Direct Consultation Callout */}
      <section className="py-14 bg-slate-50/70 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 text-center space-y-4">
          <h2 className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 tracking-tight">
            Konsultasikan Kebutuhan Maklon &amp; Dapatkan Informasi Lengkap
          </h2>
          <p className="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto leading-relaxed">
            Untuk menjaga kerahasiaan formula dan skema kemitraan bisnis (NDA), detail spesifikasi kapasitas reaktor dan proposal penawaran maklon diberikan langsung melalui sesi konsultasi bersama tim kami.
          </p>
          <div className="pt-2">
            <Link
              to="/contact"
              className="h-10 px-6 bg-[#0F58A8] hover:bg-blue-700 text-white rounded-md text-xs font-heading font-extrabold uppercase tracking-wider inline-flex items-center gap-2 shadow-2xs transition-all"
            >
              <span>Hubungi Tim Riset &amp; Dapatkan Informasi Maklon</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* ALUR KERJA PRODUKSI KIMIA KCA (DIAGRAM INFOGRAFIS PERSIS GAMBAR)          */}
      {/* ========================================================================= */}
      <section className="py-20 sm:py-28 bg-slate-50/50 text-slate-900 border-b border-slate-200 relative overflow-hidden">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Header Diagram */}
          <div className="text-center max-w-3xl mx-auto space-y-2">
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-black font-heading text-slate-900 tracking-tight">
              ALUR KERJA PRODUKSI KIMIA KCA
            </h2>
            <p className="text-sm sm:text-base text-slate-600 font-medium">
              Dari Riset &amp; Legalitas hingga Produk Dikirim ke Mitra
            </p>
          </div>

          {/* Diagram Container */}
          <div className="space-y-6">

            {/* ------------------------------------------------------------- */}
            {/* 1. TOP ROW: 5 CONNECTED STAGE CARDS (FLUID WATER THEME)       */}
            {/* ------------------------------------------------------------- */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 lg:gap-4 relative items-stretch">
              {WORKFLOW_STEPS.map((step, idx) => {
                const IconComp = step.icon
                const isNotLast = idx < WORKFLOW_STEPS.length - 1

                return (
                  <motion.div
                    key={idx}
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, margin: "-40px" }}
                    whileHover={{ y: -4, transition: { type: 'spring', stiffness: 350, damping: 22 } }}
                    transition={{ duration: 0.6, delay: idx * 0.08, ease: [0.16, 1, 0.3, 1] }}
                    className="bg-white p-6 rounded-3xl border border-sky-100 shadow-lg shadow-blue-900/5 hover:shadow-xl transition-all flex flex-col justify-between space-y-5 relative group"
                  >
                    {/* Rounded Number Badge */}
                    <div className="flex items-center justify-between">
                      <div className={`w-8 h-8 rounded-full ${step.badgeBg} text-white flex items-center justify-center font-heading font-extrabold text-xs shadow-xs`}>
                        {step.step}
                      </div>
                    </div>

                    {/* Centered Large Icon */}
                    <div className="flex flex-col items-center text-center space-y-3 pt-1">
                      <div className="p-3.5 rounded-2xl bg-sky-50/70 border border-sky-100 flex items-center justify-center group-hover:scale-105 transition-transform">
                        <IconComp className={`w-10 h-10 ${step.textColor} stroke-[1.5]`} />
                      </div>

                      {/* Phase Tag */}
                      <span className={`text-[10px] font-extrabold uppercase tracking-wider ${step.textColor} block font-mono bg-sky-50 px-2.5 py-0.5 rounded-full`}>
                        {step.phase}
                      </span>

                      {/* Step Title */}
                      <h3 className="text-sm sm:text-base font-extrabold font-heading text-slate-900 leading-tight">
                        {step.title}
                      </h3>

                      {/* Step Description */}
                      <p className="text-xs text-slate-600 leading-relaxed font-normal">
                        {step.desc}
                      </p>
                    </div>

                    {/* Checklist Activities */}
                    <div className="space-y-2 pt-3 border-t border-sky-100 text-left">
                      {step.points.map((pt, pIdx) => (
                        <div key={pIdx} className="flex items-start gap-2 text-xs text-slate-700">
                          <div className="w-4 h-4 rounded-full bg-blue-50 text-[#0F58A8] flex items-center justify-center shrink-0 mt-0.5">
                            <CheckCircle2 className="w-3.5 h-3.5" />
                          </div>
                          <span className="leading-snug font-medium">{pt}</span>
                        </div>
                      ))}
                    </div>

                    {/* Directional Connector Arrow Node (Desktop Only) */}
                    {isNotLast && (
                      <div className="hidden lg:flex absolute -right-3.5 top-1/2 -translate-y-1/2 z-20 w-7 h-7 rounded-full bg-white border border-sky-200 shadow-md items-center justify-center pointer-events-none">
                        <div className={`w-5 h-5 rounded-full ${step.badgeBg} text-white flex items-center justify-center`}>
                          <ArrowRight className="w-3 h-3 stroke-[2.5]" />
                        </div>
                      </div>
                    )}
                  </motion.div>
                )
              })}
            </div>

            {/* ------------------------------------------------------------- */}
            {/* 2. MIDDLE ROW: HASIL TAHAPAN (CONNECTED DELIVERABLES)         */}
            {/* ------------------------------------------------------------- */}
            <div className="bg-white rounded-3xl border border-sky-100 p-4 sm:p-5 shadow-lg shadow-blue-900/5 flex flex-col lg:flex-row items-stretch lg:items-center gap-4">
              
              {/* Left Badge Ribbon */}
              <div className="bg-gradient-to-r from-[#0F58A8] to-[#0284C7] text-white px-5 py-3 rounded-2xl flex items-center justify-center shrink-0 lg:w-36 text-center shadow-xs">
                <span className="font-heading font-black text-xs uppercase tracking-wider block">
                  HASIL<br className="hidden lg:block" /> TAHAPAN
                </span>
              </div>

              {/* 5 Connected Deliverable Output Cards */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 flex-1 items-center">
                {WORKFLOW_STEPS.map((step, idx) => {
                  const DelivIcon = step.deliverableIcon
                  const isNotLast = idx < WORKFLOW_STEPS.length - 1

                  return (
                    <div key={idx} className="flex items-center gap-2">
                      <div className="p-3 rounded-2xl bg-sky-50/50 border border-sky-100 flex items-center gap-2.5 flex-1 min-h-[58px] shadow-2xs">
                        <div className={`w-8 h-8 rounded-xl bg-white border border-sky-100 flex items-center justify-center shrink-0 ${step.textColor}`}>
                          <DelivIcon className="w-4 h-4" />
                        </div>
                        <span className="text-xs font-bold text-slate-800 leading-tight font-heading">
                          {step.deliverable}
                        </span>
                      </div>

                      {/* Dashed Arrow Connector */}
                      {isNotLast && (
                        <div className="hidden lg:flex items-center justify-center text-slate-400 shrink-0 px-0.5">
                          <ArrowRight className="w-3.5 h-3.5 text-slate-400" />
                        </div>
                      )}
                    </div>
                  )
                })}
              </div>
            </div>

            {/* ------------------------------------------------------------- */}
            {/* 3. BOTTOM ROW: PRINSIP PENDUKUNG (CORE PILLARS)              */}
            {/* ------------------------------------------------------------- */}
            <div className="bg-white rounded-3xl border border-sky-100 p-4 sm:p-5 shadow-lg shadow-blue-900/5 flex flex-col lg:flex-row items-stretch lg:items-center gap-4">
              
              {/* Left Badge Ribbon */}
              <div className="bg-slate-900 text-white px-5 py-3 rounded-2xl flex items-center justify-center shrink-0 lg:w-36 text-center shadow-xs">
                <span className="font-heading font-black text-xs uppercase tracking-wider block">
                  PRINSIP<br className="hidden lg:block" /> PENDUKUNG
                </span>
              </div>

              {/* 5 Principles Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 flex-1">
                {PRINCIPLES.map((pr, idx) => {
                  const Icon = pr.icon
                  return (
                    <div key={idx} className="flex items-start gap-3 p-2.5">
                      <div className={`p-2 rounded-xl bg-sky-50 border border-sky-100 shrink-0 ${pr.iconColor}`}>
                        <Icon className="w-4 h-4" />
                      </div>
                      <div className="space-y-0.5 min-w-0">
                        <strong className="text-xs font-extrabold font-heading text-slate-900 block truncate">
                          {pr.title}
                        </strong>
                        <p className="text-[11px] text-slate-600 leading-relaxed font-normal">
                          {pr.desc}
                        </p>
                      </div>
                    </div>
                  )
                })}
              </div>
            </div>

          </div>

          {/* Action Consultation Banner (Fluid Water Pill) */}
          <div className="pt-4 flex flex-col sm:flex-row items-center justify-between gap-4 p-8 sm:p-10 rounded-3xl bg-gradient-to-r from-slate-900 to-[#0A192F] text-white shadow-xl shadow-slate-900/10">
            <div className="space-y-1 text-center sm:text-left">
              <h4 className="text-base sm:text-lg font-extrabold font-heading text-white">
                Tertarik Mengembangkan Produk Kimia dengan Merek Sendiri?
              </h4>
              <p className="text-xs sm:text-sm text-slate-300">
                Konsultasikan kebutuhan formula dan perkiraan biaya produksi bersama tim ahli pabrik KCA.
              </p>
            </div>

            <button
              onClick={() => setRfqOpen(true)}
              className="btn-fluid-primary px-8 py-3 shrink-0"
            >
              <FileText className="w-4 h-4" />
              <span>Mulai Konsultasi Maklon</span>
            </button>
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* FAQ SECTION (NO EYEBROW TAG - DIRECT TITLE)                               */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-white text-slate-900 border-b border-sky-100">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-12 w-full space-y-10">
          
          <div className="text-center space-y-2 pb-6 border-b border-sky-100">
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight">
              Pertanyaan Umum Seputar Maklon (FAQ)
            </h2>
            <p className="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto font-normal">
              Informasi lengkap seputar kerahasiaan formula (NDA), legalitas izin edar, dan kapasitas batch produksi.
            </p>
          </div>

          <div className="divide-y divide-sky-100 border-y border-sky-100">
            {FAQS.map((faq, idx) => (
              <div key={idx} className="py-5 sm:py-6 space-y-2">
                <div className="flex items-center gap-3 text-sm sm:text-base font-bold font-heading text-slate-900">
                  <HelpCircle className="w-4 h-4 text-[#0F58A8] shrink-0" />
                  <span>{faq.q}</span>
                </div>
                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed pl-7 font-normal">
                  {faq.a}
                </p>
              </div>
            ))}
          </div>

        </div>
      </section>

      {/* Full Width CTA Section */}
      <CTASection />

      {/* RFQ Modal */}
      <RFQModal isOpen={rfqOpen} onClose={() => setRfqOpen(false)} />
    </main>
  )
}
