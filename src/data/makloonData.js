/**
 * PT KEDIRI CHEMICAL ABADI — MAKLOON & TOLL MANUFACTURING DATA
 * Dokumen Kontrol Mutu ISO 9001:2015
 * Zero Emoji Standard - Professional Vector & Text Only
 */

const regularScheme = {
  id: 'regular',
  isVIP: false,
  name: 'Maklon Reguler (Batch Sharing)',
  badge: 'Skema Reguler',
  target: 'UMKM, Sentra Laundry, & Brand Berkembang',
  description: 'Pilihan tepat bagi brand baru dan distributor regional yang ingin memiliki produk kimia dengan merek sendiri tanpa modal pembangunan pabrik.',
  features: [
    { title: 'Minimum Order Fleksibel', desc: 'Mulai dari kapasitas batch standar reaktor pabrik.' },
    { title: 'Formula Teruji Lab QC', desc: 'Akses ke puluhan formula non-fosfat siap edar.' },
    { title: 'Bantuan Legalitas', desc: 'Pendampingan izin edar PKRT & standarisasi kemasan.' },
    { title: 'Pilihan Kemasan Lengkap', desc: 'Jerigen 1L, 5L, 20L, hingga Drum 200L.' }
  ],
  ctaText: 'Konsultasi Maklon Reguler'
}

const dedicatedScheme = {
  id: 'dedicated-line',
  isVIP: true,
  name: 'Dedicated Production Line (Capex-Partnership)',
  badge: 'VIP Capex-Partnership (Unggulan)',
  target: 'Korporat Besar, Jaringan Hotel, & Brand Nasional',
  description: 'Skema kemitraan di mana mitra mendanai pengadaan mesin/reaktor khusus yang didedikasikan 100% untuk produk mereka dengan potongan harga khusus tiap invoice hingga modal investasi kembali.',
  features: [
    { title: 'Jalur Cepat Tanpa Antre (Zero-Queue)', desc: 'Produksi langsung berjalan kapan pun diminta tanpa harus menunggu antrean batch reguler.' },
    { title: 'Pengembalian Modal via Potongan Invoice', desc: 'Mitra memperoleh potongan harga khusus pada setiap faktur hingga nilai modal awal terpenuhi.' },
    { title: 'Mesin Menjadi Aset Pabrik KCA', desc: 'Pemeliharaan dan operasional mesin ditangani sepenuhnya oleh teknisi KCA di pabrik Mojoroto.' },
    { title: 'Harga Pokok Pabrik Tangan Pertama', desc: 'Efisiensi margin maksimal tanpa beban biaya pembangunan fasilitas gedung dan IPAL.' }
  ],
  ctaText: 'Ajukan Dedicated Line VIP'
}

export const MAKLOON_DATA = {
  title: 'Skema Kemitraan Manufaktur & Maklon',
  subtitle: 'Solusi manufaktur terpadu untuk memproduksi formula kimia merek Anda sendiri dengan fasilitas reaktor pabrik berstandar ISO 9001:2015 di Mojoroto, Kediri.',
  regularScheme,
  dedicatedScheme,
  schemes: [regularScheme, dedicatedScheme],
  pillars: [
    { title: 'Kerahasiaan Formula (NDA)', description: 'Perlindungan resep kimia eksklusif milik mitra dengan perjanjian hukum tertutup.' },
    { title: 'Bahan Baku Murni 100%', description: 'Menggunakan surfaktan murni tanpa bahan pengisi filler garam perusak mesin.' },
    { title: 'Dukungan Izin Edar PKRT', description: 'Pendampingan registrasi Kemenkes RI dan standarisasi dokumen teknis MSDS.' },
    { title: 'Kapasitas Reaktor 500+ Ton', description: 'Skalabilitas produksi massal terjamin dengan lini tangki Stainless Steel 316L.' }
  ]
}
