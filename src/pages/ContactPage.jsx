import { useState } from 'react'
import { Helmet } from 'react-helmet-async'
import { motion } from 'framer-motion'
import { 
  MapPin, 
  Phone, 
  Mail, 
  Send, 
  Factory, 
  ShieldCheck, 
  Clock, 
  Building2,
  Navigation,
  Truck,
  ExternalLink,
  CheckCircle2,
  FileCheck2,
  MessageSquare
} from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import CTASection from '@/components/sections/CTASection'

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    company: '',
    whatsapp: '',
    sector: 'Commercial Laundry & Tekstil',
    notes: '',
  })
  const [submitted, setSubmitted] = useState(false)

  const waNumber = COMPANY_DATA.contacts?.whatsappNumber || '6285812307629'
  const waDisplay = COMPANY_DATA.contacts?.whatsappDisplay || '085812307629'

  const handleSubmit = (e) => {
    e.preventDefault()
    setSubmitted(true)

    const text = `*PESAN KORESPONDENSI — PT KEDIRI CHEMICAL ABADI*
----------------------------------------
*Nama PIC:* ${formData.name}
*Perusahaan / RS / Instansi:* ${formData.company}
*Nomor WhatsApp:* ${formData.whatsapp}
*Sektor Industri:* ${formData.sector}

*Pesan / Permintaan Informasi:*
${formData.notes || 'Mohon informasi katalog dan penawaran harga resmi pabrik.'}
----------------------------------------
_Dikirim via Halaman Kontak kedirichemical.com_`

    const waUrl = `https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`

    setTimeout(() => {
      window.open(waUrl, '_blank')
      setSubmitted(false)
    }, 400)
  }

  return (
    <main className="bg-white text-slate-900 pt-6">
      <Helmet>
        <title>Hubungi Kami & Lokasi Pabrik — PT Kediri Chemical Abadi</title>
        <meta
          name="description"
          content="Hubungi pabrik PT Kediri Chemical Abadi di Mojoroto, Kediri. Hotline WhatsApp 085812307629, email kdrchemicals@gmail.com, dan peta lokasi fasilitas produksi."
        />
      </Helmet>

      {/* ========================================================================= */}
      {/* 1. HEADER BANNER UTAMA (CLEAN WHITE EDITORIAL)                            */}
      {/* ========================================================================= */}
      <section className="py-14 sm:py-20 bg-gradient-to-b from-sky-50/50 via-white to-white border-b border-sky-100 text-center">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          <div className="max-w-4xl mx-auto space-y-3">
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
              Hubungi Manajemen &amp; Tim Formulator Lab Pabrik
            </h1>

            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-3xl mx-auto font-normal pt-1">
              Konsultasikan kebutuhan formula kimia pembersih khusus, permintaan sampel uji teknis, skema kemitraan maklon private label, hingga pasokan massal skala drum 200L / IBC 1.000L dari pabrik PT Kediri Chemical Abadi.
            </p>

            {/* SLA Highlights (Clean Inline Badges) */}
            <div className="pt-4 flex items-center justify-center flex-wrap gap-x-8 gap-y-2 text-xs font-semibold text-slate-700">
              <span className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-[#0F58A8]" />
                <span>Respon WhatsApp &lt; 15 Menit</span>
              </span>
              <span className="text-slate-300 hidden sm:inline">•</span>
              <span className="flex items-center gap-2">
                <ShieldCheck className="w-4 h-4 text-emerald-600" />
                <span>Legalitas Sah OSS-RBA &amp; LKPP RI</span>
              </span>
              <span className="text-slate-300 hidden sm:inline">•</span>
              <span className="flex items-center gap-2">
                <Factory className="w-4 h-4 text-amber-600" />
                <span>Kapasitas Reaktor 500+ Ton / Bulan</span>
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 2. SPLIT CONTACT & INQUIRY SECTION (CLEAN WHITE, FLUID WATER THEME)       */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-sky-50/30 border-b border-sky-100">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
            
            {/* 1. SISI KIRI: KANTOR PUSAT & INFORMASI RESMI (5 Kolom) */}
            <div className="lg:col-span-5 bg-white border border-sky-100 rounded-3xl shadow-lg shadow-blue-900/5 overflow-hidden flex flex-col justify-between">
              {/* Volumetric Top Bar */}
              <div className="h-1.5 w-full bg-gradient-to-r from-[#0F58A8] to-[#0284C7]" />

              <div className="p-6 sm:p-8 space-y-7">
                <div className="border-b border-sky-100 pb-4 space-y-1">
                  <h2 className="font-heading font-extrabold text-xl sm:text-2xl text-slate-900 leading-tight">
                    Kantor Pusat &amp; Fasilitas Pabrik
                  </h2>
                </div>

                {/* Contact Points List */}
                <div className="space-y-5 text-xs sm:text-sm">
                  
                  {/* Alamat */}
                  <div className="flex items-start gap-3.5">
                    <div className="w-9 h-9 rounded-full bg-blue-50 border border-sky-200 text-[#0F58A8] flex items-center justify-center shrink-0 mt-0.5">
                      <MapPin className="w-4 h-4" />
                    </div>
                    <div className="space-y-0.5">
                      <strong className="text-slate-900 block font-heading text-xs font-bold uppercase tracking-wider">
                        Alamat Fasilitas Pabrik
                      </strong>
                      <p className="text-slate-700 leading-relaxed">
                        {COMPANY_DATA.address?.full || `${COMPANY_DATA.location?.address || 'Jl. Merbabu No. 12, Mojoroto'}, ${COMPANY_DATA.location?.city || 'Kota Kediri'}, ${COMPANY_DATA.location?.province || 'Jawa Timur'} ${COMPANY_DATA.location?.postalCode || '64112'}`}
                      </p>
                    </div>
                  </div>

                  {/* Hotline WA */}
                  <div className="flex items-start gap-3.5">
                    <div className="w-9 h-9 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-600 flex items-center justify-center shrink-0 mt-0.5">
                      <Phone className="w-4 h-4" />
                    </div>
                    <div className="space-y-0.5">
                      <strong className="text-slate-900 block font-heading text-xs font-bold uppercase tracking-wider">
                        Hotline WhatsApp B2B
                      </strong>
                      <a
                        href={`https://wa.me/${waNumber}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-[#0F58A8] font-bold hover:underline block text-xs"
                      >
                        +{waDisplay}
                      </a>
                    </div>
                  </div>

                  {/* Email */}
                  <div className="flex items-start gap-3.5">
                    <div className="w-9 h-9 rounded-full bg-amber-50 border border-amber-200 text-amber-600 flex items-center justify-center shrink-0 mt-0.5">
                      <Mail className="w-4 h-4" />
                    </div>
                    <div className="space-y-0.5">
                      <strong className="text-slate-900 block font-heading text-xs font-bold uppercase tracking-wider">
                        Email Resmi Penawaran &amp; Tender
                      </strong>
                      <a
                        href={`mailto:${COMPANY_DATA.contacts?.email || 'kdrchemicals@gmail.com'}`}
                        className="text-[#0F58A8] font-bold hover:underline block text-xs"
                      >
                        {COMPANY_DATA.contacts?.email || 'kdrchemicals@gmail.com'}
                      </a>
                    </div>
                  </div>

                  {/* Jam Operasional */}
                  <div className="flex items-start gap-3.5">
                    <div className="w-9 h-9 rounded-full bg-sky-50 border border-sky-200 text-sky-600 flex items-center justify-center shrink-0 mt-0.5">
                      <Clock className="w-4 h-4" />
                    </div>
                    <div className="space-y-0.5">
                      <strong className="text-slate-900 block font-heading text-xs font-bold uppercase tracking-wider">
                        Jam Kerja Kantor Pabrik
                      </strong>
                      <span className="text-slate-700 block text-xs">
                        Senin – Sabtu: 08.00 – 17.00 WIB
                      </span>
                      <span className="text-[11px] text-slate-500 block">
                        Lini Reaktor Pencampur SS 316L Beroperasi 24 Jam Sesuai Jadwal Batch
                      </span>
                    </div>
                  </div>

                </div>

                {/* Penanggung Jawab Manajemen Sah */}
                <div className="pt-4 border-t border-sky-100 text-xs space-y-2">
                  <span className="block text-slate-900 font-extrabold uppercase tracking-wider font-heading text-[11px]">
                    Penanggung Jawab Manajemen Korporat:
                  </span>
                  <div className="space-y-1.5 text-slate-700 bg-sky-50/50 p-3 rounded-2xl border border-sky-100">
                    <div className="flex items-center justify-between">
                      <span className="font-semibold text-slate-900">Direktur Utama:</span>
                      <span className="font-bold text-slate-800">{COMPANY_DATA.management?.[0]?.name || COMPANY_DATA.boardOfDirectors?.[0]?.name || 'Yan Effendi'}</span>
                    </div>
                    <div className="flex items-center justify-between border-t border-sky-100 pt-1">
                      <span className="font-semibold text-slate-900">Direktur / Formulator:</span>
                      <span className="font-bold text-slate-800">{COMPANY_DATA.management?.[1]?.name || COMPANY_DATA.boardOfDirectors?.[1]?.name || 'Yerikho Arfensias Effendi'}</span>
                    </div>
                  </div>
                </div>

              </div>
            </div>

            {/* 2. SISI KANAN: FORMULIR PESAN & PERMINTAAN PENAWARAN (7 Kolom) */}
            <div className="lg:col-span-7 bg-white border border-sky-100 rounded-3xl shadow-lg shadow-blue-900/5 overflow-hidden flex flex-col justify-between">
              {/* Volumetric Top Bar */}
              <div className="h-1.5 w-full bg-gradient-to-r from-[#059669] to-emerald-400" />

              <div className="p-6 sm:p-8 space-y-6">
                <div className="border-b border-sky-100 pb-4 space-y-1">
                  <h2 className="font-heading font-extrabold text-xl sm:text-2xl text-slate-900 leading-tight">
                    Kirimkan Pesan atau Permintaan Penawaran (RFQ)
                  </h2>
                  <p className="text-xs text-slate-600 leading-relaxed pt-0.5">
                    Isi formulir di bawah ini untuk langsung terhubung dengan tim manajemen dan formulator lab PT Kediri Chemical Abadi via WhatsApp resmi.
                  </p>
                </div>

                <form onSubmit={handleSubmit} className="space-y-4">
                  
                  {/* Row 1: Nama & Perusahaan */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="space-y-1">
                      <label className="block text-[11px] font-bold text-slate-700 uppercase font-heading">
                        Nama Lengkap PIC *
                      </label>
                      <input
                        type="text"
                        required
                        placeholder="cth. Ir. Budi Santoso"
                        value={formData.name}
                        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                        className="w-full h-10 px-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:bg-white focus:border-[#0F58A8] transition-colors"
                      />
                    </div>

                    <div className="space-y-1">
                      <label className="block text-[11px] font-bold text-slate-700 uppercase font-heading">
                        Nama Instansi / Perusahaan *
                      </label>
                      <input
                        type="text"
                        required
                        placeholder="cth. RSUD / Hotel / Sentra Laundry"
                        value={formData.company}
                        onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                        className="w-full h-10 px-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:bg-white focus:border-[#0F58A8] transition-colors"
                      />
                    </div>
                  </div>

                  {/* Row 2: WhatsApp & Sektor */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="space-y-1">
                      <label className="block text-[11px] font-bold text-slate-700 uppercase font-heading">
                        Nomor WhatsApp *
                      </label>
                      <input
                        type="tel"
                        required
                        placeholder="0812xxxxxxxx"
                        value={formData.whatsapp}
                        onChange={(e) => setFormData({ ...formData, whatsapp: e.target.value })}
                        className="w-full h-10 px-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:bg-white focus:border-[#0F58A8] transition-colors"
                      />
                    </div>

                    <div className="space-y-1">
                      <label className="block text-[11px] font-bold text-slate-700 uppercase font-heading">
                        Sektor Usaha / Kategori
                      </label>
                      <select
                        value={formData.sector}
                        onChange={(e) => setFormData({ ...formData, sector: e.target.value })}
                        className="w-full h-10 px-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-900 focus:outline-none focus:bg-white focus:border-[#0F58A8] transition-colors cursor-pointer"
                      >
                        <option value="Commercial Laundry & Tekstil">Commercial Laundry &amp; Tekstil</option>
                        <option value="Perhotelan & Resort Chains">Perhotelan &amp; Resort Chains</option>
                        <option value="Rumah Sakit & Fasilitas Medis">Rumah Sakit &amp; Fasilitas Medis</option>
                        <option value="Pabrik Manufaktur & Otomotif">Pabrik Manufaktur &amp; Otomotif</option>
                        <option value="Restoran & Food Processing">Restoran &amp; Food Processing</option>
                        <option value="Skema Maklon Private Label">Skema Maklon Private Label</option>
                        <option value="Lainnya / Kerjasama Khusus">Lainnya / Kerjasama Khusus</option>
                      </select>
                    </div>
                  </div>

                  {/* Row 3: Detail Pesan / Kebutuhan Formula */}
                  <div className="space-y-1">
                    <label className="block text-[11px] font-bold text-slate-700 uppercase font-heading">
                      Pesan / Rincian Spesifikasi Kebutuhan *
                    </label>
                    <textarea
                      required
                      rows={4}
                      placeholder="Jelaskan kebutuhan formula kimia, perkiraan volume per bulan (misal: 20 Drum / 5.000L), target harga, atau permintaan sampel uji laboratorium..."
                      value={formData.notes}
                      onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                      className="w-full p-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:bg-white focus:border-[#0F58A8] transition-colors"
                    />
                  </div>

                  {/* Submit Action */}
                  <div className="pt-2">
                    <button
                      type="submit"
                      disabled={submitted}
                      className="btn-fluid-primary w-full h-11"
                    >
                      <Send className="w-4 h-4" />
                      <span>{submitted ? 'Membuka WhatsApp Resmi...' : 'Kirim Pesan ke WhatsApp Resmi Pabrik'}</span>
                    </button>
                  </div>

                  <p className="text-[11px] text-slate-500 text-center font-normal pt-1">
                    Pesan terenkripsi dan langsung diteruskan ke staf manajemen PT Kediri Chemical Abadi.
                  </p>
                </form>

              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. GOOGLE MAPS & PETA LOKASI PABRIK (FLUID WATER THEME)                   */}
      {/* ========================================================================= */}
      <section className="py-16 sm:py-24 bg-white border-b border-sky-100">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full space-y-8">
          
          {/* Header Map Section (Direct Title) */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6 border-b border-sky-100">
            <div className="space-y-1 max-w-3xl">
              <h2 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold font-heading text-slate-900 tracking-tight leading-tight">
                Lokasi Fasilitas Produksi Mojoroto, Kediri
              </h2>
            </div>
            <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
              Fasilitas produksi seluas 2.500+ m² dengan akses armada truk fuso dan tronton kontainer yang terhubung langsung ke koridor logistik Jawa Timur.
            </p>
          </div>

          {/* Map & Plant Access Split Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-stretch">
            
            {/* Google Map Interactive Frame (8 Kolom) */}
            <div className="lg:col-span-8 overflow-hidden rounded-3xl border border-sky-100 shadow-lg shadow-blue-900/5 relative min-h-[380px] sm:min-h-[440px] bg-sky-50">
              <iframe
                title="Peta Lokasi Fasilitas Pabrik PT Kediri Chemical Abadi Mojoroto Kediri"
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3952.883713600644!2d111.99616227588383!3d-7.802144377453303!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e785721867c2df3%3A0x446ea9b5f5403e05!2sMojoroto%2C%20Kota%20Kediri%2C%20Jawa%20Timur!5e0!3m2!1sid!2sid!4v1709400000000!5m2!1sid!2sid"
                width="100%"
                height="100%"
                style={{ border: 0, minHeight: '380px' }}
                allowFullScreen=""
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                className="w-full h-full"
              />

              {/* Float Map Overlay Badge */}
              <div className="absolute top-4 left-4 z-20 bg-white/95 backdrop-blur-md p-3.5 rounded-2xl border border-sky-100 text-xs space-y-0.5 shadow-lg max-w-xs hidden sm:block">
                <div className="flex items-center gap-1.5 text-[#0F58A8] font-bold font-heading">
                  <Factory className="w-3.5 h-3.5" />
                  <span>Plant Mojoroto, Kediri</span>
                </div>
                <p className="text-[11px] text-slate-600">
                  Jl. Merbabu No. 12, Mojoroto, Kota Kediri
                </p>
              </div>
            </div>

            {/* Logistics & Navigation Card (4 Kolom) */}
            <div className="lg:col-span-4 bg-gradient-to-b from-sky-50/50 via-white to-sky-50/20 p-6 sm:p-8 rounded-3xl border border-sky-100 shadow-lg shadow-blue-900/5 flex flex-col justify-between space-y-6">
              
              <div className="space-y-4">
                <span className="text-xs font-bold uppercase tracking-wider text-[#0F58A8] block border-b border-sky-100 pb-2">
                  Akses Jalur &amp; Armada Logistik:
                </span>

                <div className="space-y-3.5 text-xs text-slate-700">
                  <div className="flex items-start gap-2.5">
                    <div className="w-7 h-7 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 mt-0.5">
                      <Truck className="w-4 h-4" />
                    </div>
                    <div>
                      <strong className="text-slate-900 block font-heading font-bold">Akses Armada Berat</strong>
                      <span className="text-slate-600">Dapat dilalui Truk Fuso, Colt Diesel Double (CDD), dan Tronton kontainer.</span>
                    </div>
                  </div>

                  <div className="flex items-start gap-2.5">
                    <div className="w-7 h-7 rounded-full bg-blue-50 text-[#0F58A8] flex items-center justify-center shrink-0 mt-0.5">
                      <Navigation className="w-4 h-4" />
                    </div>
                    <div>
                      <strong className="text-slate-900 block font-heading font-bold">Konektivitas Tol Trans-Jawa</strong>
                      <span className="text-slate-600">Akses cepat menuju Gerbang Tol Kertosono-Kediri.</span>
                    </div>
                  </div>

                  <div className="flex items-start gap-2.5">
                    <div className="w-7 h-7 rounded-full bg-amber-50 text-amber-600 flex items-center justify-center shrink-0 mt-0.5">
                      <Building2 className="w-4 h-4" />
                    </div>
                    <div>
                      <strong className="text-slate-900 block font-heading font-bold">Bandara Internasional Dhoho</strong>
                      <span className="text-slate-600">Hanya 15 menit perjalanan dari Bandara Dhoho Kediri.</span>
                    </div>
                  </div>

                  <div className="flex items-start gap-2.5">
                    <div className="w-7 h-7 rounded-full bg-sky-50 text-[#0F58A8] flex items-center justify-center shrink-0 mt-0.5">
                      <CheckCircle2 className="w-4 h-4" />
                    </div>
                    <div>
                      <strong className="text-slate-900 block font-heading font-bold">Jangkauan Ekspedisi Nasional</strong>
                      <span className="text-slate-600">Pengiriman rutin ke seluruh Jawa, Bali, Sumatera, Kalimantan, &amp; Sulawesi.</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Action Button to Open Google Maps */}
              <div className="pt-4 border-t border-sky-100">
                <a
                  href="https://maps.google.com/?q=Jl.+Merbabu+No.+12,+Mojoroto,+Kota+Kediri,+Jawa+Timur+64112"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-fluid-primary w-full text-center"
                >
                  <Navigation className="w-4 h-4" />
                  <span>Buka Navigasi Rute Maps</span>
                  <ExternalLink className="w-3.5 h-3.5" />
                </a>
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
