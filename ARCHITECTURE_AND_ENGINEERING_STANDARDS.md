# 🛠️ STRUKTUR ARSITEKTUR PROGRAM & STANDAR REKAYASA SISTEM
## PROYEK: PORTAL RESMI PT KEDIRI CHEMICAL ABADI

```
DOKUMEN STANDAR OPERASIONAL TEKNIK — STANDAR ISO 9001:2015
Nomor Dokumen    : ENG-KCA-ARCH-2026-V2 (Modular Domain Edition)
Klasifikasi      : Master Engineering & Architecture Standard
Target Pengguna  : Seluruh AI Agent, Sub-Agent, dan Frontend Engineers
Tujuan Utama     : Anti-Monolith, Isolasi File Mandiri per Kelompok, & Efisiensi Maksimal
Status Dokumen   : Aturan Wajib (Mandatory & Terkendali)
```

---

## 🏛️ 1. PRINSIP UTAMA: "ANTI-MONOLITH & DOMAIN ISOLATION"

DILARANG KERAS membuat **1 File Raksasa ("God File")** yang menumpuk semua kode, CSS, dan data di satu tempat. 

### 4 Aturan Isolasi File Baku:
1. **Aturan 1 Kelompok = 1 File Mandiri**: Setiap seksi visual memiliki 1 file komponen sendiri yang independen. Jika seksi Hero diperbaiki, file Produk tidak akan pernah terpengaruh.
2. **Batas Ukuran File (Max 150–200 Baris)**: Jika satu file JSX mendekati 200 baris, file tersebut **WAJIB** dipecah ke sub-komponen terpisah.
3. **Pemisahan Data dari Tampilan**: Seluruh data teks, angka statistik, dan daftar produk WAJIB disimpan di folder `src/data/` yang dipecah per kelompok file. Komponen JSX murni hanya membaca data via `import`.
4. **Zero CSS Monolith**: Dilarang menumpuk CSS ratusan baris di `index.css`. Gunakan utilitas Tailwind murni langsung pada komponen bersangkutan agar otomatis terkena *tree-shaking* (hanya class yang dipakai yang dikompilasi browser, sehingga aplikasi tetap super ringan).

---

## 📁 2. MATRIKS PEMBAGIAN FILE BERDASARKAN KELOMPOK

Struktur folder dan pembagian tugas file dikunci secara ketat:

```
src/
├── data/                                # PUSAT DATA TERPISAH PER KELOMPOK
│   ├── heroData.js                      # Data teks headline, badge, & 4 metrik Hero
│   ├── productsData.js                  # Database 5 formula kimia, dosis, & spesifikasi
│   ├── makloonData.js                   # Rincian skema reguler vs Dedicated Line VIP
│   ├── industriesData.js                # Database 5 sektor industri & highlight
│   └── companyData.js                   # Legalitas OSS-RBA, LKPP, & data Direksi
│
├── components/
│   ├── layout/                          # TATA LETAK GLOBAL
│   │   ├── Navbar.jsx                   # Floating Glass Island Navbar (Maks 100 baris)
│   │   └── Footer.jsx                   # Corporate Footer 12-Kolom (Maks 120 baris)
│   │
│   ├── sections/                        # SEKSI HALAMAN BERANDA (MANDIRI & TERPISAH)
│   │   ├── HeroSection.jsx              # Khusus Hero + Open Stage Kemasan
│   │   ├── ProductShowcaseSection.jsx   # Khusus Asymmetric Bento Grid Produk
│   │   ├── WhyChooseUsSection.jsx       # Khusus Foto Reaktor & 3 Box Statistik
│   │   ├── MakloonSchemeSection.jsx     # Khusus Skema Maklon Reguler vs Dedicated VIP
│   │   └── IndustriesSection.jsx        # Khusus 5 Sektor Industri
│   │
│   └── ui/                              # KOMPONEN ATOMIK RINGAN (REUSABLE)
│       ├── Button.jsx                   # Tombol Merah Solid & Outline
│       ├── Badge.jsx                    # Pill Badge & Live Pulsing Dot
│       └── RFQModal.jsx                 # Jendela Formulir Pop-up Tender
│
├── pages/                               # ENTRY POINT HALAMAN BERSIH
│   ├── HomePage.jsx                     # Mengimpor seksi-seksi secara modular
│   ├── AboutPage.jsx                    # Profil Pabrik & Dewan Direksi
│   ├── ProductsPage.jsx                 # Katalog Kimia Lengkap
│   ├── ServicesPage.jsx                 # Layanan Maklon Mandiri
│   ├── CompliancePage.jsx               # Kepatuhan Mutu ISO 9001
│   └── ContactPage.jsx                  # Korespondensi & RFQ
│
└── styles/
    └── index.css                        # HANYA @import "tailwindcss"; (Zero Bloat)
```

