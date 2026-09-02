import { motion } from 'framer-motion'
import { 
  FlaskConical, 
  Leaf, 
  Factory, 
  Droplets 
} from 'lucide-react'

export default function WhyChooseUsSection() {
  const FEATURES = [
    {
      icon: FlaskConical,
      tag: 'QC LAB PRESISI',
      title: 'Standar Mutu ISO 9001:2015',
      desc: 'Pengujian titrasi pH digital, viskositas, dan berat jenis terkalibrasi per batch sebelum rilis COA resmi.'
    },
    {
      icon: Leaf,
      tag: 'ESG SAFE',
      title: '100% Bebas Fosfat / STPP',
      desc: 'Formulasi ramah lingkungan, tidak merusak biofilter IPAL rumah sakit dan mencegah eutrofikasi.'
    },
    {
      icon: Factory,
      tag: 'KAPASITAS MASSAL',
      title: 'Reaktor Stainless Steel 316L',
      desc: 'Lini pencampuran anti-korosi berkapasitas 500+ Ton/bulan untuk kepastian pasokan industri berkelanjutan.'
    },
    {
      icon: Droplets,
      tag: 'DOSIS EFISIEN',
      title: 'Konsentrat Hemat Dosis',
      desc: 'Konsentrat aktif murni hemat dosis 10–15 ml/kg cucian, memangkas biaya chemical operasional hingga 30%.'
    }
  ]

  return (
    <section className="py-20 sm:py-28 bg-white text-slate-900 relative overflow-hidden">
      
      {/* Subtle Soap Lather / Foam Bubble Ambient Background Accent (Top-Right & Edges) */}
      <div className="absolute top-0 right-0 w-[500px] h-[500px] pointer-events-none opacity-40 select-none overflow-hidden">
        <svg viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-full text-sky-100">
          <circle cx="340" cy="80" r="90" fill="currentColor" fillOpacity="0.35" />
          <circle cx="260" cy="160" r="60" fill="currentColor" fillOpacity="0.25" />
          <circle cx="370" cy="220" r="45" fill="currentColor" fillOpacity="0.3" />
          <circle cx="190" cy="90" r="35" fill="currentColor" fillOpacity="0.2" />
          <circle cx="280" cy="50" r="25" fill="currentColor" fillOpacity="0.4" />
          <circle cx="220" cy="210" r="20" fill="currentColor" fillOpacity="0.15" />
          <circle cx="320" cy="280" r="30" fill="currentColor" fillOpacity="0.2" />
        </svg>
      </div>

      <div className="absolute bottom-0 left-0 w-80 h-80 pointer-events-none opacity-30 select-none overflow-hidden">
        <svg viewBox="0 0 300 300" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-full text-sky-100">
          <circle cx="60" cy="240" r="80" fill="currentColor" fillOpacity="0.3" />
          <circle cx="140" cy="180" r="50" fill="currentColor" fillOpacity="0.2" />
          <circle cx="80" cy="130" r="30" fill="currentColor" fillOpacity="0.25" />
        </svg>
      </div>

      <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
          
          {/* ========================================================================= */}
          {/* SISI KIRI: CLEAN IMAGE GALLERY (STAINLESS REAKTOR & KEMASAN BERSIH)       */}
          {/* Tanpa floating sticker badges / sticker cards - 100% foto bersih          */}
          {/* ========================================================================= */}
          <motion.div
            className="lg:col-span-5"
            initial={{ opacity: 0, x: -25 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="grid grid-cols-12 gap-3 sm:gap-4">
              
              {/* Foto Utama: Lini Reaktor Stainless Steel 316L */}
              <div className="col-span-12 rounded-2xl overflow-hidden bg-slate-100 border border-slate-200/80 shadow-sm aspect-[16/10] group">
                <img
                  src="/images/kca_factory_reactors.jpg"
                  alt="Fasilitas Reaktor Pencampur Stainless Steel 316L PT Kediri Chemical Abadi"
                  className="w-full h-full object-cover group-hover:scale-103 transition-transform duration-700 ease-out select-none"
                />
              </div>

              {/* Foto Pendukung 1: Lantai Pabrik & Produksi Bersih */}
              <div className="col-span-6 rounded-2xl overflow-hidden bg-slate-100 border border-slate-200/80 shadow-sm aspect-[4/3] group">
                <img
                  src="/images/kca_factory_floor.jpg"
                  alt="Lantai Fasilitas Produksi Manufaktur PT Kediri Chemical Abadi"
                  className="w-full h-full object-cover group-hover:scale-103 transition-transform duration-700 ease-out select-none"
                />
              </div>

              {/* Foto Pendukung 2: Lini Kemasan Sabun & Deterjen Standar PKRT */}
              <div className="col-span-6 rounded-2xl overflow-hidden bg-slate-50 border border-slate-200/80 shadow-sm aspect-[4/3] p-2 flex items-center justify-center group">
                <img
                  src="/images/kca_packaging_lineup.png"
                  alt="Lini Kemasan Sabun dan Kimia Pembersih PT Kediri Chemical Abadi"
                  className="w-full h-full object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-700 ease-out select-none"
                />
              </div>

            </div>
          </motion.div>

          {/* ========================================================================= */}
          {/* SISI KANAN: OPEN EDITORIAL CONTENT & BORDERLESS 2x2 FEATURE GRID          */}
          {/* ========================================================================= */}
          <motion.div
            className="lg:col-span-7 space-y-8"
            initial={{ opacity: 0, x: 25 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.7, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Main Headline & Supporting Paragraph */}
            <div className="space-y-3">
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                SOLUSI SABUN &amp; KEBERSIHAN PROFESIONAL
              </h2>

              <p className="text-slate-600 text-xs sm:text-sm lg:text-[15px] leading-relaxed font-normal max-w-2xl">
                Didirikan sejak 2004, PT Kediri Chemical Abadi memproduksi formula sabun dan kimia pembersih industri terpadu untuk rumah sakit, perhotelan nasional, sentra laundry komersial, dan sektor manufaktur. Kami mengoperasikan reaktor Stainless Steel 316L dengan air murni demineralisasi dan sistem kendali mutu ISO 9001:2015.
              </p>
            </div>

            {/* Borderless 2x2 Feature Grid (No heavy cards, no heavy borders, airy editorial) */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-7 pt-2">
              {FEATURES.map((feat, idx) => {
                const Icon = feat.icon
                return (
                  <div key={idx} className="space-y-1.5 group">
                    
                    {/* Micro-tag with subtle dot */}
                    <div className="flex items-center gap-1.5 text-[#0F58A8]">
                      <span className="w-1.5 h-1.5 rounded-full bg-[#0F58A8]" />
                      <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-[#0F58A8]">
                        {feat.tag}
                      </span>
                    </div>

                    {/* Fine Outline Icon & Bold Title */}
                    <div className="flex items-center gap-2.5 pt-0.5">
                      <div className="w-7 h-7 rounded-lg bg-sky-50 text-[#0F58A8] flex items-center justify-center shrink-0">
                        <Icon className="w-4 h-4 stroke-[1.75]" />
                      </div>
                      <h3 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                        {feat.title}
                      </h3>
                    </div>

                    {/* Concise Body Text */}
                    <p className="text-xs sm:text-[13px] text-slate-600 leading-relaxed font-normal pl-9.5">
                      {feat.desc}
                    </p>

                  </div>
                )
              })}
            </div>

          </motion.div>

        </div>
      </div>
    </section>
  )
}


