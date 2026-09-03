import os

with open('src/pages/CompliancePage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the QC_STEPS definition with our 5 bespoke industrial engineering icons
icons_code = '''// =========================================================================
// BESPOKE INDUSTRIAL CHEMICAL MANUFACTURING SVG ICONS (Authentic B2B Plant)
// =========================================================================

/** 1. Incoming Material QC: Testing Cylinder & Hydrometer Float with Graduation Marks */
function IncomingMaterialQcIcon({ className = "w-8 h-8 text-[#0F58A8]" }) {
  return (
    <svg className={className} viewBox="0 0 32 32" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M7 4h18M9 4v21a3 3 0 003 3h8a3 3 0 003-3V4" />
      <line x1="9" y1="10" x2="13" y2="10" strokeWidth="1.5" />
      <line x1="9" y1="15" x2="15" y2="15" strokeWidth="1.5" />
      <line x1="9" y1="20" x2="13" y2="20" strokeWidth="1.5" />
      <line x1="16" y1="6" x2="16" y2="20" strokeWidth="1.75" />
      <rect x="14" y="14" width="4" height="6" rx="1" fill="currentColor" fillOpacity="0.15" />
      <path d="M9 22c2-.8 4.5.8 7 0s4.5.8 7 0" strokeWidth="1.5" />
    </svg>
  )
}

/** 2. SS 316L Reactor Mixing: Jacketed Vessel with Agitator Drive & Impeller Vortex */
function JacketedReactorMixingIcon({ className = "w-8 h-8 text-[#D97706]" }) {
  return (
    <svg className={className} viewBox="0 0 32 32" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <rect x="13" y="2" width="6" height="4" rx="0.5" fill="currentColor" fillOpacity="0.15" />
      <line x1="16" y1="6" x2="16" y2="9" />
      <path d="M6 12c0-2.5 4.5-4 10-4s10 1.5 10 4v11c0 3-4.5 5-10 5s-10-2-10-5V12z" />
      <path d="M4 14v8c0 2 3 3.5 6 3.8M28 14v8c0 2-3 3.5-6 3.8" strokeWidth="1.25" strokeDasharray="2 1.5" />
      <line x1="16" y1="9" x2="16" y2="22" strokeWidth="1.5" />
      <path d="M11 18h10M10 22l6-2 6 2" strokeWidth="1.75" />
      <circle cx="24" cy="9" r="2.5" />
      <line x1="24" y1="9" x2="25" y2="8" strokeWidth="1.2" />
    </svg>
  )
}

/** 3. In-Process Lab QC: Digital pH Electrode & Analytical Beaker Sensor */
function InProcessTitrationIcon({ className = "w-8 h-8 text-[#059669]" }) {
  return (
    <svg className={className} viewBox="0 0 32 32" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M6 8h16M7 8v16a3 3 0 003 3h10a3 3 0 003-3V8" />
      <path d="M7 17c2.5-.8 5 .8 7.5 0s5 .8 7.5 0" strokeWidth="1.25" />
      <rect x="11" y="4" width="4" height="15" rx="1" fill="currentColor" fillOpacity="0.15" />
      <line x1="13" y1="19" x2="13" y2="22" strokeWidth="2" />
      <rect x="20" y="3" width="9" height="7" rx="1" />
      <line x1="22" y1="6" x2="27" y2="6" strokeWidth="1.5" />
      <line x1="15" y1="6" x2="20" y2="6" strokeWidth="1.2" strokeDasharray="2 1" />
    </svg>
  )
}

/** 4. Micro-Filtration & Packaging: 5-Micron Filter Cartridge & Packaging Container */
function MicroFiltrationPackagingIcon({ className = "w-8 h-8 text-[#7C3AED]" }) {
  return (
    <svg className={className} viewBox="0 0 32 32" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <rect x="6" y="4" width="10" height="18" rx="2" fill="currentColor" fillOpacity="0.15" />
      <line x1="8" y1="9" x2="14" y2="9" strokeWidth="1.2" strokeDasharray="1.5 1.5" />
      <line x1="8" y1="13" x2="14" y2="13" strokeWidth="1.2" strokeDasharray="1.5 1.5" />
      <line x1="8" y1="17" x2="14" y2="17" strokeWidth="1.2" strokeDasharray="1.5 1.5" />
      <path d="M19 14h6a2 2 0 012 2v10a2 2 0 01-2 2h-6a2 2 0 01-2-2V16a2 2 0 012-2z" />
      <path d="M21 14v-3h2v3" />
      <rect x="20" y="9" width="4" height="2" rx="0.5" />
      <path d="M16 13h3" strokeWidth="1.5" />
    </svg>
  )
}

/** 5. COA Release & Logistics: Official Verified Document & Quality Seal */
function CertifiedCoaLogisticsIcon({ className = "w-8 h-8 text-[#0F172A]" }) {
  return (
    <svg className={className} viewBox="0 0 32 32" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
      <path d="M6 3h13l7 7v17a2 2 0 01-2 2H6a2 2 0 01-2-2V5a2 2 0 012-2z" fill="currentColor" fillOpacity="0.08" />
      <path d="M19 3v7h7" />
      <line x1="8" y1="10" x2="14" y2="10" strokeWidth="1.5" />
      <line x1="8" y1="14" x2="18" y2="14" strokeWidth="1.5" />
      <line x1="8" y1="18" x2="16" y2="18" strokeWidth="1.5" />
      <circle cx="21" cy="22" r="4.5" fill="currentColor" fillOpacity="0.15" />
      <circle cx="21" cy="22" r="4.5" strokeWidth="1.5" />
      <path d="M19.5 22l1 1 2.5-2.5" strokeWidth="1.5" />
    </svg>
  )
}

const QC_STEPS = [
  {
    step: '01',
    phase: 'INCOMING MATERIAL QC',
    title: 'Analisis Bahan Baku Murni',
    icon: IncomingMaterialQcIcon,
    color: '#0F58A8',
    borderColor: 'border-b-[#0F58A8]',
    badgeBg: 'bg-[#0F58A8]',
    textColor: 'text-[#0F58A8]',
    checkColor: 'text-[#0F58A8]',
    iconContainerBg: 'bg-blue-50/80 border-blue-200',
    desc: 'Pemeriksaan ketat kemurnian surfaktan aktif, pelarut, dan bahan aditif dari pemasok sebelum diizinkan masuk ke jalur reaktor.',
    points: [
      'Pemeriksaan Certificate of Analysis (COA) vendor',
      'Uji organoleptik kejernihan & aroma',
      'Uji konsentrasi & berat jenis bahan baku',
      'Verifikasi sertifikasi bebas zat berbahaya'
    ],
    deliverable: 'Bahan Baku Murni Terverifikasi',
    deliverableIcon: IncomingMaterialQcIcon
  },
  {
    step: '02',
    phase: 'CONTROLLED BATCH MIXING',
    title: 'Reaksi Kimia Tangki SS 316L',
    icon: JacketedReactorMixingIcon,
    color: '#D97706',
    borderColor: 'border-b-[#D97706]',
    badgeBg: 'bg-[#D97706]',
    textColor: 'text-[#D97706]',
    checkColor: 'text-[#D97706]',
    iconContainerBg: 'bg-amber-50/80 border-amber-200',
    desc: 'Pengadukan dengan kecepatan terukur (RPM terkontrol) pada suhu konstan 28°C–32°C di reaktor Stainless Steel 316L.',
    points: [
      'Kontrol RPM pengaduk variable-speed',
      'Pemantauan suhu jaket pendingin reaktor',
      'Pelarutan bertahap anti-gumpalan (lump-free)'
    ],
    deliverable: 'Larutan Homogen 100% Sempurna',
    deliverableIcon: JacketedReactorMixingIcon
  },
  {
    step: '03',
    phase: 'LAB QC TITRATION & VERIFICATION',
    title: 'Sampling Tengah Batch (In-Process)',
    icon: InProcessTitrationIcon,
    color: '#059669',
    borderColor: 'border-b-[#059669]',
    badgeBg: 'bg-[#059669]',
    textColor: 'text-[#059669]',
    checkColor: 'text-[#059669]',
    iconContainerBg: 'bg-emerald-50/80 border-emerald-200',
    desc: 'Pengujian titrasi pH digital, densitas larutan, dan viskositas Brookfield di laboratorium QC internal selama proses pencampuran.',
    points: [
      'Titrasi elektroda pH digital akurasi 0.01',
      'Pengukuran viskositas Brookfield spindle RPM',
      'Uji berat jenis piknometer presisi 20°C'
    ],
    deliverable: 'Presisi Nilai pH Toleransi ±0.01',
    deliverableIcon: InProcessTitrationIcon
  },
  {
    step: '04',
    phase: 'MICRO FILTRATION & PACKAGING',
    title: 'Penyaringan Mikro & Packaging',
    icon: MicroFiltrationPackagingIcon,
    color: '#7C3AED',
    borderColor: 'border-b-[#7C3AED]',
    badgeBg: 'bg-[#7C3AED]',
    textColor: 'text-[#7C3AED]',
    checkColor: 'text-[#7C3AED]',
    iconContainerBg: 'bg-purple-50/80 border-purple-200',
    desc: 'Filtrasi mikro untuk memastikan cairan jernih bebas partikulat sebelum dialirkan ke jerigen, drum, atau IBC tank kemasan.',
    points: [
      'Filtrasi mikro 5-mikron penyaring partikel',
      'Penimbangan digital otomatis toleransi 0%',
      'Penyegelan tutup anti-bocor (induction sealing)'
    ],
    deliverable: 'Cairan Jernih Terkemas Bebas Endapan',
    deliverableIcon: MicroFiltrationPackagingIcon
  },
  {
    step: '05',
    phase: 'COA RELEASE & LOGISTICS',
    title: 'Penerbitan COA Resmi & Rilis',
    icon: CertifiedCoaLogisticsIcon,
    color: '#0F172A',
    borderColor: 'border-b-[#0F172A]',
    badgeBg: 'bg-[#0F172A]',
    textColor: 'text-[#0F172A]',
    checkColor: 'text-[#0F172A]',
    iconContainerBg: 'bg-slate-100 border-slate-300',
    desc: 'Penerbitan Certificate of Analysis bertandatangan Kepala Laboratorium QC dan pengarsipan retained sample selama 12 bulan.',
    points: [
      'Penerbitan dokumen COA resmi per batch',
      'Penyimpanan retained sample arsip 12 bulan',
      'Serah terima barang ke armada logistik'
    ],
    deliverable: 'Batch Lolos QC, COA & Arsip 1 Tahun',
    deliverableIcon: CertifiedCoaLogisticsIcon
  }
]'''

# Replace old QC_STEPS
import re
pattern = r'const QC_STEPS = \[.*?deliverableIcon: FileCheck2\s*\}\s*\]'
content = re.sub(pattern, icons_code, content, flags=re.DOTALL)

# Now update the card styling in the JSX from rounded-3xl to sharp rounded-xl and industrial housing
old_card = '''className="bg-white rounded-3xl p-6 border border-sky-100 shadow-lg shadow-blue-900/5 hover:shadow-xl transition-all flex flex-col justify-between space-y-5 relative group"'''
new_card = '''className="bg-white rounded-xl p-5 sm:p-6 border border-slate-200/90 shadow-sm hover:shadow-md transition-all flex flex-col justify-between space-y-5 relative group"'''
content = content.replace(old_card, new_card)

# Update step badge from rounded-full to sharp rounded-md
old_badge = '''className={`w-8 h-8 rounded-full ${step.badgeBg} text-white flex items-center justify-center font-heading font-extrabold text-xs shadow-xs`}'''
new_badge = '''className={`w-7 h-7 rounded-md ${step.badgeBg} text-white flex items-center justify-center font-mono font-bold text-xs shadow-xs`}'''
content = content.replace(old_badge, new_badge)

# Update icon housing
old_icon_housing = '''<div className="p-3.5 rounded-2xl bg-sky-50/70 border border-sky-100 flex items-center justify-center group-hover:scale-105 transition-transform">
                        <IconComp className={`w-10 h-10 ${step.textColor} stroke-[1.5]`} />
                      </div>'''
new_icon_housing = '''<div className={`w-14 h-14 rounded-lg ${step.iconContainerBg} border flex items-center justify-center group-hover:scale-105 transition-transform shadow-2xs`}>
                        <IconComp className={`w-8 h-8 ${step.textColor}`} />
                      </div>'''
content = content.replace(old_icon_housing, new_icon_housing)

# Update middle row from rounded-3xl to rounded-xl
old_middle_row = '''<div className="bg-white rounded-3xl border border-sky-100 p-4 sm:p-5 shadow-lg shadow-blue-900/5 flex flex-col lg:flex-row items-stretch lg:items-center gap-4">'''
new_middle_row = '''<div className="bg-white rounded-xl border border-slate-200/90 p-4 sm:p-5 shadow-sm flex flex-col lg:flex-row items-stretch lg:items-center gap-4">'''
content = content.replace(old_middle_row, new_middle_row)

# Update deliverable badge
old_deliv_ribbon = '''<div className="bg-gradient-to-r from-[#0F58A8] to-[#0284C7] text-white px-5 py-3 rounded-2xl flex items-center justify-center shrink-0 lg:w-36 text-center shadow-xs">'''
new_deliv_ribbon = '''<div className="bg-[#0A192F] text-white px-5 py-3 rounded-lg flex items-center justify-center shrink-0 lg:w-36 text-center shadow-xs">'''
content = content.replace(old_deliv_ribbon, new_deliv_ribbon)

# Update deliverable item cards from rounded-2xl to rounded-lg
old_deliv_card = '''className="p-3 rounded-2xl bg-sky-50/50 border border-sky-100 flex items-center gap-2.5 flex-1 min-h-[58px] shadow-2xs"'''
new_deliv_card = '''className="p-3 rounded-lg bg-slate-50 border border-slate-200/80 flex items-center gap-2.5 flex-1 min-h-[58px]"'''
content = content.replace(old_deliv_card, new_deliv_card)

with open('src/pages/CompliancePage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated src/pages/CompliancePage.jsx successfully with industrial icons!')
