import { motion } from 'framer-motion'
import { Check } from 'lucide-react'

// =========================================================================
// BESPOKE HERITAGE INDUSTRIAL CHEMICAL SVG INSIGNIA (Original Line Art)
// =========================================================================

/** 1. QC Lab & ISO 9001: Technical Dual-Ring Titration Retort & Flask Emblem */
function ApparatusTitrationSealSvg({ className = "w-10 h-10" }) {
  return (
    <svg className={className} viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
      {/* Outer Technical Calibration Ring */}
      <circle cx="26" cy="26" r="24" stroke="#0F58A8" strokeWidth="1.2" strokeDasharray="3 2" opacity="0.45" />
      <circle cx="26" cy="26" r="21.5" stroke="#0F58A8" strokeWidth="1.5" />
      <circle cx="26" cy="26" r="19" stroke="#0F58A8" strokeWidth="0.75" opacity="0.3" />
      
      {/* Retort Neck & Ground Joint */}
      <path d="M23 11h6M24.5 11v9.5l7 12a3 3 0 01-2.6 4.5H19.1a3 3 0 01-2.6-4.5l7-12V11" stroke="#0F58A8" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round" />
      
      {/* Titration Burette Tip Dripping */}
      <line x1="26" y1="6" x2="26" y2="10" stroke="#0F58A8" strokeWidth="1.5" strokeLinecap="round" />
      <circle cx="26" cy="14" r="1" fill="#0F58A8" />

      {/* Graduation Marks on Flask Neck */}
      <line x1="23.5" y1="17" x2="28.5" y2="17" stroke="#0F58A8" strokeWidth="1.2" strokeLinecap="round" />
      <line x1="24.5" y1="20" x2="27.5" y2="20" stroke="#0F58A8" strokeWidth="1" strokeLinecap="round" />

      {/* Liquid Meniscus & Fluid Volume Level */}
      <path d="M20 28.5c2-.8 4.5.8 6.5 0s4.5.8 5.5 0" stroke="#0F58A8" strokeWidth="1.5" strokeLinecap="round" />

      {/* Reactive Micro-Bubbles */}
      <circle cx="23" cy="32.5" r="1.2" fill="#0F58A8" />
      <circle cx="27" cy="34" r="1.4" fill="#0F58A8" />
      <circle cx="29" cy="31" r="0.9" fill="#0F58A8" />
    </svg>
  )
}

/** 2. 100% Bebas Fosfat: Botanical Biofilter Purity Shield Emblem */
function EcoBiofilterShieldSvg({ className = "w-10 h-10" }) {
  return (
    <svg className={className} viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
      {/* Dual Ring Eco Heraldic Frame */}
      <circle cx="26" cy="26" r="24" stroke="#059669" strokeWidth="1.2" strokeDasharray="3 2" opacity="0.45" />
      <circle cx="26" cy="26" r="21.5" stroke="#059669" strokeWidth="1.5" />
      <circle cx="26" cy="26" r="19" stroke="#059669" strokeWidth="0.75" opacity="0.3" />

      {/* Intricate Botanical Leaf with Primary Venation */}
      <path d="M17 31c0-9 9-16 18-16 0 9-7 18-16 18-1.5 0-2-.5-2-2z" stroke="#059669" strokeWidth="1.8" strokeLinejoin="round" />
      <path d="M17 31c4-4 9-8 18-16" stroke="#059669" strokeWidth="1.5" strokeLinecap="round" />

      {/* Secondary Lateral Leaf Veins */}
      <path d="M22.5 25.5l4.5 1.5M26 21.5l4.5 1.5M29.5 17.5l4 1.5" stroke="#059669" strokeWidth="1.2" strokeLinecap="round" />

      {/* Pure Water Droplet In Flow Loop */}
      <path d="M28 33.5a4.5 4.5 0 119 0c0 2.5-4.5 7-4.5 7s-4.5-4.5-4.5-7z" stroke="#059669" strokeWidth="1.6" strokeLinejoin="round" />
      <circle cx="32.5" cy="33.5" r="1.2" fill="#059669" />
    </svg>
  )
}

