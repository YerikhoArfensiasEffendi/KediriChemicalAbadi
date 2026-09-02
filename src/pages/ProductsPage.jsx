import { useState } from 'react'
import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { 
  FileText, 
  CheckCircle2, 
  Phone,
  ArrowRight
} from 'lucide-react'
import { PRODUCTS_DATA } from '@/data/productsData'
import { COMPANY_DATA } from '@/data/companyData'
import RFQModal from '@/components/ui/RFQModal'
import CTASection from '@/components/sections/CTASection'

// Professional Vector Corporate Logos & Monograms
const CorporateLogos = {
  Laundry: () => (
    <svg className="w-5 h-5 text-[#0F58A8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z" />
      <path d="M8 14a4 4 0 0 0 8 0" strokeDasharray="2 2" />
      <circle cx="12" cy="12" r="1.5" fill="currentColor" />
    </svg>
  ),
  Hospitality: () => (
    <svg className="w-5 h-5 text-[#4338CA]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 9h1M14 9h1M9 13h1M14 13h1M9 17h1M14 17h1" />
      <path d="M12 3v3" strokeWidth="2" />
    </svg>
  ),
  Healthcare: () => (
    <svg className="w-5 h-5 text-[#059669]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 4v16m-8-8h16" strokeWidth="2.5" strokeLinecap="round" />
      <circle cx="12" cy="12" r="9" strokeWidth="1.5" />
    </svg>
  ),
  Industrial: () => (
    <svg className="w-5 h-5 text-slate-800" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M2 20h20M6 20V8l6 4V8l6 4V4l4 4v12" />
      <circle cx="6" cy="14" r="1.5" fill="currentColor" />
      <circle cx="12" cy="16" r="1.5" fill="currentColor" />
    </svg>
  ),
  FnB: () => (
    <svg className="w-5 h-5 text-[#B45309]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M18 2v6a3 3 0 0 1-3 3 3 3 0 0 1-3-3V2M15 11v11M5 2v8a2 2 0 0 0 2 2h0a2 2 0 0 0 2-2V2M7 12v10" />
    </svg>
  ),
}

