#!/usr/bin/env python3
"""
PT KEDIRI CHEMICAL ABADI — QUALITY ASSURANCE & LEGAL PKRT
Modul Otomasi Konversi Dokumen PKRT (Liquid Detergent & Bleach) ke Format Microsoft Word (.docx)
Sesuai Standar ISO 9001:2015 & Regulasi Notifikasi Izin Edar Kemenkes RI

Author / Manager : Yerikho Arfensias Effendi
Direktur Utama  : Yan Effendi
Company         : PT Kediri Chemical Abadi
"""

import os
import sys
import shutil
import subprocess
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

# Import modul sanitasi metadata KCA
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
if not os.path.exists(LOGO_PATH):
    LOGO_PATH = "/Users/arthur/Documents/Meetings Agent/extracted_media/word/media/image1.png"

FLOWCHART_LD_PATH = "/Users/arthur/Documents/Meetings Agent/flowchart_diagram_clean_hd.png"
FLOWCHART_BLEACH_PATH = "/Users/arthur/Documents/Meetings Agent/flowchart_bleach_clean_hd.png"

NAVY_BLUE = "0E2A47"
LIGHT_GRAY = "F5F5F5"
BORDER_GRAY = "CCCCCC"


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


def set_cell_background(cell, hex_color):
    """Set warna background sel tabel"""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def add_kca_kop_surat(doc):
    """Menambahkan Kop Surat Resmi PT Kediri Chemical Abadi dengan logo & border"""
    kop_tbl = doc.add_table(rows=1, cols=2)
    kop_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    kop_tbl.autofit = False

    cell_logo = kop_tbl.cell(0, 0)
    cell_info = kop_tbl.cell(0, 1)

    cell_logo.width = Inches(1.2)
    cell_info.width = Inches(5.47)

    set_cell_margins(cell_logo, top=0, bottom=0, left=0, right=30)
    set_cell_margins(cell_info, top=0, bottom=0, left=30, right=0)
    for c in (cell_logo, cell_info):
        set_cell_border(c, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')

    p_logo = cell_logo.paragraphs[0]
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(0)
    p_logo.paragraph_format.space_after = Pt(0)
    if os.path.exists(LOGO_PATH):
        r_logo = p_logo.add_run()
        r_logo.add_picture(LOGO_PATH, width=Inches(1.1))

    p_info = cell_info.paragraphs[0]
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_info.paragraph_format.space_before = Pt(0)
    p_info.paragraph_format.space_after = Pt(0)
    p_info.paragraph_format.line_spacing = 1.1

    r_comp = p_info.add_run("PT KEDIRI CHEMICAL ABADI\n")
    r_comp.font.name = 'Times New Roman'
    r_comp.font.size = Pt(15)
    r_comp.font.bold = True
    r_comp.font.color.rgb = RGBColor(180, 20, 20)  # Merah KCA #B41414

    r_addr = p_info.add_run("Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161\n")
    r_addr.font.name = 'Times New Roman'
    r_addr.font.size = Pt(9)
    r_addr.font.color.rgb = RGBColor(80, 80, 80)

    r_contact = p_info.add_run("Email : kdrchemicals@gmail.com, telepon : 082244006699")
    r_contact.font.name = 'Times New Roman'
    r_contact.font.size = Pt(9)
    r_contact.font.color.rgb = RGBColor(0, 102, 204)

    # Garis Pembatas Horizontal Hitam Tebal di bawah Kop
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_before = Pt(3)
    p_line.paragraph_format.space_after = Pt(8)
    pPr = p_line._p.get_or_add_pPr()
    pBdr = parse_xml(
        r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        r'<w:bottom w:val="single" w:sz="18" w:space="1" w:color="000000"/>'
        r'</w:pBdr>'
    )
    pPr.append(pBdr)


def add_signatures(doc, space_above=6, sig_height=200):
    """Menambahkan Lembar Pengesahan Standar ISO 9001 (2 Kolom)"""
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(space_above)
    p_space.paragraph_format.space_after = Pt(2)

    sig_tbl = doc.add_table(rows=4, cols=2)
    sig_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_tbl.autofit = False

    sig_tbl.columns[0].width = Inches(3.33)
    sig_tbl.columns[1].width = Inches(3.34)

    labels = ["Dibuat / Disiapkan Oleh :", "Disetujui / Disahkan Oleh :"]
    roles = ["General Manager / Finance & Ops", "Direktur Utama"]
    names = ["Yerikho Arfensias Effendi", "Yan Effendi"]

    # Row 0: Labels
    for col_idx in range(2):
        cell = sig_tbl.cell(0, col_idx)
        set_cell_margins(cell, top=30, bottom=20, left=60, right=60)
        set_cell_border(cell, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(labels[col_idx])
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Row 1: Space for Signature
    for col_idx in range(2):
        cell = sig_tbl.cell(1, col_idx)
        set_cell_margins(cell, top=sig_height, bottom=sig_height, left=60, right=60)
        set_cell_border(cell, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("\n")

    # Row 2: Names (Underlined & Bold)
    for col_idx in range(2):
        cell = sig_tbl.cell(2, col_idx)
        set_cell_margins(cell, top=20, bottom=10, left=60, right=60)
        set_cell_border(cell, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(names[col_idx])
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.underline = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Row 3: Roles
    for col_idx in range(2):
        cell = sig_tbl.cell(3, col_idx)
        set_cell_margins(cell, top=10, bottom=20, left=60, right=60)
        set_cell_border(cell, top='none', bottom='none', left='none', right='none', insideH='none', insideV='none')
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(roles[col_idx])
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(60, 60, 60)


def configure_page_setup(doc, top=0.55, bottom=0.55, left=0.75, right=0.75):
    """Mengatur ukuran kertas A4 dan margin standar ISO 9001"""
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(top)
        section.bottom_margin = Inches(bottom)
        section.left_margin = Inches(left)
        section.right_margin = Inches(right)

    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(10.5)
    font.color.rgb = RGBColor(0, 0, 0)


# ==============================================================================
# 1. DOKUMEN PROSES PRODUKSI LIQUID DETERGENT (1 HALAMAN PERSIS FLOWCHART)
# ==============================================================================
def generate_proses_produksi_flowchart_only(output_path):
    doc = Document()
    configure_page_setup(doc, top=0.5, bottom=0.5, left=0.7, right=0.7)

    add_kca_kop_surat(doc)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("Proses Produksi KEDIRI CHEMICAL ABADI Liquid Detergent")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    # Embed High-Resolution Flowchart Diagram
    if os.path.exists(FLOWCHART_LD_PATH):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(0)
        r_img = p_img.add_run()
        r_img.add_picture(FLOWCHART_LD_PATH, width=Inches(5.6))

    doc.save(output_path)
    sanitize_docx_metadata(output_path, title="Proses Produksi Liquid Detergent - PT KCA")
    print(f"Generated: {output_path}")


# ==============================================================================
# 1B. DOKUMEN PROSES PRODUKSI LIQUID DETERGENT (FLOWCHART + TABEL ISO 9001 - 2 HALAMAN)
# ==============================================================================
def generate_proses_produksi_liquid_detergent(output_path):
    doc = Document()
    configure_page_setup(doc, top=0.5, bottom=0.5, left=0.7, right=0.7)

    # PAGE 1: KOP SURAT + DIAGRAM FLOWCHART EXACT MATCH
    add_kca_kop_surat(doc)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("Proses Produksi KEDIRI CHEMICAL ABADI Liquid Detergent")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    # Embed High-Resolution Flowchart Diagram
    if os.path.exists(FLOWCHART_LD_PATH):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(0)
        r_img = p_img.add_run()
        r_img.add_picture(FLOWCHART_LD_PATH, width=Inches(5.6))

    # PAGE 2: TABEL RINCIAN ALUR PROSES & CONTROL PARAMETER (PAS 1 HALAMAN DI HALAMAN 2)
    doc.add_page_break()
    add_kca_kop_surat(doc)

    p_title2 = doc.add_paragraph()
    p_title2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title2.paragraph_format.space_before = Pt(1)
    p_title2.paragraph_format.space_after = Pt(5)
    r_title2 = p_title2.add_run("Tabel Uraian Alur Proses Produksi & Kontrol Mutu (QC)\nKEDIRI CHEMICAL ABADI Liquid Detergent")
    r_title2.font.name = 'Times New Roman'
    r_title2.font.size = Pt(11)
    r_title2.font.bold = True
    r_title2.font.color.rgb = RGBColor(0, 0, 0)

    tbl = doc.add_table(rows=1, cols=4)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    col_widths = [Inches(1.1), Inches(2.9), Inches(2.17), Inches(0.7)]
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = w

    headers = ["Tahapan", "Uraian Proses Produksi", "Pemeriksaan / Kriteria Mutu", "Status"]
    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], NAVY_BLUE)
        set_cell_margins(hdr_cells[i], top=50, bottom=50, left=60, right=60)
        set_cell_border(hdr_cells[i],
                        top=dict(val='single', sz=6, color='0E2A47'),
                        bottom=dict(val='single', sz=6, color='0E2A47'),
                        left=dict(val='single', sz=4, color='FFFFFF'),
                        right=dict(val='single', sz=4, color='FFFFFF'))
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data = [
        ("MULAI", "Persiapan awal lini produksi deterjen cair dan sanitasi area kerja.", "Kesiapan ruang produksi & operator", "OK"),
        ("Persiapan Alat", "Persiapan alat produksi (tangki mixer HDPE / SS316, timbangan digital analitis, pengaduk mekanis) dan wadah kemasan (botol/jerigen HDPE yang bersih dan kering).", "Sanitasi alat & ruang produksi higienis, bebas kontaminan", "OK"),
        ("Persiapan Bahan", "Penimbangan bahan baku sesuai formulasi standar (SLS 10,95%, CBS-X 0,05%, NaCl 4%, Citric Acid 6%, Parfume 3%, Aqua 76%).", "Pemeriksaan label, segel, dan Certificate of Analysis (CoA)", "OK"),
        ("Pemeriksaan Bahan Baku & Kemasan", "Verifikasi mutu fisik bahan baku (kejernihan, bau, bentuk fisik) serta inspeksi visual kemasan (kebocoran, kecacatan botol/tutup).", "Jika NO -> Sortir / koreksi ulang\nJika YES -> Lanjut ke tahap pencampuran", "YES (Lanjut)"),
        ("Pencampuran Fasa Aktif & Builder", "Masukkan Sodium Lauryl Sulfate, Disodium 4,4'-bis(2-sulfostyryl)biphenyl, Sodium Chloride, dan Citric Acid sesuai kadar formula ke dalam tangki, aduk merata.", "Bahan aktif & pembangun deterjen terdispersi merata", "OK"),
        ("Pelarutan Fasa Cair & Aroma", "Masukkan air baku (Aqua) dan fragrance ke dalam tangki, lalu aduk perlahan sampai seluruh bahan larut sempurna, jernih, dan merata.", "Larutan homogen merata, bebas gumpalan, aroma menyatu", "OK"),
        ("Pemeriksaan Produk Jadi (QC)", "Pengujian mutu fisik dan kimiawi produk ruahan (bulk) oleh QC: homogenitas cairan, pH (6.0 - 8.0), kestabilan busa, dan aroma menyegarkan.", "Jika NO -> Penyesuaian formulasi fasa\nJika YES -> Lanjut proses pengemasan", "YES (Lulus)"),
        ("Pengemasan (Filling)", "Masukkan produk jadi yang telah dinyatakan lolos uji QC ke dalam wadah kemasan primer (botol 0.5L/1L, jerigen 1L/5L/20L, pail 10L, drum) berlabel resmi.", "Volume presisi, segel rapat, label rapi & simetris", "OK"),
        ("Penyimpanan", "Penyimpanan produk di gudang barang jadi pada suhu ruang sejuk (20–30°C), kering, berventilasi baik, terhindar dari paparan sinar matahari langsung.", "Penataan rapi sistem FIFO & batch tertelusur", "OK"),
        ("SELESAI", "Produk KEDIRI CHEMICAL ABADI Liquid Detergent siap didistribusikan ke pasar ritel, komersial, maupun laundry.", "Izin Edar KEMENKES RI PKD 20202520514", "SELESAI")
    ]

    for row_idx, (tahap, uraian, qc, status) in enumerate(data):
        row = tbl.add_row()
        bg = LIGHT_GRAY if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate([tahap, uraian, qc, status]):
            cell = row.cells[col_idx]
            cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=35, bottom=35, left=50, right=50)
            set_cell_border(cell,
                            top=dict(val='single', sz=4, color=BORDER_GRAY),
                            bottom=dict(val='single', sz=4, color=BORDER_GRAY),
                            left=dict(val='single', sz=4, color=BORDER_GRAY),
                            right=dict(val='single', sz=4, color=BORDER_GRAY))
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            if col_idx in (0, 3):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(7.5)
            if col_idx == 0:
                run.font.bold = True
            elif col_idx == 3:
                run.font.bold = True
                if "YES" in text or "OK" in text or "SELESAI" in text:
                    run.font.color.rgb = RGBColor(16, 120, 40)
                else:
                    run.font.color.rgb = RGBColor(180, 20, 20)

    add_signatures(doc, space_above=4, sig_height=120)
    doc.save(output_path)
    sanitize_docx_metadata(output_path, title="Proses Produksi Liquid Detergent - PT KCA")
    print(f"Generated: {output_path}")


# ==============================================================================
# 2. DOKUMEN LIST BAHAN BAKU BLEACH (EXACT MATCH & FORMATTED TABLE)
# ==============================================================================
def generate_list_bahan_baku_bleach(output_path):
    doc = Document()
    configure_page_setup(doc, top=0.55, bottom=0.55, left=0.75, right=0.75)

    add_kca_kop_surat(doc)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(14)
    r_title = p_title.add_run("List Bahan Baku KEDIRI CHEMICAL ABADI BLEACH")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    col_widths = [Inches(2.2), Inches(0.9), Inches(3.67)]
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = w

    headers = ["Nama Bahan", "%", "Fungsi"]
    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], NAVY_BLUE)
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)
        set_cell_border(hdr_cells[i],
                        top=dict(val='single', sz=6, color='0E2A47'),
                        bottom=dict(val='single', sz=6, color='0E2A47'),
                        left=dict(val='single', sz=4, color='FFFFFF'),
                        right=dict(val='single', sz=4, color='FFFFFF'))
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data = [
        ("Calcium Hypochlorite", "4,55%", "Bahan aktif pemutih & disinfektan (sumber klorin aktif)"),
        ("Sodium Carbonate", "4,55%", "Pengatur pH, penstabil larutan, membantu melarutkan kaporit"),
        ("Aqua", "90,90%", "Pelarut / medium reaksi dan pembawa larutan.")
    ]

    for row_idx, (bahan, pct, fungsi) in enumerate(data):
        row = tbl.add_row()
        bg = LIGHT_GRAY if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate([bahan, pct, fungsi]):
            cell = row.cells[col_idx]
            cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            set_cell_border(cell,
                            top=dict(val='single', sz=4, color=BORDER_GRAY),
                            bottom=dict(val='single', sz=4, color=BORDER_GRAY),
                            left=dict(val='single', sz=4, color=BORDER_GRAY),
                            right=dict(val='single', sz=4, color=BORDER_GRAY))
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            if col_idx == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(0, 0, 0)
            if col_idx == 0:
                run.font.bold = True

    # Row Total
    row_total = tbl.add_row()
    for col_idx, text in enumerate(["Total", "100%", ""]):
        cell = row_total.cells[col_idx]
        cell.width = col_widths[col_idx]
        set_cell_background(cell, "EAEAEA")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        set_cell_border(cell,
                        top=dict(val='single', sz=6, color='000000'),
                        bottom=dict(val='single', sz=6, color='000000'),
                        left=dict(val='single', sz=4, color=BORDER_GRAY),
                        right=dict(val='single', sz=4, color=BORDER_GRAY))
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if col_idx in (0, 1):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Catatan Teknis Formulasi
    p_note_title = doc.add_paragraph()
    p_note_title.paragraph_format.space_before = Pt(12)
    p_note_title.paragraph_format.space_after = Pt(3)
    r_nt = p_note_title.add_run("Keterangan Teknis & Spesifikasi Sediaan:")
    r_nt.font.name = 'Times New Roman'
    r_nt.font.size = Pt(10)
    r_nt.font.bold = True
    r_nt.font.color.rgb = RGBColor(0, 0, 0)

    notes = [
        "1. Kategori Produk: Pemutih dan Disinfektan Linen (KEMENKES RI PKD 20204520033).",
        "2. Kadar Klorin Aktif (Available Chlorine): Minimum 2.5% - 3.2% efektif membasmi kuman, bakteri pathogen, dan virus.",
        "3. Nilai pH Sediaan: 10.5 – 11.8 (Alkali stabil untuk menjaga kelarutan dan mencegah pelepasan gas klorin bebas).",
        "4. Seluruh bahan baku memenuhi spesifikasi teknis dan bersertifikat Certificate of Analysis (CoA) resmi pabrikan."
    ]
    for n in notes:
        p_n = doc.add_paragraph()
        p_n.paragraph_format.space_before = Pt(0)
        p_n.paragraph_format.space_after = Pt(2)
        p_n.paragraph_format.line_spacing = 1.15
        r_n = p_n.add_run(n)
        r_n.font.name = 'Times New Roman'
        r_n.font.size = Pt(9)
        r_n.font.color.rgb = RGBColor(40, 40, 40)

    add_signatures(doc, space_above=6, sig_height=180)
    doc.save(output_path)
    sanitize_docx_metadata(output_path, title="List Bahan Baku Bleach - PT KCA")
    print(f"Generated: {output_path}")


