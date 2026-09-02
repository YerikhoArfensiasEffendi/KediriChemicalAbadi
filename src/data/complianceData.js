/**
 * PT KEDIRI CHEMICAL ABADI — REGULATORY COMPLIANCE, QUALITY & ESG MATRIX
 * Dokumen Kontrol Mutu ISO 9001:2015
 * Penanggung Jawab: Yerikho Arfensias Effendi
 */

export const COMPLIANCE_DATA = {
  title: 'Kepatuhan Mutu, Legalitas & Komitmen Lingkungan (ESG)',
  subtitle: 'Standarisasi kendali mutu terpadu dari pengujian bahan baku, proses reaksi di tangki 316L, hingga sertifikasi keamanan lingkungan di fasilitas Mojoroto, Kediri.',
  
  // 4 Pilar Kepatuhan Utama
  pillars: [
    {
      id: 'iso-quality',
      title: 'Standar Manajemen Mutu ISO 9001:2015',
      code: 'ISO 9001:2015 QMS',
      desc: 'Setiap batch produksi melalui prosedur Standard Operating Procedure (SOP) pengujian laboratorium terakreditasi: pengujian berat jenis, pH digital, viskositas, dan stabilitas suhu 45°C.',
      points: [
        'Uji Lab Bertingkat (Bahan Baku Masuk s/d Produk Jadi)',
        'Sistem Retained Sample (Sampel Arsip Disimpan Minimal 12 Bulan)',
        'Dokumentasi Batch Record & Sertifikat Analisis (Certificate of Analysis / COA)'
      ]
    },
    {
      id: 'eco-ipal',
      title: 'Komitmen 100% Non-Fosfat & Kelayakan IPAL',
      code: 'ECO-BIOCOMPLIANT',
      desc: 'Formula pembersih KCA bebas dari senyawa fosfat (Sodium Tripolyphosphate / STPP) sehingga tidak menimbulkan eutrofikasi air dan menjaga viabilitas bakteri pengurai limbah cair rumah sakit & sentra laundry.',
      points: [
        'Menekan Beban Chemical Oxygen Demand (COD) & BOD Air Limbah',
        'Bahan Aktif Surfaktan Biodegradable (>90% Terurai Alami)',
        'Aman untuk Sistem Pengolahan Air Limbah Rumah Sakit (KARS Compliant)'
      ]
    },
    {
      id: 'k3-safety',
      title: 'Keselamatan, Kesehatan Kerja & Lingkungan (K3L)',
      code: 'SMK3 & GHS SAFETY',
      desc: 'Penerapan standar keselamatan kerja industri kimia dengan fasilitas eye-washer, APD lengkap, penanganan bahan baku berbasis Globally Harmonized System (GHS), dan ventilasi udara aktif.',
      points: [
        'Tersedia Lembar Data Keselamatan Bahan (MSDS / SDS Resmi GHS)',
        'Pelatihan Rutin Penanganan Tumpahan Bahan Kimia (Spill Kit)',
        'Zona Pabrik Terstandarisasi Pencegahan Bahaya Kebakaran & Kontaminasi'
      ]
    },
    {
      id: 'legal-governance',
      title: 'Legalitas Badan Usaha & e-Catalog Pemerintah',
      code: 'OSS-RBA & LKPP RI',
      desc: 'PT Kediri Chemical Abadi beroperasi secara sah berdasarkan hukum Republik Indonesia dengan NIB Berbasis Risiko BKPM dan terdaftar sebagai penyedia resmi barang/jasa pemerintah.',
      points: [
        'Terdaftar di e-Catalog LKPP Pengadaan Barang/Jasa Pemerintah RI',
        'KBLI Industri Kimia Sabun (20231), Kosmetik (20232), & Kimia Teknis (20299)',
        'Transparansi Pajak Korporat (NPWP & Pengusaha Kena Pajak / PKP)'
      ]
    }
  ],

  // Lembar Prosedur QC per Batch Produksi
  qcCheckpoints: [
    { step: '01', name: 'Analisis Bahan Baku Murni', desc: 'Uji kemurnian surfaktan, pelarut, dan bahan aktif sebelum masuk ke tangki reaktor.' },
    { step: '02', name: 'Reaksi Kimia Tangki 316L', desc: 'Pengadukan dengan kecepatan terukur (RPM terkontrol) pada suhu stabil.' },
    { step: '03', name: 'Sampling Tengah Batch', desc: 'Pemeriksaan pH, densitas, dan homogenitas formula di laboratorium QC internal.' },
    { step: '04', name: 'Penyaringan & Pengisian', desc: 'Filtrasi mikro untuk memastikan cairan jernih bebas endapan sebelum masuk kemasan.' },
    { step: '05', name: 'Penerbitan COA Resmi', desc: 'Penerbitan Certificate of Analysis bertandatangan Lab Head untuk setiap lot pengiriman.' }
  ]
}
