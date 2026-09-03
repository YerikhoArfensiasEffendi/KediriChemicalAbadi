/**
 * PT KEDIRI CHEMICAL ABADI — MASTER CONSULTATION, DOSAGE CALCULATOR & TECHNICAL KNOWLEDGE BASE
 * Standar Manajemen Mutu ISO 9001:2015
 * Penanggung Jawab Formulasi: Yerikho Arfensias Effendi
 */

export const STAIN_PROBLEMS = [
  {
    id: 'blood-medical',
    label: 'Darah, Serum & Cairan Biologis',
    sector: 'medis',
    severity: 'Tinggi (Infeksius)',
    desc: 'Noda hemoglobin darah dan eksudat luka pada linen kamar operasi dan rawat inap rumah sakit.',
    recommendedProducts: [
      { name: 'Alkali Booster Concentrate', sku: 'KCA-AB02', role: 'Pembuka pori serat & pelarut koagulasi protein', dose: '8 – 12 ml/kg' },
      { name: 'Liquid Detergent Non-Phosphate', sku: 'KCA-LD01', role: 'Surfaktan penetrasi inti serat noda', dose: '12 – 15 ml/kg' },
      { name: 'Oxygen Bleach Liquid Color-Safe', sku: 'KCA-OB04', role: 'Oksigen aktif pengangkat noda darah & disinfeksi', dose: '8 – 10 ml/kg' },
      { name: 'Sour Neutralizer Anti-Chlor', sku: 'KCA-SN06', role: 'Penetral sisa alkali agar pH kain netral 6.5–7.0', dose: '2 – 3 ml/kg' }
    ],
    sopSteps: [
      { step: 1, name: 'Cold Flush (Bilas Dingin)', temp: 'Suhu Normal (25–30°C)', time: '3–5 Menit', note: 'Wajib air dingin untuk mencegah denaturasi protein darah.' },
      { step: 2, name: 'Main Wash (Alkali + Deterjen)', temp: '55 – 65°C', time: '12–15 Menit', note: 'Alkali melunakkan hemoglobin, surfaktan menarik kotoran.' },
      { step: 3, name: 'Bleaching (Oxy Bleach)', temp: '60 – 70°C', time: '10–12 Menit', note: 'Menghilangkan sisa bayangan darah sekaligus disinfeksi spora patogen.' },
      { step: 4, name: 'Rinse & Neutralize (Sour)', temp: 'Suhu Normal', time: '5 Menit', note: 'Menetralkan pH serat katun agar tidak mengiritasi kulit pasien.' }
    ]
  },
  {
    id: 'heavy-oil-grease',
    label: 'Oli Mesin Berat, Gemuk & Gemuk Hitam',
    sector: 'otomotif',
    severity: 'Berat (Industri)',
    desc: 'Oli mineral hidrokarbon, grease sasis kendaraan, dan tar aspal pada wearpack mekanik & kain bengkel.',
    recommendedProducts: [
      { name: 'Emulsifier Oil & Grease Remover', sku: 'KCA-EM03', role: 'Pelarut rantai hidrokarbon oli mineral', dose: '5 – 8 ml/kg' },
      { name: 'Alkali Booster Concentrate', sku: 'KCA-AB02', role: 'Meningkatkan saponifikasi lemak & minyak mesin', dose: '10 – 15 ml/kg' },
      { name: 'Liquid Detergent Non-Phosphate', sku: 'KCA-LD01', role: 'Surfaktan pembersih residu jelaga karbon', dose: '12 – 15 ml/kg' }
    ],
    sopSteps: [
      { step: 1, name: 'Spotting / Pre-Soak (Emulsifier)', temp: '40 – 50°C', time: '10 Menit', note: 'Rendam atau semprotkan murni pada area noda oli pekat.' },
      { step: 2, name: 'Main Wash (Alkali + Emulsifier + LD)', temp: '65 – 75°C', time: '15–18 Menit', note: 'Suhu tinggi mutlak diperlukan untuk mencairkan gemuk mesin.' },
      { step: 3, name: 'Double Hot Rinse (Bilas Ganda Panas)', temp: '50°C lalu Dingin', time: '8 Menit', note: 'Mencegah noda oli yang terlepas menempel kembali (redeposition).' }
    ]
  },
  {
    id: 'hard-water',
    label: 'Air Tanah Sadah / Berkapur (>350 ppm)',
    sector: 'laundry',
    severity: 'Sedang (Operasional)',
    desc: 'Kandungan kalsium & magnesium air tanah tinggi yang mematikan busa dan membuat kain kaku menguning.',
    recommendedProducts: [
      { name: 'Alkali Booster Concentrate', sku: 'KCA-AB02', role: 'Mengikat ion Ca²⁺ dan Mg²⁺ (Sequestering Complex)', dose: '10 – 15 ml/kg' },
      { name: 'Liquid Detergent Non-Phosphate', sku: 'KCA-LD01', role: 'Surfaktan non-ionik etoksilat tahan mineral sadah', dose: '12 – 15 ml/kg' },
      { name: 'Sour Neutralizer Anti-Chlor', sku: 'KCA-SN06', role: 'Mencegah pengkristalan kapur di pori serat kain', dose: '3 – 5 ml/kg' }
    ],
    sopSteps: [
      { step: 1, name: 'Water Conditioning Cycle', temp: 'Suhu Normal', time: 'Simultan', note: 'Masukkan Alkali Booster di awal pengisian air untuk melunakkan kesadahan.' },
      { step: 2, name: 'Main Wash Dosis Terkalibrasi', temp: '50 – 60°C', time: '12 Menit', note: 'Surfaktan non-ionik KCA bekerja maksimal tanpa terikat mineral sadah.' },
      { step: 3, name: 'Anti-Scale Rinse (Sour)', temp: 'Suhu Normal', time: '5 Menit', note: 'Mencegah endapan kerak kapur mengeras pada serat katun.' }
    ]
  },
  {
    id: 'food-sauce-grease',
    label: 'Minyak Goreng, Saus Bumbu & Lemak Makanan',
    sector: 'fnb',
    severity: 'Sedang (Komersial)',
    desc: 'Lemak nabati/hewani, kecap, saus tomat, dan bumbu dapur pada taplak meja resto & seragam koki.',
    recommendedProducts: [
      { name: 'Emulsifier Oil & Grease Remover', sku: 'KCA-EM03', role: 'Emulsifikasi lemak jenuh & minyak goreng jelantah', dose: '4 – 6 ml/kg' },
      { name: 'Liquid Detergent Non-Phosphate', sku: 'KCA-LD01', role: 'Pengangkat noda protein & pigmen bumbu', dose: '10 – 12 ml/kg' },
      { name: 'Oxygen Bleach Liquid Color-Safe', sku: 'KCA-OB04', role: 'Pencerah warna motif taplak tanpa luntur', dose: '6 – 8 ml/kg' }
    ],
    sopSteps: [
      { step: 1, name: 'Warm Pre-Wash (Air Hangat)', temp: '45 – 50°C', time: '5 Menit', note: 'Melunakkan lemak beku minyak goreng dan saus mentega.' },
      { step: 2, name: 'Main Wash (Emulsifier + LD)', temp: '60°C', time: '12 Menit', note: 'Deterjen menarik kotoran, emulsifier mengikat tetesan minyak.' },
      { step: 3, name: 'Oxygen Bleach Cycle', temp: '60°C', time: '10 Menit', note: 'Mengoksidasi residu pigmen cabai/tomat tanpa merusak warna kain.' }
    ]
  },
  {
    id: 'yellowing-graying',
    label: 'Linen Kusam, Menguning & Berkerak (Yellowing)',
    sector: 'housekeeping',
    severity: 'Sedang (Estetika)',
    desc: 'Penumpukan residu deterjen curah, kapur air tanah, atau pemutih klorin berlebih pada sprei hotel.',
    recommendedProducts: [
      { name: 'Sour Neutralizer Anti-Chlor', sku: 'KCA-SN06', role: 'Iron sour pengangkat karat & pelarut residu garam', dose: '5 – 8 ml/kg' },
      { name: 'Alkali Booster Concentrate', sku: 'KCA-AB02', role: 'Stripping build-up kimia lama pada serat kain', dose: '12 – 15 ml/kg' },
      { name: 'Oxygen Bleach Liquid Color-Safe', sku: 'KCA-OB04', role: 'Pencerah optik ramah serat (Optical Brightener)', dose: '10 ml/kg' }
    ],
    sopSteps: [
      { step: 1, name: 'Stripping Cycle (Pencucian Ulang Khusus)', temp: '65 – 70°C', time: '20 Menit', note: 'Cuci dengan Alkali Booster tinggi tanpa deterjen untuk mengikis residu.' },
      { step: 2, name: 'Oxygen Recovery Wash', temp: '60°C', time: '15 Menit', note: 'Oxy Bleach mengaktifkan pencerah warna optik murni.' },
      { step: 3, name: 'Heavy Sour Rinse', temp: 'Suhu Normal', time: '7 Menit', note: 'Bilas dengan Sour Neutralizer untuk melarutkan sisa garam kapur.' }
    ]
  },
  {
    id: 'mold-musty-odor',
    label: 'Bau Apek, Jamur & Bakteri Patogen',
    sector: 'laundry',
    severity: 'Sedang (Higienis)',
    desc: 'Linen lembab terperangkap di keranjang cucian atau infeksi jamur bintik hitam akibat pengeringan kurang tuntas.',
    recommendedProducts: [
      { name: 'Oxygen Bleach Liquid Color-Safe', sku: 'KCA-OB04', role: 'Disinfektan oksidator pembasmi spora jamur', dose: '8 – 12 ml/kg' },
      { name: 'Liquid Detergent Non-Phosphate', sku: 'KCA-LD01', role: 'Surfaktan pencuci penetrasi pori mikro kain', dose: '12 – 15 ml/kg' },
      { name: 'Fabric Softener Anti-Static', sku: 'KCA-FS05', role: 'Conditioner serat anti-statik & wangi tahan lama', dose: '5 – 8 ml/kg' }
    ],
    sopSteps: [
      { step: 1, name: 'Pre-Soak Desinfeksi Oksigen', temp: '50 – 60°C', time: '15 Menit', note: 'Rendam dengan Oxy Bleach untuk membunuh spora jamur.' },
      { step: 2, name: 'Main Wash Surfaktan Murni', temp: '55°C', time: '12 Menit', note: 'Mencuci sisa koloni jamur yang mati dari jalinan benang katun.' },
      { step: 3, name: 'Conditioning Anti-Static', temp: 'Suhu Normal', time: '5 Menit', note: 'Softener KCA melindungi serat katun dengan lapisan anti-bakteri.' }
    ]
  }
]

