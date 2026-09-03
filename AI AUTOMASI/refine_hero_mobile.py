import os

with open('src/components/sections/HeroSection.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the return statement in HeroSection.jsx
mobile_hero = '''  return (
    <>
      {/* ========================================================================= */}
      {/* 1. MOBILE HERO (< lg): COMPACT, SWEET, CLEAN, HARMONIOUS, ZERO OVERLAP    */}
      {/* ========================================================================= */}
      <section className="block lg:hidden relative w-full pt-28 pb-12 px-4 bg-white text-slate-900 overflow-hidden border-b border-slate-200">
        
        {/* Factory Plant Floor Background with Soft White Gradient */}
        <div className="absolute inset-0 z-0 pointer-events-none overflow-hidden">
          <img
            src="/images/kca_factory_floor.jpg"
            alt="Fasilitas Reaktor Pabrik PT Kediri Chemical Abadi"
            className="w-full h-full object-cover object-center opacity-40"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-white/95 via-white/85 to-white" />
        </div>

        {/* Ambient Liquid Water Caustics Texture */}
        <div className="absolute inset-0 z-0 pointer-events-none overflow-hidden opacity-30 mix-blend-multiply">
          <img
            src="/images/bg_liquid_caustics_4k.png"
            alt="Liquid Water Caustics Texture"
            className="w-full h-full object-cover object-top"
          />
        </div>

        <div className="relative z-10 max-w-md mx-auto flex flex-col items-center text-center space-y-3.5">
          
          {/* Main Headline (Clean, no overlapping) */}
          <h1 className="text-xl sm:text-2xl font-black font-heading text-slate-900 tracking-tight leading-snug uppercase">
            Mitra Terpercaya Manufaktur &amp;{' '}
            <span className="text-[#0F58A8]">Formulasi Kimia Industri</span>
          </h1>

          {/* Subtitle (100% visible & readable) */}
          <p className="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal">
            Pusat riset dan manufaktur kimia pembersih konsentrat 100% non-fosfat berkapasitas 500+ Ton/bulan di Mojoroto, Kediri. Solusi pasokan massal B2B dan layanan maklon private label terpercaya.
          </p>

          {/* 3D Packaging Lineup (Floating in its own dedicated space, never covering text) */}
          <motion.div
            animate={{ y: [0, -5, 0] }}
            transition={{ repeat: Infinity, duration: 4, ease: 'easeInOut' }}
            className="w-full max-w-[320px] h-44 sm:h-52 my-1 flex items-center justify-center select-none"
          >
            <img
              src="/images/kca_packaging_lineup.png"
              alt="Lini Kemasan Produk PT Kediri Chemical Abadi"
              className="w-full h-full object-contain drop-shadow-xl select-none"
            />
          </motion.div>

          {/* 4 Corporate Trust Accreditations (2x2 Grid, crisp & compact) */}
          <div className="grid grid-cols-2 gap-2 w-full pt-1 pb-1">
            <div className="p-2.5 rounded-lg bg-white/90 border border-slate-200/90 shadow-2xs text-center">
              <span className="block text-sm font-black font-heading text-[#0F58A8]">500+ TON</span>
              <span className="text-[10px] font-medium text-slate-500 uppercase block font-heading">Reaktor Stainless/Bln</span>
            </div>
            <div className="p-2.5 rounded-lg bg-white/90 border border-slate-200/90 shadow-2xs text-center">
              <span className="block text-sm font-black font-heading text-emerald-700">100% NON-P</span>
              <span className="text-[10px] font-medium text-slate-500 uppercase block font-heading">Bebas Fosfat IPAL Safe</span>
            </div>
            <div className="p-2.5 rounded-lg bg-white/90 border border-slate-200/90 shadow-2xs text-center">
              <span className="block text-sm font-black font-heading text-slate-900">ISO 9001</span>
              <span className="text-[10px] font-medium text-slate-500 uppercase block font-heading">Titrasi Lab QC</span>
            </div>
            <div className="p-2.5 rounded-lg bg-white/90 border border-slate-200/90 shadow-2xs text-center">
              <span className="block text-sm font-black font-heading text-sky-700">EST. 2004</span>
              <span className="text-[10px] font-medium text-slate-500 uppercase block font-heading">Mojoroto, Kediri</span>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="pt-1 flex items-center justify-center gap-2.5 w-full">
            <button
              onClick={() => setRfqOpen(true)}
              className="flex-1 h-10 px-3 bg-red-600 hover:bg-red-700 text-white rounded-lg font-heading font-bold text-xs uppercase tracking-wider shadow-sm flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <span>Minta Sampel</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
            <Link
              to="/calculator"
              className="flex-1 h-10 px-3 bg-[#0A192F] hover:bg-slate-800 text-white rounded-lg font-heading font-bold text-xs uppercase tracking-wider shadow-sm flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <span>Kalkulator Dosis</span>
            </Link>
          </div>

        </div>

        {/* Seamless S-Curve Wave into next section */}
        <div className="absolute bottom-0 inset-x-0 z-20 pointer-events-none leading-none">
          <svg
            className="relative block w-full h-6 text-white"
            viewBox="0 0 1440 120"
            preserveAspectRatio="none"
          >
            <path
              d="M0,32 C360,95 620,10 980,60 C1200,90 1360,45 1440,55 L1440,120 L0,120 Z"
              fill="currentColor"
            />
          </svg>
        </div>

      </section>

      {/* ========================================================================= */}
      {/* 2. DESKTOP HERO (>= lg): 280vh APPLE-STYLE 3D SCROLL STORYTELLING TRACK   */}
      {/* ========================================================================= */}
      <div ref={containerRef} className="hidden lg:block relative w-full h-[280vh] bg-white -mt-20">'''

code = code.replace('  return (\n    <>\n      {/* Scroll Track Container (280vh) */}\n      <div ref={containerRef} className="relative w-full h-[280vh] bg-white -mt-20">', mobile_hero)

with open('src/components/sections/HeroSection.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print('Updated HeroSection.jsx with dedicated, beautiful, non-overlapping mobile hero!')
