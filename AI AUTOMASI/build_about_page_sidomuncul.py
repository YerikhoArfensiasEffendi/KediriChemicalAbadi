# -*- coding: utf-8 -*-
"""
PT Kediri Chemical Abadi
Generator Halaman Sejarah (AboutPage.jsx)
Struktur Presisi Sesuai Screenshot sidomuncul.co.id/id/history.html
Author: Yerikho Arfensias Effendi
Company: PT Kediri Chemical Abadi
"""

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
  ChevronDown
} from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import CTASection from '@/components/sections/CTASection'

const TIMELINE_DATA = [
  {
    year: '2004',
    text: 'Berbekal kepiawaian dalam rekayasa formula kimia pembersih, Bapak Yan Effendi mendirikan reaktor pencampur perdana di Mojoroto, Kediri, guna menaklukkan masalah kesadahan air tanah tinggi Jawa Timur (>350 ppm CaCO₃) bagi sentra laundry komersial.',
    boldWords: ['Bapak Yan Effendi', 'Mojoroto, Kediri', '>350 ppm CaCO₃'],
    image: '/images/kca_factory_reactors.jpg',
    imageCaption: 'Reaktor Pencampur Perdana KCA (Est. 2004)',
    align: 'left' // text on right, image on left
  },
  {
    year: '2008',
    text: 'Mengambil komitmen perlindungan ekosistem perairan, KCA memelopori formulasi 100% Bebas Fosfat (STPP-Free) dan mengoperasikan reaktor Stainless Steel 316L pertama untuk menghasilkan deterjen industri ramah lingkungan dan aman biofilter IPAL.',
    boldWords: ['100% Bebas Fosfat (STPP-Free)', 'Stainless Steel 316L', 'aman biofilter IPAL'],
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Lini Reaktor SS 316L Formulasi Non-Fosfat',
    align: 'right' // text on left, image on right
  },
  {
    year: '2014',
    text: 'Ekspansi ke sektor higienitas medis dan rumah sakit rujukan. Formulasi disinfektan dan pembersih linen medis KCA lolos uji baku mutu Biofilter IPAL standar akreditasi KARS tanpa merusak bakteri pengurai limbah cair.',
    boldWords: ['sektor higienitas medis', 'Biofilter IPAL', 'akreditasi KARS'],
    image: '/images/product_jerigen5l.jpg',
    imageCaption: 'Produk Kimia Higienitas Medis Ramah IPAL RS',
    align: 'left'
  },
  {
    year: '2019',
    text: 'Pembangunan instalasi pemurnian air Demineralisasi RO 50.000 Liter/Hari dan peluncuran skema Dedicated Production Line VIP untuk memenuhi lonjakan maklon brand nasional dengan kapasitas pabrik melampaui 500+ Ton per bulan.',
    boldWords: ['Demineralisasi RO 50.000 Liter/Hari', 'Dedicated Production Line VIP', '500+ Ton per bulan'],
    image: '/images/kca_factory_floor.jpg',
    imageCaption: 'Instalasi Demin RO & Lini Dedicated VIP',
    align: 'right'
  },
  {
    year: '2024–2026',
    text: 'Transformasi korporat generasi kedua di bawah Bapak Yerikho Arfensias Effendi, menyempurnakan sertifikasi Sistem Manajemen Mutu ISO 9001:2015, kelengkapan Izin Edar PKRT Kemenkes RI, serta kesiapan tender pengadaan nasional di platform e-Katalog LKPP RI.',
    boldWords: ['Bapak Yerikho Arfensias Effendi', 'ISO 9001:2015', 'Izin Edar PKRT Kemenkes RI', 'e-Katalog LKPP RI'],
    image: '/images/kca_packaging_lineup.png',
    imageCaption: 'Lini Manufaktur Resmi & Lab PT Kediri Chemical Abadi',
    align: 'left'
  }
]