# ==============================================================================
# 3. DOKUMEN DESKRIPSI, PENGGUNAAN & PERINGATAN LIQUID DETERGENT (EXACT 1 HALAMAN)
# ==============================================================================
def generate_deskripsi_liquid_detergent(output_path):
    doc = Document()
    configure_page_setup(doc, top=0.45, bottom=0.45, left=0.75, right=0.75)

    add_kca_kop_surat(doc)

    # Judul Dokumen
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(6)
    r_title1 = p_title.add_run("KEDIRI CHEMICAL ABADI\n")
    r_title1.font.name = 'Times New Roman'
    r_title1.font.size = Pt(12)
    r_title1.font.bold = True
    r_title1.font.color.rgb = RGBColor(0, 0, 0)
    r_title2 = p_title.add_run("Liquid Detergent")
    r_title2.font.name = 'Times New Roman'
    r_title2.font.size = Pt(11)
    r_title2.font.bold = True
    r_title2.font.color.rgb = RGBColor(0, 0, 0)

    # Section 1: Deskripsi Produk
    p_desc_head = doc.add_paragraph()
    p_desc_head.paragraph_format.space_before = Pt(2)
    p_desc_head.paragraph_format.space_after = Pt(1)
    r_dh = p_desc_head.add_run("Deskripsi Produk :")
    r_dh.font.name = 'Times New Roman'
    r_dh.font.size = Pt(9.5)
    r_dh.font.bold = True
    r_dh.font.underline = True
    r_dh.font.color.rgb = RGBColor(0, 0, 0)

    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.space_before = Pt(0)
    p_desc.paragraph_format.space_after = Pt(3)
    p_desc.paragraph_format.line_spacing = 1.05
    p_desc.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_desc = p_desc.add_run(
        "KEDIRI CHEMICAL ABADI Liquid Detergent adalah produk yang diformulasikan untuk "
        "membersihkan noda - noda yang menempel di pakaian secara maksimal, seperti noda kecap, minyak, "
        "dan oli. Dengan tambahan aroma parfum yang menyegarkan."
    )
    r_desc.font.name = 'Times New Roman'
    r_desc.font.size = Pt(9)
    r_desc.font.color.rgb = RGBColor(0, 0, 0)

    # Section 2: Cara Penggunaan
    p_use_head = doc.add_paragraph()
    p_use_head.paragraph_format.space_before = Pt(2)
    p_use_head.paragraph_format.space_after = Pt(1)
    r_uh = p_use_head.add_run("Cara Penggunaan :")
    r_uh.font.name = 'Times New Roman'
    r_uh.font.size = Pt(9.5)
    r_uh.font.bold = True
    r_uh.font.underline = True
    r_uh.font.color.rgb = RGBColor(0, 0, 0)

    # Sub-section: Mesin Cuci
    p_mc = doc.add_paragraph()
    p_mc.paragraph_format.space_before = Pt(1)
    p_mc.paragraph_format.space_after = Pt(1)
    r_mc = p_mc.add_run("Untuk Mesin Cuci (Beban Depan / Beban Atas):")
    r_mc.font.name = 'Times New Roman'
    r_mc.font.size = Pt(9)
    r_mc.font.bold = True
    r_mc.font.color.rgb = RGBColor(0, 0, 0)

    mc_steps = [
        "1. Sortir cucian Anda berdasarkan warna dan jenis kain.",
        "2. Periksa label perawatan pada pakaian untuk petunjuk pencucian yang spesifik.",
        "3. Dosis (per beban reguler, ~6-7 kg):",
        "    ► Noda normal: 35 ml   |   ► Noda berat: 50 ml   |   ► Muatan kecil: 25 ml",
        "4. Tuangkan deterjen ke dalam laci deterjen atau langsung ke dalam drum, sesuai petunjuk mesin.",
        "5. Pilih siklus pencucian berdasarkan jenis kain dan tingkat kekotoran.",
        "6. Nyalakan mesin dan biarkan menyelesaikan siklusnya."
    ]
    for s in mc_steps:
        p_s = doc.add_paragraph()
        p_s.paragraph_format.space_before = Pt(0)
        p_s.paragraph_format.space_after = Pt(0)
        p_s.paragraph_format.line_spacing = 1.05
        p_s.paragraph_format.left_indent = Inches(0.15)
        r_s = p_s.add_run(s.strip())
        r_s.font.name = 'Times New Roman'
        r_s.font.size = Pt(8.5)
        r_s.font.color.rgb = RGBColor(0, 0, 0)

    # Sub-section: Pakai Tangan
    p_hand = doc.add_paragraph()
    p_hand.paragraph_format.space_before = Pt(2)
    p_hand.paragraph_format.space_after = Pt(1)
    r_hand = p_hand.add_run("Untuk Pakai Tangan:")
    r_hand.font.name = 'Times New Roman'
    r_hand.font.size = Pt(9)
    r_hand.font.bold = True
    r_hand.font.color.rgb = RGBColor(0, 0, 0)

    hand_steps = [
        "1. Isi ember atau baskom dengan 10 liter air.",
        "2. Tambahkan deterjen:   ► Noda normal: 20 ml   |   ► Noda berat: 30 ml",
        "3. Aduk air hingga tercampur rata dan berbusa.",
        "4. Rendam pakaian selama 15-30 menit.",
        "5. Gosok perlahan bagian yang terkena noda atau kotoran.",
        "6. Bilas sampai bersih dengan air bersih 2-3 kali.",
        "7. Keringkan pakaian seperti biasa."
    ]
    for s in hand_steps:
        p_s = doc.add_paragraph()
        p_s.paragraph_format.space_before = Pt(0)
        p_s.paragraph_format.space_after = Pt(0)
        p_s.paragraph_format.line_spacing = 1.05
        p_s.paragraph_format.left_indent = Inches(0.15)
        r_s = p_s.add_run(s.strip())
        r_s.font.name = 'Times New Roman'
        r_s.font.size = Pt(8.5)
        r_s.font.color.rgb = RGBColor(0, 0, 0)

    # Section 3: Peringatan
    p_warn_head = doc.add_paragraph()
    p_warn_head.paragraph_format.space_before = Pt(2)
    p_warn_head.paragraph_format.space_after = Pt(1)
    r_wh = p_warn_head.add_run("Peringatan :")
    r_wh.font.name = 'Times New Roman'
    r_wh.font.size = Pt(9.5)
    r_wh.font.bold = True
    r_wh.font.underline = True
    r_wh.font.color.rgb = RGBColor(0, 0, 0)

    warnings = [
        "1. Jauhkan dari jangkauan anak-anak.",
        "2. Hindari kontak langsung dengan mata. Jika terjadi kontak, segera bilas dengan air bersih mengalir.",
        "3. Simpan di tempat sejuk dan kering, terhindar dari paparan sinar matahari langsung.",
        "4. Jangan ditelan. Jika tertelan secara tidak sengaja, segera minum air yang banyak dan dapatkan bantuan medis.",
        "5. Hanya untuk penggunaan luar."
    ]
    for w in warnings:
        p_w = doc.add_paragraph()
        p_w.paragraph_format.space_before = Pt(0)
        p_w.paragraph_format.space_after = Pt(0)
        p_w.paragraph_format.line_spacing = 1.05
        p_w.paragraph_format.left_indent = Inches(0.15)
        r_w = p_w.add_run(w)
        r_w.font.name = 'Times New Roman'
        r_w.font.size = Pt(8.5)
        r_w.font.color.rgb = RGBColor(0, 0, 0)

    add_signatures(doc, space_above=4, sig_height=120)
    doc.save(output_path)
    sanitize_docx_metadata(output_path, title="Deskripsi & Petunjuk Penggunaan Liquid Detergent - PT KCA")
    print(f"Generated: {output_path}")


