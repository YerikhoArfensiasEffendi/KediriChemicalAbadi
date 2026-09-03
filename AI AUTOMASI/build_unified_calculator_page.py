import os

calculator_page_code = '''import { useState, useMemo } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Helmet } from 'react-helmet-async'
import { 
  Calculator, 
  Search, 
  BookOpen, 
  CheckCircle2, 
  ArrowRight, 
  Phone, 
  Layers, 
  ShieldCheck, 
  Package, 
  X,
  Droplets,
  Clock,
  SlidersHorizontal,
  FileText,
  Sparkles
} from 'lucide-react'

import { 
  STAIN_PROBLEMS, 
  SECTORS_LIST, 
  TECHNICAL_ARTICLES 
} from '@/data/consultationData'

export default function CalculatorPage() {
  // Sektor & Masalah Noda Terpilih
  const [selectedSector, setSelectedSector] = useState('all')
  const [selectedProblemId, setSelectedProblemId] = useState(STAIN_PROBLEMS[0].id)

  // Parameter Operasional Fasilitas
  const [laundryKg, setLaundryKg] = useState(400)
  const [operatingDays, setOperatingDays] = useState(30)
  const [waterHardness, setWaterHardness] = useState('medium') // 'normal' | 'medium' | 'hard'

  // Blog / Pusat Edukasi State
  const [selectedArticleFilter, setSelectedArticleFilter] = useState('all')
  const [readingArticle, setReadingArticle] = useState(null)

  const waNumber = '6285235889758'

  // Filtered Stain Problems based on sector
  const filteredProblems = useMemo(() => {
    if (selectedSector === 'all') return STAIN_PROBLEMS
    return STAIN_PROBLEMS.filter((p) => p.sector === selectedSector)
  }, [selectedSector])

  // Active Selected Problem
  const activeProblem = useMemo(() => {
    return STAIN_PROBLEMS.find((p) => p.id === selectedProblemId) || STAIN_PROBLEMS[0]
  }, [selectedProblemId])

  // Realtime Dosage & Financial ROI Calculation
  const calculationResults = useMemo(() => {
    const hardnessFactor = waterHardness === 'hard' ? 1.25 : waterHardness === 'medium' ? 1.1 : 1.0
    const monthlyTotalKg = laundryKg * operatingDays

    // Primary Detergent Rate: 12.5 ml/kg baseline adjusted for hardness
    const effDetergentRate = (12.5 * hardnessFactor).toFixed(1)
    const kcaLitersMonth = Math.round((monthlyTotalKg * effDetergentRate) / 1000)

    // Conventional Competitor Rate: 42 ml/kg
    const retailLitersMonth = Math.round((monthlyTotalKg * 42) / 1000)

    // Financial Analysis
    const kcaPricePerLiter = 18000
    const retailPricePerLiter = 25000
    const kcaCostMonth = kcaLitersMonth * kcaPricePerLiter
    const retailCostMonth = retailLitersMonth * retailPricePerLiter
    const monthlySavings = Math.max(0, retailCostMonth - kcaCostMonth)
    const savingsPercent = Math.round((monthlySavings / retailCostMonth) * 100)

    // Smart Packaging Advice
    const drums200 = Math.floor(kcaLitersMonth / 200)
    const remLiters = kcaLitersMonth % 200
    const jerigens20 = Math.floor(remLiters / 20)
    const jerigens5 = Math.ceil((remLiters % 20) / 5)

    let packagingAdvice = []
    if (drums200 > 0) packagingAdvice.push(`${drums200} Drum 200L`)
    if (jerigens20 > 0) packagingAdvice.push(`${jerigens20} Jerigen 20L`)
    if (jerigens5 > 0) packagingAdvice.push(`${jerigens5} Jerigen 5L`)
    if (packagingAdvice.length === 0) packagingAdvice.push('1 Jerigen 5L')

    // Calculated product volumes for the active problem
    const productVolumes = activeProblem.recommendedProducts.map((p) => {
      const pDose = (p.baseMl * hardnessFactor).toFixed(1)
      const pLitersMonth = Math.round((monthlyTotalKg * pDose) / 1000)
      return {
        ...p,
        effectiveDose: `${pDose} ml/kg`,
        monthlyLiters: pLitersMonth
      }
    })

    return {
      monthlyTotalKg,
      effDetergentRate,
      kcaLitersMonth,
      retailLitersMonth,
      kcaCostMonth,
      retailCostMonth,
      monthlySavings,
      savingsPercent,
      packagingString: packagingAdvice.join(' + '),
      productVolumes
    }
  }, [laundryKg, operatingDays, waterHardness, activeProblem])

  // Filtered Knowledge Articles
  const filteredArticles = useMemo(() => {
    if (selectedArticleFilter === 'all') return TECHNICAL_ARTICLES
    return TECHNICAL_ARTICLES.filter((a) => a.category === selectedArticleFilter)
  }, [selectedArticleFilter])

  // Format IDR Currency
  const formatRupiah = (val) => {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', maximumFractionDigits: 0 }).format(val)
  }

  // Pre-filled WhatsApp Link Generator combining diagnosis & calculation
  const getUnifiedWaLink = () => {
    const text = `Halo Tim Formulator PT Kediri Chemical Abadi, saya ingin konsultasi penanganan noda dan pemesanan kimia:
- Tantangan Noda: ${activeProblem.label} (${activeProblem.severity})
- Sektor Usaha: ${activeProblem.sector.toUpperCase()}
- Beban Cucian: ${laundryKg} kg / hari (${calculationResults.monthlyTotalKg.toLocaleString('id-ID')} kg/bulan)
- Kesadahan Air: ${waterHardness.toUpperCase()}
- Estimasi Kebutuhan Konsentrat: ${calculationResults.kcaLitersMonth} Liter / bulan
- Rekomendasi Kemasan: ${calculationResults.packagingString}
- Estimasi Penghematan: ${formatRupiah(calculationResults.monthlySavings)} / bulan (${calculationResults.savingsPercent}%)
Mohon informasi penawaran resmi (RFQ) dan sampel uji coba pabrik.`
    return `https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`
  }

  return (
    <>
      <Helmet>
        <title>Pusat Formulasi, Kalkulator Dosis & Panduan Teknis | PT Kediri Chemical Abadi</title>
        <meta 
          name="description" 
          content="Sistem terpadu diagnostik noda industri, kalkulator kebutuhan dosis massal, rekomendasi kimia bebas fosfat, dan pusat tutorial teknis standar mutu ISO 9001:2015." 
        />
      </Helmet>

      {/* ========================================================================= */}
      {/* 1. HERO HEADER: JUDUL DI PALING ATAS (TANPA TAG DI ATAS JUDUL)            */}
      {/* ========================================================================= */}
      <section className="pt-28 sm:pt-36 pb-12 sm:pb-16 bg-gradient-to-b from-white via-sky-50/20 to-white text-slate-900 relative overflow-hidden">
        
        {/* Ambient Liquid Water Caustics Texture */}
        <div className="absolute inset-0 pointer-events-none opacity-20 select-none overflow-hidden mix-blend-multiply">
          <img
            src="/images/bg_liquid_caustics_4k.png"
            alt="Caustics Texture"
            className="w-full h-full object-cover object-center"
          />
        </div>

        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-10 space-y-6">
          
          {/* Main Title is the Topmost Element (No Tag/Eyebrow Above) */}
          <div className="space-y-3 max-w-4xl">
            <h1 className="text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-slate-900 tracking-tight leading-[1.15] uppercase">
              Pusat Formulasi, Kalkulator Dosis &amp; Panduan Teknis
            </h1>

            <p className="text-slate-700 text-xs sm:text-base leading-relaxed font-normal max-w-3xl">
              Sistem pendukung keputusan terpadu untuk mendiagnosis masalah noda operasional, menghitung estimasi kebutuhan cairan kimia konsentrat murni secara presisi, serta panduan SOP pencucian standar ISO 9001:2015.
            </p>
          </div>

          {/* Clean Trust Indicators Strip (Borderless, Non-AI) */}
          <div className="flex items-center gap-4 sm:gap-6 flex-wrap pt-2 border-t border-slate-200/90 text-xs text-slate-700 font-medium">
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-[#0F58A8]" />
              <span>ISO 9001:2015 Terkalibrasi</span>
            </div>
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-emerald-600" />
              <span>100% Bebas Fosfat STPP</span>
            </div>
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-[#0F58A8]" />
              <span>Efisiensi Dosis 10–15 ml/kg</span>
            </div>
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-emerald-600" />
              <span>Ramah Biofilter IPAL RS &amp; KARS</span>
            </div>
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 2. UNIFIED WORKSPACE: DIAGNOSA NODA & KALKULATOR DOSIS TERPADU            */}
      {/* ========================================================================= */}
      <section className="py-10 sm:py-16 bg-white text-slate-900 relative">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Section Heading */}
          <div className="space-y-1.5 pb-4 border-b border-slate-200">
            <span className="text-[10.5px] sm:text-[11px] font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              DIAGNOSTIK &amp; KALKULATOR KEBUTUHAN TERPADU
            </span>
            <h2 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight uppercase">
              Konsultasi Noda &amp; Estimasi Dosis Operasional
            </h2>
          </div>

          {/* STEP 1: PILIH MASALAH NODA & PARAMETER OPERASIONAL */}
          <div className="space-y-6">
            
            {/* Sektor Filter */}
            <div className="flex items-center gap-2 overflow-x-auto pb-1">
              <span className="text-xs font-bold text-slate-500 font-heading shrink-0 mr-1">
                Filter Sektor:
              </span>
              {SECTORS_LIST.map((sec) => (
                <button
                  key={sec.id}
                  onClick={() => setSelectedSector(sec.id)}
                  className={`h-8 px-4 rounded-full text-xs font-heading font-bold uppercase tracking-wider transition-all whitespace-nowrap cursor-pointer select-none ${
                    selectedSector === sec.id
                      ? 'bg-[#0F58A8] text-white shadow-xs'
                      : 'bg-slate-100 hover:bg-slate-200 text-slate-700'
                  }`}
                >
                  {sec.label}
                </button>
              ))}
            </div>

            {/* Problem Selection Pills */}
            <div className="space-y-2">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-500 font-heading block">
                Pilih Masalah Noda / Kondisi Operasional:
              </span>

              <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5">
                {filteredProblems.map((prob) => {
                  const isSelected = selectedProblemId === prob.id

                  return (
                    <button
                      key={prob.id}
                      onClick={() => setSelectedProblemId(prob.id)}
                      className={`p-3 rounded-2xl border text-left transition-all cursor-pointer flex flex-col justify-between select-none ${
                        isSelected
                          ? 'bg-blue-50/80 border-[#0F58A8] ring-1 ring-[#0F58A8] shadow-xs'
                          : 'bg-white border-slate-200/90 hover:border-slate-300 hover:bg-slate-50/60'
                      }`}
                    >
                      <div className="space-y-1">
                        <strong className="text-xs font-bold font-heading text-slate-900 block leading-snug">
                          {prob.label}
                        </strong>
                        <span className="text-[10px] text-slate-500 block">
                          Tingkat: {prob.severity}
                        </span>
                      </div>
                      <div className="pt-2 flex items-center justify-between">
                        <span className={`text-[9px] font-mono font-bold uppercase ${isSelected ? 'text-[#0F58A8]' : 'text-slate-400'}`}>
                          {isSelected ? '✓ Terpilih' : 'Pilih'}
                        </span>
                      </div>
                    </button>
                  )
                })}
              </div>
            </div>

            {/* Interactive Calculator Inputs: Capacity & Water Hardness */}
            <div className="p-6 sm:p-7 rounded-3xl bg-slate-50/80 border border-slate-200/90 grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
              
              {/* Parameter 1: Kapasitas Cucian Harian */}
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <label className="text-xs sm:text-[13px] font-bold font-heading text-slate-900">
                    Beban Cucian Harian:
                  </label>
                  <div className="flex items-center gap-1">
                    <input
                      type="number"
                      min="20"
                      max="10000"
                      step="20"
                      value={laundryKg}
                      onChange={(e) => setLaundryKg(Math.max(1, Number(e.target.value)))}
                      className="w-20 h-8 px-2 text-right rounded-lg border border-slate-300 bg-white font-mono font-bold text-xs text-slate-900"
                    />
                    <span className="text-xs font-mono font-bold text-slate-500">kg</span>
                  </div>
                </div>

                <input
                  type="range"
                  min="50"
                  max="2000"
                  step="25"
                  value={laundryKg}
                  onChange={(e) => setLaundryKg(Number(e.target.value))}
                  className="w-full accent-[#0F58A8] cursor-pointer"
                />

                <div className="flex items-center justify-between text-[10px] font-mono text-slate-400">
                  <span>50 kg (Klinik)</span>
                  <span>500 kg (Hotel)</span>
                  <span>2.000+ kg (RSUD)</span>
                </div>
              </div>

              {/* Parameter 2: Hari Kerja per Bulan */}
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <label className="text-xs sm:text-[13px] font-bold font-heading text-slate-900">
                    Hari Operasional:
                  </label>
                  <span className="text-xs font-mono font-bold text-slate-900">
                    {operatingDays} Hari / Bulan
                  </span>
                </div>

                <div className="grid grid-cols-3 gap-2">
                  {[24, 26, 30].map((days) => (
                    <button
                      key={days}
                      onClick={() => setOperatingDays(days)}
                      className={`h-9 rounded-xl border text-xs font-heading font-bold cursor-pointer transition-all ${
                        operatingDays === days
                          ? 'bg-[#0F58A8] text-white border-[#0F58A8]'
                          : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-100'
                      }`}
                    >
                      {days} Hari
                    </button>
                  ))}
                </div>
              </div>

              {/* Parameter 3: Kesadahan Air Tanah */}
              <div className="space-y-2">
                <label className="text-xs sm:text-[13px] font-bold font-heading text-slate-900 block">
                  Kondisi Kesadahan Air Tanah:
                </label>

                <div className="grid grid-cols-3 gap-2">
                  {[
                    { id: 'normal', label: 'Normal (<150 ppm)' },
                    { id: 'medium', label: 'Sedang (250 ppm)' },
                    { id: 'hard', label: 'Sadah (>350 ppm)' }
                  ].map((h) => (
                    <button
                      key={h.id}
                      onClick={() => setWaterHardness(h.id)}
                      className={`p-2 rounded-xl border text-center text-xs font-heading font-bold cursor-pointer transition-all ${
                        waterHardness === h.id
                          ? 'bg-[#0F58A8] text-white border-[#0F58A8]'
                          : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-100'
                      }`}
                    >
                      <span className="block text-[10.5px] truncate">{h.label}</span>
                    </button>
                  ))}
                </div>
              </div>

            </div>

          </div>

          {/* STEP 2: KATALOG PRODUK REKOMENDASI DENGAN FOTO PRODUK ASLI & DOSIS TERKALKULASI */}
          <div className="space-y-6">
            
            <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-3 pb-3 border-b border-slate-200">
              <div className="space-y-1">
                <span className="text-xs font-bold uppercase tracking-wider text-[#0F58A8] font-heading block">
                  KATALOG FORMULASI TERPILIH UNTUK: {activeProblem.label.toUpperCase()}
                </span>
                <h3 className="text-lg sm:text-xl font-black font-heading text-slate-900">
                  Rekomendasi Produk &amp; Estimasi Kebutuhan Bulanan Anda
                </h3>
              </div>

              <div className="text-xs text-slate-500 font-mono">
                Beban: <strong className="text-slate-900">{calculationResults.monthlyTotalKg.toLocaleString('id-ID')} kg/bulan</strong>
              </div>
            </div>

            {/* Product Catalog Cards Grid (Pure Floating Product Images) */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {calculationResults.productVolumes.map((prod, idx) => (
                <div
                  key={idx}
                  className="bg-white border border-slate-200/90 rounded-3xl p-5 shadow-sm hover:shadow-lg transition-all duration-300 flex flex-col justify-between group space-y-4"
                >
                  <div className="space-y-3">
                    
                    {/* Top Row: SKU & Role Badge */}
                    <div className="flex items-center justify-between gap-2 pb-2 border-b border-slate-100">
                      <span className="text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full bg-blue-50 text-[#0F58A8] border border-blue-100">
                        {prod.sku}
                      </span>
                      <span className="text-[10px] font-medium text-slate-500 truncate max-w-[120px]">
                        {prod.packaging}
                      </span>
                    </div>

                    {/* Pure 3D Product Image (No Box, Pure Floating Silhouette) */}
                    <div className="w-full h-40 sm:h-44 flex items-center justify-center overflow-hidden py-1 group-hover:scale-105 transition-transform duration-500">
                      <img
                        src={prod.image}
                        alt={prod.name}
                        className="w-full h-full object-contain select-none mix-blend-multiply"
                        loading="lazy"
                      />
                    </div>

                    {/* Product Name & Chemical Function */}
                    <div className="space-y-1">
                      <h4 className="font-heading font-extrabold text-sm sm:text-[15px] text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug">
                        {prod.name}
                      </h4>
                      <p className="text-[11px] text-slate-600 font-normal leading-relaxed line-clamp-2">
                        {prod.role}
                      </p>
                    </div>

                    {/* Calculated Need Metric Panel */}
                    <div className="p-3 rounded-xl bg-slate-50 border border-slate-200/80 space-y-1 text-xs">
                      <div className="flex items-center justify-between">
                        <span className="text-[10px] text-slate-500 uppercase font-bold">Dosis:</span>
                        <strong className="text-slate-900 font-heading font-bold">{prod.effectiveDose}</strong>
                      </div>
                      <div className="flex items-center justify-between pt-1 border-t border-slate-200/70 text-[#0F58A8]">
                        <span className="text-[10px] uppercase font-bold">Kebutuhan Anda:</span>
                        <strong className="font-mono font-black text-xs sm:text-sm">
                          ~{prod.monthlyLiters} Liter / bln
                        </strong>
                      </div>
                    </div>

                  </div>
                </div>
              ))}
            </div>

            {/* SOP Washing Steps & Financial ROI Summary */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start pt-4">
              
              {/* SOP Steps (7 Kolom) */}
              <div className="lg:col-span-7 space-y-3">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-900 font-heading flex items-center gap-2">
                  <Clock className="w-4 h-4 text-[#0F58A8]" />
                  <span>Alur Standar Operasional Prosedur (SOP Pencucian Optimal):</span>
                </span>

                <div className="space-y-2">
                  {activeProblem.sopSteps.map((step) => (
                    <div key={step.step} className="p-3.5 rounded-2xl bg-slate-50/90 border border-slate-200/80 flex items-start gap-3 text-xs">
                      <div className="w-6 h-6 rounded-full bg-[#0F58A8] text-white flex items-center justify-center font-bold text-xs shrink-0 font-mono mt-0.5">
                        {step.step}
                      </div>
                      <div className="space-y-0.5 flex-1 min-w-0">
                        <div className="flex items-center justify-between gap-2 flex-wrap">
                          <strong className="font-heading font-bold text-slate-900 text-xs">
                            {step.name}
                          </strong>
                          <div className="flex items-center gap-2 text-[10px] font-mono text-slate-500">
                            <span className="bg-white px-2 py-0.5 rounded border border-slate-200">{step.temp}</span>
                            <span className="bg-white px-2 py-0.5 rounded border border-slate-200">{step.time}</span>
                          </div>
                        </div>
                        <p className="text-[11.5px] text-slate-600 font-normal leading-relaxed">
                          {step.note}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Financial ROI & WhatsApp Consultation (5 Kolom) */}
              <div className="lg:col-span-5 bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-7 space-y-5 shadow-lg shadow-blue-900/5">
                <div className="space-y-1 border-b border-slate-200 pb-3">
                  <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 inline-block">
                    ANALISIS PENGHEMATAN BIAYA (ROI)
                  </span>
                  <h4 className="text-base sm:text-lg font-black font-heading text-slate-900">
                    Ringkasan Pasokan &amp; Penghematan
                  </h4>
                </div>

                {/* Packaging & Volume Box */}
                <div className="p-3.5 rounded-2xl bg-slate-50 border border-slate-200/80 flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl bg-white border border-slate-200 flex items-center justify-center shrink-0 shadow-2xs">
                    <Package className="w-5 h-5 text-[#0F58A8]" />
                  </div>
                  <div className="space-y-0.5 min-w-0 flex-1 text-xs">
                    <span className="text-[10px] font-mono font-bold uppercase text-slate-500 block">
                      Rekomendasi Kemasan Pabrik:
                    </span>
                    <strong className="text-slate-900 font-heading font-bold block truncate">
                      {calculationResults.packagingString}
                    </strong>
                  </div>
                </div>

                {/* Cost Comparison */}
                <div className="space-y-2 text-xs">
                  <div className="flex items-center justify-between pb-1 border-b border-slate-100 text-slate-600">
                    <span>Biaya Deterjen Biasa ({calculationResults.retailLitersMonth}L):</span>
                    <span className="font-mono font-bold text-slate-800">{formatRupiah(calculationResults.retailCostMonth)}</span>
                  </div>
                  <div className="flex items-center justify-between pb-1 border-b border-slate-100 text-[#0F58A8]">
                    <span className="font-bold">Biaya Konsentrat KCA ({calculationResults.kcaLitersMonth}L):</span>
                    <span className="font-mono font-extrabold">{formatRupiah(calculationResults.kcaCostMonth)}</span>
                  </div>
                  <div className="flex items-center justify-between pt-1 text-emerald-700 bg-emerald-50/70 p-2.5 rounded-xl border border-emerald-200">
                    <strong className="font-heading font-bold text-xs">Potensi Penghematan:</strong>
                    <strong className="font-mono font-black text-sm">
                      {formatRupiah(calculationResults.monthlySavings)} / bln ({calculationResults.savingsPercent}%)
                    </strong>
                  </div>
                </div>

                {/* WhatsApp Action Button */}
                <a
                  href={getUnifiedWaLink()}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full h-11 rounded-full bg-[#0F58A8] hover:bg-blue-800 text-white font-heading font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 cursor-pointer shadow-sm"
                >
                  <Phone className="w-4 h-4" />
                  <span>Kirim Hasil Konsultasi &amp; Dosis via WhatsApp</span>
                </a>
              </div>

            </div>

          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. BOTTOM SECTION: PUSAT EDUKASI & BLOG TUTORIAL TEKNIS                   */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-slate-50/60 text-slate-900 border-t border-slate-200/90">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-10">
          
          <div className="space-y-2 border-b border-slate-200 pb-5">
            <span className="text-[10.5px] sm:text-[11px] font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              PUSAT EDUKASI, ARTIKEL &amp; TUTORIAL TEKNIS
            </span>
            <h2 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight uppercase">
              Panduan Ilmiah &amp; SOP Standar Manufaktur Kimia
            </h2>
            <p className="text-xs sm:text-sm text-slate-600 max-w-2xl font-normal leading-relaxed">
              Wawasan lapangan, panduan kepatuhan KARS rumah sakit, formulasi air sadah, dan analisis akuntansi biaya yang disusun oleh praktisi dan formulator PT Kediri Chemical Abadi.
            </p>
          </div>

          {/* Category Filter Pills */}
          <div className="flex items-center gap-2 overflow-x-auto pb-1">
            <span className="text-xs font-bold text-slate-500 font-heading shrink-0 mr-1">
              Topik Pembahasan:
            </span>
            {[
              { id: 'all', label: 'Semua Artikel' },
              { id: 'SOP Medis & KARS', label: 'SOP Medis KARS' },
              { id: 'Teknik Kimia Lapangan', label: 'Teknik Air Sadah' },
              { id: 'Formulasi Noda Berat', label: 'Matriks Noda' },
              { id: 'Akuntansi Biaya Laundry', label: 'Akuntansi Dosis' },
              { id: 'Standar Mutu Lingkungan', label: 'Kepatuhan IPAL' },
            ].map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedArticleFilter(cat.id)}
                className={`h-8 px-3.5 rounded-full text-xs font-heading font-bold uppercase tracking-wider transition-all whitespace-nowrap cursor-pointer ${
                  selectedArticleFilter === cat.id
                    ? 'bg-[#0F58A8] text-white shadow-xs'
                    : 'bg-white hover:bg-slate-200 text-slate-700 border border-slate-200'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>

          {/* Articles Grid (Clean 3-Columns) */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredArticles.map((art) => (
              <div
                key={art.id}
                className="bg-white border border-slate-200/90 rounded-3xl p-6 shadow-sm hover:shadow-lg transition-all duration-300 flex flex-col justify-between group space-y-5"
              >
                <div className="space-y-3.5">
                  <div className="flex items-center justify-between gap-2">
                    <span className={`text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full border ${art.categoryColor}`}>
                      {art.category}
                    </span>
                    <span className="text-[10.5px] font-mono text-slate-400">
                      {art.readTime}
                    </span>
                  </div>

                  <h3 className="text-base sm:text-lg font-black font-heading text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug">
                    {art.title}
                  </h3>

                  <p className="text-xs text-slate-600 font-normal leading-relaxed line-clamp-3">
                    {art.summary}
                  </p>

                  <div className="space-y-1.5 pt-2 border-t border-slate-100">
                    {art.keyPoints.slice(0, 3).map((kp, kIdx) => (
                      <div key={kIdx} className="flex items-start gap-2 text-[11px] text-slate-700 font-medium">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                        <span className="line-clamp-1">{kp}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="pt-3 border-t border-slate-100 flex items-center justify-between">
                  <span className="text-[11px] text-slate-500 font-medium">
                    Oleh: {art.author.split(' ')[0]}
                  </span>
                  <button
                    onClick={() => setReadingArticle(art)}
                    className="text-xs font-bold font-heading text-[#0F58A8] uppercase tracking-wider hover:underline inline-flex items-center gap-1 cursor-pointer"
                  >
                    <span>Baca Panduan</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))}
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 4. ARTICLE READING MODAL                                                  */}
      {/* ========================================================================= */}
      <AnimatePresence>
        {readingArticle && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-slate-950/60 backdrop-blur-sm">
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 10 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 10 }}
              className="bg-white rounded-3xl max-w-3xl w-full max-h-[90vh] overflow-hidden flex flex-col shadow-2xl border border-slate-200"
            >
              {/* Modal Header */}
              <div className="p-6 border-b border-slate-200 flex items-start justify-between gap-4 bg-slate-50/70">
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <span className={`text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full border ${readingArticle.categoryColor}`}>
                      {readingArticle.category}
                    </span>
                    <span className="text-[11px] font-mono text-slate-400">
                      {readingArticle.readTime}
                    </span>
                  </div>
                  <h3 className="text-base sm:text-xl font-black font-heading text-slate-900 leading-snug">
                    {readingArticle.title}
                  </h3>
                </div>

                <button
                  onClick={() => setReadingArticle(null)}
                  className="w-8 h-8 rounded-full bg-slate-200 hover:bg-slate-300 text-slate-700 flex items-center justify-center shrink-0 cursor-pointer transition-colors"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>

              {/* Modal Scrollable Body */}
              <div className="p-6 sm:p-8 overflow-y-auto space-y-5 text-slate-800 text-xs sm:text-sm leading-relaxed font-normal whitespace-pre-line">
                {readingArticle.fullContent}
              </div>

              {/* Modal Footer */}
              <div className="p-4 sm:p-6 border-t border-slate-200 bg-slate-50/70 flex items-center justify-between gap-3 text-xs">
                <span className="text-slate-500">
                  PT Kediri Chemical Abadi • Standar Mutu ISO 9001:2015
                </span>
                <button
                  onClick={() => setReadingArticle(null)}
                  className="h-9 px-5 rounded-full bg-[#0F58A8] text-white font-heading font-bold text-xs uppercase tracking-wider cursor-pointer"
                >
                  Tutup Panduan
                </button>
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>

      {/* ========================================================================= */}
      {/* 5. SIGNATURE S-CURVE WAVE TRANSITION (Seamless into Dark Navy Footer)     */}
      {/* ========================================================================= */}
      <div className="w-full overflow-hidden leading-none bg-slate-50/60 select-none pointer-events-none -mb-[1px]">
        <svg
          viewBox="0 0 1440 120"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="w-full h-12 sm:h-20 lg:h-24 block"
          preserveAspectRatio="none"
        >
          <path
            d="M0,32L60,42.7C120,53,240,75,360,74.7C480,75,600,53,720,48C840,43,960,53,1080,64C1200,75,1320,85,1380,90.7L1440,96L1440,120L1380,120C1320,120,1200,120,1080,120C960,120,840,120,720,120C600,120,480,120,360,120C240,120,120,120,60,120L0,120Z"
            fill="#0A192F"
          />
        </svg>
      </div>
    </>
  )
}
'''

with open('src/pages/CalculatorPage.jsx', 'w', encoding='utf-8') as f:
    f.write(calculator_page_code)

print('Updated src/pages/CalculatorPage.jsx successfully!')
