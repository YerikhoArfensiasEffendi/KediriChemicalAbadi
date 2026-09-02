import { useState } from 'react'
import { motion } from 'framer-motion'
import { ArrowRight, CheckCircle2, ShieldCheck, Award } from 'lucide-react'
import { MAKLOON_DATA } from '@/data/makloonData'
import RFQModal from '@/components/ui/RFQModal'

// Professional Corporate Vector Logos for Makloon Pillars
const PillarLogos = [
  // 1. Sertifikasi Mutu & Izin Edar
  () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
      <path d="M9 12l2 2 4-4" strokeWidth="2" />
    </svg>
  ),
  // 2. Kecepatan Lead Time & Otomasi
  () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
    </svg>
  ),
  // 3. Jaminan Kerahasiaan Formula (NDA)
  () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
      <path d="M7 11V7a5 5 0 0 1 10 0v4" />
      <circle cx="12" cy="16" r="1" fill="currentColor" />
    </svg>
  ),
  // 4. Kapasitas Skala Massal (500+ Ton)
  () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M2 20h20M6 20V8l6 4V8l6 4V4l4 4v12" />
      <circle cx="12" cy="14" r="1.5" fill="currentColor" />
    </svg>
  ),
]

export default function MakloonSchemeSection() {
  const [rfqOpen, setRfqOpen] = useState(false)
  const regularScheme = MAKLOON_DATA.regularScheme || MAKLOON_DATA.schemes?.[0] || {}
  const dedicatedScheme = MAKLOON_DATA.dedicatedScheme || MAKLOON_DATA.schemes?.[1] || {}

  return (
    <>
      <section id="makloon" className="py-16 sm:py-24 bg-white text-slate-900 border-b border-sky-100">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Section Header: Direct Title & Subline (No Eyebrow Tag) */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 pb-6 border-b border-sky-100">
            <div className="space-y-2 max-w-3xl">
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                2 Pilihan Skema Manufaktur Maklon Kimia
              </h2>
            </div>
            <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
              Pilih opsi manufaktur fleksibel sesuai skala bisnis Anda, mulai dari sistem batch berkala reguler hingga jalur mesin produksi eksklusif (Dedicated Line VIP).
            </p>
          </div>

          {/* 2-Column Comparative Layout (Fluid Wave Styling) */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 divide-y lg:divide-y-0 lg:divide-x divide-sky-100">
            
            {/* Skema 1: Maklon Reguler */}
            <div className="space-y-6 pt-6 lg:pt-0">
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono font-bold text-[#0F58A8] bg-sky-50 px-3 py-1 rounded-full border border-sky-200 uppercase">
                    Skema 01 • MOQ Fleksibel
                  </span>
                  <span className="text-xs font-bold text-slate-500 font-mono">
                    Batch Sharing System
                  </span>
                </div>

                <h3 className="text-xl sm:text-2xl font-extrabold font-heading text-slate-900 leading-tight">
                  {regularScheme.name || regularScheme.title || 'Maklon Reguler (Batch Sharing)'}
                </h3>

                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                  {regularScheme.description || 'Pilihan tepat bagi brand baru dan distributor regional yang ingin memiliki produk kimia dengan merek sendiri tanpa modal pembangunan pabrik.'}
                </p>
              </div>

              {/* Features List (Open Clean List) */}
              <div className="space-y-3 pt-2 border-t border-sky-100">
                {regularScheme.features?.map((f, i) => (
                  <div key={i} className="flex items-start gap-3 text-xs sm:text-sm text-slate-800">
                    <div className="w-4 h-4 rounded-full bg-blue-50 text-[#0F58A8] flex items-center justify-center shrink-0 mt-0.5">
                      <CheckCircle2 className="w-3.5 h-3.5" />
                    </div>
                    <div>
                      <strong className="font-semibold text-slate-900">
                        {typeof f === 'object' ? f.title : f}
                      </strong>
                      {typeof f === 'object' && f.desc && (
                        <span className="text-slate-600 block sm:inline sm:ml-1"> — {f.desc}</span>
                      )}
                    </div>
                  </div>
                ))}
              </div>

              <div className="pt-2">
                <button
                  onClick={() => setRfqOpen(true)}
                  className="btn-fluid-secondary"
                >
                  <span>{regularScheme.ctaText || 'Konsultasi Maklon Reguler'}</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Skema 2: Dedicated Line VIP */}
            <div className="space-y-6 pt-8 lg:pt-0 lg:pl-16">
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono font-bold text-white bg-gradient-to-r from-[#0F58A8] to-[#0284C7] px-3 py-1 rounded-full shadow-sm uppercase">
                    Skema 02 • Jalur Prioritas Khusus
                  </span>
                  <span className="text-xs font-bold text-[#0F58A8] font-mono">
                    Capex-Partnership VIP
                  </span>
                </div>

                <h3 className="text-xl sm:text-2xl font-extrabold font-heading text-slate-900 leading-tight">
                  {dedicatedScheme.name || dedicatedScheme.title || 'Dedicated Production Line'}
                </h3>

                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                  {dedicatedScheme.description || 'Skema kemitraan di mana mitra mendanai pengadaan mesin/reaktor khusus yang didedikasikan 100% untuk produk mereka dengan potongan harga khusus tiap invoice hingga modal kembali utuh.'}
                </p>
              </div>

              {/* Features List (Open Clean List) */}
              <div className="space-y-3 pt-2 border-t border-sky-100">
                {dedicatedScheme.features?.map((f, i) => (
                  <div key={i} className="flex items-start gap-3 text-xs sm:text-sm text-slate-800">
                    <div className="w-4 h-4 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 mt-0.5">
                      <CheckCircle2 className="w-3.5 h-3.5" />
                    </div>
                    <div>
                      <strong className="font-semibold text-slate-900">
                        {typeof f === 'object' ? f.title : f}
                      </strong>
                      {typeof f === 'object' && f.desc && (
                        <span className="text-slate-600 block sm:inline sm:ml-1"> — {f.desc}</span>
                      )}
                    </div>
                  </div>
                ))}
              </div>

              <div className="pt-2">
                <button
                  onClick={() => setRfqOpen(true)}
                  className="btn-fluid-primary"
                >
                  <span>{dedicatedScheme.ctaText || 'Ajukan Dedicated Line VIP'}</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </div>

          </div>

          {/* 4 Pilar Maklon: Open Horizontal Matrix */}
          <div className="pt-8 border-t border-sky-100 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 divide-y sm:divide-y-0 sm:divide-x divide-sky-100">
            {(MAKLOON_DATA?.pillars || []).map((pillar, idx) => {
              const LogoComp = PillarLogos[idx % PillarLogos.length]
              return (
                <div key={idx} className={`space-y-2 pt-4 sm:pt-0 ${idx > 0 ? 'sm:pl-6' : ''}`}>
                  <div className="flex items-center gap-2.5">
                    <div className="w-9 h-9 rounded-full bg-sky-50 border border-sky-100 flex items-center justify-center shrink-0 text-[#0F58A8]">
                      <LogoComp />
                    </div>
                    <span className="text-xs font-extrabold font-heading text-slate-900">{pillar.title}</span>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed font-normal">{pillar.description}</p>
                </div>
              )
            })}
          </div>

        </div>
      </section>

      {/* RFQ Modal */}
      <RFQModal isOpen={rfqOpen} onClose={() => setRfqOpen(false)} />
    </>
  )
}

