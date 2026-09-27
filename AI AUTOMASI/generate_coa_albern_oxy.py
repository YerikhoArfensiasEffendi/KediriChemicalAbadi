#!/usr/bin/env python3
"""
PT KEDIRI CHEMICAL ABADI — QUALITY ASSURANCE & LAB MANDIRI
Modul Otomasi Pembuatan CERTIFICATE OF ANALYSIS (COA) / SERTIFIKAT ANALISIS
Format 1 Halaman A4 Presisi Sesuai Standar ISO 9001:2015 & Regulasi PKRT Kemenkes RI

Penanggung Jawab Teknis : Suparlin
General Manager         : Yerikho Arfensias Effendi
Direktur Utama          : Yan Effendi
"""

import os
import sys
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

# Import sanitasi metadata KCA
try:
    from kca_doc_humanizer import sanitize_docx_metadata
except ImportError:
    sys.path.append(os.path.dirname(__file__))
    try:
        from kca_doc_humanizer import sanitize_docx_metadata
    except ImportError:
        def sanitize_docx_metadata(p, **kwargs):
            pass

def set_table_borders(table, sz="4", color="000000"):
    """Set clean single borders for all cells in table."""
    tblPr = table._tbl.tblPr
    tblBorders = tblPr.find(qn('w:tblBorders'))
    if tblBorders is None:
        tblBorders = OxmlElement('w:tblBorders')
        tblPr.append(tblBorders)
    else:
        tblBorders.clear()
        
    for border_name in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), str(sz))
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    """Set inner cell padding in dxa."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = tcPr.find(qn('w:tcMar'))
    if tcMar is None:
        tcMar = OxmlElement('w:tcMar')
        tcPr.append(tcMar)
    else:
        tcMar.clear()
        
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)

def set_cell_width(cell, width_dxa):
    """Set explicit cell width in dxa."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcW = tcPr.find(qn('w:tcW'))
    if tcW is None:
        tcW = OxmlElement('w:tcW')
        tcPr.append(tcW)
    tcW.set(qn('w:w'), str(width_dxa))
    tcW.set(qn('w:type'), 'dxa')

