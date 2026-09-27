import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from kca_doc_humanizer import sanitize_docx_metadata

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def generate_tax_waiver_letter():
    base_dir = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical"
    output_dir = os.path.join(base_dir, "KCA DOKUMEN/08_LEGALITAS_HR_PJT_DAN_ADMINISTRASI_MAKLOON")
    os.makedirs(output_dir, exist_ok=True)
    doc_path = os.path.join(output_dir, "SURAT_PERMOHONAN_PENGHAPUSAN_SANKSI_DENDA_PAJAK_PASAL36_KCA.docx")

    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.85)
        section.bottom_margin = Inches(0.85)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

    # Kop Surat Resmi
    kop = doc.add_paragraph()
    kop.alignment = WD_ALIGN_PARAGRAPH.CENTER
    k1 = kop.add_run("PT KEDIRI CHEMICAL ABADI\n")
    k1.font.name = "Arial"
    k1.font.size = Pt(15)
    k1.font.bold = True
    k1.font.color.rgb = RGBColor(0, 0, 0)

    k2 = kop.add_run("Pabrik: RT.1/RW.6, Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161\n"
                    "Hotline/WhatsApp: 0822-4400-6699 | Email: kdrchemicals@gmail.com\n")
    k2.font.name = "Arial"
    k2.font.size = Pt(9)
    k2.font.color.rgb = RGBColor(0, 0, 0)

    p_line = doc.add_paragraph("═" * 58)
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p_line.runs:
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Info Surat & Tujuan
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.line_spacing = 1.15
    m1 = p_meta.add_run(
        "Nomor       : 014/KCA-DIR/TAX/IX/2026\n"
        "Lampiran    : 1 (Satu) Berkas\n"
        "Perihal     : Permohonan Pengurangan atau Penghapusan Sanksi Administrasi Perpajakan\n"
        "              (Berdasarkan Pasal 36 Ayat (1) Huruf a UU KUP)\n\n"
        "Kediri, 05 September 2026\n\n"
        "Kepada Yth.:\n"
        "Kepala Kantor Pelayanan Pajak (KPP) Pratama Kediri\n"
        "Jl. Basuki Rahmat No. 10, Kel. Pocanan, Kota Kediri, Jawa Timur 64129\n\n"
    )
    m1.font.name = "Arial"
    m1.font.size = Pt(10)
    m1.font.color.rgb = RGBColor(0, 0, 0)

    # Pembuka
    p_open = doc.add_paragraph(
        "Dengan hormat,\n\n"
        "Sehubungan dengan diterbitkannya Surat Tagihan Pajak (STP) atas keterlambatan pelaporan Surat Pemberitahuan (SPT) "
        "terhadap Wajib Pajak Badan berikut:"
    )
    p_open.paragraph_format.line_spacing = 1.15
    for r in p_open.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Identitas Wajib Pajak Table
    t_wp = doc.add_table(rows=5, cols=2)
    t_wp.alignment = WD_TABLE_ALIGNMENT.CENTER
    wp_data = [
        ("Nama Wajib Pajak", ": PT KEDIRI CHEMICAL ABADI"),
        ("NPWP Badan", ": (Diisi Nomor NPWP PT Kediri Chemical Abadi)"),
        ("Alamat Terdaftar", ": RT.1/RW.6, Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161"),
        ("Jenis Usaha / KLU", ": Industri Bahan Kimia & Sabun Pembersih (Makloon B2B)"),
        ("Penanggung Jawab", ": YAN EFFENDI (Direktur Utama) / YERIKHO ARFENSIAS EFFENDI (GM)")
    ]
    for idx, (label, val) in enumerate(wp_data):
        row = t_wp.rows[idx].cells
        row[0].text = label
        row[1].text = val
        for c in row:
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    # Isi Pokok Permohonan & Alasan
    doc.add_paragraph()
    p_isi = doc.add_paragraph(
        "Dengan ini kami mengajukan permohonan Pengurangan atau Penghapusan Sanksi Administrasi atas Surat Tagihan Pajak (STP) "
        "yang telah diterbitkan, dengan pertimbangan dan alasan yang sebenarnya sebagai berikut:\n\n"
        "1. Perusahaan Masih dalam Tahap Persiapan dan Belum Memiliki Pemasukan (Nihil):\n"
        "   Perusahaan kami saat ini masih dalam fase restrukturisasi internal, penyiapan sarana dan fasilitas produksi, serta belum memulai "
        "kegiatan komersial yang menghasilkan pendapatan atau omzet penjualan. Seluruh neraca keuangan berstatus nihil transaksi komersial.\n\n"
        "2. Adanya Kekhilafan dan Ketidaktahuan Prosedur Pelaporan (Bukan Unsur Kesengajaan):\n"
        "   Keterlambatan penyampaian laporan SPT terjadi murni karena kekhilafan pengurus baru yang belum memahami mekanisme "
        "pelaporan SPT secara daring (DJP Online) bagi wajib pajak baru yang masih belum memiliki transaksi/omzet (SPT Nihil). "
        "Hal ini sama sekali bukan merupakan tindakan kesengajaan untuk menghindar dari kewajiban perpajakan.\n\n"
        "3. Kepatuhan Berkelanjutan:\n"
        "   Kami telah melakukan pelaporan seluruh kewajiban SPT yang tertunda dan berkomitmen penuh untuk tertib administrasi perpajakan "
        "sesuai ketentuan perundang-undangan yang berlaku pada periode berikutnya.\n\n"
        "Berdasarkan ketentuan Pasal 36 Ayat (1) Huruf a Undang-Undang Nomor 6 Tahun 1983 tentang Ketentuan Umum dan Tata Cara Perpajakan "
        "(KUP) sebagaimana telah beberapa kali diubah terakhir dengan Undang-Undang Nomor 7 Tahun 2021 tentang Harmonisasi Peraturan Perpajakan (HPP), "
        "Direktur Jenderal Pajak memiliki kewenangan untuk mengurangkan atau menghapuskan sanksi administrasi berupa bunga, denda, dan kenaikan "
        "yang terutang karena kekhilafan Wajib Pajak atau bukan karena kesalahannya."
    )
    p_isi.paragraph_format.line_spacing = 1.15
    for r in p_isi.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Lampiran
    p_lamp = doc.add_paragraph(
        "Sebagai bahan pertimbangan Bapak Kepala Kantor, bersama surat ini kami lampirkan:\n"
        "1. Salinan Surat Tagihan Pajak (STP) yang dimohonkan penghapusan;\n"
        "2. Bukti Penerimaan Elektronik (BPE) pelaporan SPT terkait (status Nihil);\n"
        "3. Salinan Akta Pendirian Perusahaan dan NIB / Legalitas PT Kediri Chemical Abadi;\n"
        "4. Salinan NPWP Badan PT Kediri Chemical Abadi dan KTP Pengurus;\n"
        "5. Laporan Keuangan Neraca Sementara (membuktikan belum adanya omzet/pemasukan)."
    )
    p_lamp.paragraph_format.line_spacing = 1.15
    for r in p_lamp.runs:
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Penutup
    p_close = doc.add_paragraph(
        "Demikian permohonan ini kami sampaikan dengan harapan Bapak berkenan mengabulkan permohonan penghapusan sanksi administrasi ini. "
        "Atas perhatian, bimbingan, dan kebijaksanaan Bapak, kami ucapkan terima kasih."
    )
    p_close.paragraph_format.line_spacing = 1.15
    for r in p_close.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Tanda Tangan
    doc.add_paragraph("\n")
    t_sign = doc.add_table(rows=3, cols=2)
    t_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sign.rows[0].cells[0].text = "Hormat kami,\nPT KEDIRI CHEMICAL ABADI"
    t_sign.rows[0].cells[1].text = "Mengetahui,\nDIREKTUR UTAMA"
    t_sign.rows[1].cells[0].text = "\n\n(Meterai Rp 10.000)\n\n"
    t_sign.rows[1].cells[1].text = "\n\n\n\n"
    t_sign.rows[2].cells[0].text = "YERIKHO ARFENSIAS EFFENDI\nGeneral Manager / Finance & Ops"
    t_sign.rows[2].cells[1].text = "YAN EFFENDI\nDirektur Utama"

    for row in t_sign.rows:
        for c in row.cells:
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)
            for p in c.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.bold = True
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    doc.save(doc_path)
    
    # Salin juga ke root KCA DOKUMEN jika folder luar ada
    ext_path = "/Users/arthur/Documents/KCA DOKUMEN/08_LEGALITAS_HR_PJT_DAN_ADMINISTRASI_MAKLOON/SURAT_PERMOHONAN_PENGHAPUSAN_SANKSI_DENDA_PAJAK_PASAL36_KCA.docx"
    if os.path.exists(os.path.dirname(ext_path)):
        doc.save(ext_path)
        sanitize_docx_metadata(ext_path, title="Surat Permohonan Penghapusan Sanksi Denda Pajak KCA", author="Yerikho Arfensias Effendi")

    sanitize_docx_metadata(doc_path, title="Surat Permohonan Penghapusan Sanksi Denda Pajak KCA", author="Yerikho Arfensias Effendi")
    print("SUCCESS: Tax Waiver Letter generated at", doc_path)
    return doc_path

if __name__ == "__main__":
    generate_tax_waiver_letter()