/** 3. Reaktor 500+ Ton: Industrial Pressure Vessel & Stainless Reactor Emblem */
function ReactorJacketedVesselSvg({ className = "w-10 h-10" }) {
  return (
    <svg className={className} viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
      {/* Technical Engineering Seal Frame */}
      <circle cx="26" cy="26" r="24" stroke="#0A192F" strokeWidth="1.2" strokeDasharray="3 2" opacity="0.45" />
      <circle cx="26" cy="26" r="21.5" stroke="#0A192F" strokeWidth="1.5" />
      <circle cx="26" cy="26" r="19" stroke="#0A192F" strokeWidth="0.75" opacity="0.3" />

      {/* Heavy Drive Agitator Motor */}
      <rect x="23" y="9" width="6" height="5" rx="1" stroke="#0A192F" strokeWidth="1.5" />
      <line x1="26" y1="14" x2="26" y2="18" stroke="#0A192F" strokeWidth="1.5" />

      {/* Dished Head Reactor Tank Body with Side Jacket Baffles */}
      <path d="M17 21c0-2.8 4-4.5 9-4.5s9 1.7 9 4.5v13c0 2.8-4 4.5-9 4.5s-9-1.7-9-4.5V21z" stroke="#0A192F" strokeWidth="1.8" />

      {/* Agitator Central Shaft & Marine Impeller Blades */}
      <line x1="26" y1="18" x2="26" y2="31" stroke="#0A192F" strokeWidth="1.4" strokeDasharray="2 1.5" />
      <path d="M21 31h10M20 28l6 3 6-3" stroke="#0A192F" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />

      {/* Bourdon Tube Pressure Gauge Manometer */}
      <circle cx="35" cy="18" r="3.2" stroke="#0A192F" strokeWidth="1.3" />
      <line x1="35" y1="18" x2="36.5" y2="16.5" stroke="#0A192F" strokeWidth="1.2" strokeLinecap="round" />

      {/* Bottom Discharge Ball Valve Flange */}
      <path d="M24 38.5v3h4v-3" stroke="#0A192F" strokeWidth="1.4" strokeLinejoin="round" />
    </svg>
  )
}

/** 4. Konsentrat Hemat Dosis: Stoichiometric Pipette & Meniscus Droplet Emblem */
function StoichiometricPipetteSealSvg({ className = "w-10 h-10" }) {
  return (
    <svg className={className} viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
      {/* Concentric Precision Measurement Frame */}
      <circle cx="26" cy="26" r="24" stroke="#0284C7" strokeWidth="1.2" strokeDasharray="3 2" opacity="0.45" />
      <circle cx="26" cy="26" r="21.5" stroke="#0284C7" strokeWidth="1.5" />
      <circle cx="26" cy="26" r="19" stroke="#0284C7" strokeWidth="0.75" opacity="0.3" />

      {/* Precision Calibrated Chemist Pipette */}
      <path d="M24 10h4v3.5l-1.5 2v10l-1 3.5-1-3.5V15.5L24 13.5V10z" stroke="#0284C7" strokeWidth="1.6" strokeLinejoin="round" />

      {/* Volumetric Graduation Ticks */}
      <line x1="25" y1="18" x2="27" y2="18" stroke="#0284C7" strokeWidth="1.2" />
      <line x1="25" y1="21" x2="27" y2="21" stroke="#0284C7" strokeWidth="1.2" />
      <line x1="25" y1="24" x2="27" y2="24" stroke="#0284C7" strokeWidth="1.2" />

      {/* Falling Concentrated Pure Droplet */}
      <path d="M25 31.5c0-1 1-2.2 1-2.2s1 1.2 1 2.2a1 1 0 11-2 0z" fill="#0284C7" />

      {/* Concentric Surface Tension Wave Meniscus */}
      <ellipse cx="26" cy="38" rx="11" ry="3.2" stroke="#0284C7" strokeWidth="1.5" />
      <ellipse cx="26" cy="38" rx="6.5" ry="1.9" stroke="#0284C7" strokeWidth="1.2" opacity="0.6" />
      <ellipse cx="26" cy="38" rx="2.5" ry="0.8" stroke="#0284C7" strokeWidth="1" opacity="0.4" />
    </svg>
  )
}

// =========================================================================
// MAIN COMPONENT: WHY CHOOSE US (In-Depth Technical Engineering Overview)
// =========================================================================

