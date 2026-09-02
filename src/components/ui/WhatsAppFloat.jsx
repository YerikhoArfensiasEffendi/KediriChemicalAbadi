import { MessageCircle } from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'

export default function WhatsAppFloat() {
  const waNumber = COMPANY_DATA.contacts?.whatsappNumber || '6285812307629'

  return (
    <div className="fixed bottom-6 right-6 z-40">
      <a
        href={`https://wa.me/${waNumber}`}
        target="_blank"
        rel="noopener noreferrer"
        aria-label="Hubungi Hotline Resmi WhatsApp PT Kediri Chemical Abadi"
        className="w-13 h-13 sm:w-14 sm:h-14 bg-emerald-600 hover:bg-emerald-500 active:bg-emerald-700 text-white rounded-full shadow-2xl shadow-emerald-950/30 flex items-center justify-center transition-all duration-300 hover:scale-110 group border-2 border-white/80 cursor-pointer"
      >
        <MessageCircle className="w-6 h-6 sm:w-7 sm:h-7 text-white" />
      </a>
    </div>
  )
}
