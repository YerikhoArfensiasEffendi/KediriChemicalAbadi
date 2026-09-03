import os

new_code = '''import { motion } from 'framer-motion'
import { Check } from 'lucide-react'

// =========================================================================
// PROFESSIONAL INDUSTRIAL ENGINEERING SVG ICONS (Crisp, Clean, Non-AI)
// =========================================================================

/** 1. Laboratory Titration Flask Icon */
function FlaskTitrationIcon({ className = "w-6 h-6 text-[#0F58A8]" }) {
  return (
    <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M10 2v5.5L4.5 18a2 2 0 001.7 3h11.6a2 2 0 001.7-3L14 7.5V2" />
      <line x1="8.5" y1="2" x2="15.5" y2="2" />
      <line x1="7" y1="14" x2="17" y2="14" />
      <circle cx="10" cy="17" r="0.75" fill="currentColor" />
      <circle cx="14" cy="18" r="0.75" fill="currentColor" />
    </svg>
  )
}

/** 2. Botanical Eco & Biofilter Water Droplet Icon */
function EcoBiofilterIcon({ className = "w-6 h-6 text-emerald-600" }) {
  return (
    <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M11 20A7 7 0 014 13C4 7.5 11 3 11 3s7 4.5 7 10a7 7 0 01-7 7z" />
      <path d="M11 11v9" />
      <path d="M11 15l4-3" />
    </svg>
  )
}

/** 3. Industrial Jacketed Pressure Reactor Vessel Icon */
function StainlessReactorIcon({ className = "w-6 h-6 text-slate-800" }) {
  return (
    <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <rect x="9" y="2" width="6" height="3" rx="0.5" />
      <line x1="12" y1="5" x2="12" y2="8" />
      <path d="M5 11c0-1.7 3.1-3 7-3s7 1.3 7 3v6c0 2.8-3.1 5-7 5s-7-2.2-7-5v-6z" />
      <line x1="12" y1="8" x2="12" y2="15" />
      <path d="M9 15h6" />
    </svg>
  )
}

/** 4. Calibrated Stoichiometric Pipette Icon */
function StoichiometricPipetteIcon({ className = "w-6 h-6 text-sky-600" }) {
  return (
    <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M14 2l4 4-2 2-4-4 2-2z" />
      <path d="M12 4L4 12l-.5 3.5 3.5-.5 8-8" />
      <line x1="6.5" y1="9.5" x2="9.5" y2="12.5" />
      <line x1="8.5" y1="7.5" x2="11.5" y2="10.5" />
      <path d="M3.5 15.5L2 20l4.5-1.5" />
    </svg>
  )
}

// =========================================================================
// MAIN COMPONENT: WHY CHOOSE US (Seamless Integrated Editorial Layout)
// =========================================================================

export default function WhyChooseUsSection() {
  const PILLARS = [
    {
      svg: FlaskTitrationIcon,
      code: 'QC-ISO9001',
      tag: 'ISO 9001:2015 • SISTEM KENDALI MUTU',
      title: 'Standar Mutu ISO 9001:2015 & Validasi COA Digital',
      desc: 'Setiap tahapan pencampuran kimia di pabrik KCA melewati protokol quality control (QC) tiga tahap: kalibrasi titrasi pH potensiometrik digital, uji viskositas dinamis menggunakan viskometer Brookfield, dan penentuan berat jenis spesifik via pycnometer. Sebelum pelepasan armada distribusi, setiap batch (500L – 10.000L) wajib mengantongi Certificate of Analysis (COA) resmi bertanda tangan formulator untuk menjamin konsistensi formula nol-deviasi.',
      specs: [
        'Titrasi digital potensiometrik akurasi pH ±0.2',
        'Uji viskositas Brookfield & kestabilan termal 40°C',
        'Sertifikat Analisis (COA) bernomor seri per batch'
      ],
      tagBg: 'bg-blue-50 text-[#0F58A8] border-blue-200',
      iconBg: 'bg-blue-50/80',
      iconBorder: 'border-blue-200'
    },
    {
      svg: EcoBiofilterIcon,
      code: 'ENV-STPP0',
      tag: 'KARS COMPLIANT • ZERO PHOSPHATE',
      title: '100% Bebas Fosfat (STPP-Free) & Perlindungan Biofilter IPAL',
      desc: 'KCA menolak total penggunaan Sodium Tripolyphosphate (STPP) yang lazim dipakai deterjen curah konvensional pemicu ledakan alga (eutrofikasi) dan kematian mikrobioma pengurai limbah cair. Kami merekayasa biosurfaktan berbasis asam lemak nabati terbarukan dengan indeks biodegradasi biologi melampaui 90% (standar uji OECD 301D), menjaga instalasi pengolahan air limbah (IPAL) aerobik/anaerobik rumah sakit tetap memenuhi baku mutu lingkungan hidup.',
      specs: [
        '0% Senyawa STPP (Mencegah kerusakan biofilter IPAL)',
        'Biodegradabilitas biologis >90% standar OECD 301D',
        'Lolos uji baku mutu limbah cair rumah sakit rujukan'
      ],
      tagBg: 'bg-emerald-50 text-emerald-700 border-emerald-200',
      iconBg: 'bg-emerald-50/80',
      iconBorder: 'border-emerald-200'
    },
    {
      svg: StainlessReactorIcon,
      code: 'IND-SS316L',
      tag: '500+ TON/BULAN • SS 316L REACTORS',
      title: 'Lini Reaktor Stainless Steel 316L & Demin RO Mandiri',
      desc: 'Fasilitas manufaktur KCA di Mojoroto, Kediri mengoperasikan deretan tangki reaktor jaket pemanas Stainless Steel grade medis AISI 316L yang tahan terhadap korosi asam organik pekat dan basa kuat. Dilengkapi instalasi pengolahan air demineralisasi Reverse Osmosis (RO) mandiri berkapasitas 50.000 Liter/hari (<5 ppm TDS), menjamin kemurnian pelarut surfaktan tertinggi dan kapasitas pasokan massal melampaui 500+ Ton konsentrat per bulan tanpa jeda rantai pasok.',
      specs: [
        'Tangki jacketed Stainless Steel AISI 316L tahan korosi',
        'Instalasi Demin RO mandiri 50.000 L/hari (<5 ppm TDS)',
        'Kapasitas pasokan 500+ Ton/bulan siap kontrak B2B'
      ],
      tagBg: 'bg-slate-100 text-slate-800 border-slate-300',
      iconBg: 'bg-slate-100',
      iconBorder: 'border-slate-300'
    },
    {
      svg: StoichiometricPipetteIcon,
      code: 'COST-CONC30',
      tag: 'HIGH ACTIVE MATTER • COST-IN-USE',
      title: 'Konsentrasi Bahan Aktif Murni & Penghematan OPEX 30–40%',
      desc: 'Menghilangkan total penggunaan garam pengental murah (filler) atau pengencer air berlebih yang merusak elemen pemanas mesin cuci. Dengan konsentrasi bahan aktif murni tinggi, efisiensi dosis KCA stabil pada takaran 10–15 ml per kilogram cucian (dibandingkan 35–50 ml pada produk retail konvensional), memangkas volume pemakaian cairan, menurunkan frekuensi pengadaan logistik, dan menghemat total biaya operasional kimia hingga 40% per siklus kerja.',
      specs: [
        'Bahan aktif surfaktan murni tanpa garam filler',
        'Efisiensi dosis presisi 10–15 ml per kilogram cucian',
        'Memangkas biaya operasional kimia hingga 40%'
      ],
      tagBg: 'bg-sky-50 text-sky-700 border-sky-200',
      iconBg: 'bg-sky-50/80',
      iconBorder: 'border-sky-200'
    }
  ]

  return (
    <section className="py-20 sm:py-28 bg-gradient-to-b from-white via-sky-50/20 to-white text-slate-900 relative overflow-hidden">
      
      {/* Ambient Liquid Water Caustics Texture */}
      <div className="absolute inset-0 pointer-events-none opacity-20 select-none overflow-hidden mix-blend-multiply">
        <img
          src="/images/bg_liquid_caustics_4k.png"
          alt="Clean Ambient Liquid Water Caustics Texture"
          className="w-full h-full object-cover object-center"
        />
      </div>

      <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-10 space-y-12">
        
        {/* ========================================================================= */}
        {/* TOP EDITORIAL HEADER                                                      */}
        {/* ========================================================================= */}
        <div className="max-w-4xl space-y-3 pb-6 border-b border-slate-200">
          <span className="text-[10.5px] sm:text-[11px] font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
            STANDAR MANUFAKTUR &amp; KEMITRAAN B2B TERPERCAYA
          </span>

          <h2 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight leading-[1.25] uppercase">
            SOLUSI FORMULASI KIMIA &amp; KEBERSIHAN INDUSTRI
          </h2>

          <p className="text-slate-700 text-xs sm:text-[13.5px] leading-relaxed font-normal">
            Didirikan sejak 2004 di Kediri, Jawa Timur, PT Kediri Chemical Abadi telah menjadi mitra manufaktur kimia pembersih bagi ratusan rumah sakit rujukan akreditasi KARS, jaringan perhotelan berbintang, sentra laundry komersial, dan pabrik manufaktur. Kami mengintegrasikan rekayasa surfaktan murni bebas fosfat dengan fasilitas reaktor Stainless Steel 316L berstandar mutu ISO 9001:2015.
          </p>
        </div>

        {/* ========================================================================= */}
        {/* MAIN SPLIT: COMPOSITE GALLERY (LEFT) + 4 INTEGRATED EDITORIAL ROWS (RIGHT) */}
        {/* ========================================================================= */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-start">
          
          {/* Sisi Kiri: Composite Gallery (Stainless Bioreactor + Finished Products) */}
          <motion.div
            className="lg:col-span-5 lg:sticky lg:top-28 space-y-4"
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="relative rounded-xl overflow-hidden bg-slate-100 border border-slate-200/90 shadow-md group">
              <img
                src="/images/kca_soap_gallery_composite.jpg"
                alt="Fasilitas Reaktor Pabrik Bioreactor Stainless Steel dan Formulasi Sabun PT Kediri Chemical Abadi"
                className="w-full h-auto object-cover select-none group-hover:scale-[1.01] transition-transform duration-700 ease-out"
              />
            </div>

            {/* Industrial Plant Trust Badge */}
            <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200/90 flex items-center justify-between gap-3 text-xs">
              <div className="space-y-0.5">
                <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-slate-500 block">
                  LOKASI FASILITAS PRODUKSI
                </span>
                <strong className="text-slate-900 font-heading font-bold block text-[11.5px]">
                  Kec. Mojoroto, Kota Kediri, Jawa Timur
                </strong>
              </div>
              <div className="text-right shrink-0">
                <span className="inline-block px-2 py-0.5 rounded bg-[#0F58A8] text-white font-mono text-[10px] font-bold">
                  ISO 9001:2015
                </span>
              </div>
            </div>
          </motion.div>

          {/* Sisi Kanan: 4 In-Depth Technical Engineering Rows (Integrated Seamless, No Bubble Cards) */}
          <div className="lg:col-span-7 divide-y divide-slate-200/90">
            {PILLARS.map((pillar, idx) => {
              const SvgIcon = pillar.svg

              return (
                <motion.div
                  key={pillar.code}
                  initial={{ opacity: 0, y: 15 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true, margin: "-40px" }}
                  transition={{ duration: 0.4, delay: idx * 0.05 }}
                  className="py-7 first:pt-0 last:pb-0 space-y-3 group"
                >
                  <div className="flex items-start gap-4">
                    
                    {/* Professional Crisp Icon Container (Minimalist Crisp Housing) */}
                    <div className={`w-11 h-11 rounded-lg ${pillar.iconBg} border ${pillar.iconBorder} flex items-center justify-center shrink-0 mt-0.5 group-hover:scale-105 transition-transform duration-200`}>
                      <SvgIcon className="w-6 h-6" />
                    </div>

                    {/* Detailed Content Narrative & Specs */}
                    <div className="space-y-2 flex-1 min-w-0">
                      
                      {/* Micro Code & Category Tag */}
                      <div className="flex items-center justify-between gap-2 flex-wrap">
                        <span className={`text-[10px] font-mono font-bold uppercase tracking-wider px-2 py-0.5 rounded border ${pillar.tagBg}`}>
                          {pillar.tag}
                        </span>
                        <span className="text-[10px] font-mono font-semibold text-slate-400">
                          {pillar.code}
                        </span>
                      </div>

                      {/* Main Title */}
                      <h3 className="text-sm sm:text-base font-black font-heading text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug">
                        {pillar.title}
                      </h3>

                      {/* In-Depth Technical Explanatory Narrative */}
                      <p className="text-xs text-slate-700 leading-relaxed font-normal text-justify sm:text-left">
                        {pillar.desc}
                      </p>

                      {/* Technical Verification Bullets */}
                      <div className="pt-2 grid grid-cols-1 sm:grid-cols-3 gap-2">
                        {pillar.specs.map((spec, sIdx) => (
                          <div key={sIdx} className="flex items-center gap-1.5 text-[11px] text-slate-800 font-medium">
                            <Check className="w-3.5 h-3.5 text-[#0F58A8] shrink-0 stroke-[2.5]" />
                            <span className="line-clamp-1">{spec}</span>
                          </div>
                        ))}
                      </div>

                    </div>

                  </div>
                </motion.div>
              )
            })}
          </div>

        </div>

      </div>
    </section>
  )
}
'''

with open('src/components/sections/WhyChooseUsSection.jsx', 'w', encoding='utf-8') as f:
    f.write(new_code)

print('Updated src/components/sections/WhyChooseUsSection.jsx successfully!')
