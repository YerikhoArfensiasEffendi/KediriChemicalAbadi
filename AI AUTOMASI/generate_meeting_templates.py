#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATOR DOKUMEN TEMPLATE MEETING INTERNAL & MOU TIM
PT KEDIRI CHEMICAL ABADI — STANDAR ISO 9001:2015

Penanggung Jawab / Author : Yerikho Arfensias Effendi
Perusahaan                : PT Kediri Chemical Abadi
Direktur Utama            : Yan Effendi
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "KCA DOKUMEN", "09_DOKUMEN_DIREKSI_DAN_MANAJEMEN_PUNCAK"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

COLOR_BLACK = RGBColor(0, 0, 0) # Mandatory Pure Black (#000000)

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
    core_props.comments = "Dokumen Terkendali Sistem Manajemen Mutu ISO 9001:2015 PT Kediri Chemical Abadi"
    core_props.category = "Dokumen Manajemen Direksi"
    core_props.keywords = "PT Kediri Chemical Abadi, MOU, Jobdesk, Komitmen Manajemen"

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

# -------------------------------------------------------------
# DOKUMEN 1: SURAT KOMITMEN MANAJEMEN TERHADAP EMPLOYEE
# -------------------------------------------------------------
def build_surat_komitmen():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "SURAT KOMITMEN MANAJEMEN", "SKM-01/DIR-KCA/IX/2026")

    add_par(doc, "SURAT KOMITMEN RESMI MANAJEMEN", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_par(doc, "TENTANG KESEJAHTERAAN TIM, KEADILAN KERJA & KELANGSUNGAN KARYAWAN", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_par(doc, "Nomor: 001/SKM/KCA-DIR/IX/2026", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_par(doc, "Kami yang bertanda tangan di bawah ini, atas nama Manajemen PT Kediri Chemical Abadi:")
    p_bio = add_par(doc)
    r1 = p_bio.add_run("1. Yan Effendi\n")
    r1.bold = True
    p_bio.add_run("   Jabatan : Direktur Utama (President Director)\n")
    r2 = p_bio.add_run("2. Yerikho Arfensias Effendi\n")
    r2.bold = True
    p_bio.add_run("   Jabatan : General Manager (Director of Operations & Finance)\n")
    p_bio.add_run("   Alamat  : Jl. Merbabu No. 12, Mojoroto, Kota Kediri, Jawa Timur\n")

    add_par(doc, "Dengan penuh integritas, kesadaran profesional, dan tanggung jawab hukum, menyatakan KOMITMEN MUTLAK kepada seluruh rekan kerja dan anggota tim inti perusahaan sebagai berikut:", space_after=8)

    points = [
        ("1. Prinsip Keadilan & Transparansi Nyata",
         "Manajemen menjunjung tinggi prinsip bahwa perusahaan tidak akan pernah mengeksploitasi atau memanfaatkan tenaga kerja secara sepihak. Segala upaya, waktu, pemikiran, dan keahlian yang dicurahkan oleh rekan-rekan tim diakui secara sah sebagai kontribusi berharga bagi kemajuan PT Kediri Chemical Abadi."),
        
        ("2. Perlindungan dan Pengakuan Hak Kerja",
         "Setiap pekerjaan operasional yang dijalankan oleh Farhan (Business Operations Coordinator) serta setiap hasil karya desain kemasan dan aset digital yang diselesaikan oleh Fajar (Head of Creative & Design) dicatat secara resmi dalam dokumen perusahaan dan menjadi kewajiban yang mengikat perusahaan untuk dibayarkan kompensasinya."),

        ("3. Prioritas Arus Kas untuk Kesejahteraan Tim",
         "Manajemen menetapkan kebijakan bahwa saat arus kas dari hasil penjualan produk mulai stabil dan mencukupi, pembayaran hak kompensasi dan kesejahteraan tim MENJADI PRIORITAS UTAMA pencairan dana operasional sebelum adanya pembagian keuntungan modal (dividen) kepada pemegang saham."),

        ("4. Pertumbuhan Bersama dan Jenjang Karir Tetap",
         "Perusahaan berkomitmen membina rekan-rekan tim inti untuk tumbuh bersama, memperoleh peningkatan penghasilan yang proporsional dengan peningkatan omzet penjualan, dan menempati posisi kepemimpinan tetap seiring membesarnya skala bisnis PT Kediri Chemical Abadi.")
    ]

    for title, desc in points:
        p_pt = add_par(doc, title, bold=True, size=10, space_after=2)
        add_par(doc, desc, size=9.5, space_after=8)

    add_par(doc, "Surat Komitmen ini dibuat dengan itikad baik tanpa paksaan dari pihak manapun, ditandatangani di atas meterai yang sah, dan berlaku mengikat sejak tanggal ditetapkan.", space_after=14)

    # Tanda Tangan
    tbl_ttd = doc.add_table(rows=1, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c1.width = Inches(3.4)
    c2.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.15
    p1.add_run("Mengetahui & Menyetujui,\nDirektur Utama\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YAN EFFENDI").bold = True

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.15
    p2.add_run("Ditetapkan di Kota Kediri, 6 September 2026\nGeneral Manager\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("YERIKHO ARFENSIAS EFFENDI").bold = True

    for c in (c1, c2):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")

    filename = os.path.join(OUTPUT_DIR, "SKM-01_Surat_Komitmen_Manajemen_terhadap_Tim.docx")
    doc.save(filename)
    print(f"[OK] Saved: {filename}")

# -------------------------------------------------------------
# DOKUMEN 2: MOU FARHAN (OPERATIONS)
# -------------------------------------------------------------
def build_mou_farhan():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "PERJANJIAN KEMITRAAN KERJA", "MOU-01/KCA-OPS/IX/2026")

    add_par(doc, "SURAT PERJANJIAN KEMITRAAN KERJA (MOU)", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_par(doc, "JABATAN: BUSINESS OPERATIONS COORDINATOR", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_par(doc, "Nomor: 002/MOU-OPS/KCA/IX/2026", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_par(doc, "Pada hari ini, Minggu tanggal Enam bulan September tahun Dua Ribu Dua Puluh Enam (06-09-2026), bertempat di Kantor PT Kediri Chemical Abadi, Kota Kediri, dibuat dan ditandatangani perjanjian kerjasama oleh dan antara:", space_after=6)

    p_p1 = add_par(doc)
    p_p1.add_run("1. PT KEDIRI CHEMICAL ABADI, ").bold = True
    p_p1.add_run("berkedudukan di Jl. Merbabu No. 12, Mojoroto, Kota Kediri, dalam hal ini diwakili oleh ")
    p_p1.add_run("Yerikho Arfensias Effendi").bold = True
    p_p1.add_run(" bertindak dalam kapasitas jabatannya selaku ")
    p_p1.add_run("General Manager").bold = True
    p_p1.add_run(", selanjutnya dalam perjanjian ini disebut sebagai ")
    p_p1.add_run("PIHAK PERTAMA.\n").bold = True

    p_p2 = add_par(doc)
    p_p2.add_run("2. FARHAN, ").bold = True
    p_p2.add_run("bertempat tinggal di [ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ], Pemegang Nomor Induk Kependudukan (NIK): [ . . . . . . . . . . . . . . . . . . . . ], bertindak untuk dan atas nama pribadi, selanjutnya dalam perjanjian ini disebut sebagai ")
    p_p2.add_run("PIHAK KEDUA.\n").bold = True

    add_par(doc, "PARA PIHAK secara sadar, tanpa paksaan, dan berlandaskan itikad baik sepakat mengikatkan diri dalam kemitraan kerja dengan syarat dan ketentuan sebagai berikut:", space_after=8)

    pasal_list = [
        ("PASAL 1: PENGANGKATAN DAN RUANG LINGKUP JABATAN",
         "1. PIHAK PERTAMA menunjuk dan mempercayakan kepada PIHAK KEDUA jabatan resmi sebagai Business Operations Coordinator di PT Kediri Chemical Abadi.\n"
         "2. PIHAK KEDUA bertugas mendukung General Manager dalam mengeksekusi operasional harian, administrasi rantai pasok (stok botol, stiker label, karton), pengawasan pesanan masuk, komunikasi vendor, dan pelaporan operasional."),

        ("PASAL 2: SISTEM KERJA & FASE PERINTISAN AWAL",
         "1. PARA PIHAK memahami bahwa pada tahap awal peluncuran lini produk baru, jam kerja diatur secara adaptif dan fleksibel sesuai kebutuhan lapangan.\n"
         "2. PIHAK KEDUA berkomitmen mencurahkan dedikasi terbaik untuk memastikan setiap instruksi kerja dan target operasional yang dirancang PIHAK PERTAMA terlaksana dengan tepat waktu."),

        ("PASAL 3: SKEMA KOMPENSASI BERTAHAP & INSENTIF PENJUALAN",
         "1. Fase Arus Kas Stabil: Ketika arus kas penjualan produk mulai berjalan stabil dan mencukupi, PIHAK KEDUA berhak menerima kompensasi gaji bulanan sebesar Rp 1.500.000,- (Satu Juta Lima Ratus Ribu Rupiah) per bulan.\n"
         "2. Kenaikan Bertahap: Nilai kompensasi bulanan akan disesuaikan meningkat secara berkala seiring dengan pertumbuhan volume penjualan dan penguatan arus kas perusahaan.\n"
         "3. Insentif Skala Besar (Mass Production): Apabila penjualan produk telah memasuki skala produksi massal dan distribusi luas, PIHAK KEDUA berhak mendapatkan tambahan insentif komisi sebesar 1% (Satu Persen) dari total nilai penjualan kotor setiap produk yang terjual."),

        ("PASAL 4: KERAHASIAAN INFORMASI PERUSAHAAN (NDA)",
         "PIHAK KEDUA berkewajiban mutlak menjaga kerahasiaan seluruh informasi operasional, formula produk, daftar kontak vendor, dan strategi bisnis PT Kediri Chemical Abadi, serta dilarang membocorkannya kepada pihak ketiga tanpa izin tertulis dari PIHAK PERTAMA."),

        ("PASAL 5: PENYELESAIAN PERSELISIHAN",
         "Segala bentuk perbedaan pendapat atau perselisihan yang timbul dari pelaksanaan perjanjian ini akan diselesaikan secara musyawarah untuk mufakat dengan semangat kekeluargaan dan kemitraan.")
    ]

    for title, text in pasal_list:
        add_par(doc, title, bold=True, size=10, space_after=2)
        add_par(doc, text, size=9.5, space_after=8)

    add_par(doc, "Demikian Nota Kesepahaman ini dibuat dalam rangkap 2 (dua) bermeterai cukup dan memiliki kekuatan hukum yang sama bagi PARA PIHAK.", space_after=14)

    # Tanda Tangan
    tbl_ttd = doc.add_table(rows=1, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c1.width = Inches(3.4)
    c2.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.15
    p1.add_run("PIHAK PERTAMA\nPT Kediri Chemical Abadi\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YERIKHO ARFENSIAS EFFENDI\n").bold = True
    p1.add_run("General Manager").font.size = Pt(9)

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.15
    p2.add_run("PIHAK KEDUA\nTenaga Kemitraan Kerja\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("FARHAN\n").bold = True
    p2.add_run("Business Operations Coordinator").font.size = Pt(9)

    for c in (c1, c2):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")

    filename = os.path.join(OUTPUT_DIR, "MOU-01_Kemitraan_Kerja_Farhan_Operations.docx")
    doc.save(filename)
    print(f"[OK] Saved: {filename}")

# -------------------------------------------------------------
# DOKUMEN 3: MOU FAJAR (HEAD OF CREATIVE & DESIGN)
# -------------------------------------------------------------
def build_mou_fajar():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "PERJANJIAN KEMITRAAN KREATIF", "MOU-02/KCA-DKV/IX/2026")

    add_par(doc, "SURAT PERJANJIAN KEMITRAAN KREATIF (MOU)", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_par(doc, "JABATAN: HEAD OF CREATIVE & DESIGN", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_par(doc, "Nomor: 003/MOU-DKV/KCA/IX/2026", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_par(doc, "Pada hari ini, Minggu tanggal Enam bulan September tahun Dua Ribu Dua Puluh Enam (06-09-2026), bertempat di Kantor PT Kediri Chemical Abadi, Kota Kediri, dibuat dan ditandatangani perjanjian kerjasama oleh dan antara:", space_after=6)

    p_p1 = add_par(doc)
    p_p1.add_run("1. PT KEDIRI CHEMICAL ABADI, ").bold = True
    p_p1.add_run("berkedudukan di Jl. Merbabu No. 12, Mojoroto, Kota Kediri, dalam hal ini diwakili oleh ")
    p_p1.add_run("Yerikho Arfensias Effendi").bold = True
    p_p1.add_run(" bertindak dalam kapasitas jabatannya selaku ")
    p_p1.add_run("General Manager").bold = True
    p_p1.add_run(", selanjutnya dalam perjanjian ini disebut sebagai ")
    p_p1.add_run("PIHAK PERTAMA.\n").bold = True

    p_p2 = add_par(doc)
    p_p2.add_run("2. FAJAR, ").bold = True
    p_p2.add_run("bertempat tinggal di [ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ], Pemegang Nomor Induk Kependudukan (NIK): [ . . . . . . . . . . . . . . . . . . . . ], bertindak untuk dan atas nama pribadi, selanjutnya dalam perjanjian ini disebut sebagai ")
    p_p2.add_run("PIHAK KEDUA.\n").bold = True

    add_par(doc, "PARA PIHAK secara sadar, tanpa paksaan, dan berlandaskan itikad baik sepakat mengikatkan diri dalam kemitraan kreatif dengan syarat dan ketentuan sebagai berikut:", space_after=8)

    pasal_list = [
        ("PASAL 1: PENGANGKATAN DAN RUANG LINGKUP JABATAN",
         "1. PIHAK PERTAMA menunjuk dan mempercayakan kepada PIHAK KEDUA jabatan resmi sebagai Head of Creative & Design di PT Kediri Chemical Abadi.\n"
         "2. PIHAK KEDUA bertanggung jawab memimpin perancangan identitas visual, desain label botol/kemasan sabun & body care baru, antarmuka visual website Gen-Z, dan materi grafis promosi media sosial."),

        ("PASAL 2: SISTEM KERJA AWAL & PENCATATAN KONTRIBUSI (PROJECT LEDGER)",
         "1. PARA PIHAK memahami bahwa pada tahap awal, komitmen kerja menggunakan sistem Project Ledger terstruktur.\n"
         "2. Setiap karya desain yang diselesaikan oleh PIHAK KEDUA akan didokumentasikan dan disahkan dalam Formulir Log Kontribusi Desain (Project Ledger) yang ditandatangani oleh PARA PIHAK.\n"
         "3. Pencatatan ini menjadi bukti sah bahwa karya tersebut diakui memiliki nilai komersial nyata yang menjadi hak tagih PIHAK KEDUA kepada perusahaan."),

        ("PASAL 3: PENILAIAN PROYEK & MEKANISME PENCAIRAN BERTAHAP",
         "1. Penilaian nilai kompensasi atas setiap proyek desain dilakukan secara adil dan fleksibel berdasarkan kesepakatan bersama, tingkat kesulitan teknis, dan dampak komersialnya terhadap penjualan.\n"
         "2. Pembayaran atas proyek yang tercatat di Project Ledger dilakukan secara bertahap per proyek (per-project settlement) disesuaikan dengan ketersediaan alokasi arus kas hasil penjualan produk."),

        ("PASAL 4: HAK KEKAYAAN INTELEKTUAL & PORTOFOLIO PROFESIONAL",
         "1. Seluruh aset desain final yang diserahterimakan menjadi hak guna komersial eksklusif PT Kediri Chemical Abadi.\n"
         "2. PIHAK KEDUA tetap memiliki hak moral sebagai pencipta untuk mencantumkan karya tersebut ke dalam portofolio profesional pribadi dengan persetujuan PIHAK PERTAMA."),

        ("PASAL 5: KERAHASIAAN INFORMASI (NDA)",
         "PIHAK KEDUA wajib menjaga kerahasiaan seluruh konsep produk, rencana peluncuran, formula, dan data internal perusahaan kepada pihak luar.")
    ]

    for title, text in pasal_list:
        add_par(doc, title, bold=True, size=10, space_after=2)
        add_par(doc, text, size=9.5, space_after=8)

    add_par(doc, "Demikian Nota Kesepahaman ini dibuat dalam rangkap 2 (dua) bermeterai cukup dan memiliki kekuatan hukum yang sama bagi PARA PIHAK.", space_after=14)

    # Tanda Tangan
    tbl_ttd = doc.add_table(rows=1, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c1.width = Inches(3.4)
    c2.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.15
    p1.add_run("PIHAK PERTAMA\nPT Kediri Chemical Abadi\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YERIKHO ARFENSIAS EFFENDI\n").bold = True
    p1.add_run("General Manager").font.size = Pt(9)

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.15
    p2.add_run("PIHAK KEDUA\nTenaga Kemitraan Kreatif\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("FAJAR\n").bold = True
    p2.add_run("Head of Creative & Design").font.size = Pt(9)

    for c in (c1, c2):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")

    filename = os.path.join(OUTPUT_DIR, "MOU-02_Kemitraan_Kreatif_Fajar_Creative_Design.docx")
    doc.save(filename)
    print(f"[OK] Saved: {filename}")

# -------------------------------------------------------------
# DOKUMEN 4: FORMULIR PROJECT LEDGER DESAIN
# -------------------------------------------------------------
def build_project_ledger():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "BUKU LOG KONTRIBUSI DESAIN", "FRM-01/DKV-LEDGER/2026")

    add_par(doc, "FORMULIR CATATAN KONTRIBUSI DESAIN (PROJECT LEDGER)", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_par(doc, "DIVISI KREATIF & DESAIN KOMUNIKASI VISUAL — PT KEDIRI CHEMICAL ABADI", bold=True, size=9.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    p_info = add_par(doc)
    p_info.add_run("Nama Desainer : ").bold = True
    p_info.add_run("Fajar (Head of Creative & Design)\n")
    p_info.add_run("Supervisor     : ").bold = True
    p_info.add_run("Yerikho Arfensias Effendi (General Manager)\n")
    p_info.add_run("Periode Proyek : ").bold = True
    p_info.add_run("September – Desember 2026\n")

    add_par(doc, "Petunjuk: Setiap penyerahan file desain siap cetak (print-ready) atau aset visual digital wajib dicatat pada tabel di bawah ini dan diparaf bersama oleh Desainer dan General Manager sebagai dasar pencairan hak kompensasi.", italic=True, size=8.5, space_after=10)

    # Tabel Ledger
    headers = ["No", "Tanggal", "Nama Proyek Desain", "Format Output", "Estimasi Nilai (Rp)", "Paraf GM", "Status / Tgl Cair"]
    widths = [Inches(0.4), Inches(0.9), Inches(2.2), Inches(1.1), Inches(1.1), Inches(0.7), Inches(1.0)]

    tbl = doc.add_table(rows=11, cols=7)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    # Header Row
    hdr_cells = tbl.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = widths[i]
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(8)
        run.font.name = 'Times New Roman'
        run.font.color.rgb = COLOR_BLACK
        set_cell_margins(hdr_cells[i], top=80, bottom=80, left=40, right=40)
        set_cell_border(hdr_cells[i], top="single", bottom="single", left="single", right="single", top_sz="8", bottom_sz="8")

    # Sample Data Rows
    sample_rows = [
        ("1", "06/09/26", "Label Botol Sabun Mandi 250ml", "PDF/AI Print-Ready", "Rp . . . . . . . . . .", "", "Batch 1 Rilis"),
        ("2", "06/09/26", "Label Botol Shampoo 250ml", "PDF/AI Print-Ready", "Rp . . . . . . . . . .", "", "Batch 1 Rilis"),
        ("3", " . . . . .", "Desain Banner Web & Hero Gen-Z", "WebP/PNG Transparan", "Rp . . . . . . . . . .", "", "Alokasi Kas"),
        ("4", " . . . . .", "Paket Feed IG Launching (9 Post)", "PNG 1080x1080 px", "Rp . . . . . . . . . .", "", "Alokasi Kas"),
        ("5", " . . . . .", "Desain Label Sabun Cair 500ml", "PDF/AI Print-Ready", "Rp . . . . . . . . . .", "", "Alokasi Kas"),
        ("6", " . . . . .", "Template Etalase Shopee/Tokopedia", "PNG Template Layer", "Rp . . . . . . . . . .", "", "Alokasi Kas"),
        ("7", " . . . . .", "", "", "", "", ""),
        ("8", " . . . . .", "", "", "", "", ""),
        ("9", " . . . . .", "", "", "", "", ""),
        ("10", " . . . . .", "", "", "", "", "")
    ]

    for row_idx, data in enumerate(sample_rows, start=1):
        row_cells = tbl.rows[row_idx].cells
        for col_idx, text in enumerate(data):
            row_cells[col_idx].width = widths[col_idx]
            p = row_cells[col_idx].paragraphs[0]
            if col_idx in (0, 1, 4, 5, 6):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.font.size = Pt(8)
            run.font.name = 'Times New Roman'
            run.font.color.rgb = COLOR_BLACK
            set_cell_margins(row_cells[col_idx], top=60, bottom=60, left=40, right=40)
            set_cell_border(row_cells[col_idx], top="single", bottom="single", left="single", right="single", top_sz="4", bottom_sz="4")

    add_par(doc, "", space_after=14)

    # Tanda Tangan
    tbl_ttd = doc.add_table(rows=1, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c1.width = Inches(3.4)
    c2.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.add_run("Diverifikasi Oleh,\nGeneral Manager\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YERIKHO ARFENSIAS EFFENDI").bold = True

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.add_run("Diajukan Oleh,\nHead of Creative & Design\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("FAJAR").bold = True

    for c in (c1, c2):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")

    filename = os.path.join(OUTPUT_DIR, "FRM-01_Formulir_Project_Ledger_Desain_KCA.docx")
    doc.save(filename)
    print(f"[OK] Saved: {filename}")

# -------------------------------------------------------------
# DOKUMEN 5: SURAT KEPUTUSAN (SK) STRUKTUR & PENGANGKATAN
# -------------------------------------------------------------
def build_sk_pengangkatan():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "SURAT KEPUTUSAN DIREKSI", "SKD-01/HR-KCA/IX/2026")

    add_par(doc, "SURAT KEPUTUSAN DIREKSI PT KEDIRI CHEMICAL ABADI", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_par(doc, "TENTANG STRUKTUR ORGANISASI & PENGANGKATAN PEJABAT OPERASIONAL", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_par(doc, "Nomor: 004/SKD/DIR-KCA/IX/2026", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_par(doc, "Menimbang:", bold=True, size=10, space_after=2)
    add_par(doc, "a. Bahwa dalam rangka mendukung ekspansi bisnis, pengembangan lini produk baru sabun & body care, serta penguatan tata kelola operasional PT Kediri Chemical Abadi, dipandang perlu menetapkan struktur organisasi awal yang adaptif dan profesional;\n"
                 "b. Bahwa individu yang namanya tercantum dalam keputusan ini dinilai memiliki integritas, kompetensi, dan loyalitas untuk menjalankan amanah jabatan yang ditetapkan.", size=9.5, space_after=6)

    add_par(doc, "Mengingat:", bold=True, size=10, space_after=2)
    add_par(doc, "1. Anggaran Dasar PT Kediri Chemical Abadi;\n"
                 "2. Standar Sistem Manajemen Mutu ISO 9001:2015 Klausul 5.3 mengenai Peran, Tanggung Jawab, dan Wewenang Organisasi.", size=9.5, space_after=8)

    add_par(doc, "MEMUTUSKAN", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    add_par(doc, "Menetapkan:", bold=True, size=10, space_after=2)

    decisions = [
        ("PERTAMA", "Mengesahkan Struktur Organisasi Inti PT Kediri Chemical Abadi yang terdiri dari Direktur Utama, General Manager, Business Operations Coordinator, dan Head of Creative & Design."),
        ("KEDUA", "Mengangkat Saudara FARHAN sebagai BUSINESS OPERATIONS COORDINATOR, dengan rincian tugas dan kewenangan operasional sebagaimana terlampir dalam uraian jabatan (Job Description)."),
        ("KETIGA", "Mengangkat Saudara FAJAR sebagai HEAD OF CREATIVE & DESIGN, dengan rincian tugas dan kewenangan kepemimpinan kreatif visual sebagaimana terlampir dalam uraian jabatan (Job Description)."),
        ("KEEMPAT", "Keputusan ini berlaku terhitung sejak tanggal 6 September 2026, dengan ketentuan apabila di kemudian hari terdapat kekeliruan, akan diadakan perbaikan sebagaimana mestinya.")
    ]

    for d_title, d_text in decisions:
        p = add_par(doc)
        p.add_run(f"{d_title} : ").bold = True
        p.add_run(d_text)
        p.paragraph_format.space_after = Pt(6)

    add_par(doc, "", space_after=14)

    # Tanda Tangan
    tbl_ttd = doc.add_table(rows=1, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c1.width = Inches(3.4)
    c2.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.add_run("Mengetahui,\nDirektur Utama\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YAN EFFENDI").bold = True

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.add_run("Ditetapkan di Kota Kediri, 6 September 2026\nGeneral Manager\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("YERIKHO ARFENSIAS EFFENDI").bold = True

    for c in (c1, c2):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")

    filename = os.path.join(OUTPUT_DIR, "SKD-01_Surat_Keputusan_Struktur_dan_Jobdesk_Tim.docx")
    doc.save(filename)
    print(f"[OK] Saved: {filename}")

if __name__ == "__main__":
    print("Mengeksekusi generator dokumen Word (.docx) ISO 9001...")
    build_surat_komitmen()
    build_mou_farhan()
    build_mou_fajar()
    build_project_ledger()
    build_sk_pengangkatan()
    print("Seluruh 5 dokumen template resmi telah berhasil dibuat dan disimpan!")