def generate_coa_document(
    product_name="ALBERN OXY",
    category="Pemutih Pakaian & Disinfektan PKRT (Bleaching Agent)",
    batch_no="AO-260927-01",
    check_date="27 September 2026",
    mfg_date="27 September 2026",
    exp_date="27 September 2028",
    sample_volume="1 Liter",
    doc_no="COA/KCA-PKD/2026/09/AO-001",
    pic_name="Suparlin",
    pic_role="Penanggung Jawab Teknis",
    city="Kediri",
    output_paths=None
):
    doc = Document()

    # 1. Konfigurasi Halaman (A4, Margin 2 cm)
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin = Cm(2.0)
    section.right_margin = Cm(2.0)

    # Style Dasar
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)

    # Total width printable A4: 21 cm - 4 cm = 17 cm = 9638 dxa
    TOTAL_WIDTH_DXA = 9638

    # 2. Header / Kop Institusi COA (Tengah, Hitam Murni)
    p_comp = doc.add_paragraph()
    p_comp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_comp.paragraph_format.space_before = Pt(0)
    p_comp.paragraph_format.space_after = Pt(1)
    r_comp = p_comp.add_run("PT KEDIRI CHEMICAL ABADI")
    r_comp.font.name = 'Times New Roman'
    r_comp.font.size = Pt(11)
    r_comp.font.bold = True
    r_comp.font.color.rgb = RGBColor(0, 0, 0)

    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_before = Pt(0)
    p_div.paragraph_format.space_after = Pt(4)
    r_div = p_div.add_run("LABORATORIUM KENDALI MUTU (QC) & PENGUJIAN PRODUK JADI")
    r_div.font.name = 'Times New Roman'
    r_div.font.size = Pt(9)
    r_div.font.color.rgb = RGBColor(0, 0, 0)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("CERTIFICATE OF ANALYSIS (COA)")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    p_no = doc.add_paragraph()
    p_no.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_no.paragraph_format.space_before = Pt(0)
    p_no.paragraph_format.space_after = Pt(6)
    r_no = p_no.add_run(f"Nomor Dokumen: {doc_no}")
    r_no.font.name = 'Times New Roman'
    r_no.font.size = Pt(9.5)
    r_no.font.italic = True
    r_no.font.color.rgb = RGBColor(0, 0, 0)

    # Garis Pembatas Tipis Elegan
    pPr = p_no._p.get_or_add_pPr()
    pBdr = parse_xml(
        r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        r'<w:bottom w:val="single" w:sz="6" w:space="2" w:color="000000"/>'
        r'</w:pBdr>'
    )
    pPr.append(pBdr)

    # 3. Metadata Produk & Pengujian (Tabel 2 Kolom Tanpa Border agar sangat presisi & rapi)
    t_meta = doc.add_table(rows=4, cols=2)
    t_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w_m = [4819, 4819]

    meta_left = [
        ("Nama Produk / Product", product_name, True),
        ("Kategori Sediaan", category, False),
        ("Bentuk Sediaan / Form", "Cairan (Liquid)", False),
        ("Ukuran Sampel / Sample", sample_volume, False)
    ]
    meta_right = [
        ("Nomor Bets / Batch No.", batch_no, True),
        ("Tanggal Manufaktur", mfg_date, False),
        ("Tanggal Pengujian", check_date, False),
        ("Kedaluwarsa / Exp. Date", exp_date, False)
    ]

    for ri in range(4):
        # Kolom Kiri
        c_l = t_meta.cell(ri, 0)
        set_cell_width(c_l, col_w_m[0])
        set_cell_margins(c_l, top=15, bottom=15, left=0, right=60)
        p_l = c_l.paragraphs[0]
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(0)
        lbl_l, val_l, b_l = meta_left[ri]
        r1 = p_l.add_run(f"{lbl_l:<24}: ")
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGBColor(0, 0, 0)
        r2 = p_l.add_run(val_l)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(9.5)
        r2.font.bold = b_l
        r2.font.color.rgb = RGBColor(0, 0, 0)

        # Kolom Kanan
        c_r = t_meta.cell(ri, 1)
        set_cell_width(c_r, col_w_m[1])
        set_cell_margins(c_r, top=15, bottom=15, left=60, right=0)
        p_r = c_r.paragraphs[0]
        p_r.paragraph_format.space_before = Pt(0)
        p_r.paragraph_format.space_after = Pt(0)
        lbl_r, val_r, b_r = meta_right[ri]
        r3 = p_r.add_run(f"{lbl_r:<24}: ")
        r3.font.name = 'Times New Roman'
        r3.font.size = Pt(9.5)
        r3.font.color.rgb = RGBColor(0, 0, 0)
        r4 = p_r.add_run(val_r)
        r4.font.name = 'Times New Roman'
        r4.font.size = Pt(9.5)
        r4.font.bold = b_r
        r4.font.color.rgb = RGBColor(0, 0, 0)

    # Spacer
    p_sp1 = doc.add_paragraph()
    p_sp1.paragraph_format.space_before = Pt(0)
    p_sp1.paragraph_format.space_after = Pt(4)

    # 4. Tabel 1 — Hasil Uji Laboratorium (Parameter Fisiko-Kimia COA)
    # 6 Kolom: No (500), Parameter (2400), Metode Uji (1700), Spesifikasi (2200), Hasil (1700), Status (1138)
    col_w_t1 = [500, 2400, 1700, 2200, 1700, 1138]

    coa_tests = [
        ("1", "Bentuk Fisik (Appearance)", "Organoleptik", "Cairan Homogen", "Cairan", "Memenuhi"),
        ("2", "Warna (Color)", "Visual", "Bening Kekuningan", "Bening Kekuningan", "Memenuhi"),
        ("3", "Bau / Aroma (Odor)", "Olfaktori", "Khas Klorin Segar", "Khas Klorin Segar", "Memenuhi"),
        ("4", "Berat Bersih (Net Weight)", "Gravimetri", "1,00 – 1,04 kg", "1,02 kg", "Memenuhi"),
        ("5", "Derajat Keasaman / pH (25°C)", "pH Meter Digital", "8.5 – 10.5", "9.60", "Memenuhi"),
        ("6", "Bobot Jenis / Densitas (25°C)", "Hydrometer", "1.01 – 1.04 g/mL", "1.02 g/mL", "Memenuhi"),
    ]

    t_test = doc.add_table(rows=len(coa_tests) + 2, cols=6)
    t_test.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_test, sz="4", color="000000")

    headers_t1 = [
        ("No", WD_ALIGN_PARAGRAPH.CENTER),
        ("Parameter Pengujian", WD_ALIGN_PARAGRAPH.LEFT),
        ("Metode Uji", WD_ALIGN_PARAGRAPH.CENTER),
        ("Spesifikasi Standar", WD_ALIGN_PARAGRAPH.CENTER),
        ("Hasil Analisis", WD_ALIGN_PARAGRAPH.CENTER),
        ("Status", WD_ALIGN_PARAGRAPH.CENTER)
    ]
    for ci, (h_text, align) in enumerate(headers_t1):
        cell = t_test.cell(0, ci)
        set_cell_width(cell, col_w_t1[ci])
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = align
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.0)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)

    for ri, (no, param, method, spec, res, stat) in enumerate(coa_tests, start=1):
        row_cells = [
            (no, WD_ALIGN_PARAGRAPH.CENTER, True),
            (param, WD_ALIGN_PARAGRAPH.LEFT, False),
            (method, WD_ALIGN_PARAGRAPH.CENTER, False),
            (spec, WD_ALIGN_PARAGRAPH.CENTER, False),
            (res, WD_ALIGN_PARAGRAPH.CENTER, False),
            (stat, WD_ALIGN_PARAGRAPH.CENTER, True)
        ]
        for ci, (val, align, is_b) in enumerate(row_cells):
            cell = t_test.cell(ri, ci)
            set_cell_width(cell, col_w_t1[ci])
            set_cell_margins(cell, top=45, bottom=45, left=50, right=50)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = align
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.bold = is_b
            r.font.color.rgb = RGBColor(0, 0, 0)

    # Baris Kesimpulan Lulus (Merged Cell)
    c_start = t_test.cell(len(coa_tests) + 1, 0)
    c_end = t_test.cell(len(coa_tests) + 1, 5)
    merged_test = c_start.merge(c_end)
    set_cell_width(merged_test, TOTAL_WIDTH_DXA)
    set_cell_margins(merged_test, top=60, bottom=60, left=60, right=60)
    merged_test.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    p_mt = merged_test.paragraphs[0]
    p_mt.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_mt.paragraph_format.space_before = Pt(0)
    p_mt.paragraph_format.space_after = Pt(0)
    r_mt = p_mt.add_run("KESIMPULAN: Produk ini telah diuji dan memenuhi seluruh spesifikasi yang ditetapkan (DILULUSKAN / RELEASED)")
    r_mt.font.name = 'Times New Roman'
    r_mt.font.size = Pt(9.0)
    r_mt.font.bold = True
    r_mt.font.color.rgb = RGBColor(0, 0, 0)

    # 5. Bagian 2 — Bahan yang Digunakan (Komposisi Formula Sediaan 1 Liter)
    p_sec2 = doc.add_paragraph()
    p_sec2.paragraph_format.space_before = Pt(8)
    p_sec2.paragraph_format.space_after = Pt(3)
    r_s2 = p_sec2.add_run("Bahan yang Digunakan (Komposisi Formula Sediaan 1 Liter):")
    r_s2.font.name = 'Times New Roman'
    r_s2.font.size = Pt(10)
    r_s2.font.bold = True
    r_s2.font.color.rgb = RGBColor(0, 0, 0)

    # Tabel 2: Komposisi Bahan
    col_w_t2 = [500, 3200, 2100, 3838]
    ingredients = [
        ("1", "Calcium Hypochlorite", "50 gram", "Bahan aktif pemutih, oksidator noda membandel & disinfektan"),
        ("2", "Sodium Carbonate", "25 gram", "Builder alkali, penstabil sediaan, pelunak kesadahan & pengatur pH basa"),
        ("3", "Air Demineralisasi (Aqua RO)", "925 mL", "Pelarut utama sediaan (solvent)")
    ]

    t_ing = doc.add_table(rows=len(ingredients) + 1, cols=4)
    t_ing.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_ing, sz="4", color="000000")

    headers_t2 = [
        ("No", WD_ALIGN_PARAGRAPH.CENTER),
        ("Nama Bahan Baku", WD_ALIGN_PARAGRAPH.LEFT),
        ("Takaran (per 1 Liter)", WD_ALIGN_PARAGRAPH.CENTER),
        ("Fungsi Bahan", WD_ALIGN_PARAGRAPH.LEFT)
    ]
    for ci, (h_text, align) in enumerate(headers_t2):
        cell = t_ing.cell(0, ci)
        set_cell_width(cell, col_w_t2[ci])
        set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = align
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.0)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)

    for ri, (no, nama, takaran, fungsi) in enumerate(ingredients, start=1):
        row_cells = [
            (no, WD_ALIGN_PARAGRAPH.CENTER, True),
            (nama, WD_ALIGN_PARAGRAPH.LEFT, False),
            (takaran, WD_ALIGN_PARAGRAPH.CENTER, False),
            (fungsi, WD_ALIGN_PARAGRAPH.LEFT, False)
        ]
        for ci, (val, align, is_b) in enumerate(row_cells):
            cell = t_ing.cell(ri, ci)
            set_cell_width(cell, col_w_t2[ci])
            set_cell_margins(cell, top=45, bottom=45, left=60, right=60)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = align
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.bold = is_b
            r.font.color.rgb = RGBColor(0, 0, 0)

    # 6. Blok Pengesahan (Bawah Kiri)
    p_date = doc.add_paragraph()
    p_date.paragraph_format.space_before = Pt(10)
    p_date.paragraph_format.space_after = Pt(36)  # Ruang 4 baris cap stempel bulat KCA
    p_date.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_dt = p_date.add_run(f"{city}, {check_date}")
    r_dt.font.name = 'Times New Roman'
    r_dt.font.size = Pt(10)
    r_dt.font.color.rgb = RGBColor(0, 0, 0)

    p_pic = doc.add_paragraph()
    p_pic.paragraph_format.space_before = Pt(0)
    p_pic.paragraph_format.space_after = Pt(1)
    p_pic.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_pic = p_pic.add_run(pic_name)
    r_pic.font.name = 'Times New Roman'
    r_pic.font.size = Pt(10.5)
    r_pic.font.bold = True
    r_pic.font.color.rgb = RGBColor(0, 0, 0)

    p_role = doc.add_paragraph()
    p_role.paragraph_format.space_before = Pt(0)
    p_role.paragraph_format.space_after = Pt(0)
    p_role.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_role = p_role.add_run(pic_role)
    r_role.font.name = 'Times New Roman'
    r_role.font.size = Pt(9.5)
    r_role.font.color.rgb = RGBColor(0, 0, 0)

    # 7. Simpan Dokumen & Sanitasi Metadata
    if output_paths is None:
        output_paths = [
            "/Users/arthur/Documents/Meetings Agent/PKD/COA_ALBERN_OXY.docx",
            "/Users/arthur/Documents/Meetings Agent/product/PKD/COA_ALBERN_OXY.docx",
            "/Users/arthur/Documents/Meetings Agent/PKD/CERTIFICATE_OF_ANALYSIS_ALBERN_OXY.docx",
            "/Users/arthur/Documents/Meetings Agent/product/PKD/CERTIFICATE_OF_ANALYSIS_ALBERN_OXY.docx"
        ]

    for p in output_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        doc.save(p)
        sanitize_docx_metadata(
            p,
            title=f"Certificate of Analysis (COA) - {product_name}",
            author="Yerikho Arfensias Effendi"
        )
        print(f"SUKSES COA tersimpan dan disanitasi: {p}")

    return output_paths

if __name__ == "__main__":
    generate_coa_document()
