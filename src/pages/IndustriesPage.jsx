import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { ShieldCheck, ArrowRight } from 'lucide-react'
import IndustriesSection from '@/components/sections/IndustriesSection'
import CTASection from '@/components/sections/CTASection'

const SECTOR_BENEFITS = [
  {
    id: 'medis',
    code: 'SEC-MED01',
    badge: 'KARS COMPLIANT',
    sector: 'Rumah Sakit & Fasilitas Medis',
    metric: '100% Non-Fosfat (STPP-Free)',
    desc: 'Lolos uji akreditasi KARS, aman bagi sistem biofilter IPAL, dan mampu membasmi patogen mikroba linen infeksius secara tuntas.',
    image: '/images/kca_soap_gallery_composite.jpg',
    stat: 'OECD 301D >90%',
    topColor: 'border-t-emerald-500',
    accentText: 'text-emerald-400',
  },
  {
    id: 'hotel',
    code: 'SEC-HTL02',
    badge: 'LUXURY HOSPITALITY',
    sector: 'Jaringan Hotel & Resort',
    metric: 'Ekstra Lembut Serat Linen',
    desc: 'Optical brightener premium menjaga keputihan serat linen tanpa merapuhkan kain, memperpanjang usia pakai linen hotel.',
    image: '/images/kca_packaging_lineup.png',
    stat: '50x Siklus Cuci',
    topColor: 'border-t-[#0F58A8]',
    accentText: 'text-sky-400',
  },
  {
    id: 'laundry',
    code: 'SEC-LND03',
    badge: 'COMMERCIAL BULK',
    sector: 'Sentra Laundry Komersial',
    metric: 'Hemat Dosis 10–15 ml/kg',
    desc: 'Menurunkan biaya pembelian kimia per kilogram cucian hingga 30% dibanding deterjen curah filler konvensional.',
    image: '/images/kca_factory_floor.jpg',
    stat: 'Hemat OPEX 30%',
    topColor: 'border-t-blue-400',
    accentText: 'text-blue-300',
  },
  {
    id: 'pabrik',
    code: 'SEC-MFG04',
    badge: 'HEAVY INDUSTRIAL',
    sector: 'Pabrik & Workshop Manufaktur',
    metric: 'Heavy Duty Degreaser',
    desc: 'Daya penetrasi cepat melarutkan oli pekat hidrokarbon, gemuk mesin berat, dan kerak jelaga lantai workshop seketika.',
    image: '/images/kca_factory_reactors.jpg',
    stat: 'pH 12+ Saponifikasi',
    topColor: 'border-t-amber-500',
    accentText: 'text-amber-400',
  },
]

export default function IndustriesPage() {
  return (
    <main className="bg-white text-slate-900 pt-20">
      <Helmet>
        <title>Sektor Pasokan Industri & Analisis Efisiensi — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Formulasi kimia pembersih industri terpadu untuk rumah sakit KARS, perhotelan nasional, sentra laundry komersial, dan pabrik manufaktur."
        />
        <link rel="canonical" href="https://kedirichemical.id/industries" />
        <meta property="og:title" content="Sektor Pasokan Industri & Analisis Efisiensi — PT Kediri Chemical Abadi" />
        <meta property="og:description" content="Optimalisasi biaya operasional kimia pembersih per sektor strategis di Indonesia." />
        <meta property="og:url" content="https://kedirichemical.id/industries" />
      </Helmet>

      {/* Header Banner */}
      <section className="py-16 sm:py-20 bg-slate-50/70 border-b border-slate-200 text-center">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-12 w-full">
          <div className="max-w-3xl mx-auto space-y-3">
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-black font-heading text-slate-900 tracking-tight uppercase">
              Solusi Formulasi Khusus untuk Sektor Strategis
            </h1>

            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl mx-auto font-normal">
              Setiap industri memiliki tantangan sanitasi yang berbeda. Kami merekayasa formula kimia dengan rasio konsentrat presisi untuk menjamin efisiensi biaya terendah.
            </p>
          </div>
        </div>
      </section>

      {/* Efficiency Metrics Grid: TEGAS, TIDAK ROUNDED, WARNA KONTRAS (DARK NAVY) & BERGAMBAR */}
      <section className="py-10 sm:py-20 bg-slate-100/70 text-slate-900 border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-12 w-full space-y-10">
          
          <div className="text-center max-w-2xl mx-auto space-y-2">
            <span className="text-[10.5px] font-mono font-bold uppercase tracking-widest text-[#0F58A8] block">
              ANALISIS EFISIENSI SEKTORAL
            </span>
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-black font-heading text-slate-900 tracking-tight uppercase">
              Optimalisasi Biaya Operasional per Sektor
            </h2>
          </div>

          {/* 4 Sharp Geometric Architectural Cards with Visual Headers */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
            {SECTOR_BENEFITS.map((item, idx) => (
              <motion.div
                key={item.id}
                initial={{ opacity: 0, y: 15 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.35, delay: idx * 0.08 }}
                className={`bg-[#0A192F] text-white rounded-lg overflow-hidden border border-slate-800/90 border-t-4 ${item.topColor} shadow-xl shadow-slate-900/10 flex flex-col justify-between group hover:border-[#0F58A8]/60 transition-all duration-300`}
              >
                {/* Visual Header Image with Technical Micro-Badges */}
                <div className="relative h-32 sm:h-40 w-full overflow-hidden bg-slate-950">
                  <img
                    src={item.image}
                    alt={item.sector}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-60 mix-blend-luminosity group-hover:opacity-80 group-hover:mix-blend-normal"
                    loading="lazy"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#0A192F] via-[#0A192F]/50 to-transparent" />
                  
                  {/* Top Bar Badges */}
                  <div className="absolute top-3 left-3 right-3 flex items-center justify-between gap-2">
                    <span className="px-2 py-0.5 rounded bg-black/60 backdrop-blur-xs text-[9.5px] font-mono font-bold text-white border border-white/20">
                      {item.code}
                    </span>
                    <span className="px-2 py-0.5 rounded bg-white/10 backdrop-blur-xs text-[9.5px] font-mono font-bold text-slate-200 border border-white/15 uppercase tracking-wider">
                      {item.badge}
                    </span>
                  </div>
                </div>

                {/* Card Content Body */}
                <div className="p-4 sm:p-6 space-y-2.5 sm:space-y-3.5 flex-1 flex flex-col justify-between">
                  <div className="space-y-2">
                    <span className={`text-[11px] font-mono font-bold uppercase tracking-wider ${item.accentText} block`}>
                      {item.sector}
                    </span>
                    <h3 className="text-base sm:text-lg font-black font-heading text-white leading-snug">
                      {item.metric}
                    </h3>
                    <p className="text-xs text-slate-300 leading-relaxed font-normal">
                      {item.desc}
                    </p>
                  </div>

                  <div className="pt-3 border-t border-slate-800/90 flex items-center justify-between text-xs">
                    <div className="flex items-center gap-1.5 text-emerald-400 font-mono font-bold text-[11px]">
                      <ShieldCheck className="w-3.5 h-3.5 shrink-0" />
                      <span>Teruji Efektif</span>
                    </div>
                    <span className="font-mono text-[11px] text-slate-400 font-semibold">
                      {item.stat}
                    </span>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>

        </div>
      </section>

      {/* Industries Showcase Section */}
      <IndustriesSection />

      <CTASection />
    </main>
  )
}
