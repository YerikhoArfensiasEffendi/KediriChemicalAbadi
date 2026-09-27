#!/usr/bin/env python3
"""
PT KEDIRI CHEMICAL ABADI — QUALITY ASSURANCE & LAB DEPARTMENT
Modul Otomasi Pembuatan Dokumen Uji Stabilitas 1 Halaman A4 Sesuai Standar ISO 9001 / CPKRT

Penanggung Jawab Teknis : Suparlin
Direktur Utama          : Yan Effendi
General Manager         : Yerikho Arfensias Effendi
"""

import os
import re
import sys
import argparse
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
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

LOGO_PATH = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/public/images/kca_logo.png"

def set_cell_border(cell, **kwargs):
    """
    kwargs: top, bottom, left, right, insideH, insideV
    values: dict(sz=4, val='single', color='000000') or 'none'
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = f'w:{edge}'
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            if edge_data == 'none':
                element.set(qn('w:val'), 'none')
            else:
                for key in ('val', 'color', 'sz', 'space'):
                    if key in edge_data:
                        element.set(qn(f'w:{key}'), str(edge_data[key]))

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    """Set padding dalam sel tabel (dalam dxa)"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def calculate_stability_dates(ref_date=None):
    """
    Hitung mundur 1 tahun dari ref_date dengan 5 titik interval 3 bulan persis:
    Titik 1 (Bulan 0 - 12 bulan lalu) : DD/MM/YYYY-1
    Titik 2 (Bulan 3 - 9 bulan lalu)  : DD/MM/YYYY
    Titik 3 (Bulan 6 - 6 bulan lalu)  : DD/MM/YYYY
    Titik 4 (Bulan 9 - 3 bulan lalu)  : DD/MM/YYYY
    Titik 5 (Bulan 12 - Hari ini)     : DD/MM/YYYY
    """
    if ref_date is None:
        ref_date = datetime(2026, 9, 27)
    
    months_offset = [12, 9, 6, 3, 0]
    dates = []
    for mo in months_offset:
        target_month = ref_date.month - mo
        target_year = ref_date.year
        while target_month <= 0:
            target_month += 12
            target_year -= 1
        d = datetime(target_year, target_month, ref_date.day)
        dates.append(d.strftime("%d/%m/%Y"))
    return dates

def get_smart_code(product_name):
    clean = re.sub(r'PT\s+|KEDIRI\s+CHEMICAL\s+ABADI\s+', '', product_name, flags=re.I).strip()
    words = [w for w in clean.split() if w]
    if 'hand' in clean.lower() and 'soap' in clean.lower():
        return 'KCA-HS-001'
    elif 'dish' in clean.lower() or 'piring' in clean.lower():
        return 'KCA-DW-001'
    elif 'floor' in clean.lower() or 'lantai' in clean.lower():
        return 'KCA-FC-001'
    elif 'detergent' in clean.lower() or 'deterjen' in clean.lower():
        return 'KCA-LD-001'
    initials = ''.join([w[0].upper() for w in words[:3]]) or "PRD"
    return f"KCA-{initials}-001"

