import { useState } from 'react'
import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { 
  Factory, 
  CheckCircle2, 
  ArrowRight, 
  ShieldCheck, 
  Leaf, 
  Droplets, 
  FlaskConical, 
  Award,
  Sparkles,
  Activity,
  Gauge
} from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'

export default function WhyChooseUsSection() {
  const [activeHover, setActiveHover] = useState(null)

  const PILLARS = [
    {
      icon: Award,
      title: 'Standar Mutu ISO 9001:2015',
      desc: 'Setiap batch diuji titrasi pH digital, viskositas, dan berat jenis sebelum rilis COA resmi.',
      badge: 'QC Lab Presisi',
      color: 'text-[#0F58A8]',
      bgColor: 'bg-blue-50',
      borderColor: 'border-sky-100'
    },
    {
      icon: Leaf,
      title: '100% Bebas Fosfat / STPP',
      desc: 'Formula ramah lingkungan, tidak merusak biofilter IPAL rumah sakit dan mencegah eutrofikasi.',
      badge: 'ESG & KARS Safe',
      color: 'text-emerald-600',
      bgColor: 'bg-emerald-50',
      borderColor: 'border-emerald-100'
    },
    {
      icon: Factory,
      title: 'Kapasitas Reaktor 500+ Ton',
      desc: 'Lini pencampuran Stainless Steel 316L siap melayani kontrak pasokan skala besar tanpa jeda.',
      badge: 'Skalabilitas Tinggi',
      color: 'text-amber-600',
      bgColor: 'bg-amber-50',
      borderColor: 'border-amber-100'
    },
    {
      icon: Droplets,
      title: 'Formulasi Konsentrat Hemat Dosis',
      desc: 'Efisiensi dosis 10–15 ml/kg cucian, memangkas biaya chemical operasional hingga 30%.',
      badge: 'Efisiensi Biaya',
      color: 'text-sky-600',
      bgColor: 'bg-sky-50',
      borderColor: 'border-sky-100'
    }
  ]

  return (
    <section className="py-20 sm:py-28 bg-gradient-to-b from-white via-sky-50/20 to-white text-slate-900 relative overflow-hidden">
      
      {/* Ambient Fluid Water Glow Orbs */}
      <div className="absolute top-1/4 -left-40 w-96 h-96 bg-sky-200/30 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 -right-40 w-96 h-96 bg-blue-200/20 rounded-full blur-3xl pointer-events-none" />

      <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
          
          {/* ========================================================================= */}
          {/* SISI KIRI: GRAPHIC DESIGN STAGE (FOTO REAKTOR + FLOATING TELEMETRY NODES) */}
          {/* ========================================================================= */}
          <motion.div
            className="lg:col-span-6 relative"
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Visual Graphic Wrapper with Water Glow */}
            <div className="relative p-2 sm:p-4">
              
              {/* Central Reactor Photo Frame */}
              <div className="relative w-full aspect-[4/3] sm:aspect-[16/11] rounded-3xl overflow-hidden bg-slate-900 border border-sky-100 shadow-2xl shadow-blue-900/15 group">
                <img
                  src="/images/kca_factory_reactors.jpg"
                  alt="Fasilitas Reaktor Pencampur Stainless Steel 316L PT Kediri Chemical Abadi"
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out select-none"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-950/40 via-transparent to-transparent pointer-events-none" />
              </div>

              {/* Floating Graphic Node 1: Demin Water System (Top Right) */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: 0.2 }}
                whileHover={{ y: -4, scale: 1.02 }}
                className="absolute -top-3 right-4 sm:-right-2 z-20 bg-white/95 backdrop-blur-md px-4 py-3 rounded-2xl border border-sky-100 shadow-xl shadow-blue-900/10 flex items-center gap-3"
              >
                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-sky-400 text-white flex items-center justify-center shrink-0 shadow-sm">
                  <FlaskConical className="w-5 h-5" />
                </div>
                <div className="min-w-0">
                  <div className="flex items-center gap-1.5">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                    <span className="text-[10px] font-extrabold uppercase tracking-wider text-slate-400 block font-mono">
                      Air Murni Demin &amp; RO
                    </span>
                  </div>
                  <strong className="text-xs font-bold font-heading text-slate-900 block truncate">
                    TDS &lt; 0.05 μS/cm
                  </strong>
                </div>
              </motion.div>

              {/* Floating Graphic Node 2: Stainless Steel 316L Spec (Bottom Left) */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: 0.35 }}
                whileHover={{ y: -4, scale: 1.02 }}
                className="absolute -bottom-4 left-4 sm:-left-2 z-20 bg-white/95 backdrop-blur-md px-4 py-3 rounded-2xl border border-sky-100 shadow-xl shadow-blue-900/10 flex items-center gap-3"
              >
                <div className="w-10 h-10 rounded-xl bg-slate-900 text-white flex items-center justify-center shrink-0 shadow-sm">
                  <Factory className="w-5 h-5 text-sky-400" />
                </div>
                <div className="min-w-0">
                  <span className="text-[10px] font-extrabold uppercase tracking-wider text-slate-400 block font-mono">
                    Tangki Reaktor
                  </span>
                  <strong className="text-xs font-bold font-heading text-slate-900 block truncate">
                    Stainless Steel 316L Anti-Korosi
                  </strong>
                </div>
              </motion.div>

              {/* Floating Graphic Node 3: Realtime Batch Telemetry Badge (Bottom Right) */}
              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: 0.5 }}
                className="hidden sm:flex absolute -bottom-3 right-6 z-20 bg-gradient-to-r from-[#0F58A8] to-[#0284C7] text-white px-4 py-2.5 rounded-2xl shadow-xl shadow-blue-900/20 items-center gap-2.5"
              >
                <Activity className="w-4 h-4 text-sky-200" />
                <div className="text-left">
                  <span className="text-[9px] font-bold uppercase tracking-wider text-blue-100 block">
                    Kapasitas Batch
                  </span>
                  <span className="text-xs font-extrabold font-heading block">
                    500+ Ton / Bulan
                  </span>
                </div>
              </motion.div>

            </div>
          </motion.div>

          {/* ========================================================================= */}
          {/* SISI KANAN: OPEN EDITORIAL & 4 INTERACTIVE GRAPHIC PILLARS                */}
          {/* ========================================================================= */}
          <motion.div
            className="lg:col-span-6 space-y-7"
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.8, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Header Content */}
            <div className="space-y-3">
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                Mengapa Memilih PT Kediri Chemical Abadi?
              </h2>

              <p className="text-slate-700 text-xs sm:text-sm lg:text-[15px] leading-relaxed font-normal">
                Didirikan sejak 2004, PT Kediri Chemical Abadi telah menjadi mitra manufaktur kimia pembersih bagi ratusan rumah sakit, perhotelan nasional, sentra laundry komersial, dan industri manufaktur. Kami mengintegrasikan riset formulasi bebas fosfat dengan lini pencampuran presisi tinggi berstandar mutu ISO 9001:2015.
              </p>
            </div>

            {/* 4 Interactive Graphic Pillar Cards (2x2 Grid) */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-1">
              {PILLARS.map((pillar, idx) => {
                const Icon = pillar.icon
                const isHovered = activeHover === idx

                return (
                  <motion.div
                    key={idx}
                    onHoverStart={() => setActiveHover(idx)}
                    onHoverEnd={() => setActiveHover(null)}
                    whileHover={{ y: -3, transition: { duration: 0.2 } }}
                    className={`p-4 rounded-2xl bg-gradient-to-br from-white via-sky-50/30 to-white border ${pillar.borderColor} shadow-sm hover:shadow-md transition-all space-y-2`}
                  >
                    <div className="flex items-center justify-between">
                      <div className={`w-8 h-8 rounded-xl ${pillar.bgColor} ${pillar.color} flex items-center justify-center shrink-0`}>
                        <Icon className="w-4 h-4" />
                      </div>
                      <span className="text-[10px] font-bold font-mono px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">
                        {pillar.badge}
                      </span>
                    </div>

                    <strong className="text-xs sm:text-[13px] font-bold font-heading text-slate-900 block leading-snug">
                      {pillar.title}
                    </strong>

                    <p className="text-[11px] sm:text-xs text-slate-600 leading-relaxed font-normal">
                      {pillar.desc}
                    </p>
                  </motion.div>
                )
              })}
            </div>

            {/* Open Stat Metrics (Fluid Typography & Micro-Gauges) */}
            <div className="grid grid-cols-3 gap-4 pt-4 border-t border-sky-100">
              <div className="p-3 rounded-2xl bg-sky-50/40 border border-sky-100 space-y-0.5">
                <span className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 block">
                  20+ Thn
                </span>
                <span className="text-[10px] sm:text-xs font-semibold text-slate-500 uppercase tracking-wider block">
                  Pengalaman Manufaktur
                </span>
              </div>

              <div className="p-3 rounded-2xl bg-sky-50/40 border border-sky-100 space-y-0.5">
                <span className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-[#0F58A8] block">
                  500+ Ton
                </span>
                <span className="text-[10px] sm:text-xs font-semibold text-slate-500 uppercase tracking-wider block">
                  Kapasitas Bulanan
                </span>
              </div>

              <div className="p-3 rounded-2xl bg-sky-50/40 border border-sky-100 space-y-0.5">
                <span className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-emerald-600 block">
                  100%
                </span>
                <span className="text-[10px] sm:text-xs font-semibold text-slate-500 uppercase tracking-wider block">
                  Bebas Fosfat
                </span>
              </div>
            </div>

            {/* CTA Button (Fluid Pill) */}
            <div className="pt-1">
              <Link
                to="/about"
                className="btn-fluid-primary inline-flex items-center gap-2 px-7 py-3"
              >
                <span>Pelajari Fasilitas Reaktor Pabrik</span>
                <ArrowRight className="w-4 h-4" />
              </Link>
            </div>

          </motion.div>

        </div>
      </div>
    </section>
  )
}

