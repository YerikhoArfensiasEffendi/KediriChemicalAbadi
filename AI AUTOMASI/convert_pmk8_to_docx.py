import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from kca_doc_humanizer import sanitize_docx_metadata

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def add_header_lampiran(doc, page_num_str=""):
    # Header Lampiran Kanan Atas
    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_top.paragraph_format.space_after = Pt(2)
    p_top.paragraph_format.line_spacing = 1.0
    r_top = p_top.add_run(
        "LAMPIRAN I\n"
        "PERATURAN MENTERI KEUANGAN REPUBLIK INDONESIA\n"
        "NOMOR   8/PMK.03/2013\n"
        "TENTANG\n"
        "TATA CARA PENGURANGAN ATAU PENGHAPUSAN SANKSI ADMINISTRASI "
        "DAN PENGURANGAN ATAU PEMBATALAN SURAT KETETAPAN PAJAK ATAU SURAT TAGIHAN PAJAK\n"
    )
    r_top.font.name = "Arial"
    r_top.font.size = Pt(8)
    r_top.font.bold = True
    r_top.font.color.rgb = RGBColor(0, 0, 0)

    # Header Menteri Keuangan
    p_men = doc.add_paragraph()
    p_men.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_men.paragraph_format.space_after = Pt(6)
    p_men.paragraph_format.line_spacing = 1.05
    r_men = p_men.add_run("MENTERI KEUANGAN\nREPUBLIK INDONESIA\n")
    r_men.font.name = "Arial"
    r_men.font.size = Pt(10)
    r_men.font.bold = True
    r_men.font.color.rgb = RGBColor(0, 0, 0)
    if page_num_str:
        r_page = p_men.add_run(f"- {page_num_str} -\n")
        r_page.font.name = "Arial"
        r_page.font.size = Pt(9)
        r_page.font.bold = True
        r_page.font.color.rgb = RGBColor(0, 0, 0)