// Category Configuration & Theming
const SECTOR_GROUPS = [
  {
    id: 'laundry',
    name: 'Laundry Komersial & Rumah Sakit',
    badge: 'SENTRA LAUNDRY & GARMEN',
    desc: 'Formulasi deterjen konsentrat murni, alkali booster, emulsifier minyak, dan pencerah linen berdaya cuci tinggi yang ramah biofilter IPAL.',
    icon: CorporateLogos.Laundry,
    theme: {
      topBar: 'bg-[#0F58A8]',
      border: 'border-blue-300 hover:border-[#0F58A8]',
      badge: 'bg-[#0F58A8] text-white',
      skuBadge: 'bg-blue-100 text-[#0F58A8] border-blue-300',
      topTint: 'bg-gradient-to-b from-blue-50/80 via-white to-white',
      specBg: 'bg-blue-50/50 border-blue-100',
      btnBg: 'bg-[#0F58A8] hover:bg-blue-800 text-white',
      shadow: 'shadow-md shadow-blue-900/10 hover:shadow-2xl hover:shadow-blue-900/20 hover:-translate-y-1',
    }
  },
  {
    id: 'housekeeping',
    name: 'Housekeeping, Resort & Perhotelan',
    badge: 'HOTEL, RESORT & VILLA BINTANG 4-5',
    desc: 'Standar kebersihan premium untuk pembersih lantai, pembersih kaca bebas gores, pelembut serat mikro, dan pembersih multi-permukaan ruang tamu.',
    icon: CorporateLogos.Hospitality,
    theme: {
      topBar: 'bg-[#4338CA]',
      border: 'border-indigo-300 hover:border-[#4338CA]',
      badge: 'bg-[#4338CA] text-white',
      skuBadge: 'bg-indigo-100 text-[#4338CA] border-indigo-300',
      topTint: 'bg-gradient-to-b from-indigo-50/80 via-white to-white',
      specBg: 'bg-indigo-50/50 border-indigo-100',
      btnBg: 'bg-[#4338CA] hover:bg-indigo-800 text-white',
      shadow: 'shadow-md shadow-indigo-900/10 hover:shadow-2xl hover:shadow-indigo-900/20 hover:-translate-y-1',
    }
  },
  {
    id: 'fnb',
    name: 'Restoran, Katering, & Food Processing (F&B)',
    badge: 'FOOD CONTACT SAFE & HACCP SAFE',
    desc: 'Formula sanitasi food-grade ramah lingkungan untuk melarutkan lemak hewani pekat pada grease trap dapur, sabun cuci piring busa hemat bilas, dan descaler boiler.',
    icon: CorporateLogos.FnB,
    theme: {
      topBar: 'bg-[#B45309]',
      border: 'border-amber-300 hover:border-[#B45309]',
      badge: 'bg-[#B45309] text-white',
      skuBadge: 'bg-amber-100 text-[#B45309] border-amber-300',
      topTint: 'bg-gradient-to-b from-amber-50/80 via-white to-white',
      specBg: 'bg-amber-50/50 border-amber-100',
      btnBg: 'bg-[#B45309] hover:bg-amber-800 text-white',
      shadow: 'shadow-md shadow-amber-900/10 hover:shadow-2xl hover:shadow-amber-900/20 hover:-translate-y-1',
    }
  },
  {
    id: 'medis',
    name: 'Sanitasi Medis & Fasilitas Rumah Sakit',
    badge: 'STANDAR SANITASI AKREDITASI KARS',
    desc: 'Disinfeksi dan dekontaminasi linen medis infeksius serta ruang operasi dengan formula >90% biodegradable yang tidak merusak bakteri pengurai IPAL RS.',
    icon: CorporateLogos.Healthcare,
    theme: {
      topBar: 'bg-[#059669]',
      border: 'border-emerald-300 hover:border-[#059669]',
      badge: 'bg-[#059669] text-white',
      skuBadge: 'bg-emerald-100 text-[#059669] border-emerald-300',
      topTint: 'bg-gradient-to-b from-emerald-50/80 via-white to-white',
      specBg: 'bg-emerald-50/50 border-emerald-100',
      btnBg: 'bg-[#059669] hover:bg-emerald-800 text-white',
      shadow: 'shadow-md shadow-emerald-900/10 hover:shadow-2xl hover:shadow-emerald-900/20 hover:-translate-y-1',
    }
  },
  {
    id: 'otomotif',
    name: 'Pabrik Manufaktur & Bengkel Otomotif',
    badge: 'HEAVY DUTY INDUSTRIAL DEGREASING',
    desc: 'Pembersih dan pelarut kerak oli berat, gemuk permesinan CNC, dan pembersih lantai workshop anti-licin yang aman terhadap permukaan baja.',
    icon: CorporateLogos.Industrial,
    theme: {
      topBar: 'bg-[#0A192F]',
      border: 'border-slate-400 hover:border-[#0A192F]',
      badge: 'bg-[#0A192F] text-white',
      skuBadge: 'bg-slate-200 text-slate-900 border-slate-400',
      topTint: 'bg-gradient-to-b from-slate-100 via-white to-white',
      specBg: 'bg-slate-100/70 border-slate-200',
      btnBg: 'bg-[#0A192F] hover:bg-slate-800 text-white',
      shadow: 'shadow-md shadow-slate-900/15 hover:shadow-2xl hover:shadow-slate-900/25 hover:-translate-y-1',
    }
  },
]

