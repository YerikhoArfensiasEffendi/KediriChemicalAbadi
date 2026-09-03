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
            {/* Main Headline & Supporting Paragraph (Sido Muncul Editorial Style) */}
            <div className="space-y-2.5">
              <span className="text-[10.5px] sm:text-[11px] font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
                STANDAR MANUFAKTUR &amp; KEMITRAAN B2B TERPERCAYA
              </span>

              <h2 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight leading-[1.25] uppercase">
                SOLUSI FORMULASI KIMIA &amp; KEBERSIHAN INDUSTRI
              </h2>

              <p className="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal max-w-2xl">
                Didirikan sejak 2004, PT Kediri Chemical Abadi telah menjadi mitra manufaktur kimia pembersih bagi ratusan rumah sakit rujukan, perhotelan nasional, sentra laundry komersial, dan industri manufaktur. Kami mengintegrasikan riset formulasi konsentrat murni bebas fosfat dengan lini pencampuran Stainless Steel 316L berstandar mutu ISO 9001:2015.
              </p>
            </div>

            {/* 2x2 Borderless Feature Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-5 pt-2">
              {FEATURES.map((feat, idx) => {
                const Icon = feat.icon
                return (
                  <div key={idx} className="space-y-1.5 group">
                    
                    {/* Header Row: Seamless Raw Icon + Micro-tag */}
                    <div className="flex items-center justify-between">
                      <Icon className={`w-5 h-5 sm:w-5.5 sm:h-5.5 ${feat.iconColor} stroke-[1.85] group-hover:scale-110 transition-transform duration-300`} />
                      <span className="text-[9.5px] sm:text-[10px] font-mono font-medium text-slate-400">
                        {feat.tag}
                      </span>
                    </div>

                    {/* Bold Title */}
                    <h3 className="text-xs sm:text-[13.5px] font-bold font-heading text-slate-900 leading-snug">
                      {feat.title}
                    </h3>

                    {/* Concise Body Text */}
                    <p className="text-[11px] sm:text-xs text-slate-600 leading-relaxed font-normal">
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


