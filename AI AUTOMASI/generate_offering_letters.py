#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERATOR OFFERING LETTER (SURAT PENAWARAN KERJASAMA / KERJA)
UNTUK FARHAN & FAJAR
PT KEDIRI CHEMICAL ABADI — STANDAR ISO 9001:2015

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

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
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
    core_props.comments = "Offering Letter Resmi PT Kediri Chemical Abadi Standar ISO 9001:2015"
    core_props.category = "Surat Penawaran Kerja / Offering Letter"
    core_props.keywords = "PT Kediri Chemical Abadi, Offering Letter, Farhan, Fajar, Yerikho Arfensias Effendi"

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
    run3 = p_right.add_run(f"STANDAR ISO 9001:2015\nNo: {doc_number}\nTanggal: 6 September 2026")
    run3.font.name = 'Times New Roman'
    run3.font.size = Pt(8)
    run3.font.bold = True
    run3.font.color.rgb = COLOR_BLACK

    for c in (cell_left, cell_right):
        set_cell_border(c, top="none", left="none", right="none", bottom="single", bottom_sz="12", bottom_color="000000")
        set_cell_margins(c, top=40, bottom=80, left=40, right=40)

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_after = Pt(6)

def add_par(doc, text="", bold=False, italic=False, size=10, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=5):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(space_before)
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
# DOKUMEN 1: OFFERING LETTER — FARHAN
# -------------------------------------------------------------
def build_ol_farhan():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "SURAT PENAWARAN KERJA", "OL-01/HR-KCA/IX/2026")

    add_par(doc, "SURAT PENAWARAN KERJASAMA & HUBUNGAN KERJA", bold=True, size=12.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1)
    add_par(doc, "(JOB & PARTNERSHIP OFFERING LETTER)", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)
    add_par(doc, "Nomor: 005/HR-OL/KCA/IX/2026", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    p_tujuan = add_par(doc, "Kepada Yth,\nSaudara FARHAN\nDi Tempat\n", bold=False, size=10, space_after=6)
    p_tujuan.runs[0].font.bold = True

    add_par(doc, "Dengan hormat,", size=10, space_after=4)
    add_par(doc, "Sehubungan dengan rencana penguatan tim inti operasional dan ekspansi lini produk baru di PT Kediri Chemical Abadi, Manajemen Perusahaan menilai Saudara memiliki integritas, dedikasi, dan kecakapan yang sangat tepat untuk mengisi posisi strategis di perusahaan kami.", size=9.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6)
    add_par(doc, "Melalui surat ini, Manajemen PT Kediri Chemical Abadi dengan bangga menyampaikan penawaran resmi kerjasama dan hubungan kerja kepada Saudara dengan rincian ketentuan sebagai berikut:", size=9.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8)

    # Tabel Rincian Penawaran
    details = [
        ("1. Posisi / Jabatan", "Business Operations Coordinator (Tangan Kanan General Manager)"),
        ("2. Departemen / Divisi", "Operasional Bisnis, Rantai Pasok & Logistik"),
        ("3. Atasan Langsung", "General Manager (Yerikho Arfensias Effendi)"),
        ("4. Tanggal Efektif", "Minggu, 6 September 2026"),
        ("5. Ruang Lingkup Tugas", "• Membantu dan mengeksekusi kebutuhan harian usaha yang disiapkan GM.\n"
                                  "• Pengadaan botol (250ml/500ml), ukur stiker, dan koordinasi percetakan.\n"
                                  "• Operasional pengisian cairan sabun di pabrik dan penempelan stiker rapi.\n"
                                  "• Pengelolaan toko online resmi (Shopee & Tokopedia) serta chat pembeli.\n"
                                  "• Pengepakan paket aman (bubble wrap + kardus) dan pengiriman kurir."),
        ("6. Skema Kompensasi Gaji", "• Tahap Awal: Jam kerja fleksibel dan adaptif.\n"
                                     "• Tahap Arus Kas Stabil: Gaji bulanan dimulai bertahap sebesar Rp 1.500.000,- (Satu Juta Lima Ratus Ribu Rupiah) per bulan, dan akan terus dinaikkan seiring penguatan stabilitas arus kas perusahaan."),
        ("7. Insentif Skala Besar", "Ketika volume penjualan produk memasuki skala produksi massal dan distribusi luas, Saudara berhak atas tambahan komisi insentif sebesar 1% (Satu Persen) dari total nilai penjualan kotor setiap produk yang terjual."),
        ("8. Status Hubungan Kerja", "Kemitraan Kerja Inti yang dituangkan dalam Surat Perjanjian Kerjasama (MOU) resmi berkekuatan hukum.")
    ]

    tbl = doc.add_table(rows=len(details), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    w_col = [Inches(2.2), Inches(4.6)]
    for r_idx, (k, v) in enumerate(details):
        r_cells = tbl.rows[r_idx].cells
        for c_idx, text in enumerate([k, v]):
            r_cells[c_idx].width = w_col[c_idx]
            p = r_cells[c_idx].paragraphs[0]
            p.paragraph_format.line_spacing = 1.1
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9)
            if c_idx == 0:
                run.bold = True
            run.font.color.rgb = COLOR_BLACK
            set_cell_margins(r_cells[c_idx], top=50, bottom=50, left=60, right=60)
            set_cell_border(r_cells[c_idx], top="single", bottom="single", left="single", right="single", top_sz="4", bottom_sz="4")

    add_par(doc, "", space_after=6)
    add_par(doc, "Kami meyakini bahwa kehadiran Saudara akan membawa akselerasi besar bagi operasional perusahaan dan kita dapat tumbuh sukses bersama. Jika Saudara menyetujui seluruh ketentuan penawaran ini, mohon menandatangani lembar konfirmasi di bawah ini.", size=9.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10)

    # Tanda Tangan
    tbl_ttd = doc.add_table(rows=1, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c1.width = Inches(3.4)
    c2.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.15
    p1.add_run("Diberikan Oleh,\nPT Kediri Chemical Abadi\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YERIKHO ARFENSIAS EFFENDI\n").bold = True
    p1.add_run("General Manager").font.size = Pt(9)

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.15
    p2.add_run("Diterima & Disetujui Oleh,\nKandidat Rekan Kerja\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("FARHAN\n").bold = True
    p2.add_run("Tanggal: 6 September 2026").font.size = Pt(8.5)

    for c in (c1, c2):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")

    filename = os.path.join(OUTPUT_DIR, "OFFERING_LETTER_FARHAN_OPERATIONS.docx")
    doc.save(filename)
    print(f"[OK] Saved: {filename}")

# -------------------------------------------------------------
# DOKUMEN 2: OFFERING LETTER — FAJAR
# -------------------------------------------------------------
def build_ol_fajar():
    doc = Document()
    setup_page_layout(doc)
    sanitize_metadata(doc)
    add_header_kop(doc, "SURAT PENAWARAN KERJA", "OL-02/HR-KCA/IX/2026")

    add_par(doc, "SURAT PENAWARAN KERJASAMA & HUBUNGAN KREATIF", bold=True, size=12.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1)
    add_par(doc, "(CREATIVE PARTNERSHIP OFFERING LETTER)", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)
    add_par(doc, "Nomor: 006/HR-OL/KCA/IX/2026", italic=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    p_tujuan = add_par(doc, "Kepada Yth,\nSaudara FAJAR\nDi Tempat\n", bold=False, size=10, space_after=6)
    p_tujuan.runs[0].font.bold = True

    add_par(doc, "Dengan hormat,", size=10, space_after=4)
    add_par(doc, "Sehubungan dengan peluncuran lini produk baru sabun mandi, shampoo, dan body care berkarakter Gen-Z serta peremajaan citra digital PT Kediri Chemical Abadi, Manajemen Perusahaan menilai Saudara memiliki bakat artistik, portofolio DKV yang kuat, dan visi estetika yang selaras dengan arah bisnis kami.", size=9.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6)
    add_par(doc, "Melalui surat ini, Manajemen PT Kediri Chemical Abadi secara resmi menyampaikan penawaran kerjasama kreatif kepada Saudara dengan rincian ketentuan sebagai berikut:", size=9.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=8)

    # Tabel Rincian Penawaran
    details = [
        ("1. Posisi / Jabatan", "Head of Creative & Design (Pemimpin Divisi Desain & Visual)"),
        ("2. Departemen / Divisi", "Kreatif, Desain Komunikasi Visual & Digital Branding"),
        ("3. Atasan Langsung", "General Manager (Yerikho Arfensias Effendi)"),
        ("4. Tanggal Efektif", "Minggu, 6 September 2026"),
        ("5. Ruang Lingkup Tugas", "• Perancangan desain kemasan botol sabun & shampoo siap cetak (CMYK, 300 DPI).\n"
                                  "• Desain banner visual website resmi berstandar modern Gen-Z.\n"
                                  "• Perancangan 9 feed Instagram estetik perdana dan template Story promo.\n"
                                  "• Desain dekorasi toko dan bingkai foto produk di marketplace (Shopee/Tokped).\n"
                                  "• Dokumentasi penyerahan karya desain ke Formulir Project Ledger."),
        ("6. Sistem Kerja Awal", "Bekerja dengan sistem volunteer terstruktur di awal proyek. Setiap karya desain yang diselesaikan dicatat dan diakui secara sah oleh kedua pihak dalam Project Ledger."),
        ("7. Mekanisme Kompensasi", "Penilaian harga jasa desain bersifat fleksibel berdasarkan peminat pasar dan dampak (impact) visual terhadap penjualan. Pembayaran proyek dibayarkan bertahap satu per satu saat arus kas perusahaan sanggup membayar dan dialokasikan."),
        ("8. Hak Cipta & Portofolio", "Aset final yang dibayarkan menjadi hak komersial perusahaan, namun Saudara tetap memiliki hak moral penuh untuk mencantumkannya dalam portofolio pribadi."),
        ("9. Status Hubungan Kerja", "Kemitraan Kreatif Inti yang dituangkan dalam Surat Perjanjian Kerjasama (MOU) resmi berkekuatan hukum.")
    ]

    tbl = doc.add_table(rows=len(details), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    w_col = [Inches(2.2), Inches(4.6)]
    for r_idx, (k, v) in enumerate(details):
        r_cells = tbl.rows[r_idx].cells
        for c_idx, text in enumerate([k, v]):
            r_cells[c_idx].width = w_col[c_idx]
            p = r_cells[c_idx].paragraphs[0]
            p.paragraph_format.line_spacing = 1.1
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9)
            if c_idx == 0:
                run.bold = True
            run.font.color.rgb = COLOR_BLACK
            set_cell_margins(r_cells[c_idx], top=50, bottom=50, left=60, right=60)
            set_cell_border(r_cells[c_idx], top="single", bottom="single", left="single", right="single", top_sz="4", bottom_sz="4")

    add_par(doc, "", space_after=6)
    add_par(doc, "Karya desain Saudara akan menjadi ujung tombak wajah produk PT Kediri Chemical Abadi di mata konsumen. Jika Saudara menyetujui seluruh ketentuan penawaran ini, mohon menandatangani lembar konfirmasi di bawah ini.", size=9.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10)

    # Tanda Tangan
    tbl_ttd = doc.add_table(rows=1, cols=2)
    tbl_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = tbl_ttd.cell(0, 0), tbl_ttd.cell(0, 1)
    c1.width = Inches(3.4)
    c2.width = Inches(3.4)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.15
    p1.add_run("Diberikan Oleh,\nPT Kediri Chemical Abadi\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p1.add_run("YERIKHO ARFENSIAS EFFENDI\n").bold = True
    p1.add_run("General Manager").font.size = Pt(9)

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.15
    p2.add_run("Diterima & Disetujui Oleh,\nKandidat Rekan Kreatif\n\n\n\n\n").font.color.rgb = COLOR_BLACK
    p2.add_run("FAJAR\n").bold = True
    p2.add_run("Tanggal: 6 September 2026").font.size = Pt(8.5)

    for c in (c1, c2):
        set_cell_border(c, top="none", left="none", right="none", bottom="none")

    filename = os.path.join(OUTPUT_DIR, "OFFERING_LETTER_FAJAR_CREATIVE_DESIGN.docx")
    doc.save(filename)
    print(f"[OK] Saved: {filename}")

if __name__ == "__main__":
    build_ol_farhan()
    build_ol_fajar()
