#!/usr/bin/env python3
"""
PT KEDIRI CHEMICAL ABADI — QUALITY ASSURANCE & LAB MANDIRI DEPARTMENT
Modul Otomasi Pembuatan Sertifikat Hasil Uji Produk Jadi & Komposisi Bahan (PKRT/CPKRT)
Format 1 Halaman A4 Presisi Sesuai Standar ISO 9001:2015 & Regulasi Kemenkes RI

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
    """Set global borders on table element."""
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

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
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
    """Set explicit width for cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcW = tcPr.find(qn('w:tcW'))
    if tcW is None:
        tcW = OxmlElement('w:tcW')
        tcPr.append(tcW)
    tcW.set(qn('w:w'), str(width_dxa))
    tcW.set(qn('w:type'), 'dxa')

def create_qc_certificate(
    product_name="ALBERN OXY",
    check_date=None,
    sample_volume="1 Liter",
    specs_dict=None,
    results_dict=None,
    ingredients=None,
    pic_name="Suparlin",
    pic_role="Penanggung Jawab Teknis",
    city="Kediri",
    output_paths=None
):
    if check_date is None:
        today = datetime.now()
        bulan_indo = [
            "", "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ]
        check_date = f"{today.day} {bulan_indo[today.month]} {today.year}"

    # Default Spesifikasi & Hasil jika tidak ditentukan
    if specs_dict is None:
        specs_dict = {
            "bentuk": "Cairan",
            "warna": "Bening Kekuningan",
            "bau": "Khas Klorin Segar",
            "berat": "1,00 - 1,04 kg",
            "ph": "8.5 - 10.5",
            "densitas": "1.01 - 1.04"
        }
    if results_dict is None:
        results_dict = {
            "bentuk": "Cairan",
            "warna": "Bening Kekuningan",
            "bau": "Khas Klorin Segar",
            "berat": "1,02 kg",
            "ph": "9.6",
            "densitas": "1.02"
        }

    # Default Formula (1.000 g / 1 Liter)
    if ingredients is None:
        ingredients = [
            ("1", "Calcium Hypochlorite", "50 gram", "Bahan aktif pemutih, oksidator noda & disinfektan"),
            ("2", "Sodium Carbonate", "25 gram", "Builder alkali, penstabil sediaan & pengatur pH basa"),
            ("3", "Air Demineralisasi (Aqua RO)", "925 mL", "Pelarut utama sediaan (solvent)")
        ]

    # Inisialisasi Dokumen
    doc = Document()

    # 1. Konfigurasi Halaman (A4, Margin 2 cm)
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.0)
    section.right_margin = Cm(2.0)

    # Style Dasar
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)

    # 2. Judul Dokumen (Tengah, Bold 14pt, Times New Roman, Hitam Murni)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(10)
    p_title.paragraph_format.line_spacing = 1.15
    run_title = p_title.add_run("Sertifikat Hasil Uji Produk Jadi")
    run_title.font.name = 'Times New Roman'
    run_title.font.size = Pt(14)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0, 0, 0)

    # 3. Metadata Produk (Rata Kiri, 11pt, Hitam Murni)
    metadata_items = [
        ("Nama Produk", product_name),
        ("Tanggal Pengecekan", check_date),
        ("Sample", sample_volume)
    ]
    for label, val in metadata_items:
        p_meta = doc.add_paragraph()
        p_meta.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_meta.paragraph_format.space_before = Pt(0)
        p_meta.paragraph_format.space_after = Pt(2)
        p_meta.paragraph_format.line_spacing = 1.15
        
        # Format padding spasi agar titik dua sejajar rapi
        label_padded = f"{label:<20}: "
        r_lbl = p_meta.add_run(label_padded)
        r_lbl.font.name = 'Times New Roman'
        r_lbl.font.size = Pt(11)
        r_lbl.font.color.rgb = RGBColor(0, 0, 0)
        
        r_val = p_meta.add_run(val)
        r_val.font.name = 'Times New Roman'
        r_val.font.size = Pt(11)
        r_val.font.bold = (label == "Nama Produk")
        r_val.font.color.rgb = RGBColor(0, 0, 0)

    # Spacer kecil sebelum Tabel 1
    p_sp1 = doc.add_paragraph()
    p_sp1.paragraph_format.space_before = Pt(0)
    p_sp1.paragraph_format.space_after = Pt(6)

    # 4. Tabel 1 - Hasil Uji Produk Jadi (7 Kolom, 4 Baris)
    # Total width printable A4: 21 cm - 4 cm = 17 cm = 9638 dxa (~481.9 pt)
    table1 = doc.add_table(rows=4, cols=7)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table1, sz="6", color="000000")

    col_widths_t1 = [1377, 1377, 1377, 1377, 1377, 1377, 1376]  # total = 9638 dxa

    # Baris 1: Header
    headers_t1 = ["Parameter", "Bentuk", "Warna", "Bau", "Berat", "PH Meter", "Densitas\n(Hydrometer)"]
    for i, h in enumerate(headers_t1):
        cell = table1.cell(0, i)
        set_cell_width(cell, col_widths_t1[i])
        set_cell_margins(cell, top=80, bottom=80, left=60, right=60)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Baris 2: Spesifikasi
    spesifikasi_vals = [
        "Spesifikasi",
        specs_dict["bentuk"],
        specs_dict["warna"],
        specs_dict["bau"],
        specs_dict["berat"],
        specs_dict["ph"],
        specs_dict["densitas"]
    ]
    for i, v in enumerate(spesifikasi_vals):
        cell = table1.cell(1, i)
        set_cell_width(cell, col_widths_t1[i])
        set_cell_margins(cell, top=80, bottom=80, left=60, right=60)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(v)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.bold = (i == 0)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Baris 3: Hasil
    hasil_vals = [
        "Hasil",
        results_dict["bentuk"],
        results_dict["warna"],
        results_dict["bau"],
        results_dict["berat"],
        results_dict["ph"],
        results_dict["densitas"]
    ]
    for i, v in enumerate(hasil_vals):
        cell = table1.cell(2, i)
        set_cell_width(cell, col_widths_t1[i])
        set_cell_margins(cell, top=80, bottom=80, left=60, right=60)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(v)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.bold = (i == 0)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Baris 4: Full Width Merged Cell
    c_start = table1.cell(3, 0)
    c_end = table1.cell(3, 6)
    merged_cell = c_start.merge(c_end)
    set_cell_width(merged_cell, 9638)
    set_cell_margins(merged_cell, top=80, bottom=80, left=80, right=80)
    merged_cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    p_m = merged_cell.paragraphs[0]
    p_m.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_m.paragraph_format.space_before = Pt(0)
    p_m.paragraph_format.space_after = Pt(0)
    r_m = p_m.add_run("Produk ini telah diperiksa dan memenuhi spesifikasi yang ditetapkan")
    r_m.font.name = 'Times New Roman'
    r_m.font.size = Pt(10)
    r_m.font.bold = True
    r_m.font.color.rgb = RGBColor(0, 0, 0)

    # 5. Bagian 2 - Bahan yang Digunakan
    p_sec2 = doc.add_paragraph()
    p_sec2.paragraph_format.space_before = Pt(14)
    p_sec2.paragraph_format.space_after = Pt(4)
    p_sec2.paragraph_format.line_spacing = 1.15
    r_s2 = p_sec2.add_run("Bahan yang Digunakan (Komposisi Formula Sediaan 1 Liter):")
    r_s2.font.name = 'Times New Roman'
    r_s2.font.size = Pt(11)
    r_s2.font.bold = True
    r_s2.font.color.rgb = RGBColor(0, 0, 0)

    # Tabel 2: Komposisi Bahan
    # Total width: 9638 dxa (Col 0: 600, Col 1: 3400, Col 2: 2100, Col 3: 3538)
    table2 = doc.add_table(rows=len(ingredients) + 1, cols=4)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table2, sz="4", color="000000")

    col_widths_t2 = [600, 3400, 2100, 3538]

    # Header Tabel 2
    headers_t2 = [
        ("No", WD_ALIGN_PARAGRAPH.CENTER),
        ("Nama Bahan Baku", WD_ALIGN_PARAGRAPH.LEFT),
        ("Takaran (per 1 Liter)", WD_ALIGN_PARAGRAPH.CENTER),
        ("Fungsi Bahan", WD_ALIGN_PARAGRAPH.LEFT)
    ]
    for i, (h, align) in enumerate(headers_t2):
        cell = table2.cell(0, i)
        set_cell_width(cell, col_widths_t2[i])
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = align
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Isi Tabel 2
    for r_idx, (no, nama, takaran, fungsi) in enumerate(ingredients, start=1):
        row_data = [
            (no, WD_ALIGN_PARAGRAPH.CENTER, True),
            (nama, WD_ALIGN_PARAGRAPH.LEFT, False),
            (takaran, WD_ALIGN_PARAGRAPH.CENTER, False),
            (fungsi, WD_ALIGN_PARAGRAPH.LEFT, False)
        ]
        for c_idx, (text, align, is_bold) in enumerate(row_data):
            cell = table2.cell(r_idx, c_idx)
            set_cell_width(cell, col_widths_t2[c_idx])
            set_cell_margins(cell, top=50, bottom=50, left=80, right=80)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = align
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9.0)
            run.font.bold = is_bold
            run.font.color.rgb = RGBColor(0, 0, 0)

    # 6. Blok Pengesahan (Bawah Kiri)
    p_date = doc.add_paragraph()
    p_date.paragraph_format.space_before = Pt(14)
    p_date.paragraph_format.space_after = Pt(40)  # Ruang spasi 4 baris untuk cap stempel bulat KCA
    p_date.paragraph_format.line_spacing = 1.15
    p_date.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_dt = p_date.add_run(f"{city}, {check_date}")
    r_dt.font.name = 'Times New Roman'
    r_dt.font.size = Pt(11)
    r_dt.font.color.rgb = RGBColor(0, 0, 0)

    p_pic = doc.add_paragraph()
    p_pic.paragraph_format.space_before = Pt(0)
    p_pic.paragraph_format.space_after = Pt(2)
    p_pic.paragraph_format.line_spacing = 1.15
    p_pic.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_pic = p_pic.add_run(pic_name)
    r_pic.font.name = 'Times New Roman'
    r_pic.font.size = Pt(11)
    r_pic.font.bold = True
    r_pic.font.color.rgb = RGBColor(0, 0, 0)

    p_role = doc.add_paragraph()
    p_role.paragraph_format.space_before = Pt(0)
    p_role.paragraph_format.space_after = Pt(0)
    p_role.paragraph_format.line_spacing = 1.15
    p_role.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_role = p_role.add_run(pic_role)
    r_role.font.name = 'Times New Roman'
    r_role.font.size = Pt(11)
    r_role.font.color.rgb = RGBColor(0, 0, 0)

    # 7. Penyimpanan Dokumen & Sanitasi Metadata KCA
    if output_paths is None:
        output_paths = [
            "/Users/arthur/Documents/Meetings Agent/PKD/SERTIFIKAT_HASIL_UJI_ALBERN_OXY.docx",
            "/Users/arthur/Documents/Meetings Agent/product/PKD/SERTIFIKAT_HASIL_UJI_ALBERN_OXY.docx"
        ]

    for p in output_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        doc.save(p)
        sanitize_docx_metadata(
            p,
            title=f"Sertifikat Hasil Uji Produk Jadi - {product_name}",
            author="Yerikho Arfensias Effendi"
        )
        print(f"SUKSES: Dokumen tersimpan dan disanitasi: {p}")

    return output_paths

if __name__ == "__main__":
    create_qc_certificate(
        product_name="ALBERN OXY",
        check_date="27 September 2026",
        sample_volume="1 Liter",
        specs_dict={
            "bentuk": "Cairan",
            "warna": "Bening Kekuningan",
            "bau": "Khas Klorin Segar",
            "berat": "1,00 - 1,04 kg",
            "ph": "8.5 - 10.5",
            "densitas": "1.01 - 1.04"
        },
        results_dict={
            "bentuk": "Cairan",
            "warna": "Bening Kekuningan",
            "bau": "Khas Klorin Segar",
            "berat": "1,02 kg",
            "ph": "9.6",
            "densitas": "1.02"
        },
        ingredients=[
            ("1", "Calcium Hypochlorite", "50 gram", "Bahan aktif pemutih, oksidator noda & disinfektan"),
            ("2", "Sodium Carbonate", "25 gram", "Builder alkali, penstabil sediaan & pengatur pH basa"),
            ("3", "Air Demineralisasi (Aqua RO)", "925 mL", "Pelarut utama sediaan (solvent)")
        ],
        pic_name="Suparlin",
        pic_role="Penanggung Jawab Teknis",
        city="Kediri"
    )
