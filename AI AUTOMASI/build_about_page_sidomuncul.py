# -*- coding: utf-8 -*-
"""
PT Kediri Chemical Abadi
Generator Halaman Sejarah (AboutPage.jsx)
Fitur: 1 Layar 1 Slide Tahun Utuh dengan Animasi Scroll & Anchor Down Navigation
Author: Yerikho Arfensias Effendi
Company: PT Kediri Chemical Abadi
"""

CODE = """import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { 
  Building2, 
  Award, 
  ShieldCheck, 
  CheckCircle2, 
  Factory, 
  FlaskConical, 
  Droplets, 
  Leaf, 
  ChevronDown
} from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import CTASection from '@/components/sections/CTASection'

const TIMELINE_SLIDES = [
  {
    id: 'slide-2004',
    nextId: 'slide-2008',
    year: '2004',
    badge: 'Fase 01 • Pendirian & Riset Air Sadah',
    title: 'Titik Mula di Mojoroto: Menaklukkan Kesadahan Air Jawa Timur',
    desc: 'Didirikan oleh Yan Effendi di Mojoroto, Kota Kediri dengan modal 1 unit reaktor manual 500 Liter. Pada masa awal ini, industri laundry dan tekstil lokal menghadapi kendala busa mati dan serat kain menguning akibat tingginya kesadahan air tanah Jawa Timur (>350 ppm CaCO₃).',
    details: 'Yan Effendi berhasil merekayasa formula agen pengkhelat murni (sequestering agent) pertama di Kediri yang mengikat ion kalsium & magnesium secara stabil tanpa merusak serat kain.',
    highlights: [
      'Operasional reaktor perdana 500L dengan kontrol pemanasan terukur',
      'Riset adaptasi formula terhadap kesadahan air lokal 300–450 ppm',
      'Penyaluran perdana ke puluhan sentra laundry komersial se-Karesidenan Kediri'
    ],
    breakthrough: 'Formulasi surfaktan stabil air sadah pertama yang menekan pemborosan dosis hingga 40%.',
    image: '/images/kca_factory_reactors.jpg',
    imageCaption: 'Reaktor Pencampur Perdana KCA di Mojoroto, Kediri (Est. 2004)',
    align: 'left' // text on right, photo on left
  },
  {
    id: 'slide-2008',
    nextId: 'slide-2014',
    year: '2008',
    badge: 'Fase 02 • Inovasi Hijau & Reaktor Stainless',
    title: 'Terobosan Formula 100% Bebas Fosfat & Tangki SS 316L Pertama',
    desc: 'Di tengah maraknya deterjen industri murah berbasis STPP (senyawa fosfat yang memicu ledakan alga dan merusak ekosistem perairan), KCA mengambil komitmen tegas menghentikan total penggunaan bahan fosfat dan mengoperasikan reaktor Stainless Steel 316L pertama.',
    details: 'Sinergi surfaktan non-ionik murni dan enzim pembersih ramah lingkungan menghasilkan daya angkat noda minyak berat yang tinggi namun sepenuhnya aman terhadap saluran pembuangan air limbah.',
    highlights: [
      'Instalasi reaktor Stainless Steel 316L tahan korosi asam dan basa pekat',
      'Standarisasi formula 100% bebas STPP (mencegah pencemaran air)',
      'Konsistensi efisiensi dosis stabil pada 10–15 ml per kilogram cucian'
    ],
    breakthrough: 'Pelopor formula deterjen ramah ekosistem air di Kediri dengan efisiensi dosis tinggi.',
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Lini Manufaktur Formulasi Ramah Lingkungan Bebas Fosfat Berstandar Mutu',
    align: 'right' // text on left, photo on right
  },
  {
    id: 'slide-2014',
    nextId: 'slide-2019',
    year: '2014',
    badge: 'Fase 03 • Standarisasi Medis & Kelayakan IPAL',
    title: 'Penetrasi Rumah Sakit Rujukan & Kelayakan Biofilter IPAL KARS',
    desc: 'KCA memasuki sektor higienitas medis dengan memformulasi deterjen disinfektan dan alkali builder khusus pencucian linen ruang isolasi, bedah, dan rawat inap rumah sakit. Formula KCA lolos uji ketat IPAL karena tidak mematikan bakteri pengurai biofilter limbah cair.',
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
  {
    id: 'slide-2019',
    nextId: 'slide-2026',
    year: '2019',
    badge: 'Fase 04 • Modernisasi Demin RO & Dedicated Line VIP',
    title: 'Instalasi Demin RO 50.000 L/Hari & Skema Reaktor Dedikasi',
    desc: 'Menjawab lonjakan kebutuhan maklon private label brand nasional, KCA membangun fasilitas pengolahan air Reverse Osmosis (RO) dan demineralisasi berkapasitas 50.000 Liter/hari (<5 ppm TDS). Pada fase ini, skema reaktor khusus dedicated line resmi diluncurkan.',
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
  {
    id: 'slide-2026',
    nextId: 'dewan-direksi',
    year: '2024–2026',
    badge: 'Fase 05 • Era Manajemen Modern & ISO 9001',
    title: 'Kepemimpinan Generasi Kedua, Standar ISO 9001 & Izin Edar PKRT',
    desc: 'Estafet kepemimpinan di bawah Yerikho Arfensias Effendi mempercepat transformasi tata kelola korporat, sertifikasi Sistem Manajemen Mutu ISO 9001:2015, dan integrasi rantai pasok digital. KCA melengkapi perizinan edar PKRT Kementerian Kesehatan RI untuk seluruh varian produk.',
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
  }
]

// Smooth Scroll Helper to Next Section
function scrollToSection(id) {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' })
  }
}

export default function AboutPage() {
  return (
    <main className="min-h-screen bg-white text-slate-900 pt-20">
      <Helmet>
        <title>Sejarah & Profil Perusahaan — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Perjalanan sejarah PT Kediri Chemical Abadi sejak 2004 dari pabrik reaktor di Mojoroto, Kediri hingga menjadi pusat manufaktur kimia pembersih berkapasitas 500+ Ton/bulan berstandar ISO 9001:2015."
        />
        <meta name="author" content="Yerikho Arfensias Effendi" />
      </Helmet>

      {/* ========================================================================= */}
      {/* SLIDE 00: SEJARAH KAMI (SIDO MUNCUL HERO BANNER FULLSCREEN SLIDE)         */}
      {/* ========================================================================= */}
      <section 
        id="slide-00" 
        className="min-h-[calc(100vh-80px)] flex flex-col justify-between pt-10 pb-8 sm:pt-14 sm:pb-10 bg-white relative border-b border-slate-100"
      >
        <div className="max-w-[1300px] mx-auto px-4 sm:px-8 lg:px-12 w-full text-center space-y-6 sm:space-y-8 my-auto">
          
          {/* Header Title Flanked by Two Subtle Lines */}
          <motion.div 
            initial={{ opacity: 0, y: -15 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="flex items-center justify-center gap-4 sm:gap-8"
          >
            <div className="h-[1.5px] bg-slate-300 w-16 sm:w-32 lg:w-48" />
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold font-heading tracking-[0.18em] text-[#0F58A8] uppercase">
              SEJARAH KAMI
            </h1>
            <div className="h-[1.5px] bg-slate-300 w-16 sm:w-32 lg:w-48" />
          </motion.div>

          {/* Panoramic Factory Mosaic Visual (Sido Muncul Collage Frame) */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.98 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.7, delay: 0.15 }}
            className="max-w-5xl mx-auto"
          >
            <div className="relative overflow-hidden rounded-xl border border-slate-200/90 shadow-md bg-slate-100 aspect-[21/9]">
              <img
                src="/images/kca_factory_reactors.jpg"
                alt="Fasilitas Manufaktur Reaktor PT Kediri Chemical Abadi"
                className="w-full h-full object-cover filter brightness-[0.98] contrast-[1.03]"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-slate-900/35 via-transparent to-transparent pointer-events-none" />
              <div className="absolute bottom-3 left-4 sm:left-6 text-white text-xs sm:text-sm font-heading font-medium drop-shadow-sm">
                Fasilitas Reaktor Pencampur & Riset Formulasi • Mojoroto, Kediri
              </div>
            </div>
          </motion.div>

        </div>

        {/* Sido Muncul Anchor Down Button to Slide 01 */}
        <div className="flex justify-center pt-2">
          <button
            onClick={() => scrollToSection('slide-01')}
            className="flex flex-col items-center gap-1 text-slate-400 hover:text-[#0F58A8] transition-colors cursor-pointer group"
            aria-label="Scroll ke Narasi Pengantar"
          >
            <span className="text-[11px] font-heading font-medium tracking-wider uppercase opacity-0 group-hover:opacity-100 transition-opacity">
              Lanjut
            </span>
            <ChevronDown className="w-6 h-6 animate-bounce stroke-[2]" />
          </button>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* SLIDE 01: PROLOGUE / NARASI PENGANTAR (SIDO MUNCUL FULLSCREEN SLIDE)      */}
      {/* ========================================================================= */}
      <section 
        id="slide-01" 
        className="min-h-screen flex flex-col justify-between py-12 sm:py-16 bg-slate-50/50 border-b border-slate-200/70 relative"
      >
        <div className="max-w-4xl mx-auto px-4 sm:px-8 w-full text-center space-y-6 my-auto">
          
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: false, amount: 0.3 }}
            transition={{ duration: 0.6 }}
            className="space-y-3"
          >
            <h2 className="text-base sm:text-lg lg:text-xl font-bold font-heading uppercase tracking-wider text-[#0F58A8]">
              PERJALANAN PANJANG DARI SEBUAH REAKTOR PEMBERSIH KONSENTRAT
            </h2>

            <h3 className="text-sm sm:text-base font-bold font-heading uppercase tracking-wide text-slate-900">
              INDUSTRI KIMIA YANG BERMANFAAT BAGI MITRA BISNIS DAN LINGKUNGAN
            </h3>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 25 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: false, amount: 0.3 }}
            transition={{ duration: 0.7, delay: 0.15 }}
            className="text-sm sm:text-[15.5px] text-slate-800 leading-[1.85] font-normal text-justify sm:text-center space-y-4"
          >
            <p>
              Mengawali usaha dari sebuah unit reaktor pencampur sederhana di Mojoroto, Kota Kediri, Jawa Timur, di sinilah titik awal perjalanan usaha manufaktur kimia pembersih didirikan oleh <strong className="font-bold text-slate-900">Bapak Yan Effendi</strong> pada tahun 2004. Berangkat dari tantangan tingginya kesadahan air tanah lokal (&gt;350 ppm CaCO₃) yang kerap merusak mesin dan mematikan busa deterjen laundry lokal, beliau mendedikasikan riset formulasi konsentrat murni yang stabil dan hemat dosis.
            </p>
            <p>
              Komitmen mutu ini dilanjutkan dan diperkuat oleh <strong className="font-bold text-slate-900">Bapak Yerikho Arfensias Effendi</strong> melalui standarisasi Sistem Manajemen Mutu <strong className="font-bold text-slate-900">ISO 9001:2015</strong>, kelengkapan perizinan edar <strong className="font-bold text-slate-900">PKRT Kemenkes RI</strong>, dan kapasitas pasokan massal yang kini melampaui <strong className="font-bold text-slate-900">500+ Ton per bulan</strong>.
            </p>
          </motion.div>

        </div>

        {/* Sido Muncul Anchor Down Button to First Timeline Slide (2004) */}
        <div className="flex justify-center pt-4">
          <button
            onClick={() => scrollToSection('slide-2004')}
            className="flex flex-col items-center gap-1 text-slate-400 hover:text-[#0F58A8] transition-colors cursor-pointer group"
            aria-label="Mulai Eksplorasi Garis Waktu"
          >
            <span className="text-[11px] font-heading font-medium tracking-wider uppercase opacity-0 group-hover:opacity-100 transition-opacity">
              Mulai Garis Waktu
            </span>
            <ChevronDown className="w-6 h-6 animate-bounce stroke-[2]" />
          </button>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* SLIDES 02 - 06: 1 LAYAR 1 TAHUN DENGAN ANIMASI SCROLL & ANCHOR DOWN      */}
      {/* ========================================================================= */}
      {TIMELINE_SLIDES.map((item, idx) => {
        const isEven = item.align === 'right'

        return (
          <section
            key={item.id}
            id={item.id}
            className="min-h-screen flex flex-col justify-between py-12 sm:py-16 bg-white relative border-b border-slate-100 overflow-hidden"
          >
            {/* Center Vertical Timeline Guide Line (Desktop Only) */}
            <div className="hidden lg:block absolute left-1/2 -translate-x-1/2 top-0 bottom-0 w-[2px] bg-slate-300/80 pointer-events-none" />

            <div className="max-w-[1250px] mx-auto px-4 sm:px-8 lg:px-12 w-full my-auto relative z-10">
              
              {/* Central Node Bullet on Desktop */}
              <div className="hidden lg:flex absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 w-6 h-6 rounded-full bg-[#0F58A8] border-4 border-white shadow-sm items-center justify-center z-20" />

              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-center">
                
                {/* ───────────────────────────────────────────────────────── */}
                {/* SLIDE GANJIL (2004, 2014, 2026): FOTO KIRI, TEKS KANAN     */}
                {/* ───────────────────────────────────────────────────────── */}
                {!isEven && (
                  <>
                    {/* Sisi Kiri: Foto Polaroid/Matting Frame dengan Animasi */}
                    <motion.div 
                      initial={{ opacity: 0, x: -40, scale: 0.95 }}
                      whileInView={{ opacity: 1, x: 0, scale: 1 }}
                      viewport={{ once: false, amount: 0.3 }}
                      transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
                      className="lg:col-span-6 order-2 lg:order-1 flex justify-center lg:justify-end"
                    >
                      <div className="relative p-2.5 sm:p-3 bg-white border border-slate-200/90 shadow-md rounded-lg max-w-md w-full group">
                        <div className="overflow-hidden rounded aspect-[16/11] bg-slate-100">
                          <img
                            src={item.image}
                            alt={item.year}
                            className="w-full h-full object-cover select-none group-hover:scale-102 transition-transform duration-500"
                          />
                        </div>
                        <div className="pt-2 text-center text-xs font-heading font-medium text-slate-600">
                          {item.imageCaption}
                        </div>
                      </div>
                    </motion.div>

                    {/* Sisi Kanan: Tahun & Teks Narasi dengan Animasi */}
                    <motion.div 
                      initial={{ opacity: 0, x: 40, y: 15 }}
                      whileInView={{ opacity: 1, x: 0, y: 0 }}
                      viewport={{ once: false, amount: 0.3 }}
                      transition={{ duration: 0.7, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                      className="lg:col-span-6 order-1 lg:order-2 space-y-3.5 lg:pl-6 text-left"
                    >
                      <div className="space-y-1">
                        <span className="text-[11px] font-bold font-heading uppercase tracking-widest text-slate-500 block">
                          {item.badge}
                        </span>
                        <h3 className="text-3xl sm:text-4xl lg:text-[44px] font-bold font-heading text-[#0F58A8] tracking-tight leading-none">
                          {item.year}
                        </h3>
                      </div>

                      <h4 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                        {item.title}
                      </h4>

                      <p className="text-sm sm:text-[15px] text-slate-800 leading-[1.8] font-normal">
                        {item.desc}
                      </p>

                      <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                        {item.details}
                      </p>

                      <div className="pt-2 border-t border-slate-100 space-y-1.5">
                        {item.highlights.map((h, hIdx) => (
                          <div key={hIdx} className="flex items-start gap-2 text-xs sm:text-sm text-slate-700">
                            <CheckCircle2 className="w-4 h-4 text-[#0F58A8] shrink-0 mt-0.5" />
                            <span className="leading-snug">{h}</span>
                          </div>
                        ))}
                      </div>

                      <div className="p-3 bg-blue-50/70 border-l-2 border-[#0F58A8] rounded-r text-xs sm:text-sm text-slate-800 font-medium leading-relaxed">
                        <strong className="text-slate-900">Pencapaian:</strong> {item.breakthrough}
                      </div>
                    </motion.div>
                  </>
                )}

                {/* ───────────────────────────────────────────────────────── */}
                {/* SLIDE GENAP (2008, 2019): TEKS KIRI, FOTO KANAN            */}
                {/* ───────────────────────────────────────────────────────── */}
                {isEven && (
                  <>
                    {/* Sisi Kiri: Tahun & Teks Narasi (Rata Kanan di Desktop) */}
                    <motion.div 
                      initial={{ opacity: 0, x: -40, y: 15 }}
                      whileInView={{ opacity: 1, x: 0, y: 0 }}
                      viewport={{ once: false, amount: 0.3 }}
                      transition={{ duration: 0.7, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                      className="lg:col-span-6 order-1 lg:order-1 space-y-3.5 lg:pr-6 text-left lg:text-right flex flex-col lg:items-end"
                    >
                      <div className="space-y-1">
                        <span className="text-[11px] font-bold font-heading uppercase tracking-widest text-slate-500 block">
                          {item.badge}
                        </span>
                        <h3 className="text-3xl sm:text-4xl lg:text-[44px] font-bold font-heading text-[#0F58A8] tracking-tight leading-none">
                          {item.year}
                        </h3>
                      </div>

                      <h4 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                        {item.title}
                      </h4>

                      <p className="text-sm sm:text-[15px] text-slate-800 leading-[1.8] font-normal">
                        {item.desc}
                      </p>

                      <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                        {item.details}
                      </p>

                      <div className="pt-2 border-t border-slate-100 space-y-1.5 flex flex-col lg:items-end">
                        {item.highlights.map((h, hIdx) => (
                          <div key={hIdx} className="flex items-start gap-2 text-xs sm:text-sm text-slate-700 lg:flex-row-reverse text-left lg:text-right">
                            <CheckCircle2 className="w-4 h-4 text-[#0F58A8] shrink-0 mt-0.5" />
                            <span className="leading-snug">{h}</span>
                          </div>
                        ))}
                      </div>

                      <div className="p-3 bg-blue-50/70 border-l-2 lg:border-l-0 lg:border-r-2 border-[#0F58A8] rounded-r lg:rounded-r-none lg:rounded-l text-xs sm:text-sm text-slate-800 font-medium leading-relaxed text-left lg:text-right">
                        <strong className="text-slate-900">Pencapaian:</strong> {item.breakthrough}
                      </div>
                    </motion.div>

                    {/* Sisi Kanan: Foto Polaroid/Matting Frame */}
                    <motion.div 
                      initial={{ opacity: 0, x: 40, scale: 0.95 }}
                      whileInView={{ opacity: 1, x: 0, scale: 1 }}
                      viewport={{ once: false, amount: 0.3 }}
                      transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
                      className="lg:col-span-6 order-2 lg:order-2 flex justify-center lg:justify-start"
                    >
                      <div className="relative p-2.5 sm:p-3 bg-white border border-slate-200/90 shadow-md rounded-lg max-w-md w-full group">
                        <div className="overflow-hidden rounded aspect-[16/11] bg-slate-100">
                          <img
                            src={item.image}
                            alt={item.year}
                            className="w-full h-full object-cover select-none group-hover:scale-102 transition-transform duration-500"
                          />
                        </div>
                        <div className="pt-2 text-center text-xs font-heading font-medium text-slate-600">
                          {item.imageCaption}
                        </div>
                      </div>
                    </motion.div>
                  </>
                )}

              </div>

            </div>

            {/* Sido Muncul Anchor Down Button to Next Slide */}
            <div className="flex justify-center pt-4 relative z-20">
              <button
                onClick={() => scrollToSection(item.nextId)}
                className="flex flex-col items-center gap-1 text-slate-400 hover:text-[#0F58A8] transition-colors cursor-pointer group"
                aria-label={`Lanjut ke ${item.nextId}`}
              >
                <span className="text-[11px] font-heading font-medium tracking-wider uppercase opacity-0 group-hover:opacity-100 transition-opacity">
                  Tahun Berikutnya
                </span>
                <ChevronDown className="w-6 h-6 animate-bounce stroke-[2]" />
              </button>
            </div>

          </section>
        )
      })}

      {/* ========================================================================= */}
      {/* DEWAN DIREKSI & KEPEMIMPINAN 2 GENERASI                                    */}
      {/* ========================================================================= */}
      <section id="dewan-direksi" className="py-20 sm:py-28 bg-slate-50/70 border-t border-slate-200 relative">
        <div className="max-w-[1250px] mx-auto px-4 sm:px-8 lg:px-12 w-full space-y-12">
          
          <div className="text-center max-w-3xl mx-auto space-y-2">
            <span className="text-xs font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              TATA KELOLA PERUSAHAAN & KEPEMIMPINAN
            </span>
            <h2 className="text-xl sm:text-2xl font-bold font-heading text-slate-900 tracking-tight leading-tight uppercase">
              Dewan Direksi & Kepemimpinan 2 Generasi
            </h2>
            <p className="text-sm text-slate-600 font-normal max-w-2xl mx-auto">
              Sinergi pengalaman lebih dari 20 tahun dalam riset kimia industri dengan manajemen operasional modern berstandar ISO 9001:2015.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-14 max-w-5xl mx-auto divide-y md:divide-y-0 md:divide-x divide-slate-200 items-start">
            {COMPANY_DATA.boardOfDirectors.map((person, idx) => (
              <div
                key={idx}
                className={`space-y-4 ${idx === 1 ? 'md:pl-10 lg:pl-14 pt-8 md:pt-0' : 'md:pr-10 lg:pr-14'}`}
              >
                <div className="flex items-start gap-3.5">
                  <div className="w-12 h-12 bg-white border border-slate-300 text-[#0F58A8] flex items-center justify-center font-heading font-bold text-base shadow-2xs shrink-0 mt-0.5 rounded-md">
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

                <p className="text-sm text-slate-700 leading-relaxed font-normal">
                  {person.bio}
                </p>

                <div className="space-y-1.5 pt-2 border-t border-slate-200">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-500 block font-heading">
                    Fokus Tanggung Jawab:
                  </span>
                  <div className="space-y-1 text-xs sm:text-sm text-slate-700">
                    {(person.responsibilities || [person.focus]).map((resp, rIdx) => (
                      <div key={rIdx} className="flex items-start gap-2">
                        <CheckCircle2 className="w-4 h-4 text-[#0F58A8] shrink-0 mt-0.5" />
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
      {/* 4 KOMITMEN FUNDAMENTAL PERUSAHAAN (ESG)                                   */}
      {/* ========================================================================= */}
      <section id="komitmen-esg" className="py-16 sm:py-20 bg-white border-t border-slate-200">
        <div className="max-w-[1250px] mx-auto px-4 sm:px-8 lg:px-12 w-full space-y-8">
          
          <div className="max-w-3xl space-y-1.5">
            <span className="text-xs font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              PRINSIP INTEGRITAS & KEBERLANJUTAN
            </span>
            <h2 className="text-xl sm:text-2xl font-bold font-heading text-slate-900 tracking-tight leading-tight uppercase">
              4 Komitmen Fundamental Perusahaan
            </h2>
            <p className="text-sm text-slate-600 font-normal">
              Nilai operasional yang dipegang teguh oleh seluruh formulator lab, teknisi reaktor, dan manajemen PT Kediri Chemical Abadi.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-2 border-t border-slate-200">
            <div className="space-y-1.5 border-l-2 border-[#0F58A8] pl-3.5">
              <strong className="text-sm font-bold text-slate-900 block font-heading">
                1. Kejujuran Formulasi Murni
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Menolak penambahan filler garam murah atau pengencer air berlebih yang merusak mesin dan memboroskan biaya mitra.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-emerald-600 pl-3.5">
              <strong className="text-sm font-bold text-slate-900 block font-heading">
                2. Tanggung Jawab IPAL Lingkungan
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Komitmen 100% bebas fosfat (STPP-free) dan surfaktan biodegradasi &gt;90% menjaga kelestarian ekosistem perairan.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-amber-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                3. Akuntabilitas Legalitas & Pajak
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Beroperasi dengan perizinan OSS-RBA resmi, SPPKP dengan e-Faktur PPN 11%, dan kesiapan tender e-Katalog LKPP RI.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-indigo-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                4. Kontinuitas Pasokan Massal
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Kapasitas reaktor 500+ Ton/bulan menjamin ketersediaan pasokan kimia rutin tanpa jeda operasional.
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
"""

with open('src/pages/AboutPage.jsx', 'w', encoding='utf-8') as f:
    f.write(CODE)

print("BERHASIL: AboutPage.jsx kini berformat 1 Layar 1 Slide Tahun Utuh dengan Animasi Scroll & Anchor Down!")
