import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { Factory, CheckCircle2, ArrowRight } from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'

export default function WhyChooseUsSection() {
  return (
    <section className="py-20 sm:py-28 bg-white text-slate-900 relative">
      <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20 items-center">
          
          {/* Sisi Kiri: Foto Reaktor SS 316L (5 Kolom) */}
          <motion.div
            className="lg:col-span-5 relative"
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="relative w-full aspect-[4/3] sm:aspect-[4/5] rounded-3xl overflow-hidden bg-sky-50 border border-sky-100 shadow-xl shadow-blue-900/10 group">
              <img
                src="/images/kca_factory_reactors.jpg"
                alt="Fasilitas Reaktor Pencampur Stainless Steel 316L PT Kediri Chemical Abadi"
                className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out"
              />
              {/* Subtle Natural Light Vignette */}
              <div className="absolute inset-0 bg-gradient-to-t from-slate-900/20 via-transparent to-transparent pointer-events-none" />
            </div>
          </motion.div>

          {/* Sisi Kanan: Open Editorial Content & Open Stats (7 Kolom) */}
          <motion.div
            className="lg:col-span-7 space-y-8"
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.7, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="space-y-4">
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                Mengapa Memilih PT Kediri Chemical Abadi?
              </h2>

              <p className="text-slate-700 text-xs sm:text-sm lg:text-base leading-relaxed font-normal">
                Didirikan sejak 2004, PT Kediri Chemical Abadi telah menjadi mitra manufaktur kimia pembersih bagi ratusan rumah sakit, perhotelan nasional, sentra laundry komersial, dan industri manufaktur. Kami mengintegrasikan riset formulasi bebas fosfat dengan lini pencampuran presisi tinggi berstandar mutu ISO 9001:2015.
              </p>
            </div>

            {/* 4 Keunggulan: Open Direct Fluid List */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
              {[
                'Standar Mutu ISO 9001:2015 & QC Tiap Batch',
                '100% Bebas Fosfat & Ramah Sistem IPAL',
                'Kapasitas Reaktor 500+ Ton / Bulan',
                'Formulasi Konsentrat Hemat Dosis',
              ].map((item, i) => (
                <div key={i} className="flex items-center gap-3 text-xs sm:text-sm text-slate-800">
                  <div className="w-5 h-5 rounded-full bg-blue-50 border border-sky-200 text-[#0F58A8] flex items-center justify-center shrink-0">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                  </div>
                  <span className="font-semibold">{item}</span>
                </div>
              ))}
            </div>

            {/* Open Stat Metrics (Fluid Typography & Air Fresh Styling) */}
            <div className="grid grid-cols-3 gap-6 pt-8 border-t border-sky-100">
              <div className="space-y-1">
                <span className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 block">
                  20+ Thn
                </span>
                <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider block">
                  Pengalaman Manufaktur
                </span>
              </div>

              <div className="space-y-1">
                <span className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-[#0F58A8] block">
                  500+ Ton
                </span>
                <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider block">
                  Kapasitas Bulanan
                </span>
              </div>

              <div className="space-y-1">
                <span className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-emerald-600 block">
                  100%
                </span>
                <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider block">
                  Bebas Fosfat
                </span>
              </div>
            </div>

            {/* CTA Button (Fluid Pill) */}
            <div className="pt-2">
              <Link
                to="/about"
                className="btn-fluid-secondary inline-flex"
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
