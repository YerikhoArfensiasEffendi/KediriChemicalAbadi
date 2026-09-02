# 🎨 DESIGN STYLE GUIDE & BRAND IDENTITY SPECIFICATION
## PROYEK: PT KEDIRI CHEMICAL ABADI — BRIGHT CLEAN WHITE & ROYAL BLUE INDUSTRIAL

```
DOKUMEN PANDUAN DESAIN RESMI — STANDAR ISO 9001:2015
Nomor Dokumen   : DSG-KCA-2026-V7 (Bright Clean White & Swiss Industrial Edition)
Penanggung Jawab: Yerikho Arfensias Effendi (Director of Operations & Finance)
Direktur Utama  : Yan Effendi (President Director)
Perusahaan      : PT Kediri Chemical Abadi
Status          : Acuan Mutlak Desain (Dominan Putih Cerah, Anti-Kotak Gelap, No Monospace)
```

---

## 🏛️ 1. FILOSOFI DESAIN: "SWISS INDUSTRIAL HIGH-CLARITY (BRIGHT WHITE & BLUE)"

Desain website PT Kediri Chemical Abadi beralih sepenuhnya ke gaya **Manufaktur & Laboratorium Kimia Modern Kelas Dunia yang Terang, Bersih, dan Presisi** (seperti standar korporat *Roche, Sika, Clariant, Lonza, dan BASF Light Corporate*):

### 4 Pilar Desain Terang & Profesional:
1. **LATAR BELAKANG DOMINAN PUTIH BERSIH & CERAH (60% PURE WHITE)**:
   - Menghilangkan kesan gelap gulita (*dark terminal*). Website didominasi oleh **Putih Bersih (`#FFFFFF`)** dan **Soft Alabaster (`#F8FAFC`)** yang memberikan kesan higienis, lapang, dan berstandar laboratorium modern.
2. **HAPUS KARTU KOTAK GELAP & HAPUS FONT MONOSPACE (TERMINAL-STYLE)**:
   - DILARANG menggunakan kotak-kotak kartu hitam kecil dengan font monospace/typewriter (seperti `[ KAPASITAS REAKTOR 500+ Ton/Bln ]`).
   - Gunakan **Tampilan Metrik Tipografi Angka Besar (*Large Numerical Stat Display*)** langsung di atas kanvas terang:
     ```jsx
     // STANDAR METRIK PROFESIONAL (ANGKA BESAR + LABEL RAMPING + GARIS HALUS)
     <div className="flex flex-col border-l-2 border-blue-600 pl-4">
       <span className="text-3xl sm:text-4xl font-extrabold font-heading text-slate-900 tracking-tight">
         500+ Ton
       </span>
       <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider mt-1">
         Kapasitas Produksi / Bulan
       </span>
     </div>
     ```
3. **TIPOGRAFI MODERN SANS-SERIF KORPORAT (INTER & PLUS JAKARTA SANS)**:
   - Seluruh teks, angka statistik, dan eyebrow menggunakan font Sans-serif yang tebal, tegas, dan berwibawa (ZERO Monospace/Mesin Tik).
4. **PALET WARNA RESMI: PUTIH BERSIH 60%, NAVY KORPORAT 30%, ROYAL BLUE 10%**:
   - Selaras dengan logo molekul resmi PT Kediri Chemical Abadi dan fasilitas pabrik yang bersih dan terang.

---

## 🎨 2. PALET WARNA RESMI TERANG (60-30-10)

```
┌────────────────────────────────────────────────────────────────────────┐
│  60% PUTIH BERSIH & ALABASTER│  30% DEEP CORPORATE NAVY │ 10% ROYAL BLUE│
│  (#FFFFFF & #F8FAFC)         │  (#0A192F & #0F172A)     │ (#0F58A8/#2563│
└────────────────────────────────────────────────────────────────────────┘
```

| Token Warna | Nilai Hex | Fungsi & Peruntukan dalam Komponen |
| :--- | :--- | :--- |
| **`white-pure` (Dominan)**| `#FFFFFF` | Latar utama halaman, kanvas Hero, dan kontainer utama. |
| **`alabaster`** | `#F8FAFC` | Latar section selang-seling dan kontras lembut. |
| **`slate-light`** | `#F1F5F9` | Latar area data teknis, tabel spesifikasi, dan formulir. |
| **`navy-text` (Secondary)**| `#0A192F` / `#0F172A` | Teks judul utama (H1/H2), angka statistik, dan Footer. |
| **`blue-royal` (Aksen)** | `#0F58A8` / `#2563EB` | Tombol CTA utama (RFQ), garis aksen vertikal, dan highlight. |
| **`text-muted`** | `#64748B` | Teks paragraf pendukung dan label spesifikasi teknis. |
| **`border-hairline`** | `#E2E8F0` | Garis pembatas tipis antar kolom (Hairline 1px). |

---

## 🚫 3. DAFTAR LARANGAN KERAS DESAIN (PERMANENT BAN)

```
[ DAFTAR LARANGAN MUTLAK ]
❌ 1. DILARANG menggunakan kotak kartu hitam kecil dengan border tebal untuk statistik.
❌ 2. DILARANG menggunakan font monospace / mesin tik (font-mono) pada teks dan angka.
❌ 3. DILARANG menggunakan tema gelap gulita; website wajib dominan PUTIH TERANG & BERSIH.
❌ 4. DILARANG menggunakan segala jenis emoji (⭐, 🚀, 💡, 📦, dll).
❌ 5. DILARANG menggunakan badge kapsul bertutup keliling (pill card).
```

---

## 📐 4. ANATOMI HERO SECTION TERANG & ELEGAN

* **Latar Belakang**: Putih Bersih (`#FFFFFF`) dengan aksen watermark halus foto reaktor pabrik `kca_factory_reactors.jpg` (`opacity-[0.08]`) dan gradasi biru royal lembut di sudut atas.
* **Sisi Kiri (7 Kolom Grid)**:
  - Eyebrow: Teks Sans-serif biru royal elegan:
    `<span className="text-xs font-extrabold tracking-widest text-[#0F58A8] uppercase">PT KEDIRI CHEMICAL ABADI • EST. 2004</span>`
  - Headline Besar:
    *"Mitra Terpercaya Manufaktur & <span className="text-[#0F58A8]">Formulasi Kimia Industri</span>"*
  - Subtitle: Paragraf abu-abu gelap `text-slate-600 text-base leading-relaxed max-w-xl`.
  - Dual Tombol:
    - Tombol 1: `[ Jelajahi Produk Kimia ]` (Biru Royal `#0F58A8` solid, text-white, h-12 px-8, rounded-xl, font-bold).
    - Tombol 2: `[ Minta Penawaran (RFQ) ]` (Putih Bersih, border border-slate-300, text-slate-800, h-12 px-8, rounded-xl, font-bold).
  - **4 Metrik Statistik Tipografi Terbuka (Tanpa Kotak Hitam)**:
    `grid grid-cols-2 sm:grid-cols-4 gap-6 pt-8 border-t border-slate-200`
    - Angka besar `text-3xl font-extrabold text-slate-900` + label di bawahnya `text-xs text-slate-500 font-semibold uppercase`.
* **Sisi Kanan (5 Kolom Grid)**:
  - Foto lini kemasan `kca_packaging_lineup.png` berdiri bersih dengan bayangan kontak alami (*soft ambient occlusion shadow*) di atas lantai putih.

---

*Dokumen Terkendali PT Kediri Chemical Abadi. Disahkan oleh Yerikho Arfensias Effendi & Yan Effendi.*
