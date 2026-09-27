#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATOR BUKU PELAJARAN / TEXTBOOK PANDUAN LENGKAP OPERASIONAL & JOBDESK TIM
PT KEDIRI CHEMICAL ABADI — STANDAR MUTU ISO 9001:2015

Penanggung Jawab / Author : Yerikho Arfensias Effendi
Perusahaan                : PT Kediri Chemical Abadi
Direktur Utama            : Yan Effendi
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "KCA DOKUMEN", "09_DOKUMEN_DIREKSI_DAN_MANAJEMEN_PUNCAK"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

COLOR_BLACK = RGBColor(0, 0, 0)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}>\n'
                          f'<w:top w:val="{kwargs.get("top", "single")}" w:sz="{kwargs.get("top_sz", "4")}" w:space="0" w:color="{kwargs.get("top_color", "000000")}"/>\n'
                          f'<w:left w:val="{kwargs.get("left", "single")}" w:sz="{kwargs.get("left_sz", "4")}" w:space="0" w:color="{kwargs.get("left_color", "000000")}"/>\n'
                          f'<w:bottom w:val="{kwargs.get("bottom", "single")}" w:sz="{kwargs.get("bottom_sz", "4")}" w:space="0" w:color="{kwargs.get("bottom_color", "000000")}"/>\n'
                          f'<w:right w:val="{kwargs.get("right", "single")}" w:sz="{kwargs.get("right_sz", "4")}" w:space="0" w:color="{kwargs.get("right_color", "000000")}"/>\n'
                          f'</w:tcBorders>')
    tcPr.append(tcBorders)

def sanitize_metadata(doc):
    core_props = doc.core_properties
    core_props.author = "Yerikho Arfensias Effendi"
    core_props.last_modified_by = "Yerikho Arfensias Effendi"
    core_props.comments = "Buku Pelajaran & Panduan Lengkap Operasional, Jobdesk, dan Flowchart PT Kediri Chemical Abadi Standar ISO 9001:2015"
    core_props.category = "Buku Panduan Operasional Perusahaan"
    core_props.keywords = "PT Kediri Chemical Abadi, Buku Pelajaran, Textbook, Jobdesk, SOP, Flowchart, Yan Effendi, Yerikho, Farhan, Fajar"

def setup_page_layout(doc):
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

def add_header_kop(doc, doc_title, doc_number):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    cell_left = tbl.cell(0, 0)
    cell_right = tbl.cell(0, 1)
    cell_left.width = Inches(4.5)
    cell_right.width = Inches(2.3)

    p_left = cell_left.paragraphs[0]
    p_left.paragraph_format.space_after = Pt(2)
    p_left.paragraph_format.line_spacing = 1.15
    run1 = p_left.add_run("PT KEDIRI CHEMICAL ABADI\n")
    run1.font.name = 'Times New Roman'
    run1.font.size = Pt(12)
    run1.font.bold = True
    run1.font.color.rgb = COLOR_BLACK

    run2 = p_left.add_run("Pusat Riset Formulasi & Manufaktur Kimia Pembersih Industri\nJl. Merbabu No. 12, Mojoroto, Kota Kediri, Jawa Timur | Telp: 0858-1230-7629")
    run2.font.name = 'Times New Roman'
    run2.font.size = Pt(8.5)
    run2.font.color.rgb = COLOR_BLACK

    p_right = cell_right.paragraphs[0]
    p_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_right.paragraph_format.space_after = Pt(2)
    p_right.paragraph_format.line_spacing = 1.15
    run3 = p_right.add_run(f"STANDAR ISO 9001:2015\nNo: {doc_number}\nEdisi: September 2026")
    run3.font.name = 'Times New Roman'
    run3.font.size = Pt(8)
    run3.font.bold = True
    run3.font.color.rgb = COLOR_BLACK

    for c in (cell_left, cell_right):
        set_cell_border(c, top="none", left="none", right="none", bottom="single", bottom_sz="12", bottom_color="000000")
        set_cell_margins(c, top=40, bottom=80, left=40, right=40)

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_after = Pt(6)

def add_par(doc, text="", bold=False, italic=False, size=10, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=6):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(space_after)
    if text:
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = COLOR_BLACK
    return p

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = COLOR_BLACK
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_BLACK
    return p

