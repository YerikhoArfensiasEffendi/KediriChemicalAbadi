import { useState } from 'react'
import { Link } from 'react-router-dom'
import { MapPin, Mail, Phone, ShieldCheck, Award, FileText, ArrowRight } from 'lucide-react'
import { COMPANY_DATA } from '@/data/companyData'
import { NAVIGATION_DATA } from '@/data/navigationData'
import RFQModal from '@/components/ui/RFQModal'

export default function Footer() {
  const [rfqOpen, setRfqOpen] = useState(false)

  const waNumber = COMPANY_DATA.contacts?.whatsappNumber || '6285812307629'
  const waDisplay = COMPANY_DATA.contacts?.whatsappDisplay || '085812307629'

  return (
    <>
      <footer className="bg-[#0A192F] text-slate-300 border-t border-slate-800/80 pt-16 sm:pt-20 pb-12 sm:pb-16 relative">
        <div className="max-w-[1700px] mx-auto px-4 sm:px-8 lg:px-14 xl:px-20 w-full">
          
          {/* Main Footer Grid (Wide 12-Col Distribution) */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-14 xl:gap-16 pb-14 sm:pb-16 border-b border-slate-800/80">
            
            {/* Col 1: Brand & Identity (4 cols) */}
            <div className="lg:col-span-4 xl:col-span-4 space-y-5">
              <div className="flex items-center gap-3.5">
                <img
                  src="/images/kca_logo.png"
                  alt="Logo Resmi PT Kediri Chemical Abadi"
                  className="h-11 w-auto object-contain"
                />
                <div>
                  <span className="font-heading font-extrabold text-base sm:text-lg tracking-tight block">
                    <span className="text-blue-400">PT KEDIRI</span> <span className="text-red-500">CHEMICAL ABADI</span>
                  </span>
                  <span className="text-[11px] text-slate-400 font-bold uppercase tracking-wider block">
                    {COMPANY_DATA.brandTagline} • Est. {COMPANY_DATA.established}
                  </span>
                </div>
              </div>

              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed font-normal">
                Pusat riset dan manufaktur kimia pembersih industri konsentrat 100% non-fosfat berkapasitas 500+ Ton/bulan di Mojoroto, Kediri. Menjamin efisiensi dosis, standar IPAL KARS, dan layanan maklon private label terpercaya.
              </p>

              {/* Executive Accreditation & Legal Trustmarks (Desain Profesional & Berwibawa) */}
              <div className="pt-2 grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                
                {/* Seal 1: Legalitas OSS-RBA & LKPP RI */}
                <div className="p-3 rounded-lg bg-slate-900/90 border border-slate-800 flex items-center gap-3 shadow-xs">
                  <div className="w-9 h-9 rounded-md bg-blue-500/10 border border-blue-500/20 text-blue-400 flex items-center justify-center shrink-0">
                    <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                      <path d="m9 12 2 2 4-4"/>
                    </svg>
                  </div>
                  <div className="min-w-0 leading-tight">
                    <span className="text-[9px] font-extrabold uppercase tracking-widest text-slate-400 block truncate">
                      KEMENTERIAN INVESTASI / BKPM
                    </span>
                    <strong className="text-xs font-bold text-white block truncate mt-0.5">
                      OSS-RBA &amp; LKPP RI
                    </strong>
                    <span className="text-[10px] text-blue-400 font-medium block truncate mt-0.5">
                      KBLI 20231 • Industri Sabun
                    </span>
                  </div>
                </div>

                {/* Seal 2: Sistem Mutu ISO 9001:2015 */}
                <div className="p-3 rounded-lg bg-slate-900/90 border border-slate-800 flex items-center gap-3 shadow-xs">
                  <div className="w-9 h-9 rounded-md bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0">
                    <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <circle cx="12" cy="12" r="9"/>
                      <path d="M12 7v5l3 3"/>
                      <path d="m9 12 2 2 4-4"/>
                    </svg>
                  </div>
                  <div className="min-w-0 leading-tight">
                    <span className="text-[9px] font-extrabold uppercase tracking-widest text-slate-400 block truncate">
                      SISTEM KENDALI MUTU PABRIK
                    </span>
                    <strong className="text-xs font-bold text-white block truncate mt-0.5">
                      Standar ISO 9001:2015
                    </strong>
                    <span className="text-[10px] text-emerald-400 font-medium block truncate mt-0.5">
                      QC Lab &amp; COA Per Batch
                    </span>
                  </div>
                </div>

              </div>
            </div>

            {/* Col 2: Navigation Links (2 cols) */}
            <div className="lg:col-span-2 xl:col-span-2 space-y-4">
              <span className="text-xs font-bold text-white uppercase tracking-widest block font-heading border-b border-slate-800 pb-2">
                Navigasi Cepat
              </span>
              <ul className="space-y-2.5 text-xs font-semibold text-slate-300 font-heading">
                {NAVIGATION_DATA.footerLinks.map((link) => (
                  <li key={link.to}>
                    <Link to={link.to} className="hover:text-blue-400 transition-colors flex items-center gap-1.5 group">
                      <span className="w-1.5 h-1.5 rounded-full bg-blue-500/40 group-hover:bg-blue-400 transition-colors" />
                      <span>{link.label}</span>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>

            {/* Col 3: Lini Formulasi Utama (3 cols) */}
            <div className="lg:col-span-3 xl:col-span-3 space-y-4">
              <span className="text-xs font-bold text-white uppercase tracking-widest block font-heading border-b border-slate-800 pb-2">
                Lini Formulasi Utama
              </span>
              <ul className="space-y-2 text-xs font-medium text-slate-400">
                <li className="hover:text-slate-200 transition-colors">• Liquid Detergent Non-Phosphate (Hero)</li>
                <li className="hover:text-slate-200 transition-colors">• Hospitality & Commercial Laundry</li>
                <li className="hover:text-slate-200 transition-colors">• Food & Beverage Sanitation</li>
                <li className="hover:text-slate-200 transition-colors">• Agro & Biosecurity Peternakan</li>
                <li className="hover:text-slate-200 transition-colors">• Industrial Technical Degreaser</li>
                <li className="hover:text-slate-200 transition-colors">• Dedicated Production Line Capex</li>
              </ul>

              <div className="pt-2">
                <button
                  onClick={() => setRfqOpen(true)}
                  className="btn-fluid-primary text-xs py-2.5 px-5"
                >
                  <FileText className="w-3.5 h-3.5" />
                  <span>Minta Penawaran Resmi (RFQ)</span>
                </button>
              </div>
            </div>

            {/* Col 4: Kantor Pusat, Pabrik & Direksi (3 cols) */}
            <div className="lg:col-span-3 xl:col-span-3 space-y-4">
              <span className="text-xs font-bold text-white uppercase tracking-widest block font-heading border-b border-slate-800 pb-2">
                Kantor Pusat & Pabrik
              </span>
              <div className="space-y-3 text-xs text-slate-300">
                <div className="flex items-start gap-2.5">
                  <MapPin className="w-4 h-4 text-blue-400 shrink-0 mt-0.5" />
                  <span className="leading-relaxed">
                    {COMPANY_DATA.location.address}, {COMPANY_DATA.location.city}, {COMPANY_DATA.location.province} {COMPANY_DATA.location.postalCode}
                  </span>
                </div>
                <div className="flex items-center gap-2.5">
                  <Phone className="w-4 h-4 text-emerald-400 shrink-0" />
                  <a
                    href={`https://wa.me/${waNumber}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-emerald-400 font-bold transition-colors"
                  >
                    +62 {waDisplay} (B2B Hotline)
                  </a>
                </div>
                <div className="flex items-center gap-2.5">
                  <Mail className="w-4 h-4 text-sky-400 shrink-0" />
                  <a
                    href={`mailto:${COMPANY_DATA.contacts.email}`}
                    className="hover:text-sky-400 transition-colors"
                  >
                    {COMPANY_DATA.contacts.email}
                  </a>
                </div>
              </div>

              {/* Management Note */}
              <div className="pt-3 border-t border-slate-800/80 text-xs text-slate-400 space-y-1">
                <span className="block text-slate-200 font-bold uppercase tracking-wider">
                  Dewan Direksi & Manajemen Sah:
                </span>
                <span className="block text-slate-300">• Direktur Utama: {COMPANY_DATA.management[0].name}</span>
                <span className="block text-slate-300">• Direktur / GM: {COMPANY_DATA.management[1].name}</span>
              </div>
            </div>

          </div>

          {/* Bottom Legal Notice & Copyright Strip (Ultra-Wide Alignment) */}
          <div className="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500 text-center sm:text-left">
            <p>
              © 2026 PT Kediri Chemical Abadi. Hak Cipta Dilindungi Undang-Undang.
            </p>
            <div className="flex items-center gap-5 text-slate-400 font-medium">
              <Link to="/privacy-policy" className="hover:text-white transition-colors">
                Kebijakan Privasi & NDA
              </Link>
              <span>•</span>
              <Link to="/terms" className="hover:text-white transition-colors">
                Syarat & Ketentuan Pasokan
              </Link>
            </div>
          </div>

        </div>
      </footer>

      {/* RFQ Modal */}
      <RFQModal isOpen={rfqOpen} onClose={() => setRfqOpen(false)} />
    </>
  )
}
