import { useState, useMemo } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Helmet } from 'react-helmet-async'
import { 
  Calculator, 
  Search, 
  BookOpen, 
  CheckCircle2, 
  ArrowRight, 
  Phone, 
  RotateCcw, 
  Sparkles, 
  Layers, 
  ShieldCheck, 
  AlertCircle, 
  Package, 
  X,
  Droplets,
  Wrench,
  Clock,
  Building2,
  FileText,
  SlidersHorizontal,
  ChevronRight
} from 'lucide-react'

import { 
  STAIN_PROBLEMS, 
  SECTORS_LIST, 
  CALCULATOR_PRESETS, 
  TECHNICAL_ARTICLES 
} from '@/data/consultationData'

export default function CalculatorPage() {
  // Navigation & Primary Tabs
  const [activeMainTab, setActiveMainTab] = useState('diagnostics') // 'diagnostics' | 'calculator' | 'knowledge'

  // PANEL 1: Diagnostics & Formulation Recommender State
  const [selectedSector, setSelectedSector] = useState('all')
  const [selectedProblemId, setSelectedProblemId] = useState(STAIN_PROBLEMS[0].id)

  // PANEL 2: Industrial Dosage & Cost Calculator State
  const [selectedPresetId, setSelectedPresetId] = useState(CALCULATOR_PRESETS[0].id)
  const [laundryKg, setLaundryKg] = useState(350)
  const [operatingDays, setOperatingDays] = useState(30)
  const [waterHardness, setWaterHardness] = useState('medium') // 'normal' | 'medium' | 'hard'

  // PANEL 3: Knowledge Base & Tutorial Blog State
  const [selectedArticleFilter, setSelectedArticleFilter] = useState('all')
  const [readingArticle, setReadingArticle] = useState(null)

  const waNumber = '6285235889758'

  // Filtered Stain Problems
  const filteredProblems = useMemo(() => {
    if (selectedSector === 'all') return STAIN_PROBLEMS
    return STAIN_PROBLEMS.filter((p) => p.sector === selectedSector)
  }, [selectedSector])

  // Active Problem Object
  const activeProblem = useMemo(() => {
    return STAIN_PROBLEMS.find((p) => p.id === selectedProblemId) || STAIN_PROBLEMS[0]
  }, [selectedProblemId])

  // Active Preset Object
  const activePreset = useMemo(() => {
    return CALCULATOR_PRESETS.find((p) => p.id === selectedPresetId) || CALCULATOR_PRESETS[0]
  }, [selectedPresetId])

  // Handle preset change
  const handlePresetSelect = (preset) => {
    setSelectedPresetId(preset.id)
    setLaundryKg(preset.defaultKg)
  }

  // Dosage & Cost Calculation Engine
  const calculationResults = useMemo(() => {
    const hardnessFactor = waterHardness === 'hard' ? 1.2 : waterHardness === 'medium' ? 1.08 : 1.0
    const effKcaRate = (activePreset.kcaRate * hardnessFactor).toFixed(1)
    
    // Monthly Volume (Liters)
    const monthlyTotalKg = laundryKg * operatingDays
    const kcaLitersMonth = Math.round((monthlyTotalKg * effKcaRate) / 1000)
    const retailLitersMonth = Math.round((monthlyTotalKg * activePreset.retailRate) / 1000)
    
    // Financial Cost (IDR)
    const kcaCostMonth = kcaLitersMonth * activePreset.kcaPrice
    const retailCostMonth = retailLitersMonth * activePreset.retailPrice
    const monthlySavings = Math.max(0, retailCostMonth - kcaCostMonth)
    const savingsPercent = Math.round((monthlySavings / retailCostMonth) * 100)

    // Packaging Distribution Recommendation
    let drums200 = Math.floor(kcaLitersMonth / 200)
    let remLiters = kcaLitersMonth % 200
    let jerigens20 = Math.floor(remLiters / 20)
    let jerigens5 = Math.ceil((remLiters % 20) / 5)

    let packagingAdvice = []
    if (drums200 > 0) packagingAdvice.push(`${drums200} Drum 200L`)
    if (jerigens20 > 0) packagingAdvice.push(`${jerigens20} Jerigen 20L`)
    if (jerigens5 > 0) packagingAdvice.push(`${jerigens5} Jerigen 5L`)
    if (packagingAdvice.length === 0) packagingAdvice.push('1 Jerigen 5L')

    return {
      monthlyTotalKg,
      effKcaRate,
      kcaLitersMonth,
      retailLitersMonth,
      kcaCostMonth,
      retailCostMonth,
      monthlySavings,
      savingsPercent,
      packagingString: packagingAdvice.join(' + ')
    }
  }, [laundryKg, operatingDays, waterHardness, activePreset])

  // Filtered Knowledge Articles
  const filteredArticles = useMemo(() => {
    if (selectedArticleFilter === 'all') return TECHNICAL_ARTICLES
    return TECHNICAL_ARTICLES.filter((a) => a.category === selectedArticleFilter)
  }, [selectedArticleFilter])

  // Format IDR Currency
  const formatRupiah = (val) => {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', maximumFractionDigits: 0 }).format(val)
  }

  // Pre-filled WhatsApp Link Generator for Consultation
  const getConsultationWaLink = () => {
    const text = `Halo Tim Formulator PT Kediri Chemical Abadi, saya ingin konsultasi penanganan noda industri:
- Noda: ${activeProblem.label}
- Sektor: ${activeProblem.sector.toUpperCase()}
- Tingkat Noda: ${activeProblem.severity}
Mohon rekomendasi formulasi dan dosis yang tepat untuk operasional kami.`
    return `https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`
  }

  // Pre-filled WhatsApp Link Generator for Calculation Results
  const getCalculationWaLink = () => {
    const text = `Halo Tim Formulator PT Kediri Chemical Abadi, saya telah melakukan kalkulasi kebutuhan kimia:
- Jenis Usaha: ${activePreset.name}
- Kapasitas: ${laundryKg} kg / hari (${calculationResults.monthlyTotalKg.toLocaleString('id-ID')} kg/bulan)
- Kesadahan Air: ${waterHardness.toUpperCase()}
- Estimasi Konsentrat KCA: ${calculationResults.kcaLitersMonth} Liter / bulan
- Rekomendasi Kemasan: ${calculationResults.packagingString}
- Estimasi Penghematan Biaya: ${formatRupiah(calculationResults.monthlySavings)} / bulan (${calculationResults.savingsPercent}%)
Mohon penawaran resmi (RFQ) dan sampel uji coba.`
    return `https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`
  }

  return (
    <>
      <Helmet>
        <title>Pusat Konsultasi Formulasi & Kalkulator Dosis Kimia Industri | PT Kediri Chemical Abadi</title>
        <meta 
          name="description" 
          content="Sistem kalkulator kebutuhan kimia industri, diagnostik noda membandel, rekomendasi formula bebas fosfat, dan pusat panduan SOP pencucian standar ISO 9001:2015." 
        />
      </Helmet>

      {/* ========================================================================= */}
      {/* 1. HERO HEADER: CLEAN EDITORIAL & QUICK JUMP TABS                         */}
      {/* ========================================================================= */}
      <section className="pt-28 sm:pt-36 pb-14 sm:pb-20 bg-gradient-to-b from-slate-50 via-white to-sky-50/20 text-slate-900 relative overflow-hidden">
        
        {/* Ambient Liquid Water Caustics Texture */}
        <div className="absolute inset-0 pointer-events-none opacity-20 select-none overflow-hidden mix-blend-multiply">
          <img
            src="/images/bg_liquid_caustics_4k.png"
            alt="Caustics Texture"
            className="w-full h-full object-cover object-center"
          />
        </div>

        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full relative z-10 space-y-8">
          
          <div className="max-w-4xl space-y-3.5">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-[#0F58A8] text-xs font-mono font-bold uppercase tracking-wider">
              <Sparkles className="w-3.5 h-3.5" />
              <span>SISTEM KONSULTASI &amp; PERHITUNGAN TEKNIS TERPADU</span>
            </div>

            <h1 className="text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-slate-900 tracking-tight leading-[1.15] uppercase">
              Pusat Konsultasi Formulasi, Kalkulator Dosis &amp; Panduan Teknis
            </h1>

            <p className="text-slate-700 text-xs sm:text-base leading-relaxed font-normal max-w-3xl">
              Sistem pendukung keputusan terpadu untuk mendiagnosis masalah noda operasional, menghitung estimasi kebutuhan cairan kimia konsentrat murni, menganalisis efisiensi biaya (*Cost-in-Use*), serta panduan SOP pencucian standar industri ISO 9001:2015.
            </p>
          </div>

          {/* Quick Jump Navigation Pill Tabs */}
          <div className="flex items-center gap-2 sm:gap-3 flex-wrap pt-2">
            <button
              onClick={() => setActiveMainTab('diagnostics')}
              className={`h-11 px-5 rounded-full font-heading font-bold text-xs sm:text-sm tracking-wide transition-all inline-flex items-center gap-2.5 cursor-pointer shadow-xs ${
                activeMainTab === 'diagnostics'
                  ? 'bg-[#0F58A8] text-white shadow-md shadow-blue-900/15'
                  : 'bg-white hover:bg-slate-100 text-slate-700 border border-slate-200/90'
              }`}
            >
              <Search className="w-4 h-4" />
              <span>1. Diagnostik Noda &amp; Formulasi</span>
            </button>

            <button
              onClick={() => setActiveMainTab('calculator')}
              className={`h-11 px-5 rounded-full font-heading font-bold text-xs sm:text-sm tracking-wide transition-all inline-flex items-center gap-2.5 cursor-pointer shadow-xs ${
                activeMainTab === 'calculator'
                  ? 'bg-[#0F58A8] text-white shadow-md shadow-blue-900/15'
                  : 'bg-white hover:bg-slate-100 text-slate-700 border border-slate-200/90'
              }`}
            >
              <Calculator className="w-4 h-4" />
              <span>2. Kalkulator Kebutuhan Dosis &amp; Biaya</span>
            </button>

            <button
              onClick={() => setActiveMainTab('knowledge')}
              className={`h-11 px-5 rounded-full font-heading font-bold text-xs sm:text-sm tracking-wide transition-all inline-flex items-center gap-2.5 cursor-pointer shadow-xs ${
                activeMainTab === 'knowledge'
                  ? 'bg-[#0F58A8] text-white shadow-md shadow-blue-900/15'
                  : 'bg-white hover:bg-slate-100 text-slate-700 border border-slate-200/90'
              }`}
            >
              <BookOpen className="w-4 h-4" />
              <span>3. Pusat SOP &amp; Tutorial (Blog Teknis)</span>
            </button>
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 2. PANEL 1: DIAGNOSTIK NODA & REKOMENDASI KIMIA (FORMULATION RECOMMENDER) */}
      {/* ========================================================================= */}
      {activeMainTab === 'diagnostics' && (
        <section className="py-12 sm:py-16 bg-white text-slate-900">
          <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-10">
            
            <div className="space-y-2 border-b border-slate-200 pb-5">
              <span className="text-xs font-bold uppercase tracking-widest text-[#0F58A8] font-heading block">
                MODUL KONSULTASI INTERAKTIF
              </span>
              <h2 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight uppercase">
                Diagnostik Masalah Noda &amp; Rekomendasi Kombinasi Kimia
              </h2>
              <p className="text-xs sm:text-sm text-slate-600 max-w-2xl font-normal leading-relaxed">
                Pilih tantangan noda atau kondisi air yang Anda hadapi di lapangan. Sistem formulator kami akan langsung menyusun kombinasi kimia (*chemical stacking*) beserta SOP langkah pencucian optimal.
              </p>
            </div>

            {/* Sektor Filter Pills */}
            <div className="flex items-center gap-2 overflow-x-auto pb-2">
              <span className="text-xs font-bold text-slate-500 font-heading shrink-0 mr-1">
                Filter Sektor:
              </span>
              {SECTORS_LIST.map((sec) => (
                <button
                  key={sec.id}
                  onClick={() => setSelectedSector(sec.id)}
                  className={`h-8 px-3.5 rounded-full text-xs font-bold font-heading uppercase tracking-wider transition-all whitespace-nowrap cursor-pointer ${
                    selectedSector === sec.id
                      ? 'bg-[#0F58A8] text-white shadow-xs'
                      : 'bg-slate-100 hover:bg-slate-200 text-slate-700'
                  }`}
                >
                  {sec.label}
                </button>
              ))}
            </div>

            {/* Main Interactive Grid: Problem Checklist (Left) & Live Formulation Recommendation (Right) */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start">
              
              {/* Sisi Kiri: Daftar Checklist Noda (5 Kolom) */}
              <div className="lg:col-span-5 space-y-3">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-500 font-heading block">
                  Pilih Masalah Operasional:
                </span>

                <div className="space-y-2.5">
                  {filteredProblems.map((prob) => {
                    const isSelected = selectedProblemId === prob.id

                    return (
                      <button
                        key={prob.id}
                        onClick={() => setSelectedProblemId(prob.id)}
                        className={`w-full text-left p-4 rounded-2xl border transition-all duration-200 cursor-pointer flex items-start gap-3.5 ${
                          isSelected
                            ? 'bg-blue-50/70 border-[#0F58A8] shadow-sm ring-1 ring-[#0F58A8]'
                            : 'bg-white border-slate-200/90 hover:border-slate-300 hover:bg-slate-50/60'
                        }`}
                      >
                        <div className={`w-9 h-9 rounded-xl flex items-center justify-center shrink-0 ${
                          isSelected ? 'bg-[#0F58A8] text-white' : 'bg-slate-100 text-slate-600'
                        }`}>
                          <Droplets className="w-4 h-4" />
                        </div>

                        <div className="space-y-1 flex-1 min-w-0">
                          <div className="flex items-center justify-between gap-2">
                            <strong className="text-xs sm:text-[13.5px] font-bold font-heading text-slate-900 block truncate">
                              {prob.label}
                            </strong>
                            <span className="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-white border border-slate-200 text-slate-600 shrink-0">
                              {prob.severity}
                            </span>
                          </div>
                          <p className="text-[11px] text-slate-600 line-clamp-2 font-normal leading-relaxed">
                            {prob.desc}
                          </p>
                        </div>
                      </button>
                    )
                  })}
                </div>
              </div>

              {/* Sisi Kanan: Panel Solusi & Chemical Stacking Live (7 Kolom) */}
              <div className="lg:col-span-7 bg-slate-50/70 border border-slate-200/90 rounded-3xl p-6 sm:p-8 space-y-7">
                
                {/* Header Masalah Terpilih */}
                <div className="space-y-2 border-b border-slate-200 pb-5">
                  <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-blue-100/70 text-[#0F58A8] text-[10px] font-mono font-bold uppercase">
                    ANALISIS REKOMENDASI FORMULATOR KCA
                  </div>
                  <h3 className="text-lg sm:text-xl lg:text-2xl font-black font-heading text-slate-900">
                    Solusi Terpadu: {activeProblem.label}
                  </h3>
                  <p className="text-xs sm:text-[13px] text-slate-600 font-normal leading-relaxed">
                    {activeProblem.desc}
                  </p>
                </div>

                {/* 1. Paket Kombinasi Kimia (Chemical Stacking) */}
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold uppercase tracking-wider text-slate-900 font-heading flex items-center gap-2">
                      <Layers className="w-4 h-4 text-[#0F58A8]" />
                      <span>Rekomendasi Kombinasi Kimia (Chemical Stacking):</span>
                    </span>
                    <span className="text-[11px] font-mono text-slate-500">
                      {activeProblem.recommendedProducts.length} Produk Sinergis
                    </span>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {activeProblem.recommendedProducts.map((prod, pIdx) => (
                      <div key={pIdx} className="p-4 rounded-2xl bg-white border border-slate-200/90 shadow-2xs space-y-1.5">
                        <div className="flex items-center justify-between gap-1">
                          <strong className="text-xs font-bold font-heading text-slate-900 block truncate">
                            {prod.name}
                          </strong>
                          <span className="text-[9.5px] font-mono font-bold text-[#0F58A8] bg-blue-50 px-2 py-0.5 rounded border border-blue-100 shrink-0">
                            {prod.sku}
                          </span>
                        </div>
                        <p className="text-[11px] text-slate-600 font-normal leading-relaxed">
                          {prod.role}
                        </p>
                        <div className="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[11px]">
                          <span className="text-slate-500 font-medium">Dosis Rekomendasi:</span>
                          <strong className="text-slate-900 font-heading font-bold">{prod.dose}</strong>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* 2. Alur SOP Langkah Pencucian */}
                <div className="space-y-3">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-900 font-heading flex items-center gap-2">
                    <Clock className="w-4 h-4 text-emerald-600" />
                    <span>Tahapan Standar Operasional Prosedur (SOP):</span>
                  </span>

                  <div className="space-y-2.5">
                    {activeProblem.sopSteps.map((step) => (
                      <div key={step.step} className="p-3.5 rounded-xl bg-white border border-slate-200/80 flex items-start gap-3 text-xs">
                        <div className="w-6 h-6 rounded-full bg-[#0F58A8] text-white flex items-center justify-center font-bold text-xs shrink-0 font-mono mt-0.5">
                          {step.step}
                        </div>
                        <div className="space-y-1 flex-1 min-w-0">
                          <div className="flex items-center justify-between gap-2 flex-wrap">
                            <strong className="font-heading font-bold text-slate-900 text-xs">
                              {step.name}
                            </strong>
                            <div className="flex items-center gap-2 text-[10px] font-mono text-slate-500">
                              <span className="bg-slate-100 px-2 py-0.5 rounded">{step.temp}</span>
                              <span className="bg-slate-100 px-2 py-0.5 rounded">{step.time}</span>
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

                {/* Action Buttons */}
                <div className="pt-2 flex flex-col sm:flex-row items-center gap-3">
                  <button
                    onClick={() => {
                      setActiveMainTab('calculator')
                      window.scrollTo({ top: 300, behavior: 'smooth' })
                    }}
                    className="w-full sm:flex-1 h-11 px-5 rounded-full bg-[#0F58A8] hover:bg-blue-800 text-white font-heading font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 cursor-pointer shadow-sm"
                  >
                    <Calculator className="w-4 h-4" />
                    <span>Hitung Kebutuhan di Kalkulator</span>
                  </button>

                  <a
                    href={getConsultationWaLink()}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="w-full sm:w-auto h-11 px-6 rounded-full bg-emerald-600 hover:bg-emerald-700 text-white font-heading font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 cursor-pointer shadow-sm"
                  >
                    <Phone className="w-4 h-4" />
                    <span>Konsultasi WhatsApp</span>
                  </a>
                </div>

              </div>

            </div>

          </div>
        </section>
      )}

      {/* ========================================================================= */}
      {/* 3. PANEL 2: INDUSTRIAL DOSAGE & COST CALCULATOR                           */}
      {/* ========================================================================= */}
      {activeMainTab === 'calculator' && (
        <section className="py-12 sm:py-16 bg-white text-slate-900">
          <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-10">
            
            <div className="space-y-2 border-b border-slate-200 pb-5">
              <span className="text-xs font-bold uppercase tracking-widest text-[#0F58A8] font-heading block">
                KALKULATOR AKUNTANSI BIAYA KIMIA
              </span>
              <h2 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight uppercase">
                Kalkulator Kebutuhan Dosis &amp; Simulasi Penghematan Operasional
              </h2>
              <p className="text-xs sm:text-sm text-slate-600 max-w-2xl font-normal leading-relaxed">
                Kalkulasikan total volume cairan kimia yang dibutuhkan fasilitas Anda per bulan berdasarkan kapasitas beban cucian aktual, serta buktikan penghematan anggaran belanja kimia hingga 40%.
              </p>
            </div>

            {/* Quick Presets for Business Type */}
            <div className="space-y-2">
              <span className="text-xs font-bold text-slate-500 font-heading uppercase tracking-wider block">
                Pilih Profil Operasional Fasilitas:
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
                {CALCULATOR_PRESETS.map((preset) => {
                  const isSelected = selectedPresetId === preset.id

                  return (
                    <button
                      key={preset.id}
                      onClick={() => handlePresetSelect(preset)}
                      className={`p-4 rounded-2xl border text-left transition-all cursor-pointer ${
                        isSelected
                          ? 'bg-blue-50/70 border-[#0F58A8] ring-1 ring-[#0F58A8] shadow-xs'
                          : 'bg-white border-slate-200/90 hover:bg-slate-50'
                      }`}
                    >
                      <strong className="text-xs sm:text-[13px] font-bold font-heading text-slate-900 block truncate">
                        {preset.name}
                      </strong>
                      <span className="text-[11px] text-slate-500 block mt-1">
                        Dosis KCA: {preset.kcaRate} ml/kg • Retail: {preset.retailRate} ml/kg
                      </span>
                    </button>
                  )
                })}
              </div>
            </div>

            {/* Calculator Grid: Inputs (Left) & Realtime Summary (Right) */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
              
              {/* Sisi Kiri: Slider & Parameter Input (6 Kolom) */}
              <div className="lg:col-span-6 bg-slate-50/70 border border-slate-200/90 rounded-3xl p-6 sm:p-8 space-y-6">
                
                <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-900 font-heading flex items-center gap-2">
                    <SlidersHorizontal className="w-4 h-4 text-[#0F58A8]" />
                    <span>Parameter Operasional</span>
                  </span>
                  <span className="text-xs font-mono font-bold text-[#0F58A8]">
                    ISO 9001 Terkalibrasi
                  </span>
                </div>

                {/* 1. Beban Cucian Harian (kg) */}
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <label className="text-xs sm:text-[13px] font-bold font-heading text-slate-800">
                      Beban Cucian Harian (kg / hari):
                    </label>
                    <div className="flex items-center gap-1.5">
                      <input
                        type="number"
                        min="10"
                        max="10000"
                        step="10"
                        value={laundryKg}
                        onChange={(e) => setLaundryKg(Math.max(1, Number(e.target.value)))}
                        className="w-24 h-9 px-2 text-right rounded-lg border border-slate-300 bg-white font-mono font-bold text-sm text-slate-900 focus:outline-none focus:border-[#0F58A8]"
                      />
                      <span className="text-xs font-mono font-bold text-slate-500">kg</span>
                    </div>
                  </div>

                  <input
                    type="range"
                    min="50"
                    max="3000"
                    step="25"
                    value={laundryKg}
                    onChange={(e) => setLaundryKg(Number(e.target.value))}
                    className="w-full accent-[#0F58A8] cursor-pointer"
                  />

                  <div className="flex items-center justify-between text-[10px] font-mono text-slate-400">
                    <span>50 kg/hari (Klinik / Kost)</span>
                    <span>1.000 kg/hari (Hotel)</span>
                    <span>3.000+ kg (RSUD)</span>
                  </div>
                </div>

                {/* 2. Jumlah Hari Kerja per Bulan */}
                <div className="space-y-2">
                  <div className="flex items-center justify-between">
                    <label className="text-xs sm:text-[13px] font-bold font-heading text-slate-800">
                      Hari Operasional per Bulan:
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
                            : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
                        }`}
                      >
                        {days} Hari
                      </button>
                    ))}
                  </div>
                </div>

                {/* 3. Tingkat Kesadahan Air Tanah */}
                <div className="space-y-2">
                  <label className="text-xs sm:text-[13px] font-bold font-heading text-slate-800 block">
                    Kondisi Kesadahan Air Tanah (Hardness):
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
                        className={`p-2.5 rounded-xl border text-center text-xs font-heading font-bold cursor-pointer transition-all ${
                          waterHardness === h.id
                            ? 'bg-[#0F58A8] text-white border-[#0F58A8]'
                            : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
                        }`}
                      >
                        <span className="block text-[11px] truncate">{h.label}</span>
                      </button>
                    ))}
                  </div>
                </div>

              </div>

              {/* Sisi Kanan: Output Kalkulasi & Simulasi Penghematan (6 Kolom) */}
              <div className="lg:col-span-6 bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 space-y-6 shadow-lg shadow-blue-900/5">
                
                <div className="space-y-1 border-b border-slate-200 pb-4">
                  <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200 inline-block">
                    HASIL ANALISIS KEBUTUHAN &amp; COST-IN-USE
                  </span>
                  <h3 className="text-lg sm:text-xl font-black font-heading text-slate-900">
                    Estimasi Pasokan Kimia Bulanan
                  </h3>
                </div>

                {/* Stat Box Grid */}
                <div className="grid grid-cols-2 gap-3.5">
                  <div className="p-4 rounded-2xl bg-blue-50/60 border border-blue-100 space-y-1">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 font-heading block">
                      Total Cucian / Bulan:
                    </span>
                    <strong className="text-xl sm:text-2xl font-black font-mono text-slate-900 block">
                      {calculationResults.monthlyTotalKg.toLocaleString('id-ID')}
                      <span className="text-xs font-normal text-slate-500 ml-1">kg</span>
                    </strong>
                  </div>

                  <div className="p-4 rounded-2xl bg-blue-50/60 border border-blue-100 space-y-1">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 font-heading block">
                      Konsentrat KCA Dibutuhkan:
                    </span>
                    <strong className="text-xl sm:text-2xl font-black font-mono text-[#0F58A8] block">
                      {calculationResults.kcaLitersMonth}
                      <span className="text-xs font-normal text-slate-500 ml-1">Liter</span>
                    </strong>
                  </div>
                </div>

                {/* Packaging Advice */}
                <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl bg-white border border-slate-200 flex items-center justify-center shrink-0 shadow-2xs">
                    <Package className="w-5 h-5 text-[#0F58A8]" />
                  </div>
                  <div className="space-y-0.5 min-w-0 flex-1">
                    <span className="text-[10px] font-mono font-bold uppercase text-slate-500 block">
                      Rekomendasi Kemasan Pabrik Paling Efisien:
                    </span>
                    <strong className="text-xs sm:text-sm font-bold font-heading text-slate-900 block truncate">
                      {calculationResults.packagingString}
                    </strong>
                  </div>
                </div>

                {/* Cost Comparison Table */}
                <div className="p-4 rounded-2xl bg-slate-50/80 border border-slate-200/80 space-y-3">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-900 font-heading block">
                    Perbandingan Biaya Kimia Bulanan (Cost Comparison):
                  </span>

                  <div className="space-y-2 text-xs">
                    <div className="flex items-center justify-between pb-1.5 border-b border-slate-200">
                      <span className="text-slate-600">Deterjen Curah / Retail Biasa ({calculationResults.retailLitersMonth}L):</span>
                      <span className="font-mono font-bold text-slate-800">{formatRupiah(calculationResults.retailCostMonth)}</span>
                    </div>

                    <div className="flex items-center justify-between pb-1.5 border-b border-slate-200 text-[#0F58A8]">
                      <span className="font-bold">Konsentrat Murni KCA ({calculationResults.kcaLitersMonth}L):</span>
                      <span className="font-mono font-extrabold">{formatRupiah(calculationResults.kcaCostMonth)}</span>
                    </div>

                    <div className="flex items-center justify-between pt-1 text-emerald-700 bg-emerald-100/50 p-2.5 rounded-xl border border-emerald-200">
                      <strong className="font-heading font-extrabold text-xs sm:text-sm">Potensi Penghematan Bersih:</strong>
                      <strong className="font-mono font-black text-sm sm:text-base">
                        {formatRupiah(calculationResults.monthlySavings)} / bln ({calculationResults.savingsPercent}%)
                      </strong>
                    </div>
                  </div>
                </div>

                {/* WhatsApp Action Button */}
                <a
                  href={getCalculationWaLink()}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full h-12 rounded-full bg-[#0F58A8] hover:bg-blue-800 text-white font-heading font-bold text-xs sm:text-sm uppercase tracking-wider transition-all flex items-center justify-center gap-2 cursor-pointer shadow-md shadow-blue-900/15"
                >
                  <Phone className="w-4 h-4" />
                  <span>Kirim Hasil Kalkulasi Ini via WhatsApp</span>
                </a>

              </div>

            </div>

          </div>
        </section>
      )}

      {/* ========================================================================= */}
      {/* 4. PANEL 3: TECHNICAL KNOWLEDGE BASE & TUTORIAL BLOG                      */}
      {/* ========================================================================= */}
      {activeMainTab === 'knowledge' && (
        <section className="py-12 sm:py-16 bg-white text-slate-900">
          <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-10">
            
            <div className="space-y-2 border-b border-slate-200 pb-5">
              <span className="text-xs font-bold uppercase tracking-widest text-[#0F58A8] font-heading block">
                PUSAT EDUKASI &amp; TUTORIAL TEKNIS
              </span>
              <h2 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight uppercase">
                Artikel, SOP &amp; Panduan Formulasi Kimia Industri
              </h2>
              <p className="text-xs sm:text-sm text-slate-600 max-w-2xl font-normal leading-relaxed">
                Rangkuman wawasan teknis, panduan akreditasi rumah sakit KARS, sains pelarutan air sadah, dan perhitungan akuntansi biaya yang disusun oleh praktisi dan formulator KCA.
              </p>
            </div>

            {/* Category Filter Pills */}
            <div className="flex items-center gap-2 overflow-x-auto pb-2">
              <span className="text-xs font-bold text-slate-500 font-heading shrink-0 mr-1">
                Kategori:
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
                  className={`h-8 px-3.5 rounded-full text-xs font-bold font-heading uppercase tracking-wider transition-all whitespace-nowrap cursor-pointer ${
                    selectedArticleFilter === cat.id
                      ? 'bg-[#0F58A8] text-white shadow-xs'
                      : 'bg-slate-100 hover:bg-slate-200 text-slate-700'
                  }`}
                >
                  {cat.label}
                </button>
              ))}
            </div>

            {/* Articles Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredArticles.map((art) => (
                <motion.div
                  key={art.id}
                  initial={{ opacity: 0, y: 15 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.3 }}
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

                    {/* Key takeaways bullet points */}
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
                </motion.div>
              ))}
            </div>

          </div>
        </section>
      )}

      {/* ========================================================================= */}
      {/* 5. ARTICLE READING MODAL                                                  */}
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
                  PT Kediri Chemical Abadi • Standar ISO 9001:2015
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
      {/* 6. SIGNATURE S-CURVE WAVE TRANSITION (Smooth into Dark Navy Footer)       */}
      {/* ========================================================================= */}
      <div className="w-full overflow-hidden leading-none bg-white select-none pointer-events-none -mb-[1px]">
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
