import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { 
  ShieldCheck, 
  Award, 
  CheckCircle2, 
  FileText, 
  FlaskConical, 
  Droplets, 
  ShieldAlert, 
  Building2, 
  FileCheck2, 
  Scale, 
  Microscope, 
  Leaf, 
  Layers, 
  ArrowRight,
  Clock,
  Check,
  Factory,
  Package,
  Cpu,
  Handshake,
  Truck
} from 'lucide-react'
import CTASection from '@/components/sections/CTASection'

const QC_STEPS = [
  {
    step: '01',
    phase: 'INCOMING MATERIAL QC',
    title: 'Analisis Bahan Baku Murni',
    icon: FlaskConical,
    color: '#0F58A8',
    borderColor: 'border-b-[#0F58A8]',
    badgeBg: 'bg-[#0F58A8]',
    textColor: 'text-[#0F58A8]',
    checkColor: 'text-[#0F58A8]',
    desc: 'Pemeriksaan ketat kemurnian surfaktan aktif, pelarut, dan bahan aditif dari pemasok sebelum diizinkan masuk ke jalur reaktor.',
    points: [
      'Pemeriksaan Certificate of Analysis (COA) vendor',
      'Uji organoleptik kejernihan & aroma',
      'Uji konsentrasi & berat jenis bahan baku',
      'Verifikasi sertifikasi bebas zat berbahaya'
    ],
    deliverable: 'Bahan Baku Murni Terverifikasi',
    deliverableIcon: FlaskConical
  },
  {
    step: '02',
    phase: 'CONTROLLED BATCH MIXING',
    title: 'Reaksi Kimia Tangki SS 316L',
    icon: Factory,
    color: '#D97706',
    borderColor: 'border-b-[#D97706]',
    badgeBg: 'bg-[#D97706]',
    textColor: 'text-[#D97706]',
    checkColor: 'text-[#D97706]',
    desc: 'Pengadukan dengan kecepatan terukur (RPM terkontrol) pada suhu konstan 28°C–32°C di reaktor Stainless Steel 316L.',
    points: [
      'Kontrol RPM pengaduk variable-speed',
      'Pemantauan suhu jaket pendingin reaktor',
      'Pelarutan bertahap anti-gumpalan (lump-free)'
    ],
    deliverable: 'Larutan Homogen 100% Sempurna',
    deliverableIcon: Factory
  },
  {
    step: '03',
    phase: 'LAB QC TITRATION & VERIFICATION',
    title: 'Sampling Tengah Batch (In-Process)',
    icon: Scale,
    color: '#059669',
    borderColor: 'border-b-[#059669]',
    badgeBg: 'bg-[#059669]',
    textColor: 'text-[#059669]',
    checkColor: 'text-[#059669]',
    desc: 'Pengujian titrasi pH digital, densitas larutan, dan viskositas Brookfield di laboratorium QC internal selama proses pencampuran.',
    points: [
      'Titrasi elektroda pH digital akurasi 0.01',
      'Pengukuran viskositas Brookfield spindle RPM',
      'Uji berat jenis piknometer presisi 20°C'
    ],
    deliverable: 'Presisi Nilai pH Toleransi ±0.01',
    deliverableIcon: Scale
  },
  {
    step: '04',
    phase: 'MICRO FILTRATION & PACKAGING',
    title: 'Penyaringan Mikro & Packaging',
    icon: Layers,
    color: '#7C3AED',
    borderColor: 'border-b-[#7C3AED]',
    badgeBg: 'bg-[#7C3AED]',
    textColor: 'text-[#7C3AED]',
    checkColor: 'text-[#7C3AED]',
    desc: 'Filtrasi mikro untuk memastikan cairan jernih bebas partikulat sebelum dialirkan ke jerigen, drum, atau IBC tank kemasan.',
    points: [
      'Filtrasi mikro 5-mikron penyaring partikel',
      'Penimbangan digital otomatis toleransi 0%',
      'Penyegelan tutup anti-bocor (induction sealing)'
    ],
    deliverable: 'Cairan Jernih Terkemas Bebas Endapan',
    deliverableIcon: Layers
  },
  {
    step: '05',
    phase: 'COA RELEASE & LOGISTICS',
    title: 'Penerbitan COA Resmi & Rilis',
    icon: FileCheck2,
    color: '#0F172A',
    borderColor: 'border-b-[#0F172A]',
    badgeBg: 'bg-[#0F172A]',
    textColor: 'text-[#0F172A]',
    checkColor: 'text-[#0F172A]',
    desc: 'Penerbitan Certificate of Analysis bertandatangan Kepala Laboratorium QC dan pengarsipan retained sample selama 12 bulan.',
    points: [
      'Penerbitan dokumen COA resmi per batch',
      'Penyimpanan retained sample arsip 12 bulan',
      'Serah terima barang ke armada logistik'
    ],
    deliverable: 'Batch Lolos QC, COA & Arsip 1 Tahun',
    deliverableIcon: FileCheck2
  },
]

