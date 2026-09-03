import { useState } from 'react'
import { motion } from 'framer-motion'
import { Send, Phone } from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import RFQModal from '@/components/ui/RFQModal'

export default function CTASection() {
  const [rfqOpen, setRfqOpen] = useState(false)

  const waNumber = COMPANY_DATA.contacts?.whatsappNumber || '6285812307629'
  const waDisplay = COMPANY_DATA.contacts?.whatsappDisplay || '085812307629'

  return (
    <>
      <section className="pt-12 sm:pt-20 pb-20 sm:pb-32 bg-gradient-to-b from-white to-blue-50/40 text-slate-900 relative overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-12 w-full relative z-10 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.4 }}
            className="max-w-3xl mx-auto space-y-6"
          >
            <h2 className="text-lg sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight leading-tight uppercase">
              Siap Mengoptimalkan Efisiensi Kimia Pembersih Fasilitas Anda?
            </h2>

            <p className="text-slate-600 text-xs sm:text-[13px] leading-relaxed font-normal max-w-2xl mx-auto">
              Dapatkan formulasi konsentrat bebas fosfat yang ramah IPAL, harga pabrik kompetitif tangan pertama, serta kepastian kontinuitas pasokan massal 500+ Ton/bulan dari PT Kediri Chemical Abadi.
            </p>

            <div className="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
              <button
                onClick={() => setRfqOpen(true)}
                className="btn-fluid-primary w-full sm:w-auto h-9 sm:h-10 px-4 sm:px-6 text-[11px] sm:text-xs"
              >
                <Send className="w-3.5 h-3.5" />
                <span>Minta Penawaran Resmi (RFQ)</span>
              </button>

              <a
                href={`https://wa.me/${waNumber}`}
                target="_blank"
                rel="noopener noreferrer"
                className="btn-fluid-secondary w-full sm:w-auto h-9 sm:h-10 px-4 sm:px-6 text-[11px] sm:text-xs"
              >
                <Phone className="w-4 h-4 text-[#0F58A8]" />
                <span>WhatsApp: {waDisplay}</span>
              </a>
            </div>
          </motion.div>
        </div>

        {/* Seamless S-Curve Wave Transition into Navy Footer (#0A192F) */}
        <div className="absolute bottom-0 inset-x-0 pointer-events-none leading-none z-20">
          <svg
            className="w-full h-12 sm:h-16 lg:h-20 text-[#0A192F] block"
            viewBox="0 0 1440 120"
            preserveAspectRatio="none"
          >
            <path
              d="M0,32 C320,95 640,0 960,65 C1200,110 1360,50 1440,60 L1440,120 L0,120 Z"
              fill="currentColor"
            />
          </svg>
        </div>
      </section>

      {/* RFQ Modal */}
      <RFQModal isOpen={rfqOpen} onClose={() => setRfqOpen(false)} />
    </>
  )
}