export const SECTORS_LIST = [
  { id: 'all', label: 'Semua Sektor' },
  { id: 'laundry', label: 'Sentra Laundry Komersial' },
  { id: 'medis', label: 'Rumah Sakit & Klinik (KARS)' },
  { id: 'housekeeping', label: 'Hotel & Hospitality' },
  { id: 'fnb', label: 'F&B & Restoran' },
  { id: 'otomotif', label: 'Pabrik & Otomotif' },
]

export const CALCULATOR_PRESETS = [
  { id: 'laundry-commercial', name: 'Sentra Laundry Komersial / Kiloan', defaultKg: 350, kcaRate: 12.5, retailRate: 40, kcaPrice: 18000, retailPrice: 24000 },
  { id: 'hospital', name: 'Rumah Sakit Rujukan / RSUD (KARS)', defaultKg: 800, kcaRate: 14.0, retailRate: 45, kcaPrice: 19500, retailPrice: 28000 },
  { id: 'hotel', name: 'Hotel Berbintang & Resort', defaultKg: 500, kcaRate: 12.0, retailRate: 38, kcaPrice: 18500, retailPrice: 26000 },
  { id: 'industrial-plant', name: 'Pabrik Manufaktur / Bengkel', defaultKg: 250, kcaRate: 15.0, retailRate: 50, kcaPrice: 21000, retailPrice: 32000 },
]

