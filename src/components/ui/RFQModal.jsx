import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { X, Send, Factory, ShieldCheck } from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'

export default function RFQModal({ isOpen, onClose }) {
  const [formData, setFormData] = useState({
    name: '',
    role: '',
    company: '',
    sector: 'Commercial Laundry & Tekstil',
    service: 'Jasa Maklon Dedicated Line (Investasi Mesin Khusus) - Unggulan',
    volume: '1 - 5 Ton / Bulan',
    whatsapp: '',
    notes: '',
  })
  const [submitted, setSubmitted] = useState(false)

  // ESC key to close
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') onClose()
    }
    if (isOpen) {
      document.body.style.overflow = 'hidden'
      window.addEventListener('keydown', handleKeyDown)
    }
    return () => {
      document.body.style.overflow = 'unset'
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [isOpen, onClose])

  const handleSubmit = (e) => {
    e.preventDefault()
    setSubmitted(true)

    const text = `*PERMINTAAN PENAWARAN RESMI (RFQ) — PT KEDIRI CHEMICAL ABADI*
----------------------------------------
*Nama PIC:* ${formData.name} (${formData.role || 'Manajemen'})
*Perusahaan / RS / Hotel:* ${formData.company}
*Sektor Industri:* ${formData.sector}
*Pilihan Skema / Layanan:* ${formData.service}
*Estimasi Volume Bulanan:* ${formData.volume}
*Nomor WhatsApp PIC:* ${formData.whatsapp}

*Catatan / Spesifikasi Kebutuhan:*
${formData.notes || 'Mohon kirimkan katalog resmi dan penawaran harga pabrik.'}
----------------------------------------
_Dikirim melalui Portal Resmi PT Kediri Chemical Abadi (kedirichemical.com)_`

    const waNumber = COMPANY_DATA.contacts?.whatsappNumber || '6285812307629'
    const waUrl = `https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`

    setTimeout(() => {
      window.open(waUrl, '_blank')
      setSubmitted(false)
      onClose()
    }, 500)
  }

  if (!isOpen) return null

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-[100] flex items-center justify-center p-2.5 sm:p-6 overflow-y-auto">
        {/* Dark Backdrop */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm"
          onClick={onClose}
        />

        {/* Modal Window */}
        <motion.div
          initial={{ opacity: 0, scale: 0.95, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 20 }}
          transition={{ duration: 0.25, ease: [0.22, 1, 0.36, 1] }}
          className="relative w-full max-w-2xl bg-white text-slate-900 rounded-2xl sm:rounded-3xl shadow-2xl border border-slate-200 overflow-hidden z-10 my-8"
          onClick={(e) => e.stopPropagation()}
        >
          {/* Header Strip */}
          <div className="bg-slate-50 p-4 sm:p-7 relative border-b border-slate-200">
            <button
              onClick={onClose}
              className="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-200/80 hover:bg-[#0F58A8] text-slate-600 hover:text-white flex items-center justify-center transition-colors cursor-pointer"
              aria-label="Tutup Formulir"
            >
              <X className="w-4 h-4" />
            </button>

            <div className="flex items-center gap-2 text-[#0F58A8] text-xs font-bold uppercase tracking-wider mb-2">
              <Factory className="w-4 h-4" />
              <span>Pusat Korespondensi B2B & RFQ Pabrik</span>
            </div>

            <h3 className="text-lg sm:text-2xl font-extrabold font-heading text-slate-900">
              Formulir Permintaan Penawaran Resmi (RFQ)
            </h3>
            <p className="text-xs text-slate-600 mt-1 leading-relaxed">
              Konsultasi langsung dengan formulator lab dan manajemen pabrik PT Kediri Chemical Abadi untuk pasokan massal, formulasi khusus, atau maklon private label.
            </p>
          </div>

          {/* Form */}
          <form onSubmit={handleSubmit} className="p-6 sm:p-7 space-y-4 max-h-[75vh] overflow-y-auto">
            {/* Grid PIC Name & Role */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                  Nama Lengkap PIC *
                </label>
                <input
                  type="text"
                  required
                  placeholder="cth. Ir. Budi Santoso"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full h-11 px-4 bg-slate-50 border border-slate-300 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:border-[#0F58A8] focus:bg-white"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                  Jabatan / Posisi *
                </label>
                <input
                  type="text"
                  required
                  placeholder="cth. Procurement Manager / Direktur"
                  value={formData.role}
                  onChange={(e) => setFormData({ ...formData, role: e.target.value })}
                  className="w-full h-11 px-4 bg-slate-50 border border-slate-300 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:border-[#0F58A8] focus:bg-white"
                />
              </div>
            </div>

            {/* Grid Company & WhatsApp */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                  Nama Perusahaan / RS / Hotel *
                </label>
                <input
                  type="text"
                  required
                  placeholder="cth. PT Megah Textile / RS Graha Medika"
                  value={formData.company}
                  onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                  className="w-full h-11 px-4 bg-slate-50 border border-slate-300 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:border-[#0F58A8] focus:bg-white"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                  Nomor WhatsApp Aktif *
                </label>
                <input
                  type="text"
                  required
                  placeholder="cth. 085812307629"
                  value={formData.whatsapp}
                  onChange={(e) => setFormData({ ...formData, whatsapp: e.target.value })}
                  className="w-full h-11 px-4 bg-slate-50 border border-slate-300 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:border-[#0F58A8] focus:bg-white"
                />
              </div>
            </div>

            {/* Grid Sector & Service Option */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                  Sektor Industri
                </label>
                <select
                  value={formData.sector}
                  onChange={(e) => setFormData({ ...formData, sector: e.target.value })}
                  className="w-full h-11 px-3 bg-slate-50 border border-slate-300 rounded-xl text-xs text-slate-900 focus:outline-none focus:border-[#0F58A8] focus:bg-white cursor-pointer"
                >
                  <option value="Commercial Laundry & Tekstil">Commercial Laundry & Tekstil</option>
                  <option value="Perhotelan & Resort">Perhotelan & Resort (Linen)</option>
                  <option value="Rumah Sakit & Medis">Rumah Sakit & Fasilitas Medis</option>
                  <option value="Pabrik Manufaktur & Otomotif">Pabrik Manufaktur & Otomotif (Degreaser)</option>
                  <option value="Restoran & Food Processing">Restoran, Katering, & Food Processing</option>
                  <option value="Agro-Chemical & Peternakan">Agro-Chemical & Biosecurity Peternakan</option>
                  <option value="Lainnya">Lainnya</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                  Pilihan Skema / Layanan
                </label>
                <select
                  value={formData.service}
                  onChange={(e) => setFormData({ ...formData, service: e.target.value })}
                  className="w-full h-11 px-3 bg-slate-50 border border-slate-300 rounded-xl text-xs text-[#0F58A8] font-bold focus:outline-none focus:border-[#0F58A8] focus:bg-white cursor-pointer"
                >
                  <option value="Jasa Maklon Dedicated Line (Investasi Mesin Khusus) - Unggulan">Jasa Maklon Dedicated Line (Investasi Mesin Khusus) - Unggulan</option>
                  <option value="Jasa Maklon Reguler (Merek Sendiri / Batch Sharing)">Jasa Maklon Reguler (Merek Sendiri / Batch Sharing)</option>
                  <option value="Pasokan Rutin Kimia Pembersih Pabrik">Pasokan Rutin Kimia Pembersih Pabrik</option>
                  <option value="Pembelian Bahan Baku Kimia Murni">Pembelian Bahan Baku Kimia Murni</option>
                  <option value="Permintaan Sampel Uji Laboratorium">Permintaan Sampel Uji Laboratorium</option>
                </select>
              </div>
            </div>

            {/* Volume Selector */}
            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                Estimasi Volume Kebutuhan Bulanan
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
                {['< 1 Ton / Bln', '1 - 5 Ton / Bln', '5 - 20 Ton / Bln', '> 20 Ton / Bln'].map((vol) => (
                  <button
                    type="button"
                    key={vol}
                    onClick={() => setFormData({ ...formData, volume: vol })}
                    className={`py-2 px-3 rounded-xl border text-center font-bold transition-all cursor-pointer ${
                      formData.volume === vol
                        ? 'bg-[#0F58A8] text-white border-[#0F58A8] shadow-xs'
                        : 'bg-slate-50 border-slate-200 text-slate-700 hover:bg-slate-100'
                    }`}
                  >
                    {vol}
                  </button>
                ))}
              </div>
            </div>

            {/* Notes */}
            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase mb-1">
                Catatan / Spesifikasi Formula Tambahan
              </label>
              <textarea
                rows={3}
                placeholder="cth. Membutuhkan formula non-fosfat untuk linen RS dengan kapasitas cuci 2 Ton/hari..."
                value={formData.notes}
                onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                className="w-full p-3 bg-slate-50 border border-slate-300 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:border-[#0F58A8] focus:bg-white"
              />
            </div>

            {/* Guarantee Note */}
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 flex items-center gap-2 text-xs text-slate-600">
              <ShieldCheck className="w-4 h-4 text-emerald-600 shrink-0" />
              <span>Resmi PT Kediri Chemical Abadi • Kerahasiaan Formula Terjamin (NDA Ready)</span>
            </div>

            {/* Submit Button */}
            <div className="pt-2">
              <button
                type="submit"
                disabled={submitted}
                className="w-full py-3.5 bg-[#0F58A8] hover:bg-blue-800 active:bg-blue-900 text-white rounded-xl text-xs font-bold font-heading uppercase tracking-wider shadow-md shadow-blue-900/15 hover:shadow-lg transition-all flex items-center justify-center gap-2 cursor-pointer"
              >
                <Send className="w-4 h-4" />
                <span>{submitted ? 'Membuka WhatsApp...' : 'Kirimkan Permintaan Penawaran (RFQ)'}</span>
              </button>
            </div>
          </form>
        </motion.div>
      </div>
    </AnimatePresence>
  )
}