def add_flowchart_box(doc, lines):
    """Menambahkan diagram flowchart berbasis monospace/Times New Roman terstruktur rapi"""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_border(cell, top="single", bottom="single", left="single", right="single", top_sz="6", bottom_sz="6")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    p = cell.paragraphs[0]
    p.paragraph_format.line_spacing = 1.05
    p.paragraph_format.space_after = Pt(2)
    for line in lines:
        run = p.add_run(line + "\n")
        run.font.name = 'Courier New'
        run.font.size = Pt(8.5)
        run.font.color.rgb = COLOR_BLACK
    
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(6)

def build_textbook():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "BUKU PANDUAN UTAMA", "TEX-01/MGT-KCA/2026")

    add_par(doc, "BUKU PELAJARAN & MANUAL UTAMA OPERASIONAL TIM", bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_par(doc, "PANDUAN LENGKAP STRUKTUR TATA KELOLA, URAIAN JABATAN, RUANG LINGKUP KERJA,", bold=True, size=10.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_par(doc, "DAN STANDAR OPERASIONAL PROSEDUR (SOP) ALUR EKSEKUSI BISNIS 2026", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_par(doc, "Edisi Pengesahan: 6 September 2026 | PT Kediri Chemical Abadi", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    # -------------------------------------------------------------------------
    # MODUL 1: FONDASI, FILOSOFI & ARSITEKTUR HIERARKI
    # -------------------------------------------------------------------------
    add_heading_1(doc, "MODUL 1: FONDASI, FILOSOFI & ARSITEKTUR HIERARKI PERUSAHAAN")
    add_par(doc, "1.1 Filosofi Tata Kelola 'Two-Tier Governance & Single Reporting Bridge'", bold=True, size=10.5, space_after=2)
    add_par(doc, "Sebuah perusahaan manufaktur dan komersial yang ingin tumbuh cepat (scale-up) membutuhkan struktur organisasi yang memiliki garis komando yang sangat tegas. Tanpa garis komando yang jelas, tim akan mengalami kebingungan instruksi, saling lempar tanggung jawab, dan pimpinan puncak akan terbebani oleh urusan-urusan kecil yang tidak strategis.")
    add_par(doc, "PT Kediri Chemical Abadi mengadopsi model Two-Tier Governance, yaitu pemisahan tegas antara peran Pengawas & Pengambil Keputusan Tertinggi (Direktur Utama / Owner) dengan peran Nakhoda Eksekusi Operasional Harian (General Manager).")

    add_par(doc, "Visualisasi Diagram Pohon Hierarki & Garis Pelaporan Resmi:", bold=True, space_after=4)
    chart_lines = [
        "+-------------------------------------------------------------------------------+",
        "|                 DIREKTUR UTAMA / OWNER (YAN EFFENDI)                          |",
        "|                 [ Peran: Supreme Reviewer & Final Approver ]                  |",
        "|  - Menerima laporan komprehensif HANYA DARI General Manager (Satu Pintu)      |",
        "|  - Hak Keputusan Mutlak: APPROVE or NOT                                       |",
        "|  - Supervisi Mutu Formulasi Kimia Lab & Kepatuhan Legalitas Pabrik            |",
        "+---------------------------------------+---------------------------------------+",
        "                                        |",
        "                        (Jalur Laporan & Otorisasi 1 Pintu)",
        "                                        v",
        "+---------------------------------------+---------------------------------------+",
        "|              GENERAL MANAGER (YERIKHO ARFENSIAS EFFENDI)                      |",
        "|              [ Peran: Operations & Executive Lead / Nakhoda ]                 |",
        "|  - Menyusun Proposal Proyek, Analisis HPP, Anggaran & Target Omzet            |",
        "|  - Memimpin Komando Eksekusi Harian setelah Proyek Mendapat Status APPROVED   |",
        "|  - Mengontrol Arus Kas (Cash Flow) & Otorisasi Pengeluaran Kas Belanja        |",
        "|  - Memberikan Approval Akhir Desain Cetak & Kemitraan Strategis               |",
        "+-------------------+---------------------------------------+-------------------+",
        "                    |                                       |",
        "       (Instruksi Operasional Harian)          (Instruksi Desain & Aset Visual)",
        "                    v                                       v",
        "+-------------------+-------------------+   +-------------------+-------------------+",
        "|  BUSINESS OPERATIONS COORDINATOR      |   |       HEAD OF CREATIVE & DESIGN       |",
        "|             (FARHAN)                  |   |                (FAJAR)                |",
        "|  - Melapor 100% kepada GM             |   |  - Melapor 100% kepada GM             |",
        "|  - Pengadaan Botol, Stiker & Kardus   |   |  - Desain Kemasan Botol Siap Cetak    |",
        "|  - Operasional Filling & Packing      |   |  - Desain Banner Web & Katalog        |",
        "|  - Toko Marketplace (Shopee/Tokopedia)|   |  - 9 Feed Instagram & Story Promo     |",
        "|  - Logistik Ekspedisi & Stok Gudang   |   |  - Serah Terima via Project Ledger    |",
        "+---------------------------------------+   +---------------------------------------+"
    ]
    add_flowchart_box(doc, chart_lines)

    add_par(doc, "1.2 Dua Hukum Baku Komunikasi Organisasi:", bold=True, size=10, space_after=2)
    add_par(doc, "Hukum 1: Farhan dan Fajar hanya memiliki SATU ATASAN LANGSUNG, yaitu General Manager (Yerikho). Farhan dan Fajar TIDAK DIPERKENANKAN meminta persetujuan teknis atau melapor langsung kepada Direktur Utama. Seluruh koordinasi wajib melalui General Manager.")
    add_par(doc, "Hukum 2: Direktur Utama / Owner dilindungi dari rutinitas teknis (tidak mengurusi chat pembeli, packing kardus, atau revisi postingan IG). Beliau fokus pada pengawasan mutu formula laboratorium dan evaluasi kelayakan proyek dari General Manager.")

    # -------------------------------------------------------------------------
    # MODUL 2: BUKU INDUK JOBDESK & RUANG LINGKUP KERJA
    # -------------------------------------------------------------------------
    add_heading_1(doc, "MODUL 2: BUKU INDUK URAIAN JABATAN (JOB DESCRIPTIONS) & RUANG LINGKUP")

    # JABATAN 1: DIRUT
    add_heading_2(doc, "2.1 DIREKTUR UTAMA / OWNER (YAN EFFENDI)")
    add_par(doc, "A. Profil & Maksud Jabatan:", bold=True, space_after=2)
    add_par(doc, "Menjadi pengawas korporat tertinggi dan gerbang persetujuan mutlak (Gatekeeper) bagi setiap rencana ekspansi usaha, sekaligus bertindak sebagai penasihat senior dalam formulasi kimia di pabrik.")

    add_par(doc, "B. Ruang Lingkup Tanggung Jawab (Scope of Work):", bold=True, space_after=2)
    add_par(doc, "1. Executive Review: Menerima presentasi proposal proyek baru dari General Manager, mengkaji kelayakan teknis dan potensi keuntungan/risiko, lalu memberikan keputusan: APPROVE atau NOT.\n"
                 "2. Pengawasan Mutu Formulasi: Meneliti dan meracik formula sabun mandi cair, shampoo, dan body care di lab pabrik Mojoroto (menjaga busa melimpah, aroma mewah, dan pH netral 5.5 - 6.5).\n"
                 "3. Pengawasan Reaktor Manufaktur: Memantau kebersihan dan pengoperasian tangki reaktor Stainless Steel 316L pada saat produksi massal.\n"
                 "4. Pengawasan Kepatuhan Regulasi: Memastikan formula memenuhi standar uji izin edar PKRT / BPOM serta standar ISO 9001:2015.")

    add_par(doc, "C. Batas Wewenang (Authority Boundary):", bold=True, space_after=2)
    add_par(doc, "• Wewenang Penuh: Memberikan status APPROVE/NOT pada proposal proyek, menentukan formula kimia, dan mengevaluasi laba dividen.\n"
                 "• Larangan Wewenang: Tidak menangani operasional harian teknis seperti pengadaan botol, packing pesanan, atau pengelolaan akun marketplace.")

    # JABATAN 2: GM
    add_heading_2(doc, "2.2 GENERAL MANAGER (YERIKHO ARFENSIAS EFFENDI)")
    add_par(doc, "A. Profil & Maksud Jabatan:", bold=True, space_after=2)
    add_par(doc, "Nakhoda tertinggi jalannya bisnis harian, pengontrol ketat arus kas, perancang strategi komersial, dan pemimpin operasional bagi Farhan dan Fajar.")

    add_par(doc, "B. Ruang Lingkup Tanggung Jawab (Scope of Work):", bold=True, space_after=2)
    add_par(doc, "1. Penyusunan Proposal Proyek ke Owner: Menyusun rencana bisnis lini produk baru (varian aroma, kalkulasi HPP, harga jual pasar, modal kemasan, dan proyeksi omzet) untuk diajukan ke Direktur Utama.\n"
                 "2. Pengendalian Finansial & Kas: Menghitung HPP, mengontrol pengeluaran kas belanja harian, dan memastikan pencairan hak gaji Farhan dan proyek Fajar terlaksana saat arus kas stabil.\n"
                 "3. Otorisasi Desain & Pengadaan: Memeriksa dan memberikan persetujuan akhir (ACC) atas desain stiker Fajar sebelum dicetak, serta menyetujui anggaran belanja botol dari Farhan.\n"
                 "4. Delegasi & Supervisi Tim: Mengarahkan tugas harian Farhan dan Fajar, memeriksa ketepatan waktu, dan menyelesaikan hambatan operasional lapangan.\n"
                 "5. Penjualan Skala Besar (B2B): Menjalin kemitraan maklon industri, pasokan hotel, dan jaringan reseller kampus.")

    add_par(doc, "C. Batas Wewenang (Authority Boundary):", bold=True, space_after=2)
    add_par(doc, "• Wewenang Penuh: Otorisasi seluruh kas belanja usaha, penetapan harga jual produk, persetujuan naik cetak desain, dan penandatanganan MOU tim.\n"
                 "• Kewajiban: Wajib mendapatkan status APPROVE dari Direktur Utama sebelum mengeksekusi proyek baru yang menggunakan alokasi modal besar.")

    # JABATAN 3: FARHAN
    add_heading_2(doc, "2.3 BUSINESS OPERATIONS COORDINATOR (FARHAN)")
    add_par(doc, "A. Profil & Maksud Jabatan:", bold=True, space_after=2)
    add_par(doc, "Tangan kanan General Manager di lapangan yang mengendalikan rantai pasok fisik dari pengadaan botol, stiker label, operasional pengisian sabun, administrasi toko marketplace, hingga pengiriman barang ke kurir.")

    add_par(doc, "B. Ruang Lingkup Tanggung Jawab (Scope of Work):", bold=True, space_after=2)
    add_par(doc, "1. Divisi Pengadaan (Procurement):\n"
                 "   - Mensurvei dan membeli sampel botol 250ml dan 500ml dengan tutup pump/flip-top yang berkualitas dan tidak mudah pecah.\n"
                 "   - Mengukur dimensi stiker botol secara fisik (tinggi mm x keliling mm) dan menyerahkan data akurat tersebut kepada Fajar.\n"
                 "   - Membawa file cetak Fajar ke percetakan stiker label vinyl tahan air, memeriksa hasil cetak sebelum dibawa pulang.\n"
                 "   - Mengadakan perlengkapan packing: kardus karton pelindung, bubble wrap tebal, lakban fragil, dan plastik polymailer.\n\n"
                 "2. Divisi Pengisian & Kerapian Botol (Filling & Packaging):\n"
                 "   - Membantu proses pengisian cairan sabun mandi cair / shampoo dari jerigen/tangki ke dalam botol kemasan.\n"
                 "   - Memasang stiker label pada botol secara presisi, simetris, tegak lurus, dan bersih tanpa kerutan atau gelembung udara.\n"
                 "   - Melakukan pengecekan mutu fisik (Quality Control): memastikan leher botol tersegel rapat dan tidak ada kebocoran cairan.\n\n"
                 "3. Divisi Marketplace & Layanan Pelanggan (Admin Toko):\n"
                 "   - Membuka dan mengelola akun toko resmi PT Kediri Chemical Abadi di Shopee, Tokopedia, dan TikTok Shop.\n"
                 "   - Mengunggah foto produk dari Fajar, menyusun judul produk ramah pencarian SEO, dan menulis deskripsi spesifikasi wangi & netto.\n"
                 "   - Memantau notifikasi pesanan masuk secara berkala (Pukul 09.00, 13.00, dan 17.00 WIB).\n"
                 "   - Membalas pesan chat calon pembeli secara sopan, ramah, dan cepat.\n\n"
                 "4. Divisi Logistik & Pengiriman (Fulfillment):\n"
                 "   - Membungkus botol pesanan dengan double bubble wrap tebal dan memasukkannya ke dalam kardus packing kardus pelindung.\n"
                 "   - Mencetak dan menempelkan resi pengiriman otomatis dari marketplace.\n"
                 "   - Menyerahkan paket ke gerai kurir ekspedisi (J&T, SiCepat, Shopee Xpress, JNE) sebelum batas cut-off sore.\n\n"
                 "5. Divisi Pencatatan & Pelaporan Harian:\n"
                 "   - Menghitung sisa stok botol kosong, stiker cadangan, dan botol siap jual di rak gudang setiap sore.\n"
                 "   - Melaporkan rekapitulasi harian kepada General Manager: jumlah paket terkirim, nomor resi, dan kendala lapangan.")

    add_par(doc, "C. Jadwal Rutinitas Kerja Farhan (Daily Working Rhythm):", bold=True, space_after=2)
    add_par(doc, "• 08.30 – 09.30 WIB: Buka dashboard Shopee/Tokopedia, rekap seluruh orderan masuk semalam, cetak label resi pengiriman.\n"
                 "• 09.30 – 12.00 WIB: Ambil produk dari rak gudang, periksa segel tutup botol, lakukan packing bubble wrap & kardus secara rapi.\n"
                 "• 12.00 – 13.00 WIB: Istirahat siang.\n"
                 "• 13.00 – 15.00 WIB: Koordinasi vendor botol/percetakan stiker, pasang stiker untuk stok baru, atau isi botol sabun.\n"
                 "• 15.00 – 16.30 WIB: Serah terima paket pesanan ke gerai kurir ekspedisi.\n"
                 "• 16.30 – 17.00 WIB: Hitung sisa stok fisik dan kirim laporan harian ke WhatsApp General Manager.")

    add_par(doc, "D. Batas Wewenang & Larangan Mutlak Farhan:", bold=True, space_after=2)
    add_par(doc, "• DILARANG mengubah harga jual atau memberikan diskon di marketplace tanpa izin tertulis dari General Manager.\n"
                 "• DILARANG mengeluarkan uang kas untuk belanja botol/stiker tanpa persetujuan anggaran dari General Manager.\n"
                 "• DILARANG mengirim pesanan dengan kondisi botol rembes atau packing tipis tanpa bubble wrap.")

    # JABATAN 4: FAJAR
    add_heading_2(doc, "2.4 HEAD OF CREATIVE & DESIGN (FAJAR)")
    add_par(doc, "A. Profil & Maksud Jabatan:", bold=True, space_after=2)
    add_par(doc, "Pemimpin identitas visual dan estetika merek perusahaan yang bertanggung jawab mengubah formulasi kimia pabrik menjadi produk yang terlihat mewah, harum, estetik, dan membuat anak muda/wanita langsung tertarik membeli.")

    add_par(doc, "B. Ruang Lingkup Tanggung Jawab (Scope of Work):", bold=True, space_after=2)
    add_par(doc, "1. Desain Kemasan Produk Siap Cetak (Packaging Design):\n"
                 "   - Merancang konsep visual label stiker botol sabun mandi, shampoo, dan body care baru bergaya modern Gen-Z (warna bersih, tipografi tegas, berkelas).\n"
                 "   - Menggunakan ukuran dimensi presisi yang diberikan oleh Farhan (misal: label 6 x 12 cm).\n"
                 "   - Menyusun tata letak label dengan elemen wajib: Nama Merek, Nama Varian Wangi (misal: Vanilla Bloom), Keunggulan Formula (100% Non-Phosphate, Ph-Balanced), Netto (ml), Komposisi / Ingredients, Cara Pakai, Logo Resmi KCA, dan Info Produsen.\n"
                 "   - Menyiapkan master file siap cetak (Print-Ready File): Format PDF Vektor / Adobe Illustrator, Color Mode CMYK, Resolusi 300 DPI, dan disertai batas lebihan potong (Bleed 2-3 mm & Crop Marks).\n\n"
                 "2. Desain Aset Digital Website Resmi:\n"
                 "   - Merancang banner visual pahlawan (Hero Banner) produk baru untuk website kca.co.id.\n"
                 "   - Mendesain mock-up visual botol kemasan 3D yang bersih dan profesional untuk katalog produk online.\n\n"
                 "3. Desain Konten Media Sosial (Instagram & Facebook):\n"
                 "   - Merancang paket 9 feed Instagram pertama bertema estetik untuk peluncuran lini merek baru.\n"
                 "   - Membuat template visual Instagram Story (Promo Peluncuran, Testimoni Pengguna, dan Edukasi Keunggulan Sabun Non-Fosfat).\n"
                 "   - Mendesain foto profil resmi, banner Facebook, dan highlight cover.\n\n"
                 "4. Desain Visual Toko Marketplace:\n"
                 "   - Mendesain foto utama produk di Shopee/Tokopedia berukuran 1080 x 1080 px dengan bingkai promosi yang eye-catching.\n"
                 "   - Mendesain banner dekorasi toko online agar toko terlihat profesional dan bonafide.\n\n"
                 "5. Pencatatan Kontribusi Proyek (Project Ledger):\n"
                 "   - Mendokumentasikan dan menyerahkan master file akhir kepada General Manager.\n"
                 "   - Mengisi Formulir Project Ledger bersama General Manager sebagai dasar hak pencairan kompensasi proyek.")

    add_par(doc, "C. Spesifikasi Teknis Cetak Standar Percetakan Fajar:", bold=True, space_after=2)
    add_par(doc, "• Color Space: CMYK (Cyan, Magenta, Yellow, Key/Black) — DILARANG mengirim file RGB ke percetakan agar warna tidak kusam saat dicetak.\n"
                 "• Resolution: Minimal 300 DPI (Dots Per Inch) agar teks kecil komposisi terbaca tajam dan tidak pecah.\n"
                 "• Safe Zone & Bleed: Jarak teks penting dari tepi potong minimal 3 mm; lebihan potong (bleed) 2 mm keliling.")

    add_par(doc, "D. Batas Wewenang & Larangan Mutlak Fajar:", bold=True, space_after=2)
    add_par(doc, "• DILARANG mengirimkan file desain langsung ke vendor percetakan sebelum disetujui secara tertulis (ACC) oleh General Manager.\n"
                 "• DILARANG mengubah ukuran label stiker tanpa koordinasi ukuran fisik botol dengan Farhan.\n"
                 "• DILARANG mempublikasikan materi promosi di media sosial tanpa review preview dari General Manager.")

    # -------------------------------------------------------------------------
    # MODUL 3: FLOWCHART & SOP ALUR OPERASIONAL
    # -------------------------------------------------------------------------
    add_heading_1(doc, "MODUL 3: FLOWCHART & STANDAR OPERASIONAL PROSEDUR (SOP) LENGKAP")

    add_heading_2(doc, "3.1 FLOWCHART GERBANG KEPUTUSAN PROYEK (SUPREME APPROVAL GATE)")
    flow_gate = [
        "                      [ GENERAL MANAGER (YERIKHO) ]",
        "                                    |",
        "            Menyusun Proposal Proyek Lini Produk Baru",
        "       (Konsep Sabun Gen-Z, Riset Pasar, Kalkulasi HPP, & Target)",
        "                                    |",
        "                                    v",
        "         +-----------------------------------------------------+",
        "         |      PENGAJUAN LAPORAN KE DIREKTUR UTAMA            |",
        "         |               (YAN EFFENDI)                         |",
        "         +--------------------------+--------------------------+",
        "                                    |",
        "                        (Kajian Kelayakan Bisnis)",
        "                                    |",
        "                                    v",
        "                           /-----------------\\",
        "                          /                   \\",
        "                         <  KEPUTUSAN DIRUT:   >",
        "                          \\  APPROVE or NOT?  /",
        "                           \\-----------------/",
        "                                   /     \\",
        "                     [ STATUS: NOT ]     [ STATUS: APPROVE ]",
        "                           /                 \\",
        "                          v                   v",
        "         +-------------------------+   +-------------------------------+",
        "         | PROYEK DITOLAK / REVISI |   | PROYEK RESMI BERJALAN !       |",
        "         |                         |   | (Lampu Hijau Eksekusi Modal)  |",
        "         | - GM meninjau ulang HPP |   +---------------+---------------+",
        "         | - Perbaiki proposal     |                   |",
        "         +-------------------------+                   v",
        "                                       [ GM MEMBAGI TUGAS KE TIM ]",
        "                                       Farhan: Eksekusi Botol & Cetak",
        "                                       Fajar : Eksekusi Desain Label"
    ]
    add_flowchart_box(doc, flow_gate)

    add_heading_2(doc, "3.2 FLOWCHART PELUNCURAN PRODUK BARU DARI HULU KE HILIR (END-TO-END)")
    flow_product = [
        "[ TAHAP 1: KONSEP ]    -> Yerikho menetapkan konsep produk Sabun Mandi Gen-Z 250ml.",
        "                               |",
        "                               v",
        "[ TAHAP 2: PROPOSAL ]  -> Yerikho mengajukan proposal ke Yan Effendi -> ACC APPROVE.",
        "                               |",
        "                               v",
        "[ TAHAP 3: FORMULA ]   -> Yan Effendi meracik formula sabun wangi & lembut di lab pabrik.",
        "                               |",
        "                               v",
        "[ TAHAP 4: BOTOL ]     -> Farhan beli sampel botol 250ml -> Ukur stiker 6x12 cm -> Beri ke Fajar.",
        "                               |",
        "                               v",
        "[ TAHAP 5: DESAIN ]    -> Fajar desain label stiker 6x12 cm CMYK 300 DPI -> Yerikho ACC.",
        "                               |",
        "                               v",
        "[ TAHAP 6: PRODUKSI ]  -> Farhan cetak stiker -> Isi sabun ke botol -> Tempel stiker rapi.",
        "                               |",
        "                               v",
        "[ TAHAP 7: MARKETING ] -> Fajar bikin materi Feed IG & foto etalase Shopee 1080x1080 px.",
        "                               |",
        "                               v",
        "[ TAHAP 8: PENJUALAN ] -> Farhan upload ke Shopee/Tokopedia -> Balas chat -> Bungkus paket -> Kirim.",
        "                               |",
        "                               v",
        "[ TAHAP 9: KEUANGAN ]  -> Yerikho rekap kas masuk -> Cairkan hak gaji Farhan & proyek Fajar!"
    ]
    add_flowchart_box(doc, flow_product)

    add_heading_2(doc, "3.3 FLOWCHART ALUR PEMENUHAN PESANAN HARIAN (ORDER FULFILLMENT)")
    flow_order = [
        "   09.00 WIB   -> Farhan buka Shopee/Tokopedia & WA -> Cetak seluruh resi pesanan masuk.",
        "        |",
        "        v",
        " 10.00-12.00   -> Ambil botol di rak gudang -> Cek fisik tutup rapat & tidak bocor (QC).",
        "        |",
        "        v",
        " 13.00-14.30   -> Bungkus botol dengan double bubble wrap -> Masukkan kardus -> Lakban fragil.",
        "        |",
        "        v",
        "   15.00 WIB   -> Serahkan paket ke gerai kurir ekspedisi (J&T/SiCepat/Shopee Xpress).",
        "        |",
        "        v",
        "   17.00 WIB   -> Rekap sisa stok fisik & kirim laporan harian ke WhatsApp General Manager."
    ]
    add_flowchart_box(doc, flow_order)

    # -------------------------------------------------------------------------
    # MODUL 4: STUDI KASUS & PEMECAHAN MASALAH
    # -------------------------------------------------------------------------
    add_heading_1(doc, "MODUL 4: STUDI KASUS OPERASIONAL & PANDUAN PEMECAHAN MASALAH")
    add_par(doc, "Modul ini wajib dipelajari oleh seluruh tim sebagai panduan tindakan cepat ketika menghadapi masalah di lapangan:")

    cases = [
        ("Kasus 1: Botol Kemasan Bocor Saat Diterima Pembeli di Luar Kota",
         "Penyebab: Tutup botol kurang kencang atau perlindungan bubble wrap terlalu tipis.\n"
         "Tindakan Cepat Farhan: (1) Minta maaf dengan sopan di chat Shopee, (2) Minta foto bukti unboxing, (3) Lapor ke Yerikho untuk otorisasi kirim barang pengganti (retur gratis), (4) Evaluasi teknik packing dengan menambahkan segel isolasi di leher tutup botol."),

        ("Kasus 2: Hasil Cetak Stiker Label Miring atau Kekecilan dari Botol",
         "Penyebab: Kesalahan pengukuran manual atau tidak adanya garis bleed potong.\n"
         "Tindakan Cepat Farhan & Fajar: (1) Jangan pasang stiker yang cacat ke botol jualan, (2) Farhan membawa botol fisik langsung ke tempat Fajar, (3) Fajar mencocokkan master artboard dengan botol fisik, (4) Cetak sampel 1 lembar dulu untuk dites sebelum mencetak ratusan lembar."),

        ("Kasus 3: Pesanan Toko Melonjak Drastis 5x Lipat Saat Event Promo",
         "Penyebab: Kampanye media sosial Fajar berhasil menarik minat pasar secara masif.\n"
         "Tindakan Cepat Tim: (1) Farhan segera memeriksa sisa stok botol dan sabun, lapor ke Yerikho, (2) Jika stok menipis, Yerikho meminta Pak Yan untuk menambah jadwal produksi pengadukan sabun di pabrik, (3) Farhan fokus penuh pada packing dengan sistem borongan rapi.")
    ]

    for ctitle, cdesc in cases:
        add_par(doc, ctitle, bold=True, size=10, space_after=2)
        add_par(doc, cdesc, size=9.5, space_after=8)

    # -------------------------------------------------------------------------
    # MODUL 5: MATRIKS WEWENANG & PENGESAHAN
    # -------------------------------------------------------------------------
    add_heading_1(doc, "MODUL 5: MATRIKS WEWENANG (AUTHORITY MATRIX) & PENGESAHAN RESMI")

    headers = ["Jenis Keputusan Bisnis", "Pelaksana", "Reviewer / Approver", "Dampak Jika 'NOT'"]
    widths = [Inches(2.5), Inches(1.3), Inches(1.6), Inches(1.8)]
    tbl_auth = doc.add_table(rows=7, cols=4)
    tbl_auth.alignment = WD_TABLE_ALIGNMENT.CENTER

    auth_data = [
        ("Jenis Keputusan Bisnis", "Pelaksana", "Reviewer / Approver", "Dampak Jika 'NOT'"),
        ("Peluncuran Proyek Baru & Modal", "Yerikho (GM)", "Yan Effendi (Dirut)", "Proyek tidak boleh jalan"),
        ("Perubahan Formulasi Kimia Sabun", "Yan Effendi (Dirut)", "Yan Effendi (Dirut)", "Formula baku dipertahankan"),
        ("Persetujuan Desain Label Naik Cetak", "Fajar (Creative)", "Yerikho (GM)", "Desain wajib direvisi Fajar"),
        ("Otorisasi Belanja Botol, Stiker & Kardus", "Farhan (Ops)", "Yerikho (GM)", "Dana kas belanja tidak cair"),
        ("Penetapan Harga Jual & Promo Diskon", "Yerikho (GM)", "Yerikho (GM)", "Harga standar berlaku"),
        ("Pencairan Hak Gaji & Project Ledger", "Yerikho (GM)", "Yerikho & Yan Effendi", "Menunggu arus kas siap")
    ]

    for r_idx, row in enumerate(auth_data):
        for c_idx, val in enumerate(row):
            cell = tbl_auth.rows[r_idx].cells[c_idx]
            cell.width = widths[c_idx]
            p = cell.paragraphs[0]
            if r_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(val)
                run.bold = True
                run.font.size = Pt(8.5)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                run = p.add_run(val)
                run.font.size = Pt(8)
            run.font.name = 'Times New Roman'
            run.font.color.rgb = COLOR_BLACK
            set_cell_margins(cell, top=60, bottom=60, left=40, right=40)
            set_cell_border(cell, top="single", bottom="single", left="single", right="single", top_sz="4", bottom_sz="4")

    add_par(doc, "", space_after=14)

    # Lembar Pengesahan
    add_par(doc, "LEMBAR PENGESAHAN BUKU PANDUAN UTAMA", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_par(doc, "Buku Pelajaran & Manual Operasional ini disahkan secara resmi dan mengikat seluruh jajaran manajemen PT Kediri Chemical Abadi sejak tanggal 6 September 2026.", size=9.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    tbl_ttd = doc.add_table(rows=2, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c3, c4 = tbl_ttd.cell(1, 0), tbl_ttd.cell(1, 1)

    for c in (c1, c2, c3, c4):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")
        c.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.add_run("Disetujui Oleh,\nDirektur Utama / Owner\n(Supreme Reviewer & Approver)\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YAN EFFENDI").bold = True

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.add_run("Ditetapkan di Kota Kediri, 6 September 2026\nGeneral Manager\n(Operations & Executive Lead)\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("YERIKHO ARFENSIAS EFFENDI").bold = True

    p3 = c3.paragraphs[0]
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.add_run("\n\nPihak Yang Menjalankan,\nBusiness Operations Coordinator\n\n\n\n").font.color.rgb = COLOR_BLACK
    p3.add_run("FARHAN").bold = True

    p4 = c4.paragraphs[0]
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.add_run("\n\nPihak Yang Menjalankan,\nHead of Creative & Design\n\n\n\n").font.color.rgb = COLOR_BLACK
    p4.add_run("FAJAR").bold = True

    filename = os.path.join(OUTPUT_DIR, "BUKU_PANDUAN_OPERASIONAL_DAN_JOBDESK_KCA_2026.docx")
    doc.save(filename)
    print(f"[OK] Textbook & Manual saved: {filename}")

if __name__ == "__main__":
    build_textbook()
