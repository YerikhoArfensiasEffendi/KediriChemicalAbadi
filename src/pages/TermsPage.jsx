import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { FileCheck, ShieldAlert, Truck, RefreshCw, CheckCircle2 } from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import CTASection from '@/components/sections/CTASection'

export default function TermsPage() {
  const waDisplay = COMPANY_DATA.contacts?.whatsappDisplay || '085812307629'

  return (
    <main className="bg-white text-slate-900 pt-20">
      <Helmet>
        <title>Syarat & Ketentuan Pasokan B2B — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Standar operasional perdagangan B2B, toleransi deviasi mutu batch QC, ketentuan penyerahan Loco/Franco Pabrik, dan garansi penggantian batch."
        />
      </Helmet>

      {/* Header Banner */}
      <section className="py-16 sm:py-20 bg-slate-50/70 border-b border-slate-200 text-center">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-12 w-full">
          <div className="max-w-3xl mx-auto space-y-3">
            <span className="text-xs font-extrabold tracking-widest text-[#0F58A8] uppercase block">
              SYARAT & KETENTUAN OPERASIONAL B2B
            </span>

            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight">
              Syarat & Ketentuan Pasokan Kimia Industri
            </h1>

            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl mx-auto font-normal">
              Standar tata kelola perdagangan dan kontrak pengadaan massal yang berlaku di fasilitas produksi PT Kediri Chemical Abadi, Kota Kediri.
            </p>
          </div>
        </div>
      </section>

      {/* Content */}
      <section className="py-20 sm:py-24 bg-white text-slate-900 border-b border-slate-200">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-12 w-full space-y-10">
          
          {/* Item 1: Standar QC & Toleransi Mutu */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="bg-slate-50 rounded-3xl p-6 sm:p-8 border border-slate-200 space-y-4 shadow-xs"
          >
            <div className="flex items-center gap-3 text-[#0F58A8] text-xs font-bold uppercase">
              <FileCheck className="w-5 h-5" />
              <span>1. Standar Kontrol Mutu & Toleransi Batch QC</span>
            </div>
            <p className="text-sm text-slate-700 leading-relaxed">
              Setiap lot produksi kimia diuji sebelum keluar dari fasilitas pabrik Mojoroto. Deviasi parameter fisik (pH digital: ±0.3, Berat Jenis: ±0.02 g/cm³, Viskositas: ±5%) diakui sebagai batas toleransi teknis yang sah sesuai Certificate of Analysis (COA) resmi.
            </p>
          </motion.div>

          {/* Item 2: Ketentuan Penyerahan Loco / Franco */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="bg-slate-50 rounded-3xl p-6 sm:p-8 border border-slate-200 space-y-4 shadow-xs"
          >
            <div className="flex items-center gap-3 text-[#0F58A8] text-xs font-bold uppercase">
              <Truck className="w-5 h-5" />
              <span>2. Mekanisme Penyerahan Barang (Incoterms Loco / Franco)</span>
            </div>
            <p className="text-sm text-slate-700 leading-relaxed">
              Penyerahan pesanan dapat disepakati berdasarkan skema Loco Pabrik (pengambilan mandiri di gudang KCA Kediri) atau Franco Gudang Pembeli (pengiriman difasilitasi armada ekspedisi rekanan dengan biaya terhitung resmi dalam Purchase Order).
            </p>
          </motion.div>

          {/* Item 3: Garansi Penggantian Batch */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="bg-slate-50 rounded-3xl p-6 sm:p-8 border border-slate-200 space-y-4 shadow-xs"
          >
            <div className="flex items-center gap-3 text-[#0F58A8] text-xs font-bold uppercase">
              <RefreshCw className="w-5 h-5" />
              <span>3. Kebijakan Garansi & Penggantian Batch (Batch Replacement)</span>
            </div>
            <p className="text-sm text-slate-700 leading-relaxed">
              Apabila terdapat ketidaksesuaian spesifikasi produk terhadap COA yang terbukti secara laboratoris dalam waktu 7 (tujuh) hari kerja sejak barang diterima, PT Kediri Chemical Abadi memberikan jaminan penggantian batch 100% tanpa biaya tambahan.
            </p>
            <div className="p-3 bg-white rounded-xl border border-slate-200 flex items-center gap-2 text-xs text-emerald-700 font-semibold">
              <CheckCircle2 className="w-4 h-4 shrink-0 text-emerald-600" />
              <span>Jaminan Mutu Teruji • Retained Sample Disimpan 12 Bulan</span>
            </div>
          </motion.div>

          {/* Sign-off */}
          <div className="p-6 rounded-2xl bg-slate-50 border border-slate-200 text-xs text-slate-600 space-y-1">
            <span className="block text-slate-900 font-bold uppercase">Manajemen Pabrik & Penjualan B2B:</span>
            <span>{COMPANY_DATA.legalName} • Plant Mojoroto, Kediri</span>
            <br />
            <span>Hotline Resmi: +62 {waDisplay} | Email: {COMPANY_DATA.contacts?.email}</span>
          </div>

        </div>
      </section>

      <CTASection />
    </main>
  )
}