---

## ⚙️ 3. CONTOH IMPLEMENTASI DATA TERISOLASI

### File Data 1: `src/data/heroData.js`
```javascript
export const HERO_DATA = {
  badge: 'PT KEDIRI CHEMICAL ABADI • EST. 2004',
  titlePrefix: 'Your Trusted Partner for',
  titleHighlight: 'Industrial Chemical Formulations',
  subtitle: 'Pusat riset dan manufaktur kimia pembersih konsentrat 100% non-fosfat berkapasitas 500+ Ton/bulan di Mojoroto, Kediri. Solusi pasokan massal dan maklon private label terpercaya.',
  ctaPrimary: 'Jelajahi Produk Kimia',
  ctaSecondary: 'Minta Penawaran (RFQ)',
  stats: [
    { label: 'Kapasitas', value: '500+ Ton/Bln' },
    { label: 'Teknologi', value: '100% Non-Fosfat' },
    { label: 'Pengadaan', value: 'Resmi LKPP' },
    { label: 'Pengalaman', value: '20+ Tahun' }
  ]
}
```

### File Komponen: `src/components/sections/HeroSection.jsx`
```jsx
// Komponen hanya mengimpor data, tidak ada teks hardcoded panjang!
import { HERO_DATA } from '@/data/heroData'

export default function HeroSection() {
  return (
    <section className="relative w-full bg-[#0A192F] text-white pt-28 pb-52 overflow-hidden">
      {/* Visual Render yang Ringan & Bersih */}
      <h1>{HERO_DATA.titlePrefix} <span className="text-red-500">{HERO_DATA.titleHighlight}</span></h1>
    </section>
  )
}
```

---

## 🚀 4. KEUNTUNGAN POLA MODULAR INI:

| Parameter | Pola Monolitik (Cara Lama) | Pola Terisolasi (Standar KCA Baru) |
| :--- | :--- | :--- |
| **Ukuran File** | 1 File raksasa (500–1000 baris) | **Terbagi menjadi file kecil (80–150 baris)** |
| **Kemudahan Debug** | Sulit mencari baris yang error | **Langsung buka file kelompok bersangkutan** |
| **Risiko Efek Samping** | Mengubah Hero bisa merusak Produk | **0% Efek Samping (Isolasi Total)** |
| **Kecepatan Compile (Vite)**| Lambat karena me-reload file besar | **Instan (< 50ms Hot Module Replacement)** |
| **CSS Bloat** | CSS menumpuk di 1 file besar | **Pure Tailwind Tree-Shaken (Super Ringan)** |

---

## 🚦 5. CHECKLIST PEMERIKSAAN MANDIRI (DEVELOPER / AI AGENT)

```
[ QUALITY GATE KELOMPOK FILE ]
├── [ ] 1. Apakah file komponen JSX memiliki panjang < 200 baris?
├── [ ] 2. Apakah data teks/angka sudah dipisahkan ke file `src/data/[namaKelompok].js`?
├── [ ] 3. Apakah styling menggunakan Tailwind murni tanpa menulis class custom di index.css?
└── [ ] 4. Apakah perubahan pada seksi ini diuji tanpa mempengaruhi seksi lain?
```

---

*Dokumen Standar Arsitektur Terisolasi PT Kediri Chemical Abadi. Acuan Wajib Rekayasa Perangkat Lunak.*