export default function WhyChooseUsSection() {
  const PILLARS = [
    {
      svg: ApparatusTitrationSealSvg,
      code: 'QC-ISO9001',
      tag: 'ISO 9001:2015 • SISTEM KENDALI MUTU',
      title: 'Standar Mutu ISO 9001:2015 & Validasi COA Digital',
      desc: 'Setiap tahapan pencampuran kimia di pabrik KCA melewati protokol quality control (QC) tiga tahap: kalibrasi titrasi pH potensiometrik digital, uji viskositas dinamis menggunakan viskometer Brookfield, dan penentuan berat jenis spesifik via pycnometer. Sebelum pelepasan armada distribusi, setiap batch (500L – 10.000L) wajib mengantongi Certificate of Analysis (COA) resmi bertanda tangan formulator untuk menjamin konsistensi formula nol-deviasi.',
      specs: [
        'Titrasi digital potensiometrik akurasi pH ±0.2',
        'Uji viskositas Brookfield & kestabilan termal 40°C',
        'Sertifikat Analisis (COA) bernomor seri per batch'
      ],
      borderAccent: 'hover:border-[#0F58A8]/50',
      tagBg: 'bg-blue-50 text-[#0F58A8] border-blue-200'
    },
    {
      svg: EcoBiofilterShieldSvg,
      code: 'ENV-STPP0',
      tag: 'KARS COMPLIANT • ZERO PHOSPHATE',
      title: '100% Bebas Fosfat (STPP-Free) & Perlindungan Biofilter IPAL',
      desc: 'KCA menolak total penggunaan Sodium Tripolyphosphate (STPP) yang lazim dipakai deterjen curah konvensional pemicu ledakan alga (eutrofikasi) dan kematian mikrobioma pengurai limbah cair. Kami merekayasa biosurfaktan berbasis asam lemak nabati terbarukan dengan indeks biodegradasi biologi melampaui 90% (standar uji OECD 301D), menjaga instalasi pengolahan air limbah (IPAL) aerobik/anaerobik rumah sakit tetap memenuhi baku mutu lingkungan hidup.',
      specs: [
        '0% Senyawa STPP (Mencegah kerusakan biofilter IPAL)',
        'Biodegradabilitas biologis >90% standar OECD 301D',
        'Lolos uji baku mutu limbah cair rumah sakit rujukan'
      ],
      borderAccent: 'hover:border-emerald-600/50',
      tagBg: 'bg-emerald-50 text-emerald-700 border-emerald-200'
    },
    {
      svg: ReactorJacketedVesselSvg,
      code: 'IND-SS316L',
      tag: '500+ TON/BULAN • SS 316L REACTORS',
      title: 'Lini Reaktor Stainless Steel 316L & Demin RO Mandiri',
      desc: 'Fasilitas manufaktur KCA di Mojoroto, Kediri mengoperasikan deretan tangki reaktor jaket pemanas Stainless Steel grade medis AISI 316L yang tahan terhadap korosi asam organik pekat dan basa kuat. Dilengkapi instalasi pengolahan air demineralisasi Reverse Osmosis (RO) mandiri berkapasitas 50.000 Liter/hari (<5 ppm TDS), menjamin kemurnian pelarut surfaktan tertinggi dan kapasitas pasokan massal melampaui 500+ Ton konsentrat per bulan tanpa jeda rantai pasok.',
      specs: [
        'Tangki jacketed Stainless Steel AISI 316L tahan korosi',
        'Instalasi Demin RO mandiri 50.000 L/hari (<5 ppm TDS)',
        'Kapasitas pasokan 500+ Ton/bulan siap kontrak B2B'
      ],
      borderAccent: 'hover:border-slate-800/50',
      tagBg: 'bg-slate-100 text-slate-800 border-slate-300'
    },
    {
      svg: StoichiometricPipetteSealSvg,
      code: 'COST-CONC30',
      tag: 'HIGH ACTIVE MATTER • COST-IN-USE',
      title: 'Konsentrasi Bahan Aktif Murni & Penghematan OPEX 30–40%',
      desc: 'Menghilangkan total penggunaan garam pengental murah (filler) atau pengencer air berlebih yang merusak elemen pemanas mesin cuci. Dengan konsentrasi bahan aktif murni tinggi, efisiensi dosis KCA stabil pada takaran 10–15 ml per kilogram cucian (dibandingkan 35–50 ml pada produk retail konvensional), memangkas volume pemakaian cairan, menurunkan frekuensi pengadaan logistik, dan menghemat total biaya operasional kimia hingga 40% per siklus kerja.',
      specs: [
        'Bahan aktif surfaktan murni tanpa garam filler',
        'Efisiensi dosis presisi 10–15 ml per kilogram cucian',
        'Memangkas biaya operasional kimia operasional hingga 40%'
      ],
      borderAccent: 'hover:border-sky-600/50',
      tagBg: 'bg-sky-50 text-sky-700 border-sky-200'
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
        {/* MAIN SPLIT: COMPOSITE GALLERY (LEFT) + 4 IN-DEPTH TECHNICAL PANELS (RIGHT)*/}
        {/* ========================================================================= */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-start">
          
          {/* Sisi Kiri: Composite Gallery (Stainless Bioreactor + Finished Products) */}
          <motion.div
            className="lg:col-span-5 lg:sticky lg:top-28 space-y-4"
            initial={{ opacity: 0, x: -25 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-60px" }}
            transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="relative rounded-3xl overflow-hidden bg-white border border-slate-200/90 shadow-xl shadow-blue-900/10 p-2 sm:p-2.5 group hover:shadow-2xl hover:shadow-blue-900/15 transition-all duration-500">
              <img
                src="/images/kca_soap_gallery_composite.jpg"
                alt="Fasilitas Reaktor Pabrik Bioreactor Stainless Steel dan Formulasi Sabun PT Kediri Chemical Abadi"
                className="w-full h-auto object-cover rounded-2xl select-none group-hover:scale-[1.01] transition-transform duration-700 ease-out"
              />
            </div>

            {/* Industrial Plant Trust Badge */}
            <div className="p-4 rounded-2xl bg-slate-50/90 border border-slate-200/90 flex items-center justify-between gap-3 text-xs">
              <div className="space-y-0.5">
                <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-slate-500 block">
                  LOKASI FASILITAS PRODUKSI
                </span>
                <strong className="text-slate-900 font-heading font-bold block text-[12px]">
                  Kec. Mojoroto, Kota Kediri, Jawa Timur
                </strong>
              </div>
              <div className="text-right shrink-0">
                <span className="inline-block px-2.5 py-1 rounded-md bg-[#0F58A8] text-white font-mono text-[10px] font-bold">
                  ISO 9001:2015
                </span>
              </div>
            </div>
          </motion.div>

          {/* Sisi Kanan: 4 In-Depth Technical Engineering Panels */}
          <div className="lg:col-span-7 space-y-6">
            {PILLARS.map((pillar, idx) => {
              const SvgIcon = pillar.svg

              return (
                <motion.div
                  key={pillar.code}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true, margin: "-40px" }}
                  transition={{ duration: 0.5, delay: idx * 0.08 }}
                  className={`bg-white border border-slate-200/90 rounded-2xl p-5 sm:p-6 shadow-sm hover:shadow-md transition-all duration-300 ${pillar.borderAccent} group relative overflow-hidden`}
                >
                  <div className="flex flex-col sm:flex-row sm:items-start gap-4 sm:gap-5">
                    
                    {/* Bespoke Heritage Industrial SVG Emblem */}
                    <div className="w-13 h-13 sm:w-14 sm:h-14 rounded-xl bg-slate-50 border border-slate-200/80 flex items-center justify-center shrink-0 shadow-2xs group-hover:scale-105 transition-transform duration-300">
                      <SvgIcon className="w-9 h-9 sm:w-10 sm:h-10" />
                    </div>

                    {/* Detailed Content Narrative & Specs */}
                    <div className="space-y-2.5 flex-1 min-w-0">
                      
                      {/* Micro Code & Category Tag */}
                      <div className="flex items-center justify-between gap-2 flex-wrap">
                        <span className={`text-[9.5px] sm:text-[10px] font-mono font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full border ${pillar.tagBg}`}>
                          {pillar.tag}
                        </span>
                        <span className="text-[10px] font-mono font-bold text-slate-400">
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
                      <div className="pt-2 border-t border-slate-100 space-y-1.5">
                        {pillar.specs.map((spec, sIdx) => (
                          <div key={sIdx} className="flex items-center gap-2 text-[11px] sm:text-[11.5px] text-slate-800 font-medium">
                            <div className="w-3.5 h-3.5 rounded-full bg-slate-100 text-slate-700 flex items-center justify-center shrink-0">
                              <Check className="w-2.5 h-2.5 stroke-[2.5]" />
                            </div>
                            <span>{spec}</span>
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