export const TECHNICAL_ARTICLES = [
  {
    id: 'sop-linen-rs-kars',
    category: 'SOP Medis & KARS',
    categoryColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    title: 'SOP Pencucian Linen Infeksius & Bedah Standar Akreditasi KARS',
    readTime: '6 Menit Baca',
    date: 'Standar Mutu 2026',
    author: 'Tim Formulator PT Kediri Chemical Abadi',
    summary: 'Prosedur operasional baku desinfeksi termokimia linen rumah sakit untuk mematikan bakteri patogen nosokomial tanpa merusak serat katun maupun instalasi IPAL.',
    keyPoints: [
      'Pemisahan linen infeksius berkantung kuning vs linen non-infeksius',
      'Desinfeksi suhu termal 65–71°C dengan Oksigen Aktif tanpa merapuhkan katun',
      'Larangan penggunaan klorin pekat pada noda darah untuk mencegah fiksasi noda permanen',
      'Kewajiban proses netralisasi akhir (Sour) pada rentang pH kulit sehat 6.5–7.0'
    ],
    fullContent: `Pencucian linen rumah sakit bukan sekadar proses pembersihan estetika, melainkan mata rantai kritis dalam pengendalian infeksi nosokomial (Hospital Acquired Infections - HAIs). Kegagalan proses pencucian dapat mentransmisikan patogen resisten seperti Methicillin-Resistant Staphylococcus Aureus (MRSA) dan spora bakteri berbahaya.

Tahapan Baku Prosedur Pencucian Linen Medis:

1. Penerimaan & Pemisahan Linen (Sluicing Area)
Linen Infeksius: Linen yang terpapar darah, cairan tubuh, eksudat luka, atau berasal dari ruang isolasi infeksius wajib dimasukkan dalam kantung plastik kuning tertutup.
Linen Non-Infeksius: Linen dari poliklinik rawat jalan dan ruang administrasi diproses di jalur terpisah untuk mencegah kontaminasi silang.

2. Siklus Bilas Awal (Cold Water Flush)
Wajib Menggunakan Air Dingin (25–30°C) selama 3–5 menit.
Alasan Ilmiah: Air panas di atas 45°C akan mendenaturasi dan mengkoagulasi protein hemoglobin darah, menyebabkan noda mengikat permanen ke inti serat katun (stain fixation).

3. Siklus Pencucian Utama (Main Wash)
Kimia Utama: Liquid Detergent Non-Phosphate KCA (12–15 ml/kg) + Alkali Booster Concentrate KCA (8–10 ml/kg).
Suhu Operasional: 60–65°C selama 15 menit.
Mekanisme: Suhu panas dikombinasikan pH alkali (10.5–11.5) membuka pori serat linen dan menyabunkan lemak biologis, memungkinkan surfaktan meresap tuntas.

4. Siklus Desinfeksi & Pemutihan (Bleaching Cycle)
Kimia: Oxygen Bleach Liquid Color-Safe KCA (8–10 ml/kg).
Keunggulan vs Klorin: Oksigen aktif membunuh spora patogen tanpa merapuhkan serat tenun dan tidak menghasilkan gas toksik klorin yang membahayakan petugas laundry.

5. Siklus Penetralan Akhir (Sour Neutralizing)
Kimia: Sour Neutralizer KCA (2–3 ml/kg).
Target pH Akhir Linen: Wajib berada pada rentang pH 6.5 – 7.0.
Pentingnya Medis: Residu alkali pada linen yang tidak dinetralkan akan memicu dermatitis kontak, ruam alergi, dan decubitus pada pasien rawat inap lama.`
  },
  {
    id: 'mengatasi-air-sadah-jawa-timur',
    category: 'Teknik Kimia Lapangan',
    categoryColor: 'bg-blue-50 text-blue-700 border-blue-200',
    title: 'Menaklukkan Air Sadah (>350 ppm CaCO₃) Tanpa Merusak Serat Kain & Mesin',
    readTime: '5 Menit Baca',
    date: 'Panduan Lapangan Wilayah Jawa Timur',
    author: 'Yerikho Arfensias Effendi',
    summary: 'Solusi teknis mengatasi air tanah sumur bor berkapur tinggi di Jawa Timur agar daya cuci deterjen tidak drop, mesin cuci bebas kerak kapur, dan linen tidak kaku abu-abu.',
    keyPoints: [
      'Dampak kesadahan: Kation Ca²⁺ dan Mg²⁺ mengikat surfaktan konvensional hingga 50%',
      'Ciri visual: Busa mati mendadak, kain terasa kasar seperti amplas, kerak putih di heater mesin',
      'Mekanisme agen pengkhelat (Sequestering Complex) dalam Alkali Booster KCA',
      'Perhitungan efisiensi biaya: Melunakkan air vs boros deterjen 200%'
    ],
    fullContent: `Sebagian besar sentra industri laundry dan rumah sakit di wilayah Kediri, Tulungagung, Nganjuk, Jombang, hingga Surabaya mengandalkan air tanah sumur dalam (deep well). Uji laboratorium KCA menunjukkan rata-rata kesadahan total (Total Hardness) berkisar antara 280 ppm hingga 450 ppm CaCO₃ (kategori sangat sadah / very hard water).

Mengapa Air Sadah Jadi Musuh Utama Pengusaha Laundry?

1. Fenomena Deaktivasi Surfaktan
Ion Kalsium (Ca²⁺) dan Magnesium (Mg²⁺) bermuatan positif ganda akan bereaksi langsung dengan molekul surfaktan anionik deterjen konvensional, membentuk endapan garam tidak larut (lime soap). Akibatnya daya bersih deterjen turun drastis hingga 50%. Operator laundry secara keliru melipatgandakan dosis deterjen, menyebabkan lonjakan biaya operasional kimia hingga 2x lipat.

2. Kerusakan Serat Linen (Graying & Encrustation)
Endapan garam kalsium mengkristal di dalam sela-sela jalinan benang katun. Hasilnya serat kain menjadi kaku, kasar, dan mudah sobek saat proses setrika roll (flatwork ironer). Warna putih cemerlang perlahan berubah menjadi kusam keabu-abuan.

3. Kerak Elemen Pemanas Mesin (Scale Buildup)
Endapan kalsium karbonat menempel pada elemen pemanas mesin cuci extractor, membentuk lapisan isolator panas. Mesin membutuhkan konsumsi listrik/gas hingga 30% lebih banyak untuk mencapai suhu yang sama.

Solusi Rekayasa Kimia KCA:
1. Penambahan Alkali Booster Concentrate: Mengandung senyawa Polycarboxylate Sequestering Agent murni yang bertindak sebagai penjepit ion Ca²⁺ dan Mg²⁺, mengurung ion mineral sadah sebelum sempat mengganggu kerja surfaktan.
2. Penggunaan Surfaktan Non-Ionik Tahan Sadah: Liquid Detergent Non-Phosphate KCA diformulasikan dengan gugus etoksilat non-ionik yang tidak terpengaruh muatan listrik ion kalsium, sehingga tetap menghasilkan daya pembersihan 100% prima pada air sesadah apapun.`
  },
  {
    id: 'matriks-penghilang-noda-khusus',
    category: 'Formulasi Noda Berat',
    categoryColor: 'bg-amber-50 text-amber-700 border-amber-200',
    title: 'Matriks Kimia Penghilang Noda Membandel: Oli Mesin, Kunyit, Getah & Jamur',
    readTime: '7 Menit Baca',
    date: 'Formulasi Formulator KCA',
    author: 'Tim Laboratorium Riset KCA',
    summary: 'Tabel referensi komprehensif pelarut kimia berbasis polaritas senyawa untuk mengangkat noda spesifik tanpa merusak warna kain asli.',
    keyPoints: [
      'Klasifikasi noda: Berbasis minyak (non-polar), berbasis protein (amfoter), pigmen organik',
      'Teknik spotting pre-treatment sebelum pencucian massal',
      'Aturan emas suhu pencucian untuk setiap jenis noda kimia',
      'Kombinasi Emulsifier + Oxy Bleach untuk noda bumbu masakan resto'
    ],
    fullContent: `Prinsip dasar penghilangan noda industri adalah mencocokkan polaritas pelarut kimia dengan polaritas molekul noda. Menggunakan air dan deterjen biasa untuk noda oli mesin berat tidak akan pernah tuntas karena minyak bersifat non-polar hidrokarbon, sedangkan molekul air bersifat sangat polar.

Matriks Solusi Lapangan KCA:

1. Oli Mesin Berat & Gemuk (Non-polar hidrokarbon): Gunakan Emulsifier Oil & Grease KCA pada suhu 65–75°C. Spotting murni pada noda, diamkan 5 menit, cuci dengan air panas.
2. Darah Segar & Kering (Protein biologis Albumin & Hemoglobin): Gunakan Alkali Booster + Liquid Detergent dengan air dingin 25°C. Bilas dingin terlebih dahulu. Hindari air panas sebelum darah larut!
3. Kunyit & Saus Kari (Pigmen Kurkuminoid organik): Gunakan Oxy Bleach Liquid Color-Safe pada suhu 60°C. Rendam 15 menit dengan Oxy Bleach panas, cuci normal.
4. Keringat Daki Kerah (Campuran sebum lemak & garam tubuh): Gunakan Emulsifier + Alkali Booster pada suhu 55°C. Sikat ringan area kerah dengan pasta konsentrat, bilas tuntas.
5. Karat Air Sumur (Oksida Besi Fe₂O₃): Gunakan Sour Neutralizer Rust Stripper pada suhu 40–50°C. Asam organik lemah melarutkan ion besi tanpa membakar serat.
6. Jamur Bintik Hitam (Spora fungi seluler lembab): Gunakan Oxy Bleach pada suhu 60°C. Rendam 30 menit dalam larutan oksidator pekat.`
  },
  {
    id: 'kalkulasi-efisiensi-konsentrat-vs-retail',
    category: 'Akuntansi Biaya Laundry',
    categoryColor: 'bg-indigo-50 text-indigo-700 border-indigo-200',
    title: 'Kalkulasi Akuntansi: Menghitung Efisiensi Dosis Konsentrat vs Deterjen Retail',
    readTime: '5 Menit Baca',
    date: 'Analisis Finansial B2B',
    author: 'Yerikho Arfensias Effendi',
    summary: 'Membedah rumus matematis Cost-in-Use per kilogram cucian. Bukti mengapa deterjen konsentrat murni jauh lebih menguntungkan dibanding deterjen murah ber-filler garam.',
    keyPoints: [
      'Perangkap Harga Per Liter Murah pada deterjen curah filler garam dapur (NaCl)',
      'Rumus Cost-in-Use (CIU) = (Dosis ml / 1.000) x Harga Kimia per Liter',
      'Studi kasus laundry hotel 500 kg/hari: Hemat hingga Rp 3.375.000 / bulan',
      'Pengurangan biaya logistik, tempat penyimpanan, dan limbah jerigen kosong'
    ],
    fullContent: `Banyak manajer operasional terjebak membeli deterjen curah kiloan berharga murah (misal Rp 10.000 / liter). Padahal setelah diuji di laboratorium KCA:
- 70% komposisinya hanyalah air dan garam dapur (Sodium Chloride / NaCl) sebagai bahan pengental semu.
- Kadar bahan aktif surfaktan murni (Active Matter) hanya berkisar antara 4% – 6%.
- Akibatnya, operator laundry membutuhkan dosis hingga 40 – 50 ml per kg cucian agar busa tampak keluar.

Perbandingan Matematis Cost-in-Use (CIU):

Kasus: Beban Cucian 500 kg Linen per Hari

Opsi A: Deterjen Curah / Retail Konvensional
Harga: Rp 10.000 / Liter
Dosis Rata-rata: 45 ml / kg cucian
Kebutuhan Harian: (500 kg x 45 ml) / 1.000 = 22.5 Liter / hari
Biaya Kimia Harian: 22.5 Liter x Rp 10.000 = Rp 225.000 / hari
Biaya Kimia Bulanan (30 Hari): Rp 6.750.000 / bulan

Opsi B: Liquid Detergent Non-Phosphate KCA (Konsentrat Murni)
Harga: Rp 18.000 / Liter
Dosis Rata-rata: 12.5 ml / kg cucian (Active Matter 20% murni)
Kebutuhan Harian: (500 kg x 12.5 ml) / 1.000 = 6.25 Liter / hari
Biaya Kimia Harian: 6.25 Liter x Rp 18.000 = Rp 112.500 / hari
Biaya Kimia Bulanan (30 Hari): Rp 3.375.000 / bulan

Kesimpulan Penghematan Finansial:
- Penghematan Langsung: Rp 3.375.000 per bulan (Hemat 50% Biaya Pembelian Kimia).
- Hemat Tempat & Logistik: Hanya menyimpan 187.5 Liter (9 jerigen 20L) vs 675 Liter (34 jerigen).
- Perlindungan Mesin: Zero garam dapur berarti nol risiko karat pada drum stainless mesin cuci extractor mahal Anda.`
  },
  {
    id: 'kepatuhan-ipal-bebas-fosfat',
    category: 'Standar Mutu Lingkungan',
    categoryColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    title: 'Standar Baku Mutu Air Limbah: Mengapa Bebas Fosfat (STPP-Free) Wajib untuk IPAL',
    readTime: '6 Menit Baca',
    date: 'Kepatuhan Regulasi Lingkungan',
    author: 'Tim Kepatuhan Mutu ISO KCA',
    summary: 'Penjelasan ilmiah dampak fosfat terhadap kolam aerasi IPAL rumah sakit, ancaman denda dinas lingkungan hidup, dan keunggulan sertifikasi OECD 301D.',
    keyPoints: [
      'Baku mutu air limbah Permen LHK tentang limbah domestik & medis',
      'Mekanisme eutrofikasi: Fosfat memicu blooming alga dan menghabiskan Dissolved Oxygen (DO)',
      'Kematian bakteri pengurai aerobik di instalasi IPAL akibat konsentrasi fosfat tinggi',
      'Formulasi KCA dengan surfaktan terurai hayati (biodegradable >90%)'
    ],
    fullContent: `Berdasarkan Permen LHK dan regulasi dinas lingkungan hidup daerah, air buangan rumah sakit dan sentra pencucian komersial diuji secara berkala untuk parameter BOD, COD, TSS, dan kadar Fosfat Total maksimum yang sangat ketat (<2 mg/L).

Pelanggaran terhadap baku mutu ini dapat berakibat pada pencabutan izin operasional, kegagalan akreditasi KARS rumah sakit, hingga sanksi pidana lingkungan.

Mengapa Deterjen Ber-Fosfat Sangat Berbahaya Bagi Biofilter IPAL?

1. Pembunuh Mikroba Pengurai Alami
Sistem pengolahan air limbah modern mengandalkan kolam aerasi biologis berisi miliaran mikroorganisme pengurai (activated sludge). Konsentrasi fosfat anorganik berlebih meracuni mikrobioma anaerobik/aerobik, menyebabkan sistem biofilter macet total dan air limbah berbau busuk menyengat.

2. Ledakan Eutrofikasi di Badan Air Penerima
Fosfat adalah nutrien pembatas pertumbuhan alga. Ketika air limbah laundry mengandung STPP dibuang ke sungai atau danau, terjadi fenomena algal bloom yang menutupi permukaan air, menghabiskan oksigen terlarut (Dissolved Oxygen - DO), dan mematikan ekosistem perairan.

Komitmen Mutu Ramah Lingkungan PT Kediri Chemical Abadi:
Seluruh lini produk PT Kediri Chemical Abadi 100% Bebas Fosfat / STPP-Free:
- Menggantikan fosfat dengan builder kompleks ramah hayati berbasis sitrat dan polikarboksilat biodegradable.
- Lolos pengujian degradasi hayati standar internasional OECD 301D dengan tingkat dekomposisi biologis melampaui 90% dalam 28 hari.
- Menjamin hasil uji laboratorium IPAL mitra rumah sakit dan industri selalu berada di bawah ambang batas baku mutu resmi pemerintah.`
  }
]