# ==============================================================================
# 4. MASTER GABUNGAN: LIST BAHAN BAKU & PROSES PRODUKSI LIQUID DETERGENT (2 HALAMAN)
# ==============================================================================
def generate_master_list_bahan_dan_proses_liquid_detergent(output_path):
    doc = Document()
    configure_page_setup(doc, top=0.5, bottom=0.5, left=0.7, right=0.7)

    # HALAMAN 1: LIST BAHAN BAKU
    add_kca_kop_surat(doc)

    p_title1 = doc.add_paragraph()
    p_title1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title1.paragraph_format.space_before = Pt(4)
    p_title1.paragraph_format.space_after = Pt(12)
    r_title1 = p_title1.add_run("List Bahan Baku KEDIRI CHEMICAL ABADI Liquid Detergent")
    r_title1.font.name = 'Times New Roman'
    r_title1.font.size = Pt(13)
    r_title1.font.bold = True
    r_title1.font.color.rgb = RGBColor(0, 0, 0)

    tbl1 = doc.add_table(rows=1, cols=3)
    tbl1.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl1.autofit = False

    col_widths = [Inches(2.3), Inches(0.85), Inches(3.72)]
    for i, w in enumerate(col_widths):
        tbl1.columns[i].width = w

    headers = ["Nama Bahan", "%", "Fungsi"]
    hdr_cells = tbl1.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], NAVY_BLUE)
        set_cell_margins(hdr_cells[i], top=90, bottom=90, left=100, right=100)
        set_cell_border(hdr_cells[i],
                         top=dict(val='single', sz=6, color='0E2A47'),
                         bottom=dict(val='single', sz=6, color='0E2A47'),
                         left=dict(val='single', sz=4, color='FFFFFF'),
                         right=dict(val='single', sz=4, color='FFFFFF'))
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_bb = [
        ("Sodium Lauryl Sulfate (SLS)", "10,95%", "Sebagai surfaktan pembersih kotoran, lemak, dan pembusa aktif melimpah."),
        ("Disodium 4,4'-bis(2-sulfostyryl)biphenyl (CBS-X)", "0,05%", "Sebagai optical brightener agent yang mencerahkan serat kain pakaian tanpa phosphate."),
        ("Sodium Chloride", "4,00%", "Sebagai penstabil, pelarut SLS, dan pengatur viskositas / pengental formula."),
        ("Citric Acid", "6,00%", "Sebagai pengatur pH (buffer) menjaga keasaman optimal produk agar tetap stabil dan efektif."),
        ("Parfume", "3,00%", "Sebagai bahan pewangi segar yang memberikan kesegaran tahan lama pada cucian."),
        ("Air Baku (Aqua)", "76,00%", "Sebagai pelarut utama dan media reaksi seluruh komponen formula.")
    ]

    for row_idx, (bahan, pct, fungsi) in enumerate(data_bb):
        row = tbl1.add_row()
        bg = LIGHT_GRAY if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate([bahan, pct, fungsi]):
            cell = row.cells[col_idx]
            cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
            set_cell_border(cell,
                            top=dict(val='single', sz=4, color=BORDER_GRAY),
                            bottom=dict(val='single', sz=4, color=BORDER_GRAY),
                            left=dict(val='single', sz=4, color=BORDER_GRAY),
                            right=dict(val='single', sz=4, color=BORDER_GRAY))
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            if col_idx == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0, 0, 0)
            if col_idx == 0:
                run.font.bold = True

    # Total Row
    row_total = tbl1.add_row()
    for col_idx, text in enumerate(["Total", "100%", ""]):
        cell = row_total.cells[col_idx]
        cell.width = col_widths[col_idx]
        set_cell_background(cell, "EAEAEA")
        set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
        set_cell_border(cell,
                        top=dict(val='single', sz=6, color='000000'),
                        bottom=dict(val='single', sz=6, color='000000'),
                        left=dict(val='single', sz=4, color=BORDER_GRAY),
                        right=dict(val='single', sz=4, color=BORDER_GRAY))
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if col_idx in (0, 1):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Catatan Teknis Formulasi
    p_note_title = doc.add_paragraph()
    p_note_title.paragraph_format.space_before = Pt(10)
    p_note_title.paragraph_format.space_after = Pt(3)
    r_nt = p_note_title.add_run("Keterangan Teknis & Spesifikasi Sediaan:")
    r_nt.font.name = 'Times New Roman'
    r_nt.font.size = Pt(10)
    r_nt.font.bold = True
    r_nt.font.color.rgb = RGBColor(0, 0, 0)

    notes = [
        "1. Kategori Produk: Sediaan Untuk Mencuci - Deterjen Cair (KEMENKES RI PKD 20202520514).",
        "2. Bentuk Sediaan: Cairan Kental Jernih Transparan, Aroma Floral / Segar Mewah.",
        "3. Nilai pH Sediaan: 6.0 – 8.0 (Netral Lembut, tidak mengiritasi tangan dan menjaga keawetan serat kain).",
        "4. Non-Phosphate Formulation: Ramah lingkungan dan tidak mencemari ekosistem air."
    ]
    for n in notes:
        p_n = doc.add_paragraph()
        p_n.paragraph_format.space_before = Pt(0)
        p_n.paragraph_format.space_after = Pt(1.5)
        p_n.paragraph_format.line_spacing = 1.1
        r_n = p_n.add_run(n)
        r_n.font.name = 'Times New Roman'
        r_n.font.size = Pt(8.5)
        r_n.font.color.rgb = RGBColor(40, 40, 40)

    add_signatures(doc, space_above=6, sig_height=180)

    # HALAMAN 2: PROSES PRODUKSI FLOWCHART
    doc.add_page_break()
    add_kca_kop_surat(doc)

    p_title2 = doc.add_paragraph()
    p_title2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title2.paragraph_format.space_before = Pt(2)
    p_title2.paragraph_format.space_after = Pt(8)
    r_title2 = p_title2.add_run("Proses Produksi KEDIRI CHEMICAL ABADI Liquid Detergent")
    r_title2.font.name = 'Times New Roman'
    r_title2.font.size = Pt(13)
    r_title2.font.bold = True
    r_title2.font.color.rgb = RGBColor(0, 0, 0)

    if os.path.exists(FLOWCHART_LD_PATH):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(0)
        r_img = p_img.add_run()
        r_img.add_picture(FLOWCHART_LD_PATH, width=Inches(5.6))

    doc.save(output_path)
    sanitize_docx_metadata(output_path, title="Dokumen List Bahan Baku dan Proses Produksi Liquid Detergent - PT KCA")
    print(f"Generated: {output_path}")