export default function ProductsPage() {
  const [rfqOpen, setRfqOpen] = useState(false)
  const [selectedProductForRfq, setSelectedProductForRfq] = useState(null)

  const products = Array.isArray(PRODUCTS_DATA) ? PRODUCTS_DATA : []
  const waNumber = COMPANY_DATA.contacts?.whatsappNumber || '6285812307629'

  const handleOpenRfq = (product) => {
    setSelectedProductForRfq(product)
    setRfqOpen(true)
  }

  return (
    <main className="bg-white text-slate-900">
      <Helmet>
        <title>Katalog Kimia B2B Terpadu per Sektor — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Katalog teknis kimia pembersih 100% non-fosfat terkelompok per sektor industri: Laundry, Perhotelan, Restoran F&B, Rumah Sakit, dan Manufaktur Otomotif."
        />
      </Helmet>

      {/* Header Banner (Fluid Water Theme Canvas) */}
      <section className="py-14 sm:py-20 bg-gradient-to-b from-sky-50/50 via-white to-white border-b border-sky-100 text-center">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          <div className="max-w-3xl mx-auto space-y-3">
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Matriks Formulasi Kimia Pembersih per Sektor Industri
            </h1>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl mx-auto font-normal pt-1">
              Seluruh produk diformulasikan dari bahan aktif berkualitas tinggi, 100% bebas fosfat, hemat dosis per siklus pencucian, dan aman bagi sistem pengolahan limbah cair (IPAL).
            </p>
          </div>
        </div>
      </section>

      {/* Direct Grouped Products Display by Sector */}
      <div className="space-y-16 sm:space-y-24 py-12 sm:py-20">
        {SECTOR_GROUPS.map((sector, sIdx) => {
          const sectorProducts = products.filter((p) => p.category === sector.id)
          if (sectorProducts.length === 0) return null

          const IconComp = sector.icon
          const theme = sector.theme

          return (
            <section
              key={sector.id}
              id={sector.id}
              className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-8"
            >
              {/* Sector Header Block */}
              <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-4 border-b border-sky-100">
                <div className="space-y-1 max-w-2xl">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-full bg-sky-50 border border-sky-100 flex items-center justify-center shrink-0 text-[#0F58A8]">
                      <IconComp />
                    </div>
                    <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-slate-500 bg-slate-100 px-2.5 py-0.5 rounded-full">
                      {sector.badge}
                    </span>
                    <span className={`text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full border ${theme.skuBadge}`}>
                      {sectorProducts.length} Produk
                    </span>
                  </div>

                  <h2 className="text-xl sm:text-2xl font-extrabold font-heading text-slate-900 tracking-tight">
                    {sector.name}
                  </h2>
                </div>

                <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
                  {sector.desc}
                </p>
              </div>

              {/* Volumetric Product Cards Grid for this Sector */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {sectorProducts.map((product) => (
                  <motion.div
                    key={product.id}
                    initial={{ opacity: 0, y: 15 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.3 }}
                    className={`bg-white border rounded-3xl transition-all duration-300 flex flex-col justify-between group relative overflow-hidden ${theme.border} shadow-lg shadow-blue-900/5 hover:shadow-xl hover:-translate-y-1`}
                  >
                    {/* Top Color Accent Strip */}
                    <div className={`h-1.5 w-full ${theme.topBar}`} />

                    <div className="p-5 sm:p-6 space-y-4 bg-gradient-to-b from-sky-50/40 via-white to-white">
                      
                      {/* Top Bar: SKU & Badge */}
                      <div className="flex items-center justify-between gap-2 border-b border-sky-100 pb-3">
                        <span className={`text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full border ${theme.skuBadge}`}>
                          {product.sku}
                        </span>
                        {product.badge && (
                          <span className={`text-[10px] font-extrabold uppercase px-2.5 py-0.5 rounded-full tracking-wider truncate ${theme.badge}`}>
                            {product.badge}
                          </span>
                        )}
                      </div>

                      {/* Product Header: 3D Photo Stage & Title */}
                      <div className="space-y-3">
                        <div className="w-full h-36 bg-white/80 border border-sky-100 rounded-2xl p-3 flex items-center justify-center overflow-hidden shadow-2xs group-hover:scale-102 transition-transform duration-500">
                          <img
                            src={product.image || '/images/product_jerigen5l.jpg'}
                            alt={product.title}
                            className="w-full h-full object-contain filter drop-shadow-md select-none"
                            loading="lazy"
                          />
                        </div>

                        <div className="space-y-1">
                          <h3 className="font-heading font-extrabold text-sm sm:text-base text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug">
                            {product.title}
                          </h3>
                          <p className="text-xs text-slate-600 leading-relaxed font-normal line-clamp-2">
                            {product.description}
                          </p>
                        </div>
                      </div>

                      {/* 4-Grid Technical Specification Matrix */}
                      <div className="grid grid-cols-2 gap-2 p-3 rounded-2xl bg-sky-50/50 border border-sky-100 text-xs">
                        <div className="space-y-0.5">
                          <span className="text-[9px] text-slate-500 block uppercase font-bold tracking-wider">
                            Bahan Aktif:
                          </span>
                          <strong className="text-slate-900 block text-[11px] font-bold truncate font-heading">
                            {product.activeMatter}
                          </strong>
                        </div>

                        <div className="space-y-0.5">
                          <span className="text-[9px] text-slate-500 block uppercase font-bold tracking-wider">
                            Rentang pH:
                          </span>
                          <strong className="text-slate-900 block text-[11px] font-bold truncate font-heading">
                            {product.phRange}
                          </strong>
                        </div>

                        <div className="space-y-0.5">
                          <span className="text-[9px] text-slate-500 block uppercase font-bold tracking-wider">
                            Dosis Pakai:
                          </span>
                          <strong className="text-slate-900 block text-[11px] font-bold truncate font-heading">
                            {product.dosage}
                          </strong>
                        </div>

                        <div className="space-y-0.5">
                          <span className="text-[9px] text-slate-500 block uppercase font-bold tracking-wider">
                            Kemasan:
                          </span>
                          <strong className="text-slate-900 block text-[11px] font-bold truncate font-heading">
                            {product.packaging}
                          </strong>
                        </div>
                      </div>

                      {/* Bullet Key Highlights */}
                      <div className="space-y-1.5 text-xs text-slate-700">
                        {product.features?.map((ft, fIdx) => (
                          <div key={fIdx} className="flex items-center gap-1.5">
                            <div className="w-3.5 h-3.5 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                              <CheckCircle2 className="w-3 h-3" />
                            </div>
                            <span className="truncate font-medium">{ft}</span>
                          </div>
                        ))}
                      </div>

                    </div>

                    {/* Card Action: RFQ Button & WhatsApp (Fluid Pill) */}
                    <div className="p-4 bg-white border-t border-sky-100 flex items-center gap-2">
                      <button
                        onClick={() => handleOpenRfq(product)}
                        className={`flex-1 h-10 px-3 rounded-full text-xs font-bold font-heading uppercase tracking-wider transition-all flex items-center justify-center gap-1.5 cursor-pointer shadow-xs ${theme.btnBg}`}
                      >
                        <FileText className="w-3.5 h-3.5" />
                        <span>Minta RFQ</span>
                      </button>

                      <a
                        href={`https://wa.me/${waNumber}?text=${encodeURIComponent(`Halo Tim Formulator PT Kediri Chemical Abadi, saya ingin konsultasi teknis mengenai produk: ${product.title} (SKU: ${product.sku}).`)}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="h-10 px-3.5 bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 rounded-full text-xs font-bold transition-colors flex items-center justify-center cursor-pointer shadow-2xs"
                        title="Konsultasi via WhatsApp"
                      >
                        <Phone className="w-4 h-4 text-emerald-600" />
                      </a>
                    </div>

                  </motion.div>
                ))}
              </div>
            </section>
          )
        })}
      </div>

      {/* Full Width CTA Section */}
      <CTASection />

      {/* RFQ Modal */}
      <RFQModal 
        isOpen={rfqOpen} 
        onClose={() => setRfqOpen(false)} 
        initialProduct={selectedProductForRfq?.title}
      />
    </main>
  )
}