// Helper function to render text with bold terms
function renderFormattedText(text, boldWords) {
  let parts = [text]
  boldWords.forEach((word) => {
    let nextParts = []
    parts.forEach((p) => {
      if (typeof p === 'string') {
        const split = p.split(word)
        split.forEach((s, idx) => {
          if (s) nextParts.push(s)
          if (idx < split.length - 1) {
            nextParts.push(<strong key={word + idx} className="font-bold text-slate-900">{word}</strong>)
          }
        })
      } else {
        nextParts.push(p)
      }
    })
    parts = nextParts
  })
  return parts
}

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
      {/* SECTION 00: SEJARAH KAMI (SIDO MUNCUL HERO BANNER)                        */}
      {/* ========================================================================= */}
      <section className="pt-14 pb-16 sm:pt-20 sm:pb-20 bg-white relative">
        <div className="max-w-[1300px] mx-auto px-4 sm:px-8 lg:px-12 w-full text-center space-y-8 sm:space-y-12">
          
          {/* Header Title Flanked by Two Subtle Lines */}
          <div className="flex items-center justify-center gap-4 sm:gap-8">
            <div className="h-[1.5px] bg-slate-300 w-16 sm:w-32 lg:w-48" />
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold font-heading tracking-[0.18em] text-[#0F58A8] uppercase">
              SEJARAH KAMI
            </h1>
            <div className="h-[1.5px] bg-slate-300 w-16 sm:w-32 lg:w-48" />
          </div>

          {/* Panoramic Factory Mosaic Visual (Sido Muncul Collage Frame) */}
          <div className="max-w-5xl mx-auto">
            <div className="relative overflow-hidden rounded-xl border border-slate-200/90 shadow-md bg-slate-100 aspect-[21/9]">
              <img
                src="/images/kca_factory_reactors.jpg"
                alt="Fasilitas Manufaktur Reaktor PT Kediri Chemical Abadi"
                className="w-full h-full object-cover filter brightness-[0.98] contrast-[1.03]"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-slate-900/35 via-transparent to-transparent pointer-events-none" />
              <div className="absolute bottom-3 left-4 sm:left-6 text-white text-xs sm:text-sm font-heading font-medium drop-shadow-sm">
                Fasilitas Reaktor Pencampur & Riset Formulasi • Mojoroto, Kediri
              </div>
            </div>
          </div>

          {/* Sido Muncul Anchor Down Bouncing Arrow */}
          <div className="pt-4 flex justify-center">
            <ChevronDown className="w-6 h-6 text-slate-400 animate-bounce stroke-[2]" />
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* SECTION 01: PROLOGUE / NARASI PENGANTAR (SIDO MUNCUL SUB-JUDUL & T-DESC)  */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-slate-50/50 border-y border-slate-200/70 relative">
        <div className="max-w-4xl mx-auto px-4 sm:px-8 w-full text-center space-y-5">
          
          <h2 className="text-base sm:text-lg lg:text-xl font-bold font-heading uppercase tracking-wider text-[#0F58A8]">
            PERJALANAN PANJANG DARI SEBUAH REAKTOR PEMBERSIH KONSENTRAT
          </h2>

          <h3 className="text-sm sm:text-base font-bold font-heading uppercase tracking-wide text-slate-900">
            INDUSTRI KIMIA YANG BERMANFAAT BAGI MITRA BISNIS DAN LINGKUNGAN
          </h3>

          <p className="text-sm sm:text-[15.5px] text-slate-800 leading-[1.85] font-normal text-justify sm:text-center pt-2">
            Mengawali usaha dari sebuah unit reaktor pencampur di Mojoroto, Kota Kediri, Jawa Timur, di sinilah titik awal perjalanan usaha manufaktur kimia pembersih didirikan oleh <strong>Bapak Yan Effendi</strong> pada tahun 2004. Berangkat dari tantangan tingginya kesadahan air tanah lokal (&gt;350 ppm CaCO₃) yang kerap menggagalkan efisiensi pencucian dan merusak mesin cuci laundry lokal, beliau mendedikasikan riset formulasi konsentrat murni yang stabil terhadap ion sadah. Komitmen mutu ini dilanjutkan dan diperkuat oleh <strong>Bapak Yerikho Arfensias Effendi</strong> melalui standarisasi Sistem Manajemen Mutu <strong>ISO 9001:2015</strong>, kelengkapan perizinan edar <strong>PKRT Kemenkes RI</strong>, dan kapasitas pasokan yang kini melampaui <strong>500+ Ton per bulan</strong>.
          </p>

          <div className="pt-6 flex justify-center">
            <ChevronDown className="w-6 h-6 text-slate-400 animate-bounce stroke-[2]" />
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* SECTIONS 02 - 06: TIMELINE SEJARAH BERGANTIAN (SIDO MUNCUL TIMELINE)      */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-28 bg-white relative overflow-hidden">
        <div className="max-w-[1250px] mx-auto px-4 sm:px-8 lg:px-12 w-full relative">

          {/* Central Vertical Timeline Guide Line (Desktop) */}
          <div className="hidden lg:block absolute left-1/2 -translate-x-1/2 top-10 bottom-10 w-[2px] bg-slate-300" />

          <div className="space-y-24 sm:space-y-36">
            {TIMELINE_DATA.map((item, idx) => {
              const isEven = idx % 2 === 1

              return (
                <div 
                  key={item.year}
                  className="relative grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-center"
                >
                  {/* Central Node Bullet on Desktop (Sido Muncul Signature) */}
                  <div className="hidden lg:flex absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 w-6 h-6 rounded-full bg-[#0F58A8] border-4 border-white shadow-sm items-center justify-center z-20" />

                  {/* ───────────────────────────────────────────────────────── */}
                  {/* KONDISI 1: GANJIL (KIRI: Foto  |  KANAN: Tahun & Narasi)  */}
                  {/* ───────────────────────────────────────────────────────── */}
                  {!isEven && (
                    <>
                      {/* Sisi Kiri: Foto dengan Matting Frame (Sido Muncul Polaroid Style) */}
                      <div className="lg:col-span-6 order-2 lg:order-1 flex justify-center lg:justify-end">
                        <div className="relative p-2.5 sm:p-3 bg-white border border-slate-200/90 shadow-md rounded-lg max-w-md w-full">
                          <div className="overflow-hidden rounded aspect-[16/11] bg-slate-100">
                            <img
                              src={item.image}
                              alt={item.year}
                              className="w-full h-full object-cover select-none"
                            />
                          </div>
                          <div className="pt-2 text-center text-xs font-heading font-medium text-slate-600">
                            {item.imageCaption}
                          </div>
                        </div>
                      </div>

                      {/* Sisi Kanan: Tahun & Teks Narasi */}
                      <div className="lg:col-span-6 order-1 lg:order-2 space-y-3 lg:pl-6 text-left">
                        <h3 className="text-3xl sm:text-4xl lg:text-[42px] font-bold font-heading text-[#0F58A8] tracking-tight leading-none">
                          {item.year}
                        </h3>
                        <p className="text-sm sm:text-base text-slate-800 leading-[1.8] font-normal max-w-lg">
                          {renderFormattedText(item.text, item.boldWords)}
                        </p>
                      </div>
                    </>
                  )}

                  {/* ───────────────────────────────────────────────────────── */}
                  {/* KONDISI 2: GENAP (KIRI: Tahun & Narasi  |  KANAN: Foto)    */}
                  {/* ───────────────────────────────────────────────────────── */}
                  {isEven && (
                    <>
                      {/* Sisi Kiri: Tahun & Teks Narasi (Rata Kanan di Desktop) */}
                      <div className="lg:col-span-6 order-1 lg:order-1 space-y-3 lg:pr-6 text-left lg:text-right flex flex-col lg:items-end">
                        <h3 className="text-3xl sm:text-4xl lg:text-[42px] font-bold font-heading text-[#0F58A8] tracking-tight leading-none">
                          {item.year}
                        </h3>
                        <p className="text-sm sm:text-base text-slate-800 leading-[1.8] font-normal max-w-lg">
                          {renderFormattedText(item.text, item.boldWords)}
                        </p>
                      </div>

                      {/* Sisi Kanan: Foto dengan Matting Frame */}
                      <div className="lg:col-span-6 order-2 lg:order-2 flex justify-center lg:justify-start">
                        <div className="relative p-2.5 sm:p-3 bg-white border border-slate-200/90 shadow-md rounded-lg max-w-md w-full">
                          <div className="overflow-hidden rounded aspect-[16/11] bg-slate-100">
                            <img
                              src={item.image}
                              alt={item.year}
                              className="w-full h-full object-cover select-none"
                            />
                          </div>
                          <div className="pt-2 text-center text-xs font-heading font-medium text-slate-600">
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
      {/* DEWAN DIREKSI & KEPEMIMPINAN 2 GENERASI                                    */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-20 bg-slate-50/70 border-t border-slate-200 relative">
        <div className="max-w-[1250px] mx-auto px-4 sm:px-8 lg:px-12 w-full space-y-10">
          
          <div className="text-center max-w-3xl mx-auto space-y-2">
            <span className="text-xs font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              TATA KELOLA PERUSAHAAN & KEPEMIMPINAN
            </span>
            <h2 className="text-xl sm:text-2xl font-bold font-heading text-slate-900 tracking-tight leading-tight uppercase">
              Dewan Direksi & Kepemimpinan 2 Generasi
            </h2>
            <p className="text-sm text-slate-600 font-normal max-w-2xl mx-auto">
              Sinergi pengalaman lebih dari 20 tahun dalam riset kimia industri dengan manajemen operasional modern berstandar ISO 9001:2015.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-14 max-w-5xl mx-auto divide-y md:divide-y-0 md:divide-x divide-slate-200 items-start">
            {COMPANY_DATA.boardOfDirectors.map((person, idx) => (
              <div
                key={idx}
                className={`space-y-4 ${idx === 1 ? 'md:pl-10 lg:pl-14 pt-8 md:pt-0' : 'md:pr-10 lg:pr-14'}`}
              >
                <div className="flex items-start gap-3.5">
                  <div className="w-12 h-12 bg-white border border-slate-300 text-[#0F58A8] flex items-center justify-center font-heading font-bold text-base shadow-2xs shrink-0 mt-0.5 rounded-md">
                    {person.name.split(' ').map((n) => n[0]).join('')}
                  </div>
                  <div>
                    <h3 className="text-base font-bold font-heading text-slate-900 leading-snug">
                      {person.name}
                    </h3>
                    <span className="text-xs font-semibold text-[#0F58A8] block">
                      {person.role}
                    </span>
                    <span className="text-xs text-slate-500 block pt-0.5 font-medium">
                      Rekam Jejak: {person.experience}
                    </span>
                  </div>
                </div>

                <p className="text-sm text-slate-700 leading-relaxed font-normal">
                  {person.bio}
                </p>

                <div className="space-y-1.5 pt-2 border-t border-slate-200">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-500 block font-heading">
                    Fokus Tanggung Jawab:
                  </span>
                  <div className="space-y-1 text-xs sm:text-sm text-slate-700">
                    {(person.responsibilities || [person.focus]).map((resp, rIdx) => (
                      <div key={rIdx} className="flex items-start gap-2">
                        <CheckCircle2 className="w-4 h-4 text-[#0F58A8] shrink-0 mt-0.5" />
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
      {/* 4 KOMITMEN FUNDAMENTAL PERUSAHAAN (ESG)                                   */}
      {/* ========================================================================= */}
      <section className="py-14 sm:py-18 bg-white border-t border-slate-200">
        <div className="max-w-[1250px] mx-auto px-4 sm:px-8 lg:px-12 w-full space-y-8">
          
          <div className="max-w-3xl space-y-1.5">
            <span className="text-xs font-bold font-heading uppercase tracking-widest text-[#0F58A8] block">
              PRINSIP INTEGRITAS & KEBERLANJUTAN
            </span>
            <h2 className="text-xl sm:text-2xl font-bold font-heading text-slate-900 tracking-tight leading-tight uppercase">
              4 Komitmen Fundamental Perusahaan
            </h2>
            <p className="text-sm text-slate-600 font-normal">
              Nilai operasional yang dipegang teguh oleh seluruh formulator lab, teknisi reaktor, dan manajemen PT Kediri Chemical Abadi.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-2 border-t border-slate-200">
            <div className="space-y-1.5 border-l-2 border-[#0F58A8] pl-3.5">
              <strong className="text-sm font-bold text-slate-900 block font-heading">
                1. Kejujuran Formulasi Murni
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Menolak penambahan filler garam murah atau pengencer air berlebih yang merusak mesin dan memboroskan biaya mitra.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-emerald-600 pl-3.5">
              <strong className="text-sm font-bold text-slate-900 block font-heading">
                2. Tanggung Jawab IPAL Lingkungan
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Komitmen 100% bebas fosfat (STPP-free) dan surfaktan biodegradasi >90% menjaga kelestarian ekosistem perairan.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-amber-600 pl-3.5">
              <strong className="text-sm font-bold text-slate-900 block font-heading">
                3. Akuntabilitas Legalitas & Pajak
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                Beroperasi dengan perizinan OSS-RBA resmi, SPPKP dengan e-Faktur PPN 11%, dan kesiapan tender e-Katalog LKPP RI.
              </p>
            </div>

            <div className="space-y-1.5 border-l-2 border-indigo-600 pl-3.5">
              <strong className="text-sm font-bold text-slate-900 block font-heading">
                4. Kontinuitas Pasokan Massal
              </strong>
              <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
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

print("BERHASIL: AboutPage.jsx ditulis ulang persis seperti screenshot Sido Muncul!")