# ==============================================================================
# 5. MASTER GABUNGAN: LIST BAHAN BAKU & PROSES PRODUKSI BLEACH (2 HALAMAN)
# ==============================================================================
def generate_master_list_bahan_dan_proses_bleach(output_path):
    doc = Document()
    configure_page_setup(doc, top=0.5, bottom=0.5, left=0.7, right=0.7)

    # HALAMAN 1: LIST BAHAN BAKU
    add_kca_kop_surat(doc)

    p_title1 = doc.add_paragraph()
    p_title1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title1.paragraph_format.space_before = Pt(4)
    p_title1.paragraph_format.space_after = Pt(12)
    r_title1 = p_title1.add_run("List Bahan Baku KEDIRI CHEMICAL ABADI BLEACH")
    r_title1.font.name = 'Times New Roman'
    r_title1.font.size = Pt(13)
    r_title1.font.bold = True
    r_title1.font.color.rgb = RGBColor(0, 0, 0)

    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    col_widths = [Inches(2.2), Inches(0.9), Inches(3.77)]
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = w

    headers = ["Nama Bahan", "%", "Fungsi"]
    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], NAVY_BLUE)
        set_cell_margins(hdr_cells[i], top=90, bottom=90, left=100, right=100)
        set_cell_border(hdr_cells[i],
                        top=dict(val='single', sz=6, color='0E2A47'),
                        bottom=dict(val='single', sz=6, color='0E2A47'),
                        left=dict(val='single', sz=4, color='FFFFFF'),
                        right=dict(val='single', sz=4, color='FFFFFF'))
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data = [
        ("Calcium Hypochlorite", "4,55%", "Bahan aktif pemutih & disinfektan (sumber klorin aktif)"),
        ("Sodium Carbonate", "4,55%", "Pengatur pH, penstabil larutan, membantu melarutkan kaporit"),
        ("Aqua", "90,90%", "Pelarut / medium reaksi dan pembawa larutan.")
    ]

    for row_idx, (bahan, pct, fungsi) in enumerate(data):
        row = tbl.add_row()
        bg = LIGHT_GRAY if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate([bahan, pct, fungsi]):
            cell = row.cells[col_idx]
            cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
            set_cell_border(cell,
                            top=dict(val='single', sz=4, color=BORDER_GRAY),
                            bottom=dict(val='single', sz=4, color=BORDER_GRAY),
                            left=dict(val='single', sz=4, color=BORDER_GRAY),
                            right=dict(val='single', sz=4, color=BORDER_GRAY))
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            if col_idx == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(0, 0, 0)
            if col_idx == 0:
                run.font.bold = True

    # Row Total
    row_total = tbl.add_row()
    for col_idx, text in enumerate(["Total", "100%", ""]):
        cell = row_total.cells[col_idx]
        cell.width = col_widths[col_idx]
        set_cell_background(cell, "EAEAEA")
        set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
        set_cell_border(cell,
                        top=dict(val='single', sz=6, color='000000'),
                        bottom=dict(val='single', sz=6, color='000000'),
                        left=dict(val='single', sz=4, color=BORDER_GRAY),
                        right=dict(val='single', sz=4, color=BORDER_GRAY))
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if col_idx in (0, 1):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Catatan Teknis Formulasi
    p_note_title = doc.add_paragraph()
    p_note_title.paragraph_format.space_before = Pt(10)
    p_note_title.paragraph_format.space_after = Pt(3)
    r_nt = p_note_title.add_run("Keterangan Teknis & Spesifikasi Sediaan:")
    r_nt.font.name = 'Times New Roman'
    r_nt.font.size = Pt(10)
    r_nt.font.bold = True
    r_nt.font.color.rgb = RGBColor(0, 0, 0)

    notes = [
        "1. Kategori Produk: Pemutih dan Disinfektan Linen (KEMENKES RI PKD 20204520033).",
        "2. Kadar Klorin Aktif (Available Chlorine): Minimum 2.5% - 3.2% efektif membasmi kuman, bakteri pathogen, dan virus.",
        "3. Nilai pH Sediaan: 10.5 – 11.8 (Alkali stabil untuk menjaga kelarutan dan mencegah pelepasan gas klorin bebas).",
        "4. Seluruh bahan baku memenuhi spesifikasi teknis dan bersertifikat Certificate of Analysis (CoA) resmi pabrikan."
    ]
    for n in notes:
        p_n = doc.add_paragraph()
        p_n.paragraph_format.space_before = Pt(0)
        p_n.paragraph_format.space_after = Pt(1.5)
        p_n.paragraph_format.line_spacing = 1.1
        r_n = p_n.add_run(n)
        r_n.font.name = 'Times New Roman'
        r_n.font.size = Pt(8.5)
        r_n.font.color.rgb = RGBColor(40, 40, 40)

    add_signatures(doc, space_above=6, sig_height=180)

    # HALAMAN 2: PROSES PRODUKSI FLOWCHART
    doc.add_page_break()
    add_kca_kop_surat(doc)

    p_title2 = doc.add_paragraph()
    p_title2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title2.paragraph_format.space_before = Pt(2)
    p_title2.paragraph_format.space_after = Pt(8)
    r_title2 = p_title2.add_run("Proses Produksi KEDIRI CHEMICAL ABADI Bleach")
    r_title2.font.name = 'Times New Roman'
    r_title2.font.size = Pt(13)
    r_title2.font.bold = True
    r_title2.font.color.rgb = RGBColor(0, 0, 0)

    if os.path.exists(FLOWCHART_BLEACH_PATH):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(0)
        p_img.paragraph_format.space_after = Pt(0)
        r_img = p_img.add_run()
        r_img.add_picture(FLOWCHART_BLEACH_PATH, width=Inches(5.6))

    doc.save(output_path)
    sanitize_docx_metadata(output_path, title="Dokumen List Bahan Baku dan Proses Produksi Bleach - PT KCA")
    print(f"Generated: {output_path}")