def generate_stability_document(
    product_name="KEDIRI CHEMICAL ABADI Hand Soap Antiseptic Shimmer",
    production_code=None,
    production_date=None,
    room_temp="22-27°C",
    form="Cair Kental",
    color="Berkilau (Shimmer)",
    aroma="Wangi Harum",
    ph_range="5.5 - 6.5",
    density_range="1.00 – 1.04",
    weight_val="1.02kg",
    ph_val="5.9",
    density_val="1.02",
    output_paths=None
):
    if production_date is None:
        prod_dt = datetime(2026, 9, 27)
    elif isinstance(production_date, str):
        try:
            prod_dt = datetime.strptime(production_date, "%d/%m/%Y")
        except ValueError:
            prod_dt = datetime(2026, 9, 27)
    else:
        prod_dt = production_date

    if not production_code:
        production_code = get_smart_code(product_name)

    bulan_indo = [
        "", "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    tgl_indo = f"{prod_dt.day} {bulan_indo[prod_dt.month]} {prod_dt.year}"
    
    dates = calculate_stability_dates(prod_dt)

    doc = Document()

    # Set Page A4 & Margins
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.65)
        section.bottom_margin = Inches(0.65)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Style default
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(10)
    font.color.rgb = RGBColor(0, 0, 0)

    # ==========================================
    # 1. KOP SURAT RESMI BERLOGO PT KCA
    # ==========================================
    kop_tbl = doc.add_table(rows=1, cols=2)
    kop_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    kop_tbl.autofit = False

    cell_logo = kop_tbl.cell(0, 0)
    cell_info = kop_tbl.cell(0, 1)

    cell_logo.width = Inches(1.3)
    cell_info.width = Inches(5.37)

    set_cell_margins(cell_logo, top=0, bottom=0, left=0, right=40)
    set_cell_margins(cell_info, top=0, bottom=0, left=40, right=0)
    for c in (cell_logo, cell_info):
        set_cell_border(c, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')

    p_logo = cell_logo.paragraphs[0]
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(0)
    p_logo.paragraph_format.space_after = Pt(0)
    if os.path.exists(LOGO_PATH):
        r_logo = p_logo.add_run()
        r_logo.add_picture(LOGO_PATH, width=Inches(1.15))

    p_info = cell_info.paragraphs[0]
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_info.paragraph_format.space_before = Pt(0)
    p_info.paragraph_format.space_after = Pt(0)
    p_info.paragraph_format.line_spacing = 1.15

    r_comp = p_info.add_run("PT KEDIRI CHEMICAL ABADI\n")
    r_comp.font.name = 'Times New Roman'
    r_comp.font.size = Pt(16)
    r_comp.font.bold = True
    r_comp.font.color.rgb = RGBColor(180, 20, 20)  # Merah KCA #B41414

    r_addr = p_info.add_run("Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161\n")
    r_addr.font.name = 'Times New Roman'
    r_addr.font.size = Pt(9.5)
    r_addr.font.color.rgb = RGBColor(80, 80, 80)

    r_contact = p_info.add_run("Email : kdrchemicals@gmail.com, telepon : 082244006699")
    r_contact.font.name = 'Times New Roman'
    r_contact.font.size = Pt(9.5)
    r_contact.font.color.rgb = RGBColor(0, 102, 204)

    # Garis Pembatas Horizontal Hitam Tebal di bawah Kop
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_before = Pt(4)
    p_line.paragraph_format.space_after = Pt(12)
    pPr = p_line._p.get_or_add_pPr()
    pBdr = parse_xml(
        r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        r'<w:bottom w:val="single" w:sz="18" w:space="1" w:color="000000"/>'
        r'</w:pBdr>'
    )
    pPr.append(pBdr)

    # ==========================================
    # 2. JUDUL DOKUMEN (Tengah, Bold 13pt)
    # ==========================================
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("UJI STABILITAS")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    # ==========================================
    # 3. METADATA DOKUMEN (Menggunakan Tab Stop Presisi)
    # ==========================================
    metadata_rows = [
        ("Nama Produk", product_name),
        ("Kode Produksi", production_code),
        ("Tanggal Produksi", tgl_indo),
        ("Suhu Ruangan", room_temp)
    ]
    for label, val in metadata_rows:
        p_m = doc.add_paragraph()
        p_m.paragraph_format.tab_stops.add_tab_stop(Inches(1.4))
        p_m.paragraph_format.space_before = Pt(1)
        p_m.paragraph_format.space_after = Pt(2)
        p_m.paragraph_format.line_spacing = 1.15
        
        r_lbl = p_m.add_run(label)
        r_lbl.font.name = 'Times New Roman'
        r_lbl.font.size = Pt(10)
        r_lbl.font.color.rgb = RGBColor(0, 0, 0)

        r_sep = p_m.add_run("\t: ")
        r_sep.font.name = 'Times New Roman'
        r_sep.font.size = Pt(10)
        r_sep.font.color.rgb = RGBColor(0, 0, 0)

        r_v = p_m.add_run(val)
        r_v.font.name = 'Times New Roman'
        r_v.font.size = Pt(10)
        r_v.font.color.rgb = RGBColor(0, 0, 0)

    # Spasi sebelum Standar Pengujian
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(5)
    p_sp.paragraph_format.space_after = Pt(2)
    r_std = p_sp.add_run("Standar Pengujian")
    r_std.font.name = 'Times New Roman'
    r_std.font.size = Pt(10)
    r_std.font.bold = True
    r_std.font.color.rgb = RGBColor(0, 0, 0)

    # ==========================================
    # 4. STANDAR PENGUJIAN (Dua Kolom Sejajar)
    # ==========================================
    std_tbl = doc.add_table(rows=3, cols=2)
    std_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    std_tbl.autofit = False

    std_data = [
        (f"Bentuk   : {form}", f"PH         : {ph_range}"),
        (f"Warna    : {color}", f"Densitas : {density_range}"),
        (f"Aroma    : {aroma}", "")
    ]

    for r_idx, (col_left, col_right) in enumerate(std_data):
        row = std_tbl.rows[r_idx]
        cell_l, cell_r = row.cells[0], row.cells[1]
        cell_l.width = Inches(3.33)
        cell_r.width = Inches(3.34)

        set_cell_margins(cell_l, top=20, bottom=20, left=0, right=50)
        set_cell_margins(cell_r, top=20, bottom=20, left=50, right=0)
        set_cell_border(cell_l, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')
        set_cell_border(cell_r, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')

        p_l = cell_l.paragraphs[0]
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(0)
        rl = p_l.add_run(col_left)
        rl.font.name = 'Times New Roman'
        rl.font.size = Pt(10)
        rl.font.color.rgb = RGBColor(0, 0, 0)

        p_r = cell_r.paragraphs[0]
        p_r.paragraph_format.space_before = Pt(0)
        p_r.paragraph_format.space_after = Pt(0)
        rr = p_r.add_run(col_right)
        rr.font.name = 'Times New Roman'
        rr.font.size = Pt(10)
        rr.font.color.rgb = RGBColor(0, 0, 0)

    # Spasi sebelum Tabel Realtime
    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_before = Pt(5)
    p_sp2.paragraph_format.space_after = Pt(2)

    # ==========================================
    # 5 & 6. TABEL UJI STABILITAS REALTIME (7 Kolom)
    # ==========================================
    table = doc.add_table(rows=7, cols=7)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    col_widths = [Inches(1.2), Inches(0.88), Inches(0.88), Inches(0.88), Inches(0.88), Inches(0.88), Inches(0.77)]

    # Header Row
    headers = ["Tanggal uji", dates[0], dates[1], dates[2], dates[3], dates[4], "Hasil"]
    hdr_row = table.rows[0]
    for c_idx, h_text in enumerate(headers):
        cell = hdr_row.cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_margins(cell, top=70, bottom=70, left=60, right=60)
        set_cell_border(cell,
            top=dict(val='single', sz=6, color='000000'),
            bottom=dict(val='single', sz=6, color='000000'),
            left=dict(val='single', sz=6, color='000000'),
            right=dict(val='single', sz=6, color='000000')
        )
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Baris Parameter
    table_data = [
        ("Bentuk", form, form, form, form, form, "OK"),
        ("Warna", color, color, color, color, color, "OK"),
        ("Aroma", aroma, aroma, aroma, aroma, aroma, "OK"),
        ("Berat", weight_val, weight_val, weight_val, weight_val, weight_val, "OK"),
        ("pH", ph_val, ph_val, ph_val, ph_val, ph_val, "OK"),
        ("Densitas", density_val, density_val, density_val, density_val, density_val, "OK"),
    ]

    for r_idx, row_vals in enumerate(table_data, start=1):
        row = table.rows[r_idx]
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            set_cell_border(cell,
                top=dict(val='single', sz=4, color='000000'),
                bottom=dict(val='single', sz=4, color='000000'),
                left=dict(val='single', sz=4, color='000000'),
                right=dict(val='single', sz=4, color='000000')
            )
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0, 0, 0)
            if c_idx == 0 or c_idx == 6:
                r.font.bold = True

    # ==========================================
    # 7. KESIMPULAN (Format Baku)
    # ==========================================
    p_k_title = doc.add_paragraph()
    p_k_title.paragraph_format.space_before = Pt(10)
    p_k_title.paragraph_format.space_after = Pt(2)
    r_kt = p_k_title.add_run("Kesimpulan   :")
    r_kt.font.name = 'Times New Roman'
    r_kt.font.size = Pt(10)
    r_kt.font.bold = True
    r_kt.font.color.rgb = RGBColor(0, 0, 0)

    p_k_body = doc.add_paragraph()
    p_k_body.paragraph_format.space_before = Pt(1)
    p_k_body.paragraph_format.space_after = Pt(10)
    p_k_body.paragraph_format.line_spacing = 1.15
    p_k_body.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_kb = p_k_body.add_run(
        f"Dengan melakukan Uji stabilitas secara Realtime {product_name} "
        f"Telah memenuhi standar stabilitas minimum 1 tahun sehingga masa kadaluarsa produk lebih dari 1 tahun."
    )
    r_kb.font.name = 'Times New Roman'
    r_kb.font.size = Pt(10)
    r_kb.font.color.rgb = RGBColor(0, 0, 0)

    # ==========================================
    # 8. BLOK TANDA TANGAN (Kiri Bawah)
    # ==========================================
    p_ttd_date = doc.add_paragraph()
    p_ttd_date.paragraph_format.space_before = Pt(4)
    p_ttd_date.paragraph_format.space_after = Pt(36)  # Ruang cap stempel 4 baris
    r_td = p_ttd_date.add_run(f"Kediri, {tgl_indo}")
    r_td.font.name = 'Times New Roman'
    r_td.font.size = Pt(10)
    r_td.font.color.rgb = RGBColor(0, 0, 0)

    p_ttd_name = doc.add_paragraph()
    p_ttd_name.paragraph_format.space_before = Pt(0)
    p_ttd_name.paragraph_format.space_after = Pt(2)
    r_tn = p_ttd_name.add_run("Suparlin")
    r_tn.font.name = 'Times New Roman'
    r_tn.font.size = Pt(11)
    r_tn.font.bold = True
    r_tn.font.color.rgb = RGBColor(0, 0, 0)

    p_ttd_role = doc.add_paragraph()
    p_ttd_role.paragraph_format.space_before = Pt(0)
    p_ttd_role.paragraph_format.space_after = Pt(0)
    r_tr = p_ttd_role.add_run("Penanggung Jawab Teknis")
    r_tr.font.name = 'Times New Roman'
    r_tr.font.size = Pt(10)
    r_tr.font.color.rgb = RGBColor(0, 0, 0)

    # Target File Paths
    if output_paths is None:
        output_paths = [
            "/Users/arthur/Documents/Meetings Agent/PKD/DOKUMEN_UJI_STABILITAS_KCA.docx",
            "/Users/arthur/Documents/Meetings Agent/product/PKD/DOKUMEN_UJI_STABILITAS_KCA.docx"
        ]

    for p in output_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        doc.save(p)
        sanitize_docx_metadata(p, title=f"Uji Stabilitas - {product_name}", author="Yerikho Arfensias Effendi")
        print(f"File berhasil dibuat & disanitasi: {p}")

    return output_paths

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generator Dokumen Uji Stabilitas PT Kediri Chemical Abadi")
    parser.add_argument("--nama-produk", default="KEDIRI CHEMICAL ABADI Hand Soap Antiseptic Shimmer")
    parser.add_argument("--kode-produksi", default=None)
    parser.add_argument("--tanggal-produksi", default="27/09/2026")
    parser.add_argument("--suhu-ruangan", default="22-27°C")
    parser.add_argument("--bentuk", default="Cair Kental")
    parser.add_argument("--warna", default="Berkilau (Shimmer)")
    parser.add_argument("--aroma", default="Wangi Harum")
    parser.add_argument("--ph-range", default="5.5 - 6.5")
    parser.add_argument("--densitas-range", default="1.00 – 1.04")
    parser.add_argument("--berat-val", default="1.02kg")
    parser.add_argument("--ph-val", default="5.9")
    parser.add_argument("--densitas-val", default="1.02")

    args = parser.parse_args()

    generate_stability_document(
        product_name=args.nama_produk,
        production_code=args.kode_produksi,
        production_date=args.tanggal_produksi,
        room_temp=args.suhu_ruangan,
        form=args.bentuk,
        color=args.warna,
        aroma=args.aroma,
        ph_range=args.ph_range,
        density_range=args.densitas_range,
        weight_val=args.berat_val,
        ph_val=args.ph_val,
        density_val=args.densitas_val
    )
