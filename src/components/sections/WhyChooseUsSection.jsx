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
      tag: 'QC Lab Presisi',
      title: 'Standar Mutu ISO 9001:2015',
      desc: 'Setiap batch diuji titrasi pH digital, viskositas, dan berat jenis sebelum rilis COA resmi.',
      iconColor: 'text-[#0F58A8]',
      tagColor: 'text-slate-400'
    },
    {
      icon: Leaf,
      tag: 'ESG & KARS Safe',
      title: '100% Bebas Fosfat / STPP',
      desc: 'Formulasi ramah lingkungan, tidak merusak biofilter IPAL rumah sakit dan mencegah eutrofikasi.',
      iconColor: 'text-emerald-600',
      tagColor: 'text-slate-400'
    },
    {
      icon: Factory,
      tag: 'Skalabilitas Tinggi',
      title: 'Kapasitas Reaktor 500+ Ton',
      desc: 'Lini pencampuran Stainless Steel 316L siap melayani kontrak pasokan skala besar tanpa jeda.',
      iconColor: 'text-slate-700',
      tagColor: 'text-slate-400'
    },
    {
      icon: Droplets,
      tag: 'Efisiensi Biaya',
      title: 'Formulasi Konsentrat Hemat Dosis',
      desc: 'Efisiensi dosis 10–15 ml/kg cucian, memangkas biaya chemical operasional hingga 30%.',
      iconColor: 'text-sky-600',
      tagColor: 'text-slate-400'
    }
  ]

  return (
    <section className="py-20 sm:py-28 bg-gradient-to-b from-white via-sky-50/15 to-white text-slate-900 relative overflow-hidden">
      
      {/* ========================================================================= */}
      {/* 1. AMBIENT LIQUID WATER CAUSTICS TEXTURE (Clean Asset Texture)            */}
      {/* ========================================================================= */}
      <div className="absolute inset-0 pointer-events-none opacity-20 select-none overflow-hidden mix-blend-multiply">
        <img
          src="/images/bg_liquid_caustics_4k.png"
          alt="Clean Ambient Liquid Water Caustics Texture"
          className="w-full h-full object-cover object-center"
        />
      </div>

      <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
          
          {/* ========================================================================= */}
          {/* 2. SISI KIRI: COMPOSITE GALLERY (STAINLESS REAKTOR + SABUN & BOTOL DISPENSER)*/}
          {/* ========================================================================= */}
          <motion.div
            className="lg:col-span-5"
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="relative rounded-3xl overflow-hidden bg-white/80 backdrop-blur-sm border border-slate-200/90 shadow-2xl shadow-blue-900/10 p-2 sm:p-2.5 group hover:shadow-blue-900/15 transition-all duration-500">
              <img
                src="/images/kca_soap_gallery_composite.jpg"
                alt="Fasilitas Reaktor Pabrik Bioreactor Stainless Steel dan Formulasi Sabun PT Kediri Chemical Abadi"
                className="w-full h-auto object-cover rounded-2xl select-none group-hover:scale-[1.01] transition-transform duration-700 ease-out"
              />
            </div>
          </motion.div>

          {/* ========================================================================= */}
          {/* 3. SISI KANAN: EDITORIAL HIERARCHY & 2x2 FEATURE GRID                     */}
          {/* ========================================================================= */}
          <motion.div
            className="lg:col-span-7 space-y-7"
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.8, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Main Headline & Supporting Paragraph */}
            <div className="space-y-3.5">
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight uppercase">
                SOLUSI SABUN &amp; KEBERSIHAN PROFESIONAL
              </h2>

              <p className="text-slate-600 text-xs sm:text-sm lg:text-[14px] leading-relaxed font-normal max-w-2xl">
                Didirikan sejak 2004, PT Kediri Chemical Abadi telah menjadi mitra manufaktur kimia pembersih bagi ratusan rumah sakit, perhotelan nasional, sentra laundry komersial, dan industri manufaktur. Kami mengintegrasikan riset formulasi bebas fosfat dengan lini pencampuran presisi tinggi berstandar mutu ISO 9001:2015.
              </p>
            </div>

            {/* 2x2 Borderless Feature Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-10 gap-y-7 pt-3">
              {FEATURES.map((feat, idx) => {
                const Icon = feat.icon
                return (
                  <div key={idx} className="space-y-2 group">
                    
                    {/* Header Row: Fine Outline Icon on Left + Micro-tag on Right */}
                    <div className="flex items-center justify-between">
                      <div className="w-8 h-8 rounded-lg bg-sky-50/80 border border-sky-100 flex items-center justify-center shrink-0 shadow-2xs group-hover:bg-blue-50 transition-colors">
                        <Icon className={`w-4 h-4 ${feat.iconColor} stroke-[1.75]`} />
                      </div>
                      <span className="text-[10px] sm:text-[11px] font-mono font-medium text-slate-400">
                        {feat.tag}
                      </span>
                    </div>

                    {/* Bold Title */}
                    <h3 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                      {feat.title}
                    </h3>

                    {/* Concise Body Text */}
                    <p className="text-xs text-slate-600 leading-relaxed font-normal">
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