def convert_to_pdf(docx_path):
    """Konversi docx ke pdf menggunakan LibreOffice headless"""
    try:
        cmd = [
            "/opt/homebrew/bin/soffice",
            "--headless",
            "--convert-to", "pdf",
            docx_path,
            "--outdir", os.path.dirname(docx_path)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
        if os.path.exists(pdf_path):
            print(f"Converted to PDF: {pdf_path}")
            return pdf_path
    except Exception as e:
        print(f"PDF conversion error for {docx_path}: {e}")
    return None


def main():
    base_dir = "/Users/arthur/Documents/Meetings Agent"
    pkd_dir = os.path.join(base_dir, "PKD")
    ld_dir = os.path.join(pkd_dir, "LIQUID DETERGENT")
    bleach_dir = os.path.join(pkd_dir, "BLEACH")

    for d in [pkd_dir, ld_dir, bleach_dir]:
        os.makedirs(d, exist_ok=True)

    # 1. Dokumen Persis Halaman 1 (Flowchart 1 Hal Standalone)
    fc_only_path = os.path.join(ld_dir, "DOKUMEN_PROSES_PRODUKSI_LIQUID_DETERGENT.docx")
    generate_proses_produksi_flowchart_only(fc_only_path)
    convert_to_pdf(fc_only_path)

    # 1B. Dokumen Proses Produksi Lengkap dengan Tabel QC (2 Hal)
    p1_full_path = os.path.join(ld_dir, "DOKUMEN_PROSES_PRODUKSI_DAN_KONTROL_MUTU_LIQUID_DETERGENT.docx")
    generate_proses_produksi_liquid_detergent(p1_full_path)
    convert_to_pdf(p1_full_path)

    # 2. Dokumen Persis Halaman 2: List Bahan Baku Bleach (1 Hal)
    p2_path = os.path.join(bleach_dir, "DOKUMEN_LIST_BAHAN_BAKU_BLEACH.docx")
    generate_list_bahan_baku_bleach(p2_path)
    convert_to_pdf(p2_path)

    # 3. Dokumen Persis Halaman 3: Deskripsi, Penggunaan, dan Peringatan Liquid Detergent (1 Hal)
    p3_path = os.path.join(ld_dir, "DOKUMEN_DESKRIPSI_PENGGUNAAN_DAN_PERINGATAN_LIQUID_DETERGENT.docx")
    generate_deskripsi_liquid_detergent(p3_path)
    convert_to_pdf(p3_path)

    # 4. Master Gabungan Paket Standar Kemenkes PKRT:
    # Liquid Detergent Master (2 Hal: List Bahan Baku + Proses Produksi)
    master_ld = os.path.join(ld_dir, "DOKUMEN_LIST_BAHAN_BAKU_DAN_PROSES_PRODUKSI_LIQUID_DETERGENT.docx")
    generate_master_list_bahan_dan_proses_liquid_detergent(master_ld)
    convert_to_pdf(master_ld)

    # Bleach Master (2 Hal: List Bahan Baku + Proses Produksi)
    master_bleach = os.path.join(bleach_dir, "DOKUMEN_LIST_BAHAN_BAKU_DAN_PROSES_PRODUKSI_BLEACH.docx")
    generate_master_list_bahan_dan_proses_bleach(master_bleach)
    convert_to_pdf(master_bleach)

    # Copy dokumen utama ke root PKD dan root Meetings Agent agar mudah diakses
    all_docs = [
        (fc_only_path, "DOKUMEN_PROSES_PRODUKSI_LIQUID_DETERGENT.docx"),
        (p1_full_path, "DOKUMEN_PROSES_PRODUKSI_DAN_KONTROL_MUTU_LIQUID_DETERGENT.docx"),
        (p2_path, "DOKUMEN_LIST_BAHAN_BAKU_BLEACH.docx"),
        (p3_path, "DOKUMEN_DESKRIPSI_PENGGUNAAN_DAN_PERINGATAN_LIQUID_DETERGENT.docx"),
        (master_ld, "DOKUMEN_LIST_BAHAN_BAKU_DAN_PROSES_PRODUKSI_LIQUID_DETERGENT.docx"),
        (master_bleach, "DOKUMEN_LIST_BAHAN_BAKU_DAN_PROSES_PRODUKSI_BLEACH.docx")
    ]

    for src_docx, name in all_docs:
        src_pdf = os.path.splitext(src_docx)[0] + ".pdf"
        
        # Ke PKD/
        shutil.copy2(src_docx, os.path.join(pkd_dir, name))
        if os.path.exists(src_pdf):
            shutil.copy2(src_pdf, os.path.join(pkd_dir, os.path.splitext(name)[0] + ".pdf"))
            
        # Ke root Meetings Agent/
        shutil.copy2(src_docx, os.path.join(base_dir, name))
        if os.path.exists(src_pdf):
            shutil.copy2(src_pdf, os.path.join(base_dir, os.path.splitext(name)[0] + ".pdf"))

    print("\n✅ Seluruh dokumen berhasil diperbarui, disanitasi metadata, dan dikonversi ke PDF!")


if __name__ == "__main__":
    main()