def generate_pmk8_complete_docs():
    target_dir = "/Users/arthur/Documents/KCA DOKUMEN/LAPORAN PAJAK"
    local_target_dir = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/KCA DOKUMEN/LAPORAN PAJAK"
    os.makedirs(target_dir, exist_ok=True)
    os.makedirs(local_target_dir, exist_ok=True)

    # =========================================================================
    # FILE 1: LAMPIRAN I PMK 8/PMK.03/2013 FORMAT LENGKAP RESMI (FORMAT A, B, C, D)
    # =========================================================================
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    # -------------------------------------------------------------
    # FORMAT A: PERMOHONAN PENGURANGAN ATAU PENGHAPUSAN SANKSI ADMINISTRASI
    # -------------------------------------------------------------
    add_header_lampiran(doc)

    p_title_a = doc.add_paragraph()
    p_title_a.paragraph_format.space_after = Pt(6)
    r_ta = p_title_a.add_run("A. FORMAT SURAT PERMOHONAN PENGURANGAN ATAU PENGHAPUSAN SANKSI ADMINISTRASI:\n")
    r_ta.font.name = "Arial"
    r_ta.font.size = Pt(10)
    r_ta.font.bold = True
    r_ta.font.color.rgb = RGBColor(0, 0, 0)

    # Tabel Meta Nomor/Tanggal
    t_meta = doc.add_table(rows=3, cols=2)
    t_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_meta.rows[0].cells[0].text = "Nomor       : ............................................................. (1)"
    t_meta.rows[0].cells[1].text = "...............................................(2)"
    t_meta.rows[1].cells[0].text = "Lampiran    : ............................................................. (3)"
    t_meta.rows[1].cells[1].text = ""
    t_meta.rows[2].cells[0].text = "Hal         : Permohonan Pengurangan atau Penghapusan\n              Sanksi Administrasi"
    t_meta.rows[2].cells[1].text = ""
    for r in t_meta.rows:
        for c in r.cells:
            for p in c.paragraphs:
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.line_spacing = 1.05
                for run in p.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(9.5)
                    run.font.color.rgb = RGBColor(0, 0, 0)

    p_yth = doc.add_paragraph(
        "\nYth. Direktur Jenderal Pajak\n"
        "u.b. Kepala KPP ............................................................. (4)\n\n"
        "Yang bertanda tangan di bawah ini:\n"
        "Nama                 : ......................................................................................... (5)\n"
        "NPWP                 : ......................................................................................... (6)\n"
        "Jabatan              : ......................................................................................... (7)\n"
        "Alamat               : ......................................................................................... (8)\n"
        "Nomor Telepon        : ......................................................................................... (9)\n"
        "Bertindak selaku     : [  ] Wajib Pajak\n"
        "                       [  ] Wakil                 [  ] Kuasa\n"
        "                       dari Wajib Pajak\n"
        "                       Nama     : ..................................................................... (10)\n"
        "                       NPWP     : ..................................................................... (11)\n"
        "                       Alamat   : ..................................................................... (12)\n\n"
        "bersama ini mengajukan pengurangan/penghapusan sanksi administrasi yang tercantum dalam "
        "Surat Ketetapan Pajak Kurang Bayar (SKPKB)/Surat Ketetapan Pajak Kurang Bayar Tambahan (SKPKBT)/Surat Tagihan Pajak (STP)*):\n"
        "Nomor & Tanggal      : ......................................................................................... (13)\n"
        "Jenis Pajak          : ......................................................................................... (14)\n"
        "Masa/Tahun*) Pajak   : ......................................................................................... (15)\n\n"
        "Alasan permohonan pengurangan/penghapusan sanksi administrasi:\n"
        "...................................................................................................................................................................\n"
        "..............................................................................................................................................................(16)\n\n"
        "Berdasarkan hal tersebut di atas, dengan ini dimohon pengurangan/penghapusan sanksi administrasi menjadi sebesar Rp.........................................................(17).\n\n"
        "Sehubungan dengan permohonan tersebut, kami informasikan bahwa kami telah membayar pajak yang terutang sebesar "
        "Rp..................................(18) tanggal ......................................(19) pada bank ...........................................(20) "
        "dengan NTPN .............................................(21)\n\n"
        "Sebagai kelengkapan permohonan, terlampir disampaikan: (22)"
    )
    p_yth.paragraph_format.space_after = Pt(4)
    p_yth.paragraph_format.line_spacing = 1.15
    for run in p_yth.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Tabel Lampiran Format A
    t_lamp_a = doc.add_table(rows=3, cols=3)
    t_lamp_a.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lamp_a)
    headers_a = ["No.", "Jenis Dokumen", "Set/Lembar"]
    for i, h in enumerate(headers_a):
        cell = t_lamp_a.rows[0].cells[i]
        cell.text = h
        set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = "Arial"
        p.runs[0].font.size = Pt(9)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    # Sample empty rows
    for r_idx in range(1, 3):
        row = t_lamp_a.rows[r_idx]
        for c_idx in range(3):
            cell = row.cells[c_idx]
            cell.text = " "
            set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
            p = cell.paragraphs[0]
            if p.runs:
                p.runs[0].font.name = "Arial"
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    doc.add_paragraph()
    p_penutup_a = doc.add_paragraph(
        "Demikian surat permohonan kami sampaikan untuk dapat dipertimbangkan.\n\n"
        "                                                                                        Wajib Pajak/Wakil/Kuasa**)\n\n\n\n"
        "                                                                                                   (23)\n"
        "                                                                                        ......................................................\n\n"
        "Keterangan:\n"
        "1. Beri tanda X pada [  ] yang sesuai;\n"
        "2. *) Diisi salah satu yang sesuai;\n"
        "3. **) Diisi salah satu yang sesuai dan dalam hal surat permohonan ditandatangani oleh kuasa harus dilampiri Surat Kuasa Khusus."
    )
    p_penutup_a.paragraph_format.line_spacing = 1.15
    for run in p_penutup_a.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # ------------------ PETUNJUK PENGISIAN FORMAT A ------------------
    doc.add_page_break()
    add_header_lampiran(doc, "3")

    p_pet_title_a = doc.add_paragraph()
    p_pet_title_a.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_pta = p_pet_title_a.add_run("PETUNJUK PENGISIAN SURAT PERMOHONAN\nPENGURANGAN ATAU PENGHAPUSAN SANKSI ADMINISTRASI\n")
    r_pta.font.name = "Arial"
    r_pta.font.size = Pt(10)
    r_pta.font.bold = True
    r_pta.font.color.rgb = RGBColor(0, 0, 0)

    petunjuk_a_text = (
        "Nomor (1)  : Diisi sesuai dengan penomoran surat Wajib Pajak.\n"
        "Nomor (2)  : Diisi dengan nama kota dan tanggal surat permohonan ditandatangani.\n"
        "Nomor (3)  : Diisi dengan jumlah lampiran yang disertakan dalam surat permohonan Wajib Pajak.\n"
        "Nomor (4)  : Diisi dengan nama dan alamat Kantor Pelayanan Pajak tempat Wajib Pajak terdaftar dan/atau tempat Pengusaha Kena Pajak dikukuhkan.\n"
        "Nomor (5)  : Diisi dengan nama Wajib Pajak/wakil/kuasa sesuai peraturan perundangan-undangan di bidang ketentuan umum dan tata cara perpajakan, yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi.\n"
        "Nomor (6)  : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi.\n"
        "Nomor (7)  : Diisi dengan jabatan wakil/kuasa yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi dan dalam hal permohonan diajukan oleh Wajib Pajak orang pribadi Nomor (7) tidak perlu diisi.\n"
        "Nomor (8)  : Diisi dengan alamat Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi.\n"
        "Nomor (9)  : Diisi dengan nomor telepon Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi.\n"
        "Nomor (10) : Diisi dengan nama Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (11) : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (12) : Diisi dengan alamat Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau penghapusan sanksi administrasi adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (13) : Diisi dengan nomor dan tanggal surat ketetapan pajak atau Surat Tagihan Pajak yang diajukan permohonan pengurangan atau penghapusan sanksi administrasi.\n"
        "Nomor (14) : Diisi dengan jenis pajak, seperti Pajak Penghasilan Badan, Pajak Pertambahan Nilai, Pajak Penghasilan Pasal 21.\n"
        "Nomor (15) : Diisi dengan Masa Pajak atau Tahun Pajak.\n"
        "Nomor (16) : Diisi dengan alasan permohonan pengurangan atau penghapusan sanksi administrasi.\n"
        "Nomor (17) : Diisi dengan jumlah sanksi administrasi menurut Wajib Pajak.\n"
        "Nomor (18) : Diisi dengan jumlah pajak terutang yang telah dibayar oleh Wajib Pajak yang menjadi dasar pengenaan sanksi administrasi yang tercantum dalam surat ketetapan pajak atau Surat Tagihan Pajak dan dalam hal pembayaran dilakukan lebih dari 1 (satu) kali dicantumkan masing-masing pembayaran.\n"
        "Nomor (19) : Diisi dengan tanggal pembayaran pajak yang terutang oleh Wajib Pajak dan dalam hal pembayaran dilakukan lebih dari 1 (satu) kali dicantumkan masing-masing tanggal pembayaran.\n"
        "Nomor (20) : Diisi dengan nama bank tempat pembayaran pajak yang terutang oleh Wajib Pajak dan dalam hal pembayaran dilakukan lebih dari 1 (satu) kali dicantumkan masing-masing tempat pembayaran.\n"
        "Nomor (21) : Diisi dengan Nomor Transaksi Penerimaan Negara (NTPN) sesuai dengan yang tercantum dalam Surat Setoran Pajak (SSP) pembayaran pajak yang terutang oleh Wajib Pajak dan dalam hal pembayaran dilakukan lebih dari 1 (satu) kali dicantumkan masing-masing NTPN.\n"
        "Nomor (22) : Diisi dengan jenis dokumen dan jumlah lembar masing-masing jenis dokumen yang dilampirkan oleh Wajib Pajak.\n"
        "Nomor (23) : Diisi dengan tanda tangan dan nama pemohon."
    )
    p_pet_a = doc.add_paragraph(petunjuk_a_text)
    p_pet_a.paragraph_format.line_spacing = 1.15
    for run in p_pet_a.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------
    # FORMAT B: PEMBATALAN SURAT KETETAPAN PAJAK YANG TIDAK BENAR
    # -------------------------------------------------------------
    doc.add_page_break()
    add_header_lampiran(doc, "5")

    p_title_b = doc.add_paragraph()
    r_tb = p_title_b.add_run("B. FORMAT SURAT PERMOHONAN PENGURANGAN ATAU PEMBATALAN SURAT KETETAPAN PAJAK YANG TIDAK BENAR:\n")
    r_tb.font.name = "Arial"
    r_tb.font.size = Pt(10)
    r_tb.font.bold = True
    r_tb.font.color.rgb = RGBColor(0, 0, 0)

    p_b_body = doc.add_paragraph(
        "Nomor       : ............................................................. (1)                 ........................(2)\n"
        "Lampiran    : ............................................................. (3)\n"
        "Hal         : Permohonan Pengurangan atau Pembatalan Surat\n"
        "              Ketetapan Pajak yang Tidak Benar\n\n"
        "Yth. Direktur Jenderal Pajak\n"
        "u.b. Kepala KPP ............................................................. (4)\n\n"
        "Yang bertanda tangan di bawah ini:\n"
        "Nama                 : ......................................................................................... (5)\n"
        "NPWP                 : ......................................................................................... (6)\n"
        "Jabatan              : ......................................................................................... (7)\n"
        "Alamat               : ......................................................................................... (8)\n"
        "Nomor Telepon        : ......................................................................................... (9)\n"
        "Bertindak selaku     : [  ] Wajib Pajak\n"
        "                       [  ] Wakil                 [  ] Kuasa\n"
        "                       dari Wajib Pajak\n"
        "                       Nama     : ..................................................................... (10)\n"
        "                       NPWP     : ..................................................................... (11)\n"
        "                       Alamat   : ..................................................................... (12)\n\n"
        "bersama ini mengajukan permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar atas "
        "Surat Ketetapan Pajak Kurang Bayar/Surat Ketetapan Pajak Kurang Bayar Tambahan/Surat Ketetapan Pajak Lebih Bayar/Surat Ketetapan Pajak Nihil*):\n"
        "Nomor & Tanggal      : ......................................................................................... (13)\n"
        "Jenis Pajak          : ......................................................................................... (14)\n"
        "Masa/Tahun*) Pajak   : ......................................................................................... (15)\n\n"
        "Alasan permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar:\n"
        "...................................................................................................................................................................\n"
        "..............................................................................................................................................................(16)\n\n"
        "Berdasarkan hal tersebut di atas, perhitungan pajak yang masih harus dibayar/jumlah rugi*) menurut kami adalah sebesar Rp....................................(17).\n\n"
        "Sebagai kelengkapan permohonan, terlampir disampaikan: (18)"
    )
    p_b_body.paragraph_format.line_spacing = 1.15
    for run in p_b_body.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Tabel Lampiran Format B
    t_lamp_b = doc.add_table(rows=3, cols=3)
    t_lamp_b.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lamp_b)
    for i, h in enumerate(headers_a):
        cell = t_lamp_b.rows[0].cells[i]
        cell.text = h
        set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = "Arial"
        p.runs[0].font.size = Pt(9)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    for r_idx in range(1, 3):
        row = t_lamp_b.rows[r_idx]
        for c_idx in range(3):
            cell = row.cells[c_idx]
            cell.text = " "
            set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
            p = cell.paragraphs[0]
            if p.runs:
                p.runs[0].font.name = "Arial"
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    p_penutup_b = doc.add_paragraph(
        "\nDemikian surat permohonan kami sampaikan untuk dapat dipertimbangkan.\n\n"
        "                                                                                        Wajib Pajak/Wakil/Kuasa**)\n\n\n\n"
        "                                                                                                   (19)\n"
        "                                                                                        ......................................................\n\n"
        "Keterangan:\n"
        "1. Beri tanda X pada [  ] yang sesuai;\n"
        "2. *) Diisi salah satu yang sesuai;\n"
        "3. **) Diisi salah satu yang sesuai dan dalam hal surat permohonan ditandatangani oleh kuasa harus dilampiri Surat Kuasa Khusus."
    )
    p_penutup_b.paragraph_format.line_spacing = 1.15
    for run in p_penutup_b.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # ------------------ PETUNJUK PENGISIAN FORMAT B ------------------
    doc.add_page_break()
    add_header_lampiran(doc, "7")

    p_pet_title_b = doc.add_paragraph()
    p_pet_title_b.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ptb = p_pet_title_b.add_run("PETUNJUK PENGISIAN SURAT PERMOHONAN PENGURANGAN ATAU\nPEMBATALAN SURAT KETETAPAN PAJAK YANG TIDAK BENAR\n")
    r_ptb.font.name = "Arial"
    r_ptb.font.size = Pt(10)
    r_ptb.font.bold = True
    r_ptb.font.color.rgb = RGBColor(0, 0, 0)

    petunjuk_b_text = (
        "Nomor (1)  : Diisi sesuai dengan penomoran surat Wajib Pajak.\n"
        "Nomor (2)  : Diisi dengan kota dan tanggal surat permohonan ditandatangani.\n"
        "Nomor (3)  : Diisi dengan jumlah lampiran yang disertakan dalam surat permohonan Wajib Pajak.\n"
        "Nomor (4)  : Diisi dengan nama dan alamat Kantor Pelayanan Pajak tempat Wajib Pajak terdaftar dan/atau tempat Pengusaha Kena Pajak dikukuhkan.\n"
        "Nomor (5)  : Diisi dengan nama Wajib Pajak/wakil/kuasa sesuai peraturan perundangan-undangan di bidang ketentuan umum dan tata cara perpajakan, yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar.\n"
        "Nomor (6)  : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar.\n"
        "Nomor (7)  : Diisi dengan jabatan wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar dan dalam hal permohonan diajukan oleh Wajib Pajak orang pribadi Nomor (7) tidak perlu diisi.\n"
        "Nomor (8)  : Diisi dengan alamat Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar.\n"
        "Nomor (9)  : Diisi dengan nomor telepon Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar.\n"
        "Nomor (10) : Diisi dengan nama Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (11) : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (12) : Diisi dengan alamat Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar adalah pengurus atau kuasa dari Wajib Pajak.\n"
        "Nomor (13) : Diisi dengan nomor dan tanggal surat ketetapan pajak yang diajukan permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar.\n"
        "Nomor (14) : Diisi dengan jenis pajak, seperti Pajak Penghasilan Badan, Pajak Pertambahan Nilai, Pajak Penghasilan Pasal 21.\n"
        "Nomor (15) : Diisi dengan Masa Pajak atau Tahun Pajak.\n"
        "Nomor (16) : Diisi dengan alasan permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar.\n"
        "Nomor (17) : Diisi dengan jumlah pajak yang masih harus dibayar atau jumlah rugi menurut Wajib Pajak.\n"
        "Nomor (18) : Diisi dengan jenis dokumen dan jumlah lembar masing-masing jenis dokumen yang dilampirkan oleh Wajib Pajak.\n"
        "Nomor (19) : Diisi dengan tanda tangan dan nama pemohon."
    )
    p_pet_b = doc.add_paragraph(petunjuk_b_text)
    p_pet_b.paragraph_format.line_spacing = 1.15
    for run in p_pet_b.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------
    # FORMAT C: PEMBATALAN SURAT TAGIHAN PAJAK YANG TIDAK BENAR
    # -------------------------------------------------------------
    doc.add_page_break()
    add_header_lampiran(doc, "9")

    p_title_c = doc.add_paragraph()
    r_tc = p_title_c.add_run("C. FORMAT SURAT PERMOHONAN PENGURANGAN ATAU PEMBATALAN SURAT TAGIHAN PAJAK YANG TIDAK BENAR:\n")
    r_tc.font.name = "Arial"
    r_tc.font.size = Pt(10)
    r_tc.font.bold = True
    r_tc.font.color.rgb = RGBColor(0, 0, 0)

    p_c_body = doc.add_paragraph(
        "Nomor       : ............................................................. (1)                 ........................(2)\n"
        "Lampiran    : ............................................................. (3)\n"
        "Hal         : Permohonan Pengurangan atau Pembatalan\n"
        "              Surat Tagihan Pajak yang Tidak Benar\n\n"
        "Yth. Direktur Jenderal Pajak\n"
        "u.b. Kepala KPP ............................................................. (4)\n\n"
        "Yang bertanda tangan di bawah ini:\n"
        "Nama                 : ......................................................................................... (5)\n"
        "NPWP                 : ......................................................................................... (6)\n"
        "Jabatan              : ......................................................................................... (7)\n"
        "Alamat               : ......................................................................................... (8)\n"
        "Nomor Telepon        : ......................................................................................... (9)\n"
        "Bertindak selaku     : [  ] Wajib Pajak\n"
        "                       [  ] Wakil                 [  ] Kuasa\n"
        "                       dari Wajib Pajak\n"
        "                       Nama     : ..................................................................... (10)\n"
        "                       NPWP     : ..................................................................... (11)\n"
        "                       Alamat   : ..................................................................... (12)\n\n"
        "bersama ini mengajukan permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar atas Surat Tagihan Pajak:\n"
        "Nomor & Tanggal      : ......................................................................................... (13)\n"
        "Jenis Pajak          : ......................................................................................... (14)\n"
        "Masa/Tahun*) Pajak   : ......................................................................................... (15)\n\n"
        "Alasan permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar:\n"
        "...................................................................................................................................................................\n"
        "..............................................................................................................................................................(16)\n\n"
        "Berdasarkan hal tersebut di atas, dengan ini dimohon pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar menjadi sebesar Rp........................................(17)\n\n"
        "Sebagai kelengkapan permohonan, terlampir disampaikan: (18)"
    )
    p_c_body.paragraph_format.line_spacing = 1.15
    for run in p_c_body.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Tabel Lampiran Format C
    t_lamp_c = doc.add_table(rows=3, cols=3)
    t_lamp_c.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lamp_c)
    for i, h in enumerate(headers_a):
        cell = t_lamp_c.rows[0].cells[i]
        cell.text = h
        set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = "Arial"
        p.runs[0].font.size = Pt(9)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    for r_idx in range(1, 3):
        row = t_lamp_c.rows[r_idx]
        for c_idx in range(3):
            cell = row.cells[c_idx]
            cell.text = " "
            set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
            p = cell.paragraphs[0]
            if p.runs:
                p.runs[0].font.name = "Arial"
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    p_penutup_c = doc.add_paragraph(
        "\nDemikian surat permohonan kami sampaikan untuk dapat dipertimbangkan.\n\n"
        "                                                                                        Wajib Pajak/Wakil/Kuasa**)\n\n\n\n"
        "                                                                                                   (19)\n"
        "                                                                                        ......................................................\n\n"
        "Keterangan:\n"
        "1. Beri tanda X pada [  ] yang sesuai;\n"
        "2. *) Diisi salah satu yang sesuai;\n"
        "3. **) Diisi salah satu yang sesuai dan dalam hal surat permohonan ditandatangani oleh kuasa harus dilampiri Surat Kuasa Khusus."
    )
    p_penutup_c.paragraph_format.line_spacing = 1.15
    for run in p_penutup_c.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # ------------------ PETUNJUK PENGISIAN FORMAT C ------------------
    doc.add_page_break()
    add_header_lampiran(doc, "11")

    p_pet_title_c = doc.add_paragraph()
    p_pet_title_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ptc = p_pet_title_c.add_run("PETUNJUK PENGISIAN SURAT PERMOHONAN PENGURANGAN ATAU PEMBATALAN\nSURAT TAGIHAN PAJAK YANG TIDAK BENAR\n")
    r_ptc.font.name = "Arial"
    r_ptc.font.size = Pt(10)
    r_ptc.font.bold = True
    r_ptc.font.color.rgb = RGBColor(0, 0, 0)

    petunjuk_c_text = (
        "Nomor (1)  : Diisi sesuai dengan penomoran surat Wajib Pajak.\n"
        "Nomor (2)  : Diisi dengan kota dan tanggal surat permohonan ditandatangani.\n"
        "Nomor (3)  : Diisi dengan jumlah lampiran yang disertakan dalam surat permohonan Wajib Pajak.\n"
        "Nomor (4)  : Diisi dengan nama dan alamat Kantor Pelayanan Pajak tempat Wajib Pajak terdaftar dan/atau tempat Pengusaha Kena Pajak dikukuhkan.\n"
        "Nomor (5)  : Diisi dengan nama Wajib Pajak/wakil/kuasa sesuai peraturan perundangan-undangan di bidang ketentuan umum dan tata cara perpajakan, yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar.\n"
        "Nomor (6)  : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar.\n"
        "Nomor (7)  : Diisi dengan jabatan wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar dan dalam hal permohonan diajukan oleh Wajib Pajak Orang Pribadi Nomor (7) tidak perlu diisi.\n"
        "Nomor (8)  : Diisi dengan alamat Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar.\n"
        "Nomor (9)  : Diisi dengan nomor telepon Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar.\n"
        "Nomor (10) : Diisi dengan nama Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (11) : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (12) : Diisi dengan alamat Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (13) : Diisi dengan nomor dan tanggal Surat Tagihan Pajak yang diajukan permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar.\n"
        "Nomor (14) : Diisi dengan jenis pajak, seperti Pajak Penghasilan Badan, Pajak Pertambahan Nilai, Pajak Penghasilan Pasal 21.\n"
        "Nomor (15) : Diisi dengan Masa Pajak atau Tahun Pajak.\n"
        "Nomor (16) : Diisi dengan alasan permohonan pengurangan atau pembatalan Surat Tagihan Pajak yang tidak benar.\n"
        "Nomor (17) : Diisi dengan jumlah pajak yang harus dibayar menurut Wajib Pajak.\n"
        "Nomor (18) : Diisi dengan jenis dokumen dan jumlah lembar masing-masing jenis dokumen yang dilampirkan.\n"
        "Nomor (19) : Diisi dengan tanda tangan dan nama pemohon."
    )
    p_pet_c = doc.add_paragraph(petunjuk_c_text)
    p_pet_c.paragraph_format.line_spacing = 1.15
    for run in p_pet_c.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------
    # FORMAT D: PEMBATALAN SKP HASIL PEMERIKSAAN / VERIFIKASI
    # -------------------------------------------------------------
    doc.add_page_break()
    add_header_lampiran(doc, "13")

    p_title_d = doc.add_paragraph()
    r_td = p_title_d.add_run("D. FORMAT SURAT PERMOHONAN PEMBATALAN SURAT KETETAPAN PAJAK HASIL PEMERIKSAAN ATAU VERIFIKASI:\n")
    r_td.font.name = "Arial"
    r_td.font.size = Pt(10)
    r_td.font.bold = True
    r_td.font.color.rgb = RGBColor(0, 0, 0)

    p_d_body = doc.add_paragraph(
        "Nomor       : ............................................................. (1)                 ........................(2)\n"
        "Lampiran    : ............................................................. (3)\n"
        "Hal         : Permohonan Pembatalan Surat Ketetapan Pajak\n"
        "              Hasil Pemeriksaan atau Verifikasi\n\n"
        "Yth. Direktur Jenderal Pajak\n"
        "u.b. Kepala KPP ............................................................. (4)\n\n"
        "Yang bertanda tangan di bawah ini:\n"
        "Nama                 : ......................................................................................... (5)\n"
        "NPWP                 : ......................................................................................... (6)\n"
        "Jabatan              : ......................................................................................... (7)\n"
        "Alamat               : ......................................................................................... (8)\n"
        "Nomor Telepon        : ......................................................................................... (9)\n"
        "Bertindak selaku     : [  ] Wajib Pajak\n"
        "                       [  ] Wakil                 [  ] Kuasa\n"
        "                       dari Wajib Pajak\n"
        "                       Nama     : ..................................................................... (10)\n"
        "                       NPWP     : ..................................................................... (11)\n"
        "                       Alamat   : ..................................................................... (12)\n\n"
        "bersama ini mengajukan permohonan pembatalan surat ketetapan pajak hasil pemeriksaan/verifikasi*) atas "
        "Surat Ketetapan Pajak Kurang Bayar/Surat Ketetapan Pajak Kurang Bayar Tambahan/Surat Ketetapan Pajak Lebih Bayar/Surat Ketetapan Pajak Nihil*):\n"
        "Nomor & Tanggal      : ......................................................................................... (13)\n"
        "Jenis Pajak          : ......................................................................................... (14)\n"
        "Masa/Tahun*) Pajak   : ......................................................................................... (15)\n\n"
        "Alasan permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi karena surat ketetapan pajak diterbitkan tanpa:\n"
        "[  ] penyampaian surat pemberitahuan hasil pemeriksaan atau surat pemberitahuan hasil verifikasi.\n"
        "[  ] pembahasan akhir hasil pemeriksaan atau pembahasan akhir hasil verifikasi dengan Wajib Pajak.\n\n"
        "Dengan uraian sebagai berikut:\n"
        "...................................................................................................................................................................\n"
        "..............................................................................................................................................................(16)\n\n"
        "Sebagai kelengkapan permohonan, terlampir disampaikan: (17)"
    )
    p_d_body.paragraph_format.line_spacing = 1.15
    for run in p_d_body.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Tabel Lampiran Format D
    t_lamp_d = doc.add_table(rows=3, cols=3)
    t_lamp_d.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lamp_d)
    for i, h in enumerate(headers_a):
        cell = t_lamp_d.rows[0].cells[i]
        cell.text = h
        set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.name = "Arial"
        p.runs[0].font.size = Pt(9)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    for r_idx in range(1, 3):
        row = t_lamp_d.rows[r_idx]
        for c_idx in range(3):
            cell = row.cells[c_idx]
            cell.text = " "
            set_cell_margins(cell, top=40, bottom=40, left=80, right=80)
            p = cell.paragraphs[0]
            if p.runs:
                p.runs[0].font.name = "Arial"
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    p_penutup_d = doc.add_paragraph(
        "\nDemikian surat permohonan kami sampaikan untuk dapat dipertimbangkan.\n\n"
        "                                                                                        Wajib Pajak/Wakil/Kuasa**)\n\n\n\n"
        "                                                                                                   (18)\n"
        "                                                                                        ......................................................\n\n"
        "Keterangan:\n"
        "1. Beri tanda X pada [  ] yang sesuai;\n"
        "2. *) Diisi salah satu yang sesuai;\n"
        "3. **) Diisi salah satu yang sesuai dan dalam hal surat permohonan ditandatangani oleh kuasa harus dilampiri Surat Kuasa Khusus."
    )
    p_penutup_d.paragraph_format.line_spacing = 1.15
    for run in p_penutup_d.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # ------------------ PETUNJUK PENGISIAN FORMAT D ------------------
    doc.add_page_break()
    add_header_lampiran(doc, "15")

    p_pet_title_d = doc.add_paragraph()
    p_pet_title_d.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ptd = p_pet_title_d.add_run("PETUNJUK PENGISIAN SURAT PERMOHONAN PEMBATALAN SURAT KETETAPAN PAJAK\nHASIL PEMERIKSAAN ATAU VERIFIKASI\n")
    r_ptd.font.name = "Arial"
    r_ptd.font.size = Pt(10)
    r_ptd.font.bold = True
    r_ptd.font.color.rgb = RGBColor(0, 0, 0)

    petunjuk_d_text = (
        "Nomor (1)  : Diisi sesuai dengan penomoran surat Wajib Pajak.\n"
        "Nomor (2)  : Diisi dengan kota dan tanggal surat permohonan ditandatangani.\n"
        "Nomor (3)  : Diisi dengan jumlah lampiran yang disertakan dalam surat permohonan Wajib Pajak.\n"
        "Nomor (4)  : Diisi dengan nama dan alamat Kantor Pelayanan Pajak tempat Wajib Pajak terdaftar dan/atau tempat Pengusaha Kena Pajak dikukuhkan.\n"
        "Nomor (5)  : Diisi dengan nama Wajib Pajak/wakil/kuasa sesuai peraturan perundangan-undangan di bidang ketentuan umum dan tata cara perpajakan, yang menandatangani surat permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi.\n"
        "Nomor (6)  : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi.\n"
        "Nomor (7)  : Diisi dengan jabatan wakil/kuasa yang menandatangani surat permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi dan dalam hal permohonan diajukan oleh Wajib Pajak Orang Pribadi Nomor (7) tidak perlu diisi.\n"
        "Nomor (8)  : Diisi dengan alamat Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi.\n"
        "Nomor (9)  : Diisi dengan nomor telepon Wajib Pajak/wakil/kuasa yang menandatangani surat permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi.\n"
        "Nomor (10) : Diisi dengan nama Wajib Pajak apabila yang menandatangani surat permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (11) : Diisi dengan Nomor Pokok Wajib Pajak Wajib Pajak apabila yang menandatangani surat permohonan pengurangan atau pembatalan surat ketetapan pajak yang tidak benar adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (12) : Diisi dengan alamat Wajib Pajak apabila yang menandatangani surat permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi adalah wakil atau kuasa dari Wajib Pajak.\n"
        "Nomor (13) : Diisi dengan nomor dan tanggal surat ketetapan pajak yang diajukan permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi.\n"
        "Nomor (14) : Diisi dengan jenis pajak, seperti Pajak Penghasilan Badan, Pajak Pertambahan Nilai, Pajak Penghasilan Pasal 21.\n"
        "Nomor (15) : Diisi dengan Masa Pajak atau Tahun Pajak.\n"
        "Nomor (16) : Diisi dengan alasan permohonan pembatalan surat ketetapan pajak hasil pemeriksaan atau verifikasi.\n"
        "Nomor (17) : Diisi dengan jenis dokumen dan jumlah lembar masing-masing jenis dokumen yang dilampirkan.\n"
        "Nomor (18) : Diisi dengan tanda tangan dan nama pemohon.\n\n"
        "Salinan sesuai dengan aslinya\n"
        "KEPALA BIRO UMUM\n"
        "u.b.\n"
        "KEPALA BAGIAN T.U. KEMENTERIAN\n\n"
        "GIARTO\n"
        "NIP 195904201984021001\n\n"
        "MENTERI KEUANGAN REPUBLIK INDONESIA,\n"
        "ttd.\n"
        "AGUS D.W. MARTOWARDOJO"
    )
    p_pet_d = doc.add_paragraph(petunjuk_d_text)
    p_pet_d.paragraph_format.line_spacing = 1.15
    for run in p_pet_d.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Simpan file lengkap
    file1_name = "LAMPIRAN_I_PMK_8_PMK.03_2013_FORMAT_LENGKAP_A_B_C_D.docx"
    path1 = os.path.join(target_dir, file1_name)
    path1_local = os.path.join(local_target_dir, file1_name)
    doc.save(path1)
    doc.save(path1_local)
    sanitize_docx_metadata(path1, title="Lampiran I PMK 8 PMK.03 2013 Format Lengkap", author="Yerikho Arfensias Effendi")
    sanitize_docx_metadata(path1_local, title="Lampiran I PMK 8 PMK.03 2013 Format Lengkap", author="Yerikho Arfensias Effendi")
    print("SUCCESS: File 1 saved at", path1)

    # =========================================================================
    # FILE 2: FORMAT A KHUSUS SIAP PAKAI / EDIT UNTUK KCA (PENGHAPUSAN SANKSI STP)
    # =========================================================================
    doc_a = Document()
    for s in doc_a.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    add_header_lampiran(doc_a)

    p_ta2 = doc_a.add_paragraph()
    r_ta2 = p_ta2.add_run("A. FORMAT SURAT PERMOHONAN PENGURANGAN ATAU PENGHAPUSAN SANKSI ADMINISTRASI:\n")
    r_ta2.font.name = "Arial"
    r_ta2.font.size = Pt(10)
    r_ta2.font.bold = True
    r_ta2.font.color.rgb = RGBColor(0, 0, 0)

    p_a_editable = doc_a.add_paragraph(
        "Nomor       : 019/KCA-DIR/TAX-PMK8/IX/2026                 Kediri, 07 September 2026\n"
        "Lampiran    : 1 (Satu) Berkas\n"
        "Hal         : Permohonan Pengurangan atau Penghapusan\n"
        "              Sanksi Administrasi\n\n"
        "Yth. Direktur Jenderal Pajak\n"
        "u.b. Kepala KPP Pratama Kediri\n"
        "Jl. Basuki Rahmat No. 10, Kel. Pocanan, Kota Kediri, Jawa Timur 64129\n\n"
        "Yang bertanda tangan di bawah ini:\n"
        "Nama                 : YAN EFFENDI\n"
        "NPWP                 : (Diisi Nomor NPWP Pribadi Bpk. Yan Effendi)\n"
        "Jabatan              : Direktur Utama\n"
        "Alamat               : RT.1/RW.6, Pagung, Kec. Semen, Kab. Kediri, Jawa Timur 64161\n"
        "Nomor Telepon        : 0822-4400-6699\n"
        "Bertindak selaku     : [X] Wajib Pajak\n"
        "                       [X] Wakil                 [  ] Kuasa\n"
        "                       dari Wajib Pajak\n"
        "                       Nama     : PT KEDIRI CHEMICAL ABADI\n"
        "                       NPWP     : (Diisi Nomor NPWP 16 Digit PT Kediri Chemical Abadi)\n"
        "                       Alamat   : RT.1/RW.6, Pagung, Kec. Semen, Kab. Kediri, Jawa Timur 64161\n\n"
        "bersama ini mengajukan pengurangan/penghapusan sanksi administrasi yang tercantum dalam Surat Tagihan Pajak (STP)*):\n"
        "Nomor & Tanggal      : (Diisi Nomor STP & Tanggal Terbit STP dari Lembar Denda Kemarin)\n"
        "Jenis Pajak          : Pajak Penghasilan Badan / PPN / PPh 21\n"
        "Masa/Tahun*) Pajak   : Tahun Pajak 2026\n\n"
        "Alasan permohonan pengurangan/penghapusan sanksi administrasi:\n"
        "Keterlambatan penyampaian laporan terjadi karena kekhilafan Wajib Pajak baru yang masih dalam tahap penyiapan sarana dan fasilitas pabrik. Perusahaan belum memulai kegiatan operasional usaha yang menghasilkan pendapatan atau omzet penjualan (berstatus NIHIL), dan keterlambatan ini sama sekali bukan merupakan tindakan kesengajaan untuk menghindari kewajiban perpajakan.\n\n"
        "Berdasarkan hal tersebut di atas, dengan ini dimohon pengurangan/penghapusan sanksi administrasi menjadi sebesar Rp 0,- (Nihil / Dihapuskan 100%).\n\n"
        "Sehubungan dengan permohonan tersebut, kami informasikan bahwa pajak yang terutang adalah sebesar Rp 0,- (Nihil / Belum Ada Kegiatan Usaha Komersial).\n\n"
        "Sebagai kelengkapan permohonan, terlampir disampaikan:"
    )
    p_a_editable.paragraph_format.line_spacing = 1.15
    for run in p_a_editable.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0, 0, 0)

    t_lamp_edit = doc_a.add_table(rows=4, cols=3)
    t_lamp_edit.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lamp_edit)
    lamp_rows = [
        ("No.", "Jenis Dokumen", "Set/Lembar"),
        ("1.", "Salinan Surat Tagihan Pajak (STP) Denda", "1 Lembar"),
        ("2.", "Surat Pernyataan Belum Beroperasi / WP NE Bermeterai", "1 Lembar"),
        ("3.", "Salinan NPWP Badan PT KCA & KTP Direktur Utama", "1 Lembar")
    ]
    for r_i, r_data in enumerate(lamp_rows):
        for c_i, val in enumerate(r_data):
            cell = t_lamp_edit.rows[r_i].cells[c_i]
            cell.text = val
            set_cell_margins(cell, top=35, bottom=35, left=60, right=60)
            p = cell.paragraphs[0]
            if r_i == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.runs[0].font.bold = True
            p.runs[0].font.name = "Arial"
            p.runs[0].font.size = Pt(8.5)
            p.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    p_close_edit = doc_a.add_paragraph(
        "\nDemikian surat permohonan kami sampaikan untuk dapat dipertimbangkan.\n\n"
        "                                                                                        Wajib Pajak/Wakil/Kuasa**)\n"
        "                                                                                        PT KEDIRI CHEMICAL ABADI\n\n"
        "                                                                                        (Meterai Rp 10.000 & Cap PT)\n\n\n\n"
        "                                                                                        YAN EFFENDI\n"
        "                                                                                        Direktur Utama\n\n"
        "Keterangan:\n"
        "1. Beri tanda X pada [  ] yang sesuai;\n"
        "2. *) Diisi salah satu yang sesuai;\n"
        "3. **) Diisi salah satu yang sesuai dan dalam hal surat permohonan ditandatangani oleh kuasa harus dilampiri Surat Kuasa Khusus."
    )
    p_close_edit.paragraph_format.line_spacing = 1.15
    for run in p_close_edit.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)
        if "YAN EFFENDI" in run.text:
            run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    file2_name = "FORMAT_A_PERMOHONAN_PENGHAPUSAN_SANKSI_ADMINISTRASI_PMK8.docx"
    path2 = os.path.join(target_dir, file2_name)
    path2_local = os.path.join(local_target_dir, file2_name)
    doc_a.save(path2)
    doc_a.save(path2_local)
    sanitize_docx_metadata(path2, title="Format A Permohonan Penghapusan Sanksi Administrasi PMK 8", author="Yerikho Arfensias Effendi")
    sanitize_docx_metadata(path2_local, title="Format A Permohonan Penghapusan Sanksi Administrasi PMK 8", author="Yerikho Arfensias Effendi")
    print("SUCCESS: File 2 saved at", path2)

if __name__ == "__main__":
    generate_pmk8_complete_docs()