const QC_PRINCIPLES = [
  {
    icon: Award,
    title: 'AKURASI ANALITIK',
    desc: 'Metode uji terkalibrasi ISO 9001:2015 & ASTM.',
    iconColor: 'text-[#0F58A8]'
  },
  {
    icon: ShieldCheck,
    title: 'TOLERANSI NOL',
    desc: 'Nol toleransi cacat formula dan spesifikasi fisik.',
    iconColor: 'text-[#D97706]'
  },
  {
    icon: Clock,
    title: 'ARSIP 12 BULAN',
    desc: 'Retained sample terjaga untuk uji banding dan audit berkala.',
    iconColor: 'text-[#059669]'
  },
  {
    icon: FileCheck2,
    title: 'TRANSPARANSI COA',
    desc: 'Setiap lot disertai lembar analisis resmi bertandatangan.',
    iconColor: 'text-[#7C3AED]'
  },
  {
    icon: Leaf,
    title: 'RAMAH LINGKUNGAN',
    desc: '100% bebas fosfat dan aman bagi instalasi IPAL.',
    iconColor: 'text-[#0F172A]'
  },
]

export default function CompliancePage() {
  return (
    <main className="bg-white text-slate-900 pt-20">
      <Helmet>
        <title>Kepatuhan Mutu, Legalitas & Standar IPAL — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Standar mutu ISO 9001:2015, terdaftar e-Catalog LKPP, formulasi non-fosfat ramah IPAL, dan prosedur kendali mutu per batch PT Kediri Chemical Abadi."
        />
        <link rel="canonical" href="https://kedirichemical.id/compliance" />
        <meta property="og:title" content="Kepatuhan Mutu, Legalitas & Standar IPAL — PT Kediri Chemical Abadi" />
        <meta property="og:description" content="Standar mutu ISO 9001:2015, izin PKRT, formulasi non-fosfat ramah IPAL rumah sakit di Kediri." />
        <meta property="og:url" content="https://kedirichemical.id/compliance" />
      </Helmet>

      {/* ========================================================================= */}
      {/* 1. HEADER BANNER UTAMA                                                    */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-20 bg-slate-50/70 border-b border-slate-200 text-center">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          <div className="max-w-4xl mx-auto space-y-3">
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Kepatuhan Mutu, Legalitas &amp; Komitmen Lingkungan (ESG)
            </h1>

            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl mx-auto font-normal">
              Standarisasi kendali mutu terpadu dari pengujian bahan baku murni, proses reaksi di tangki Stainless Steel 316L, hingga sertifikasi keamanan lingkungan di fasilitas Mojoroto, Kediri.
            </p>

            {/* Quick Validation Highlights Row */}
            <div className="pt-4 flex items-center justify-center flex-wrap gap-4 text-xs font-bold text-slate-800">
              <span className="flex items-center gap-1.5">
                <Award className="w-4 h-4 text-[#0F58A8]" />
                <span>ISO 9001:2015 QMS Ready</span>
              </span>
              <span className="text-slate-300">•</span>
              <span className="flex items-center gap-1.5">
                <Leaf className="w-4 h-4 text-emerald-600" />
                <span>100% Bebas Fosfat / STPP</span>
              </span>
              <span className="text-slate-300">•</span>
              <span className="flex items-center gap-1.5">
                <ShieldAlert className="w-4 h-4 text-amber-600" />
                <span>Standar K3L &amp; GHS Safety</span>
              </span>
              <span className="text-slate-300">•</span>
              <span className="flex items-center gap-1.5">
                <Building2 className="w-4 h-4 text-blue-600" />
                <span>KBLI 20231 &amp; Siap LKPP RI</span>
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 2. STANDAR MANAJEMEN MUTU ISO 9001:2015 & SISTEM QC BERTINGKAT            */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-white text-slate-900 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Section Heading */}
          <div className="max-w-3xl space-y-2">
            <h2 className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Standar Manajemen Mutu ISO 9001:2015 &amp; Prosedur Uji Bertingkat
            </h2>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
              Setiap batch formula kimia pembersih di fasilitas PT Kediri Chemical Abadi diproduksi di bawah kendali mutu terstruktur. Kami menerapkan Standard Operating Procedure (SOP) pengujian laboratorium mulai dari verifikasi bahan baku masuk, pemantauan homogenitas saat pencampuran reaktor Stainless Steel 316L, hingga analisis akhir sebelum produk diloloskan ke gudang distribusi.
            </p>
          </div>

          {/* Integrated Editorial Grid (No Boxed Cards) */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-start pt-2">
            
            {/* Sisi Kiri: Tabel Parameter Uji Analitik Laboratorium (7 Kolom) */}
            <div className="lg:col-span-7 space-y-6">
              <span className="text-xs font-extrabold uppercase tracking-wider text-slate-900 block border-b border-slate-200 pb-2">
                Parameter Pengujian Fisik &amp; Kimia Laboratorium
              </span>

              <div className="divide-y divide-slate-200 border-y border-slate-200">
                <div className="py-3.5 grid grid-cols-1 sm:grid-cols-12 gap-2 sm:gap-4 items-start">
                  <div className="sm:col-span-4 flex items-center gap-2 text-[#0F58A8]">
                    <Scale className="w-4 h-4 shrink-0" />
                    <strong className="text-xs font-bold text-slate-900">Titrasi pH Digital</strong>
                  </div>
                  <div className="sm:col-span-8 text-xs text-slate-600 leading-relaxed">
                    Pengukuran elektroda pH meter digital akurasi ±0.01 (Metode ASTM D1172) untuk menjamin netralitas serat kain linen atau konsistensi daya alkali pembersih.
                  </div>
                </div>

                <div className="py-3.5 grid grid-cols-1 sm:grid-cols-12 gap-2 sm:gap-4 items-start">
                  <div className="sm:col-span-4 flex items-center gap-2 text-[#0F58A8]">
                    <Droplets className="w-4 h-4 shrink-0" />
                    <strong className="text-xs font-bold text-slate-900">Berat Jenis &amp; Viskositas</strong>
                  </div>
                  <div className="sm:col-span-8 text-xs text-slate-600 leading-relaxed">
                    Uji viskosimeter Brookfield (ASTM D2196) dan piknometer densitas presisi 20°C guna memastikan kelancaran pompa dosing otomatis mesin cuci komersial.
                  </div>
                </div>

                <div className="py-3.5 grid grid-cols-1 sm:grid-cols-12 gap-2 sm:gap-4 items-start">
                  <div className="sm:col-span-4 flex items-center gap-2 text-[#0F58A8]">
                    <FlaskConical className="w-4 h-4 shrink-0" />
                    <strong className="text-xs font-bold text-slate-900">Stabilitas Suhu 45°C</strong>
                  </div>
                  <div className="sm:col-span-8 text-xs text-slate-600 leading-relaxed">
                    Uji inkubasi termal akselerasi oven 45°C selama 30 hari untuk memastikan formula tidak memisah, tidak mengendap, dan aroma tetap stabil pada suhu ruang tropis.
                  </div>
                </div>

                <div className="py-3.5 grid grid-cols-1 sm:grid-cols-12 gap-2 sm:gap-4 items-start">
                  <div className="sm:col-span-4 flex items-center gap-2 text-[#0F58A8]">
                    <Microscope className="w-4 h-4 shrink-0" />
                    <strong className="text-xs font-bold text-slate-900">Uji Surfaktan Aktif</strong>
                  </div>
                  <div className="sm:col-span-8 text-xs text-slate-600 leading-relaxed">
                    Analisis kuantitatif kadar bahan aktif surfaktan (Total Active Matter) dengan metode titrasi dua fase (ISO 2271) untuk memastikan daya angkat noda optimal.
                  </div>
                </div>
              </div>

              {/* Poin Pengarsipan & COA */}
              <div className="space-y-2 pt-2 text-xs text-slate-700">
                <div className="flex items-start gap-2.5">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                  <div>
                    <strong className="font-bold text-slate-900">Sistem Retained Sample 12 Bulan:</strong>
                    <span className="text-slate-600 ml-1">Sampel arsip berlabel lot produksi disimpan di ruang berpendingin khusus minimal 1 tahun untuk keperluan uji banding berkala.</span>
                  </div>
                </div>

                <div className="flex items-start gap-2.5">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                  <div>
                    <strong className="font-bold text-slate-900">Penerbitan COA Resmi (Certificate of Analysis):</strong>
                    <span className="text-slate-600 ml-1">Dokumen COA bertandatangan Kepala Laboratorium QC diterbitkan menyertai setiap lot pengiriman ke mitra industri.</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Sisi Kanan: Alur Dokumentasi SOP Kendali Mutu (5 Kolom) */}
            <div className="lg:col-span-5 space-y-6">
              <span className="text-xs font-extrabold uppercase tracking-wider text-slate-900 block border-b border-slate-200 pb-2">
                Alur Dokumentasi SOP Kendali Mutu
              </span>

              <div className="space-y-4 pl-3 border-l-2 border-slate-200 text-xs">
                <div className="relative space-y-0.5">
                  <span className="text-[10px] font-mono font-bold text-[#0F58A8] block">
                    SOP-KCA-QC-01
                  </span>
                  <strong className="text-slate-900 block font-bold text-xs">
                    Verifikasi Bahan Baku Masuk (Raw Material Inspection)
                  </strong>
                  <p className="text-slate-600 leading-relaxed">
                    Pemeriksaan COA vendor, uji kemurnian visual, dan titrasi konsentrasi bahan kimia dasar sebelum masuk tangki penampungan.
                  </p>
                </div>

                <div className="relative space-y-0.5 pt-2">
                  <span className="text-[10px] font-mono font-bold text-[#0F58A8] block">
                    SOP-KCA-QC-02
                  </span>
                  <strong className="text-slate-900 block font-bold text-xs">
                    Monitoring Reaksi Reaktor SS 316L (In-Process Control)
                  </strong>
                  <p className="text-slate-600 leading-relaxed">
                    Pengawasan kecepatan putar agitator (RPM), kestabilan temperatur jaket pemanas/pendingin, dan waktu reaksi pelarutan batch.
                  </p>
                </div>

                <div className="relative space-y-0.5 pt-2">
                  <span className="text-[10px] font-mono font-bold text-[#0F58A8] block">
                    SOP-KCA-QC-03
                  </span>
                  <strong className="text-slate-900 block font-bold text-xs">
                    Filtrasi &amp; Sampling Produk Akhir (Finished Goods QC)
                  </strong>
                  <p className="text-slate-600 leading-relaxed">
                    Proses penyaringan mikro partikel asing, sampling homogenitas cairan, dan pengujian laboratorium komprehensif.
                  </p>
                </div>

                <div className="relative space-y-0.5 pt-2">
                  <span className="text-[10px] font-mono font-bold text-emerald-700 block">
                    SOP-KCA-QC-04
                  </span>
                  <strong className="text-slate-900 block font-bold text-xs">
                    Penerbitan COA &amp; Batch Release
                  </strong>
                  <p className="text-slate-600 leading-relaxed">
                    Pemberian kode lot unik pada setiap kemasan, rilis sertifikat analisis resmi (COA), dan pengarsipan retained sample.
                  </p>
                </div>
              </div>
            </div>

          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. KOMITMEN 100% NON-FOSFAT & KELAYAKAN IPAL MEDIS / KARS                  */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-slate-50/50 text-slate-900 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Section Heading */}
          <div className="max-w-3xl space-y-2">
            <h2 className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Komitmen 100% Non-Fosfat &amp; Kelayakan IPAL Medis / Industri
            </h2>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
              Formula pembersih KCA secara ketat tidak menggunakan senyawa fosfat (Sodium Tripolyphosphate / STPP). Penggunaan senyawa fosfat dalam deterjen konvensional merupakan penyebab utama terjadinya ledakan pertumbuhan alga (eutrofikasi) yang menghabiskan oksigen terlarut dan merusak bakteri pengurai pada instalasi pengolahan air limbah (IPAL).
            </p>
          </div>

          {/* Detailed Comparative Table */}
          <div className="space-y-4">
            <span className="text-xs font-extrabold uppercase tracking-wider text-slate-900 block border-b border-slate-200 pb-2">
              Matriks Perbandingan Dampak Lingkungan Formula KCA vs Deterjen Konvensional
            </span>

            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left border-collapse">
                <thead>
                  <tr className="border-b border-slate-300 text-slate-500 uppercase tracking-wider text-[10px]">
                    <th className="py-3 px-4 font-bold">Parameter Lingkungan</th>
                    <th className="py-3 px-4 font-bold text-[#0F58A8]">Formulasi PT Kediri Chemical Abadi</th>
                    <th className="py-3 px-4 font-bold text-slate-700">Deterjen Konvensional Pasaran</th>
                    <th className="py-3 px-4 font-bold">Dampak Terhadap IPAL / Lingkungan</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-200 text-slate-800">
                  <tr className="hover:bg-slate-50">
                    <td className="py-3.5 px-4 font-bold text-slate-900">Kandungan Fosfat (STPP)</td>
                    <td className="py-3.5 px-4 font-bold text-emerald-700">0.00% (Bebas Fosfat Murni)</td>
                    <td className="py-3.5 px-4 text-rose-700 font-semibold">15% – 30% Senyawa Fosfat</td>
                    <td className="py-3.5 px-4 text-slate-600">Mencegah ledakan alga (eutrofikasi) dan pendangkalan sungai.</td>
                  </tr>
                  <tr className="hover:bg-slate-50">
                    <td className="py-3.5 px-4 font-bold text-slate-900">Biodegradabilitas (OECD 301D)</td>
                    <td className="py-3.5 px-4 font-bold text-emerald-700">&gt;90% Terurai Alami (28 Hari)</td>
                    <td className="py-3.5 px-4 text-slate-600">&lt;60% Residu Kimia Persisten</td>
                    <td className="py-3.5 px-4 text-slate-600">Surfaktan cepat diurai oleh mikroorganisme pengurai tanah &amp; air.</td>
                  </tr>
                  <tr className="hover:bg-slate-50">
                    <td className="py-3.5 px-4 font-bold text-slate-900">Beban Organik (BOD &amp; COD)</td>
                    <td className="py-3.5 px-4 font-bold text-emerald-700">Rendah (Low Chemical Oxygen Demand)</td>
                    <td className="py-3.5 px-4 text-rose-700 font-semibold">Tinggi (Beban Bio-Digester Berat)</td>
                    <td className="py-3.5 px-4 text-slate-600">Menjaga kadar Chemical Oxygen Demand buangan di bawah baku mutu Permen LHK.</td>
                  </tr>
                  <tr className="hover:bg-slate-50">
                    <td className="py-3.5 px-4 font-bold text-slate-900">Kelayakan IPAL RS (KARS)</td>
                    <td className="py-3.5 px-4 font-bold text-emerald-700">100% Aman Bakteri Aerob/Anaerob</td>
                    <td className="py-3.5 px-4 text-slate-600">Berisiko Mematikan Bio-Filter</td>
                    <td className="py-3.5 px-4 text-slate-600">Lolos audit akreditasi mutu sanitasi rumah sakit tipe A, B, dan C.</td>
                  </tr>
                  <tr className="hover:bg-slate-50">
                    <td className="py-3.5 px-4 font-bold text-slate-900">Karakteristik Busa (Foam Profile)</td>
                    <td className="py-3.5 px-4 font-bold text-emerald-700">Low-Foam (Busa Terkendali Presisi)</td>
                    <td className="py-3.5 px-4 text-slate-600">High-Foam (Busa Meluap)</td>
                    <td className="py-3.5 px-4 text-slate-600">Hemat konsumsi air bilasan hingga 30% dan meringankan kerja motor mesin cuci.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 4. KESELAMATAN, KESEHATAN KERJA & LINGKUNGAN (K3L & GHS SAFETY)            */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-white text-slate-900 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Section Heading */}
          <div className="max-w-3xl space-y-2">
            <h2 className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Keselamatan, Kesehatan Kerja &amp; Lingkungan (K3L &amp; GHS Safety)
            </h2>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
              Keselamatan tenaga kerja teknis dan integritas lingkungan produksi merupakan pilar fundamental operasi pabrik kami. Seluruh area reaktor pencampuran, penyimpanan konsentrat asam/basa, serta gudang bahan pelarut didesain mengikuti standar keselamatan industri kimia modern dengan zonasi bahaya terpadu.
            </p>
          </div>

          {/* Integrated 3-Column Specifications */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 sm:gap-10 pt-2 border-t border-slate-200">
            
            <div className="space-y-2.5">
              <div className="flex items-center gap-2 text-amber-700">
                <ShieldAlert className="w-4 h-4" />
                <strong className="text-xs font-bold font-heading text-slate-900">
                  Instalasi Tanggap Darurat Pabrik
                </strong>
              </div>
              <p className="text-xs text-slate-600 leading-relaxed">
                Stasiun darurat pencuci mata (emergency eye-washer) dan shower dekontaminasi air bertekanan terpasang di setiap area reaktor. Dilengkapi bak penampung tumpahan sekunder (secondary containment bund) dan perlengkapan spill kit penetralisir bahan kimia.
              </p>
            </div>

            <div className="space-y-2.5">
              <div className="flex items-center gap-2 text-amber-700">
                <FileText className="w-4 h-4" />
                <strong className="text-xs font-bold font-heading text-slate-900">
                  Dokumen MSDS 16 Bab Standar GHS
                </strong>
              </div>
              <p className="text-xs text-slate-600 leading-relaxed">
                Setiap formula disertai Lembar Data Keselamatan Bahan (Material Safety Data Sheet) resmi 16 bab berbahasa Indonesia dan Inggris sesuai Globally Harmonized System, lengkap dengan identifikasi bahaya, petunjuk P3K, dan tindakan penanggulangan kebakaran.
              </p>
            </div>

            <div className="space-y-2.5">
              <div className="flex items-center gap-2 text-amber-700">
                <Layers className="w-4 h-4" />
                <strong className="text-xs font-bold font-heading text-slate-900">
                  Zonasi APD &amp; Ventilasi Aktif
                </strong>
              </div>
              <p className="text-xs text-slate-600 leading-relaxed">
                Kewajiban penggunaan Alat Pelindung Diri (respirator uap kimia, sarung tangan nitril, goggle safety, dan safety shoes). Ruang pencampuran didukung sirkulasi exhaust fan aktif untuk menjamin kualitas udara ruang kerja di bawah Nilai Ambang Batas (NAB).
              </p>
            </div>

          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 5. LEGALITAS BADAN USAHA, IZIN KEMENKES & LKPP RI                          */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-slate-50/50 text-slate-900 border-b border-slate-200">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Section Heading */}
          <div className="max-w-3xl space-y-2">
            <h2 className="text-xl sm:text-2xl lg:text-3xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Legalitas Badan Usaha, Sertifikasi PKRT &amp; Terdaftar LKPP RI
            </h2>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
              PT Kediri Chemical Abadi beroperasi secara sah dan patuh terhadap regulasi hukum Republik Indonesia. Dengan perizinan NIB Berbasis Risiko dari Kementerian Investasi/BKPM, kami memenuhi kualifikasi legalitas penuh untuk pengadaan barang/jasa instansi pemerintah, RSUD daerah, BUMN, maupun tender korporasi swasta berskala nasional.
            </p>
          </div>

          {/* Integrated Corporate Legal Matrix */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-2 border-t border-slate-200">
            <div className="space-y-1.5 border-l-2 border-blue-600 pl-3.5">
              <span className="text-[10px] uppercase font-bold text-slate-400 block tracking-wider">
                Entitas Korporasi
              </span>
              <strong className="text-xs font-bold text-slate-900 block">PT KEDIRI CHEMICAL ABADI</strong>
              <p className="text-[11px] text-slate-600">Didirikan tahun 2004 di Mojoroto, Kediri, Jawa Timur.</p>
            </div>

            <div className="space-y-1.5 border-l-2 border-blue-600 pl-3.5">
              <span className="text-[10px] uppercase font-bold text-slate-400 block tracking-wider">
                Klasifikasi Usaha (KBLI)
              </span>
              <strong className="text-xs font-bold text-slate-900 block">KBLI 20231 &amp; 20232</strong>
              <p className="text-[11px] text-slate-600">Industri Sabun, Bahan Pembersih, &amp; Toll Compounding Kimia.</p>
            </div>

            <div className="space-y-1.5 border-l-2 border-blue-600 pl-3.5">
              <span className="text-[10px] uppercase font-bold text-slate-400 block tracking-wider">
                Administrasi Fiskal
              </span>
              <strong className="text-xs font-bold text-slate-900 block">Pengusaha Kena Pajak (PKP)</strong>
              <p className="text-[11px] text-slate-600">Penerbitan e-Faktur resmi PPN 11% tertib pajak.</p>
            </div>

            <div className="space-y-1.5 border-l-2 border-blue-600 pl-3.5">
              <span className="text-[10px] uppercase font-bold text-slate-400 block tracking-wider">
                Pengadaan Pemerintah
              </span>
              <strong className="text-xs font-bold text-slate-900 block">Siap e-Katalog LKPP RI</strong>
              <p className="text-[11px] text-slate-600">Memenuhi syarat penyedia pengadaan RSUD &amp; instansi negara.</p>
            </div>
          </div>

        </div>
      </section>

      {/* ========================================================================= */}
      {/* 6. ALUR KENDALI MUTU PRODUKSI (QC) KCA (DIAGRAM 3-TIER PERSIS SERVICES)   */}
      {/* ========================================================================= */}
      <section className="py-20 sm:py-28 bg-slate-50/50 text-slate-900 border-b border-slate-200 relative overflow-hidden">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-12">
          
          {/* Header Diagram */}
          <div className="text-center max-w-3xl mx-auto space-y-2">
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-black font-heading text-slate-900 tracking-tight">
              ALUR KENDALI MUTU PRODUKSI (QC) KCA
            </h2>
            <p className="text-sm sm:text-base text-slate-600 font-medium">
              Dari Verifikasi Bahan Baku Murni hingga Penerbitan COA &amp; Pengiriman Batch
            </p>
          </div>

          {/* Diagram Container */}
          <div className="space-y-6">

            {/* ------------------------------------------------------------- */}
            {/* 1. TOP ROW: 5 CONNECTED STAGE CARDS (FLUID WATER THEME)       */}
            {/* ------------------------------------------------------------- */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3.5 sm:gap-4 relative items-stretch">
              {QC_STEPS.map((step, idx) => {
                const IconComp = step.icon
                const isNotLast = idx < QC_STEPS.length - 1

                return (
                  <motion.div
                    key={idx}
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, margin: "-40px" }}
                    whileHover={{ y: -6, transition: { type: 'spring', stiffness: 350, damping: 22 } }}
                    transition={{ duration: 0.6, delay: idx * 0.09, ease: [0.16, 1, 0.3, 1] }}
                    className="bg-white rounded-xl p-4 sm:p-6 border border-slate-200/90 shadow-xs hover:shadow-md transition-all flex flex-col justify-between space-y-3.5 sm:space-y-5 relative group"
                  >
                    {/* Circle Number Badge (Top Left) */}
                    <div className="flex items-center justify-between">
                      <div className={`w-7 h-7 rounded-md ${step.badgeBg} text-white flex items-center justify-center font-mono font-bold text-xs shadow-xs`}>
                        {step.step}
                      </div>
                    </div>

                    {/* Centered Large Icon */}
                    <div className="flex flex-col items-center text-center space-y-3 pt-1">
                      <div className={`w-11 h-11 sm:w-14 sm:h-14 rounded-lg ${step.iconContainerBg} border flex items-center justify-center group-hover:scale-105 transition-transform shadow-2xs`}>
                        <IconComp className={`w-6 h-6 sm:w-8 sm:h-8 ${step.textColor}`} />
                      </div>

                      {/* Phase Tag */}
                      <span className={`text-[10px] font-extrabold uppercase tracking-wider ${step.textColor} block bg-sky-50 px-2.5 py-0.5 rounded-full font-mono`}>
                        {step.phase}
                      </span>

                      {/* Step Title */}
                      <h3 className="text-xs sm:text-base font-extrabold font-heading text-slate-900 leading-tight">
                        {step.title}
                      </h3>

                      {/* Step Description */}
                      <p className="text-[11px] sm:text-xs text-slate-600 leading-relaxed font-normal">
                        {step.desc}
                      </p>
                    </div>

                    {/* Checklist Activities */}
                    <div className="space-y-2 pt-3 border-t border-sky-100 text-left">
                      {step.points.map((pt, pIdx) => (
                        <div key={pIdx} className="flex items-start gap-2 text-xs text-slate-700">
                          <div className="w-4 h-4 rounded-full bg-blue-50 text-[#0F58A8] flex items-center justify-center shrink-0 mt-0.5">
                            <CheckCircle2 className="w-3.5 h-3.5" />
                          </div>
                          <span className="leading-snug font-medium">{pt}</span>
                        </div>
                      ))}
                    </div>

                    {/* Directional Connector Arrow Node (Desktop Only) */}
                    {isNotLast && (
                      <div className="hidden lg:flex absolute -right-3.5 top-1/2 -translate-y-1/2 z-20 w-7 h-7 rounded-full bg-white border border-sky-200 shadow-md items-center justify-center pointer-events-none">
                        <div className={`w-5 h-5 rounded-full ${step.badgeBg} text-white flex items-center justify-center`}>
                          <ArrowRight className="w-3 h-3 stroke-[2.5]" />
                        </div>
                      </div>
                    )}
                  </motion.div>
                )
              })}
            </div>

            {/* ------------------------------------------------------------- */}
            {/* 2. MIDDLE ROW: HASIL TAHAPAN (CONNECTED DELIVERABLES)         */}
            {/* ------------------------------------------------------------- */}
            <div className="bg-white rounded-xl border border-slate-200/90 p-4 sm:p-5 shadow-sm flex flex-col lg:flex-row items-stretch lg:items-center gap-4">
              
              {/* Left Badge Ribbon */}
              <div className="bg-[#0A192F] text-white px-5 py-3 rounded-lg flex items-center justify-center shrink-0 lg:w-36 text-center shadow-xs">
                <span className="font-heading font-black text-xs uppercase tracking-wider block">
                  HASIL<br className="hidden lg:block" /> TAHAPAN
                </span>
              </div>

              {/* 5 Connected Deliverable Output Cards */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 flex-1 items-center">
                {QC_STEPS.map((step, idx) => {
                  const DelivIcon = step.deliverableIcon
                  const isNotLast = idx < QC_STEPS.length - 1

                  return (
                    <div key={idx} className="flex items-center gap-2">
                      <div className="p-3 rounded-lg bg-slate-50 border border-slate-200/80 flex items-center gap-2.5 flex-1 min-h-[58px]">
                        <div className={`w-8 h-8 rounded-xl bg-white border border-sky-100 flex items-center justify-center shrink-0 ${step.textColor}`}>
                          <DelivIcon className="w-4 h-4" />
                        </div>
                        <span className="text-xs font-bold text-slate-800 leading-tight font-heading">
                          {step.deliverable}
                        </span>
                      </div>

                      {/* Dashed Arrow Connector */}
                      {isNotLast && (
                        <div className="hidden lg:flex items-center justify-center text-slate-400 shrink-0 px-0.5">
                          <ArrowRight className="w-3.5 h-3.5 text-slate-400" />
                        </div>
                      )}
                    </div>
                  )
                })}
              </div>
            </div>

            {/* ------------------------------------------------------------- */}
            {/* 3. BOTTOM ROW: PRINSIP PENDUKUNG (CORE PILLARS)              */}
            {/* ------------------------------------------------------------- */}
            <div className="bg-white rounded-xl border border-slate-200/90 p-4 sm:p-5 shadow-sm flex flex-col lg:flex-row items-stretch lg:items-center gap-4">
              
              {/* Left Badge Ribbon */}
              <div className="bg-slate-900 text-white px-5 py-3 rounded-2xl flex items-center justify-center shrink-0 lg:w-36 text-center shadow-xs">
                <span className="font-heading font-black text-xs uppercase tracking-wider block">
                  PRINSIP<br className="hidden lg:block" /> PENDUKUNG
                </span>
              </div>

              {/* 5 Principles Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 flex-1">
                {QC_PRINCIPLES.map((pr, idx) => {
                  const Icon = pr.icon
                  return (
                    <div key={idx} className="flex items-start gap-3 p-2.5 rounded-lg">
                      <div className={`p-2 rounded-xl bg-sky-50 border border-sky-100 shrink-0 ${pr.iconColor}`}>
                        <Icon className="w-4 h-4" />
                      </div>
                      <div className="space-y-0.5 min-w-0">
                        <strong className="text-xs font-extrabold font-heading text-slate-900 block truncate">
                          {pr.title}
                        </strong>
                        <p className="text-[11px] text-slate-600 leading-relaxed font-normal">
                          {pr.desc}
                        </p>
                      </div>
                    </div>
                  )
                })}
              </div>
            </div>

            {/* ------------------------------------------------------------- */}
            {/* 4. BOTTOM BRAND FOOTER BADGE CAPSULE                          */}
            {/* ------------------------------------------------------------- */}
            <div className="flex justify-center pt-2">
              <div className="inline-flex items-center gap-3 px-6 py-2.5 rounded-full bg-white border border-sky-100 text-slate-800 text-xs shadow-2xs">
                <ShieldCheck className="w-4 h-4 text-[#0F58A8]" />
                <span className="font-extrabold font-heading text-slate-900 tracking-wide">
                  PT KEDIRI CHEMICAL ABADI
                </span>
                <span className="text-slate-300 hidden sm:inline">•</span>
                <span className="text-slate-600 font-normal hidden sm:inline">
                  Standar Mutu ISO 9001:2015 &amp; Jaminan Kualitas Formula Presisi
                </span>
              </div>
            </div>

          </div>

        </div>
      </section>

      {/* Full Width CTA Section */}
      <CTASection />
    </main>
  )
}
