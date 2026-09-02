import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { Factory, Building, Hotel, HeartPulse, UtensilsCrossed, ArrowRight, ShieldCheck, CheckCircle2, TrendingDown } from 'lucide-react'
import IndustriesSection from '@/components/sections/IndustriesSection'
import CTASection from '@/components/sections/CTASection'

const SECTOR_BENEFITS = [
  {
    sector: 'Rumah Sakit & Fasilitas Medis',
    metric: '100% Non-Fosfat',
    desc: 'Lolos uji akreditasi KARS, aman bagi sistem bakteri IPAL, dan mampu membasmi patogen mikroba linen infeksius.',
  },
  {
    sector: 'Jaringan Hotel Bintang 4-5 & Resort',
    metric: 'Ekstra Lembut Serat Linen',
    desc: 'Optical brightener premium menjaga keputihan serat linen tanpa merapuhkan kain, memperpanjang usia pakai linen hotel.',
  },
  {
    sector: 'Sentra Laundry Komersial',
    metric: 'Hemat Dosis 10-15 ml/kg',
    desc: 'Menurunkan biaya chemical per kilogram cucian hingga 30% dibanding produk retail konvensional.',
  },
  {
    sector: 'Pabrik & Workshop Manufaktur',
    metric: 'Heavy Duty Degreaser',
    desc: 'Daya penetrasi cepat melarutkan oli pekat, gemuk mesin berat, dan kerak oli lantai workshop seketika.',
  },
]

export default function IndustriesPage() {
  return (
    <main className="bg-white text-slate-900 pt-6">
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
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight">
              Solusi Formulasi Khusus untuk Sektor Strategis
            </h1>

            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl mx-auto font-normal">
              Setiap industri memiliki tantangan sanitasi yang berbeda. Kami merekayasa formula kimia dengan rasio konsentrat presisi untuk menjamin efisiensi biaya terendah.
            </p>
          </div>
        </div>
      </section>

      {/* Efficiency Metrics Grid */}
      <section className="py-16 bg-white text-slate-900 border-b border-sky-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-12 w-full space-y-8">
          <div className="text-center max-w-2xl mx-auto space-y-2">
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900">
              Optimalisasi Biaya Operasional per Sektor
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {SECTOR_BENEFITS.map((item, idx) => (
              <div key={idx} className="p-6 rounded-3xl bg-gradient-to-b from-sky-50/50 via-white to-sky-50/20 border border-sky-100 space-y-3 flex flex-col justify-between shadow-lg shadow-blue-900/5 hover:shadow-xl hover:-translate-y-1 transition-all">
                <div>
                  <span className="text-xs font-bold text-[#0F58A8] uppercase tracking-wider block mb-1">
                    {item.sector}
                  </span>
                  <strong className="text-lg font-extrabold font-heading text-slate-900 block mb-2">
                    {item.metric}
                  </strong>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    {item.desc}
                  </p>
                </div>
                <div className="pt-3 border-t border-sky-100 flex items-center gap-1.5 text-xs text-emerald-600 font-semibold">
                  <div className="w-4 h-4 rounded-full bg-emerald-50 flex items-center justify-center">
                    <ShieldCheck className="w-3.5 h-3.5" />
                  </div>
                  <span>Teruji Efektif</span>
                </div>
              </div>
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
