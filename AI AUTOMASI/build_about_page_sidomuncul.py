# -*- coding: utf-8 -*-
"""
PT Kediri Chemical Abadi
Script Generator Halaman Sejarah Perusahaan (AboutPage.jsx)
Mengikuti Standar Desain Sido Muncul (sidomuncul.co.id/id/history.html)
Author: Yerikho Arfensias Effendi
Company: PT Kediri Chemical Abadi
"""

import os

CODE = """import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { 
  Building2, 
  Award, 
  ShieldCheck, 
  CheckCircle2, 
  Factory, 
  FlaskConical, 
  Droplets, 
  Leaf, 
  Clock, 
  Users, 
  MapPin, 
  ChevronDown,
  ArrowRight
} from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import CTASection from '@/components/sections/CTASection'

const TIMELINE_MILESTONES = [
  {
    year: '2004',
    badge: 'Fase 01 • Pendirian & Riset Air Sadah',
    title: 'Titik Mula di Mojoroto: Menaklukkan Kesadahan Air Jawa Timur',
    desc: 'Didirikan oleh Yan Effendi di Mojoroto, Kota Kediri dengan modal awal 1 unit reaktor manual 500 Liter. Pada masa awal ini, industri laundry komersial dan tekstil lokal menghadapi kendala busa mati dan serat kain menguning akibat tingginya kesadahan air tanah Jawa Timur (>350 ppm CaCO₃).',
    details: 'Yan Effendi berhasil merekayasa formulasi agen pengkhelat murni (sequestering agent) pertama di Kediri yang mampu mengikat ion kalsium dan magnesium secara stabil tanpa merusak serat kain.',
    highlights: [
      'Operasional reaktor perdana 500L dengan kontrol pemanasan terukur',
      'Riset adaptasi formula terhadap kesadahan air lokal 300–450 ppm',
      'Penyaluran perdana ke puluhan sentra laundry komersial Karesidenan Kediri'
    ],
    breakthrough: 'Formulasi surfaktan stabil air sadah pertama yang menekan pemborosan dosis hingga 40%.',
    image: '/images/kca_factory_reactors.jpg',
    imageCaption: 'Reaktor Pencampur Perdana PT Kediri Chemical Abadi di Mojoroto, Kediri (Est. 2004)'
  },
  {
    year: '2008',
    badge: 'Fase 02 • Inovasi Hijau & Reaktor Stainless',
    title: 'Terobosan Formula 100% Bebas Fosfat & Tangki SS 316L Pertama',
    desc: 'Di tengah maraknya deterjen industri murah berbasis STPP (senyawa fosfat yang merusak ekosistem perairan dan memicu ledakan alga), KCA mengambil keputusan strategis untuk menghentikan total penggunaan bahan fosfat dan menginvestasikan reaktor pencampur Stainless Steel 316L pertama.',
    details: 'Pengembangan sinergi surfaktan non-ionik murni dan enzim pembersih ramah lingkungan menghasilkan daya angkat noda lemak minyak yang tinggi namun sepenuhnya aman terhadap saluran air limbah.',
    highlights: [
      'Instalasi reaktor Stainless Steel 316L tahan korosi asam dan basa pekat',
      'Standarisasi formula 100% bebas STPP (mencegah pencemaran air)',
      'Konsistensi efisiensi dosis stabil pada 10–15 ml per kilogram cucian'
    ],
    breakthrough: 'Pelopor formula deterjen ramah ekosistem air di Kediri dengan efisiensi dosis tinggi.',
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Lini Manufaktur Formulasi Ramah Lingkungan Bebas Fosfat Berstandar Mutu'
  },
  {
    year: '2014',
    badge: 'Fase 03 • Standarisasi Medis & Kelayakan IPAL',
    title: 'Penetrasi Rumah Sakit Rujukan & Kelayakan Biofilter IPAL KARS',
    desc: 'KCA memasuki sektor higienitas medis dengan memformulasi deterjen disinfektan dan alkali builder khusus pencucian linen ruang isolasi, bedah, dan rawat inap rumah sakit. Formula KCA lolos uji ketat instalasi pengolahan limbah karena tidak mematikan bakteri pengurai biofilter IPAL.',
    details: 'Menggunakan biosurfaktan yang terurai secara alami (>90% biodegradasi OECD 301D) dipadukan dengan senyawa oksigen aktif untuk disinfeksi termokimia tanpa merusak serat kain linen medis.',
    highlights: [
      'Lolos uji baku mutu limbah cair pada sistem IPAL biofilter rumah sakit',
      'Penyediaan formula Alkali Booster, Emulsifier Noda Darah, dan Oxy Bleach',
      'Kemitraan resmi dengan puluhan RSUD dan RS swasta se-Jawa Timur'
    ],
    breakthrough: 'Standar mutu linen medis lolos uji akreditasi KARS dengan nol risiko kerusakan IPAL.',
    image: '/images/product_jerigen5l.jpg',
    imageCaption: 'Produk Kimia Higienitas Medis & Pembersih Konsentrat Ramah Biofilter IPAL RS'
  },
  {
    year: '2019',
    badge: 'Fase 04 • Modernisasi Demin RO & Dedicated Line',
    title: 'Instalasi Demin RO 50.000 L/Hari & Skema Reaktor Dedikasi',
    desc: 'Menjawab lonjakan kebutuhan maklon private label brand nasional, KCA membangun fasilitas pengolahan air Reverse Osmosis (RO) dan demineralisasi berkapasitas 50.000 Liter/hari (<5 ppm TDS). Pada fase ini, skema reaktor khusus dedicated line resmi diluncurkan.',
    details: 'Penggunaan air demineralisasi murni memastikan kemurnian reaktif bahan aktif surfaktan mencapai tingkat optimal dan memperpanjang masa simpan produk jadi hingga lebih dari 24 bulan tanpa degradasi.',
    highlights: [
      'Pembangunan instalasi Double-Stage RO & Mixed-Bed Resin (<5 ppm TDS)',
      'Peningkatan kapasitas total pabrik melampaui 500+ Ton konsentrat per bulan',
      'Peluncuran skema Dedicated Line maklon dengan jaminan kerahasiaan NDA'
    ],
    breakthrough: 'Pabrik kimia di Jawa Timur dengan fasilitas air demin mandiri dan kapasitas skala besar.',
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Instalasi Pengolahan Air Demineralisasi RO 50.000 L/Hari & Reaktor Kapasitas 500+ Ton/Bln'
  },
  {
    year: '2024–2026',
    badge: 'Fase 05 • Era Manajemen Modern & ISO 9001',
    title: 'Kepemimpinan Generasi Kedua, Standar ISO 9001 & Izin Edar PKRT',
    desc: 'Estafet kepemimpinan di bawah Yerikho Arfensias Effendi mempercepat transformasi tata kelola korporat, sertifikasi Sistem Manajemen Mutu ISO 9001:2015, dan integrasi rantai pasok digital. KCA melengkapi perizinan edar PKRT Kementerian Kesehatan RI untuk seluruh varian produk.',
    details: 'Penerapan standar titrasi digital QC laboratorium, kepatuhan perpajakan e-Faktur PPN 11%, dan kesiapan pengadaan tender pemerintah di platform e-Katalog LKPP RI.',
    highlights: [
      'Sertifikasi Sistem Manajemen Mutu ISO 9001:2015 untuk konsistensi batch',
      'Kelengkapan izin edar PKRT Kemenkes RI untuk seluruh lini sabun & pembersih',
      'Kesiapan tender nasional e-Katalog LKPP RI dan ekspansi distribusi logistik antarpulau'
    ],
    breakthrough: 'Produsen kimia konsentrat terpercaya dengan legalitas lengkap dan kapasitas industri 500+ Ton.',
    image: '/images/kca_packaging_lineup.png',
    imageCaption: 'Lini Produk Resmi & Fasilitas Lab PT Kediri Chemical Abadi Standar ISO 9001:2015'
  }
]

export default function AboutPage() {
  return (
    <main className="min-h-screen bg-white text-slate-900 pt-20">
      <Helmet>
        <title>Sejarah & Profil Perusahaan — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Perjalanan sejarah PT Kediri Chemical Abadi sejak 2004 dari pabrik reaktor di Mojoroto, Kediri hingga menjadi pusat manufaktur kimia pembersih berkapasitas 500+ Ton/bulan berstandar ISO 9001:2015."
        />
        <meta name="author" content="Yerikho Arfensias Effendi" />
      </Helmet>

      {/* ========================================================================= */}
      {/* 1. HERO SECTION: SEJARAH KAMI (SIDO MUNCUL STYLE: h1.line + MOSAIC IMG)   */}
      {/* ========================================================================= */}
      <section className="pt-12 pb-10 sm:pt-16 sm:pb-14 bg-white relative overflow-hidden">
        
        {/* Ambient 4K Caustics Texture Accent */}
        <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden select-none opacity-20 mix-blend-multiply">
          <img
            src="/images/bg_liquid_caustics_4k.png"
            alt="Water Sheen Texture"
            className="w-full h-full object-cover object-top"
          />
        </div>

        <div className="max-w-[1400px] mx-auto px-4 sm:px-8 lg:px-12 w-full relative z-10 space-y-8">
          
          {/* Header Title with Sido Muncul's Signature Horizontal Accent Lines */}
          <div className="flex items-center justify-center gap-4 sm:gap-6 text-center">
            <div className="hidden sm:block h-px bg-slate-300 w-16 sm:w-28 lg:w-40" />
            <h1 className="text-xl sm:text-2xl lg:text-3xl font-black font-heading tracking-widest text-[#0F58A8] uppercase">
              Sejarah Kami
            </h1>
            <div className="hidden sm:block h-px bg-slate-300 w-16 sm:w-28 lg:w-40" />
          </div>

          {/* Panoramic Factory Mosaic Visual (Clean Border Frame) */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="relative overflow-hidden rounded-xl sm:rounded-2xl border border-slate-200/90 shadow-sm bg-slate-100 aspect-[21/9] sm:aspect-[24/9]"
          >
            <img
              src="/images/kca_factory_reactors.jpg"
              alt="Fasilitas Manufaktur Reaktor PT Kediri Chemical Abadi"
              className="w-full h-full object-cover object-center filter brightness-[0.98] contrast-[1.03]"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-slate-900/40 via-transparent to-transparent pointer-events-none" />
            
            <div className="absolute bottom-3 sm:bottom-4 left-4 sm:left-6 text-white text-xs sm:text-sm font-heading font-medium drop-shadow-sm">
              Fasilitas Reaktor Pencampur & Pusat Riset Formulasi • Mojoroto, Kediri
            </div>
          </motion.div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 2. PROLOGUE / NARASI PENGANTAR (SIDO MUNCUL STYLE: sub-judul & t-desc)    */}
      {/* ========================================================================= */}
      <section className="py-10 sm:py-14 bg-slate-50/60 border-y border-slate-200/80 relative">
        <div className="max-w-4xl mx-auto px-4 sm:px-8 w-full text-center space-y-4">
          
          <h2 className="text-sm sm:text-base lg:text-lg font-black font-heading uppercase tracking-wider text-slate-900">
            Perjalanan Panjang dari Sebuah Reaktor Pembersih Konsentrat
          </h2>

          <h3 className="text-xs sm:text-[13px] font-bold font-heading uppercase tracking-widest text-[#0F58A8]">
            Industri Kimia Ramah Lingkungan yang Bermanfaat bagi Mitra Bisnis dan Ekosistem Perairan
          </h3>

          <div className="pt-2 text-xs sm:text-[13.5px] text-slate-700 leading-relaxed space-y-3 font-normal text-justify sm:text-center">
            <p>
              Mengawali kiprah dari sebuah unit reaktor pencampur sederhana di Mojoroto, Kota Kediri, perjalanan usaha 
              <strong> PT Kediri Chemical Abadi</strong> dirintis oleh <strong>Bapak Yan Effendi</strong> pada tahun 2004. Berangkat dari keprihatinan mendalam terhadap mahalnya biaya operasional dan kerusakan mesin cuci akibat tingginya tingkat kesadahan air tanah lokal (&gt;350 ppm CaCO₃), beliau mendedikasikan riset mandiri untuk menghasilkan formula deterjen konsentrat yang mampu mengikat ion mineral secara stabil tanpa merusak serat kain.
            </p>
            <p>
              Komitmen terhadap mutu dan integritas lingkungan terus berlanjut ke generasi kepemimpinan 
              <strong> Bapak Yerikho Arfensias Effendi</strong>. Melalui sertifikasi Sistem Manajemen Mutu <strong>ISO 9001:2015</strong>, legalitas perizinan edar PKRT Kementerian Kesehatan RI, serta kapasitas produksi yang melampaui <strong>500+ Ton per bulan</strong>, PT Kediri Chemical Abadi kini telah bertumbuh menjadi mitra terpercaya bagi ratusan rumah sakit rujukan, jejaring perhotelan nasional, sentra laundry komersial, dan industri manufaktur di seluruh penjuru Indonesia.
            </p>
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. ALTERNATING TIMELINE MILESTONES (SIDO MUNCUL EXACT HISTORY TIMELINE)   */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-white relative overflow-hidden">
        
        <div className="max-w-[1300px] mx-auto px-4 sm:px-8 lg:px-12 w-full relative">

          {/* Central Vertical Guide Line (Desktop Only) */}
          <div className="hidden lg:block absolute left-1/2 -translate-x-1/2 top-4 bottom-12 w-0.5 bg-slate-200" />

          {/* Milestone Items List */}
          <div className="space-y-16 sm:space-y-24">
            {TIMELINE_MILESTONES.map((item, idx) => {
              const isEven = idx % 2 === 1

              return (
                <div 
                  key={item.year}
                  className="relative grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center"
                >
                  {/* Central Node Bullet on Desktop */}
                  <div className="hidden lg:flex absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-white border-2 border-[#0F58A8] shadow-xs items-center justify-center z-20">
                    <div className="w-2.5 h-2.5 rounded-full bg-[#0F58A8]" />
                  </div>

                  {/* KONDISI 1: GANJIL (KIRI: Foto | KANAN: Teks) */}
                  {!isEven && (
                    <>
                      <div className="lg:col-span-6 order-2 lg:order-1">
                        <div className="relative overflow-hidden rounded-xl border border-slate-200/90 shadow-sm bg-slate-50 aspect-[16/11]">
                          <img
                            src={item.image}
                            alt={item.title}
                            className="w-full h-full object-cover select-none"
                          />
                          <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-slate-900/60 via-slate-900/20 to-transparent p-3 text-white text-[11px] font-heading font-medium">
                            {item.imageCaption}
                          </div>
                        </div>
                      </div>

                      <div className="lg:col-span-6 space-y-3 order-1 lg:order-2 lg:pl-4">
                        <div className="space-y-1">
                          <span className="text-[10.5px] font-bold font-heading uppercase tracking-widest text-slate-500 block">
                            {item.badge}
                          </span>
                          <h3 className="text-3xl sm:text-4xl lg:text-5xl font-black font-heading text-[#0F58A8] tracking-tight leading-none">
                            {item.year}
                          </h3>
                        </div>

                        <h4 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                          {item.title}
                        </h4>

                        <p className="text-xs sm:text-[13px] text-slate-700 leading-relaxed font-normal">
                          {item.desc}
                        </p>

                        <p className="text-xs sm:text-[13px] text-slate-600 leading-relaxed font-normal">
                          {item.details}
                        </p>

                        <div className="pt-2 border-t border-slate-100 space-y-1.5">
                          {item.highlights.map((h, hIdx) => (
                            <div key={hIdx} className="flex items-start gap-2 text-xs text-slate-700">
                              <CheckCircle2 className="w-3.5 h-3.5 text-[#0F58A8] shrink-0 mt-0.5" />
                              <span className="leading-snug">{h}</span>
                            </div>
                          ))}
                        </div>

                        <div className="p-2.5 bg-blue-50/70 border-l-2 border-[#0F58A8] rounded-r text-[11.5px] text-slate-800 font-medium leading-relaxed">
                          <strong>Pencapaian:</strong> {item.breakthrough}
                        </div>
                      </div>
                    </>
                  )}

                  {/* KONDISI 2: GENAP (KIRI: Teks (Rata Kanan) | KANAN: Foto) */}
                  {isEven && (
                    <>
                      <div className="lg:col-span-6 space-y-3 order-1 lg:order-1 lg:pr-4 lg:text-right">
                        <div className="space-y-1">
                          <span className="text-[10.5px] font-bold font-heading uppercase tracking-widest text-slate-500 block">
                            {item.badge}
                          </span>
                          <h3 className="text-3xl sm:text-4xl lg:text-5xl font-black font-heading text-[#0F58A8] tracking-tight leading-none">
                            {item.year}
                          </h3>
                        </div>

                        <h4 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                          {item.title}
                        </h4>

                        <p className="text-xs sm:text-[13px] text-slate-700 leading-relaxed font-normal">
                          {item.desc}
                        </p>

                        <p className="text-xs sm:text-[13px] text-slate-600 leading-relaxed font-normal">
                          {item.details}
                        </p>

                        <div className="pt-2 border-t border-slate-100 space-y-1.5 flex flex-col lg:items-end">
                          {item.highlights.map((h, hIdx) => (
                            <div key={hIdx} className="flex items-start gap-2 text-xs text-slate-700 lg:flex-row-reverse text-left lg:text-right">
                              <CheckCircle2 className="w-3.5 h-3.5 text-[#0F58A8] shrink-0 mt-0.5" />
                              <span className="leading-snug">{h}</span>
                            </div>
                          ))}
                        </div>

                        <div className="p-2.5 bg-blue-50/70 border-l-2 lg:border-l-0 lg:border-r-2 border-[#0F58A8] rounded-r lg:rounded-r-none lg:rounded-l text-[11.5px] text-slate-800 font-medium leading-relaxed text-left lg:text-right">
                          <strong>Pencapaian:</strong> {item.breakthrough}
                        </div>
                      </div>

                      <div className="lg:col-span-6 order-2 lg:order-2">
                        <div className="relative overflow-hidden rounded-xl border border-slate-200/90 shadow-sm bg-slate-50 aspect-[16/11]">
                          <img
                            src={item.image}
                            alt={item.title}
                            className="w-full h-full object-cover select-none"
                          />
                          <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-slate-900/60 via-slate-900/20 to-transparent p-3 text-white text-[11px] font-heading font-medium">
                            {item.imageCaption}
                          </div>
                        </div>
                      </div>
                    </>
                  )}

                </div>
              )
            })}
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 4. STRUKTUR MANAJEMEN & DEWAN DIREKSI (SIDO MUNCUL CORPORATE DIRECTORS)  */}
      {/* ========================================================================= */}
      <section className="py-14 sm:py-18 bg-slate-50/80 border-t border-slate-200 relative">
        <div className="max-w-[1300px] mx-auto px-4 sm:px-8 lg:px-12 w-full space-y-10">
          
          <div className="text-center max-w-3xl mx-auto space-y-2">
            <span className="text-[10.5px] font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              TATA KELOLA PERUSAHAAN & KEPEMIMPINAN
            </span>
            <h2 className="text-xl sm:text-2xl font-black font-heading text-slate-900 tracking-tight leading-tight uppercase">
              Dewan Direksi & Kepemimpinan 2 Generasi
            </h2>
            <p className="text-xs sm:text-[13px] text-slate-600 font-normal max-w-2xl mx-auto">
              Sinergi pengalaman lebih dari 20 tahun dalam riset kimia industri dengan manajemen operasional modern berstandar ISO 9001:2015.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12 max-w-5xl mx-auto divide-y md:divide-y-0 md:divide-x divide-slate-200 items-start">
            {COMPANY_DATA.boardOfDirectors.map((person, idx) => (
              <div
                key={idx}
                className={`space-y-4 ${idx === 1 ? 'md:pl-10 lg:pl-12 pt-8 md:pt-0' : 'md:pr-10 lg:pr-12'}`}
              >
                <div className="flex items-start gap-3.5">
                  <div className="w-12 h-12 bg-white border border-slate-300 text-[#0F58A8] flex items-center justify-center font-heading font-black text-base shadow-2xs shrink-0 mt-0.5 rounded-md">
                    {person.name.split(' ').map((n) => n[0]).join('')}
                  </div>
                  <div>
                    <h3 className="text-sm sm:text-base font-bold font-heading text-slate-900 leading-snug">
                      {person.name}
                    </h3>
                    <span className="text-xs font-semibold text-[#0F58A8] block">
                      {person.role}
                    </span>
                    <span className="text-[11px] text-slate-500 block pt-0.5 font-medium">
                      Rekam Jejak: {person.experience}
                    </span>
                  </div>
                </div>

                <p className="text-xs sm:text-[13px] text-slate-700 leading-relaxed font-normal">
                  {person.bio}
                </p>

                <div className="space-y-1.5 pt-2 border-t border-slate-200">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 block font-heading">
                    Fokus Tanggung Jawab:
                  </span>
                  <div className="space-y-1 text-xs text-slate-700">
                    {(person.responsibilities || [person.focus]).map((resp, rIdx) => (
                      <div key={rIdx} className="flex items-start gap-2">
                        <CheckCircle2 className="w-3.5 h-3.5 text-[#0F58A8] shrink-0 mt-0.5" />
                        <span className="leading-snug">{resp}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 5. NILAI UTAMA KORPORAT & VISI MISI (SIDO MUNCUL CORPORATE VALUES)        */}
      {/* ========================================================================= */}
      <section className="py-12 sm:py-16 bg-white border-t border-slate-200">
        <div className="max-w-[1300px] mx-auto px-4 sm:px-8 lg:px-12 w-full space-y-8">
          
          <div className="max-w-3xl space-y-1.5">
            <span className="text-[10.5px] font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              PRINSIP INTEGRITAS & KEBERLANJUTAN
            </span>
            <h2 className="text-xl sm:text-2xl font-black font-heading text-slate-900 tracking-tight leading-tight uppercase">
              4 Komitmen Fundamental Perusahaan
            </h2>
            <p className="text-xs sm:text-[13px] text-slate-600 font-normal">
              Nilai operasional yang dipegang teguh oleh seluruh formulator lab, teknisi reaktor, dan manajemen PT Kediri Chemical Abadi.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-2 border-t border-slate-200">
            <div className="space-y-1.5 border-l-2 border-[#0F58A8] pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                1. Kejujuran Formulasi Murni
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Menolak penambahan filler garam murah atau pengencer air berlebih yang merusak mesin dan memboroskan biaya mitra.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-emerald-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                2. Tanggung Jawab IPAL Lingkungan
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Komitmen 100% bebas fosfat (STPP-free) dan surfaktan biodegradasi &gt;90% menjaga kelestarian ekosistem perairan.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-amber-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                3. Akuntabilitas Legalitas & Pajak
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Beroperasi dengan perizinan OSS-RBA resmi, SPPKP dengan e-Faktur PPN 11%, dan kesiapan tender e-Katalog LKPP RI.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-indigo-600 pl-3.5">
              <strong className="text-xs font-bold text-slate-900 block font-heading">
                4. Kontinuitas Pasokan Massal
              </strong>
              <p className="text-xs text-slate-600 leading-relaxed">
                Kapasitas reaktor 500+ Ton/bulan menjamin ketersediaan pasokan kimia rutin tanpa jeda operasional.
              </p>
            </div>
          </div>

        </div>
      </section>

      {/* Full Width CTA Section */}
      <CTASection />
    </main>
  )
}
"""

with open('src/pages/AboutPage.jsx', 'w', encoding='utf-8') as f:
    f.write(CODE)

print("SUKSES: AboutPage.jsx berhasil diperbarui sesuai standar sejarah Sido Muncul!")
