import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { ShieldCheck, Lock, FileText, CheckCircle2 } from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import CTASection from '@/components/sections/CTASection'

export default function PrivacyPolicyPage() {
  const waDisplay = COMPANY_DATA.contacts?.whatsappDisplay || '085812307629'

  return (
    <main className="bg-white text-slate-900 pt-20">
      <Helmet>
        <title>Kebijakan Privasi & Klausul Kerahasiaan (NDA) — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Perlindungan kerahasiaan formula mitra maklon (Non-Disclosure Agreement) dan kepatuhan terhadap UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi (UU PDP)."
        />
      </Helmet>

      {/* Header Banner */}
      <section className="py-16 sm:py-20 bg-slate-50/70 border-b border-slate-200 text-center">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-12 w-full">
          <div className="max-w-3xl mx-auto space-y-3">
            <span className="text-xs font-extrabold tracking-widest text-[#0F58A8] uppercase block">
              KERAHASIAAN FORMULA & DATA KORPORAT
            </span>

            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight">
              Kebijakan Privasi & Perjanjian Kerahasiaan (NDA)
            </h1>

            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl mx-auto font-normal">
              Komitmen legal PT Kediri Chemical Abadi dalam melindungi kerahasiaan resep formula mitra maklon private label dan integritas data korespondensi bisnis B2B.
            </p>
          </div>
        </div>
      </section>

      {/* Content Section */}
      <section className="py-20 sm:py-24 bg-white text-slate-900 border-b border-slate-200">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-12 w-full space-y-12">
          
          {/* Section 1: NDA Formula */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="bg-slate-50 rounded-3xl p-6 sm:p-8 border border-slate-200 space-y-4 shadow-xs"
          >
            <div className="flex items-center gap-3 text-[#0F58A8] text-xs font-bold uppercase">
              <ShieldCheck className="w-5 h-5" />
              <span>1. Perlindungan Formula Mitra Maklon (Non-Disclosure Agreement)</span>
            </div>
            <p className="text-sm text-slate-700 leading-relaxed">
              Seluruh resep khusus, spesifikasi bahan aktif, rasio konsentrat, aroma, dan rancangan kemasan yang dikembangkan bersama atau diserahkan oleh mitra kepada PT Kediri Chemical Abadi dilindungi penuh di bawah perjanjian Non-Disclosure Agreement (NDA) yang mengikat secara hukum.
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
              <div className="flex items-start gap-2.5 p-3 rounded-xl bg-white border border-slate-200 text-xs text-slate-700">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <span>Formula tidak akan direplikasi atau dijual ke pihak ketiga.</span>
              </div>
              <div className="flex items-start gap-2.5 p-3 rounded-xl bg-white border border-slate-200 text-xs text-slate-700">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <span>Akses formula di laboratorium dibatasi hanya untuk staf QC berwenang.</span>
              </div>
            </div>
          </motion.div>

          {/* Section 2: UU PDP */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="bg-slate-50 rounded-3xl p-6 sm:p-8 border border-slate-200 space-y-4 shadow-xs"
          >
            <div className="flex items-center gap-3 text-[#0F58A8] text-xs font-bold uppercase">
              <FileText className="w-5 h-5" />
              <span>2. Kepatuhan Undang-Undang Perlindungan Data Pribadi (UU PDP)</span>
            </div>
            <p className="text-sm text-slate-700 leading-relaxed">
              Sesuai Undang-Undang No. 27 Tahun 2022 tentang Perlindungan Data Pribadi (UU PDP), data kontak PIC korporat (nama, email, nomor WhatsApp, nama instansi) yang dikirimkan melalui formulir tender RFQ hanya dipergunakan semata-mata untuk keperluan korespondensi resmi penawaran harga pabrik dan tidak akan dialihkan kepada pihak lain tanpa persetujuan tertulis.
            </p>
          </motion.div>

          {/* Section 3: Keamanan Server & Data */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="bg-slate-50 rounded-3xl p-6 sm:p-8 border border-slate-200 space-y-4 shadow-xs"
          >
            <div className="flex items-center gap-3 text-[#0F58A8] text-xs font-bold uppercase">
              <Lock className="w-5 h-5" />
              <span>3. Keamanan Transmisi & Enkripsi Data</span>
            </div>
            <p className="text-sm text-slate-700 leading-relaxed">
              Website korporat kami menggunakan protokol enkripsi standar industri TLS 1.3 dengan sertifikat SSL aktif untuk menjamin setiap transmisi data korespondensi aman dari intersepsi pihak luar.
            </p>
          </motion.div>

          {/* Legal Sign-off */}
          <div className="p-6 rounded-2xl bg-slate-50 border border-slate-200 text-xs text-slate-600 space-y-1">
            <span className="block text-slate-900 font-bold uppercase">Kontak Penanggung Jawab Privasi & Legal:</span>
            <span>Direksi Legal & Kepatuhan: {COMPANY_DATA.boardOfDirectors[1].name}</span>
            <br />
            <span>Email Resmi: {COMPANY_DATA.contacts?.email} | WhatsApp: +62 {waDisplay}</span>
          </div>

        </div>
      </section>

      <CTASection />
    </main>
  )
}
