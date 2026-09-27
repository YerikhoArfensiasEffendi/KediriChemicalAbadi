import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from kca_doc_humanizer import sanitize_docx_metadata

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shd = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shd))

def generate_wp_ne_documents():
    base_dir = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical"
    output_dir = os.path.join(base_dir, "KCA DOKUMEN/08_LEGALITAS_HR_PJT_DAN_ADMINISTRASI_MAKLOON")
    os.makedirs(output_dir, exist_ok=True)
    doc_path = os.path.join(output_dir, "BERKAS_PERMOHONAN_WP_NON_EFEKTIF_NE_KCA.docx")

    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.85)
        s.bottom_margin = Inches(0.85)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    # -------------------------------------------------------------
    # DOKUMEN 1: SURAT PENGANTAR PERMOHONAN PENETAPAN WP NON-EFEKTIF
    # -------------------------------------------------------------
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

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.line_spacing = 1.15
    m_run = p_meta.add_run(
        "Nomor       : 015/KCA-DIR/TAX-NE/IX/2026\n"
        "Lampiran    : 1 (Satu) Berkas Lengkap\n"
        "Perihal     : Permohonan Penetapan Wajib Pajak Non-Efektif (WP NE)\n"
        "              Berdasarkan Peraturan Direktur Jenderal Pajak Nomor PER-04/PJ/2020\n\n"
        "Kediri, 05 September 2026\n\n"
        "Kepada Yth.:\n"
        "Kepala Kantor Pelayanan Pajak (KPP) Pratama Kediri\n"
        "Jl. Basuki Rahmat No. 10, Kel. Pocanan, Kota Kediri, Jawa Timur 64129\n\n"
    )
    m_run.font.name = "Arial"
    m_run.font.size = Pt(10)
    m_run.font.color.rgb = RGBColor(0, 0, 0)

    p_isi1 = doc.add_paragraph(
        "Dengan hormat,\n\n"
        "Sehubungan dengan status kegiatan usaha perusahaan yang saat ini masih dalam tahap perintisan, restrukturisasi modal, "
        "dan persiapan sarana fasilitas pabrik, dengan ini kami yang bertanda tangan di bawah ini bertindak atas nama "
        "Wajib Pajak Badan:\n"
    )
    p_isi1.paragraph_format.line_spacing = 1.15
    for r in p_isi1.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Identitas WP Table
    t_wp = doc.add_table(rows=5, cols=2)
    t_wp.alignment = WD_TABLE_ALIGNMENT.CENTER
    wp_data = [
        ("Nama Wajib Pajak", ": PT KEDIRI CHEMICAL ABADI"),
        ("NPWP Badan", ": (Diisi Nomor NPWP 16 Digit PT Kediri Chemical Abadi)"),
        ("Alamat Terdaftar", ": RT.1/RW.6, Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161"),
        ("Nomor Telepon / HP", ": 0822-4400-6699"),
        ("Nama Penanggung Jawab", ": YERIKHO ARFENSIAS EFFENDI (General Manager) / YAN EFFENDI (Direktur Utama)")
    ]
    for idx, (label, val) in enumerate(wp_data):
        row = t_wp.rows[idx].cells
        row[0].text = label
        row[1].text = val
        for c in row:
            set_cell_margins(c)
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    doc.add_paragraph()
    p_isi2 = doc.add_paragraph(
        "Mengajukan permohonan kepada Bapak Kepala KPP Pratama Kediri untuk menetapkan Wajib Pajak Badan tersebut di atas "
        "sebagai WAJIB PAJAK NON-EFEKTIF (WP NE), dengan alasan bahwa:\n\n"
        "1. Wajib Pajak Badan belum melakukan kegiatan usaha komersial dan belum memperoleh peredaran bruto (omzet penjualan) "
        "sama sekali, serta belum mempekerjakan karyawan tetap berbayar pajak (kegiatan komersial nihil).\n"
        "2. Wajib Pajak Badan saat ini sedang dalam proses penyiapan sarana pabrik dan restrukturisasi internal sehingga belum ada "
        "kegiatan transaksi operasional bisnis aktif.\n\n"
        "Hal ini sesuai dengan ketentuan Pasal 24 Ayat (2) Huruf d Peraturan Direktur Jenderal Pajak Nomor PER-04/PJ/2020 tentang "
        "Petunjuk Teknis Pelaksanaan Administrasi Nomor Pokok Wajib Pajak, Sertifikat Elektronik, dan Pengukuhan Pengusaha Kena Pajak, "
        "yang menyatakan bahwa penetapan Wajib Pajak Non-Efektif dapat dilakukan terhadap Wajib Pajak Badan yang belum atau tidak melakukan "
        "kegiatan usaha tetapi belum dibubarkan.\n\n"
        "Sebagai kelengkapan berkas, bersama ini kami lampirkan:\n"
        "1. Surat Pernyataan Wajib Pajak Non-Efektif bermeterai Rp 10.000;\n"
        "2. Formulir Permohonan Penetapan Wajib Pajak Non-Efektif resmi DJP;\n"
        "3. Salinan Kartu NPWP Badan PT Kediri Chemical Abadi;\n"
        "4. Salinan KTP dan NPWP Penanggung Jawab (Direksi);\n"
        "5. Salinan Akta Pendirian Perusahaan dan NIB OSS RBA.\n\n"
        "Demikian permohonan ini kami sampaikan. Kami berkomitmen untuk segera mengajukan permohonan pengaktifan kembali (reaktivasi) "
        "apabila perusahaan telah resmi memulai kegiatan operasional usaha yang menghasilkan omzet. Atas perhatian dan bantuan Bapak, "
        "kami ucapkan terima kasih."
    )
    p_isi2.paragraph_format.line_spacing = 1.15
    for r in p_isi2.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Tanda Tangan Surat Pengantar
    doc.add_paragraph("\n")
    t_sign1 = doc.add_table(rows=3, cols=2)
    t_sign1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sign1.rows[0].cells[0].text = "Pemohon / Wajib Pajak,\nPT KEDIRI CHEMICAL ABADI"
    t_sign1.rows[0].cells[1].text = "Mengetahui,\nDIREKTUR UTAMA"
    t_sign1.rows[1].cells[0].text = "\n\n\n\n"
    t_sign1.rows[1].cells[1].text = "\n\n\n\n"
    t_sign1.rows[2].cells[0].text = "YERIKHO ARFENSIAS EFFENDI\nGeneral Manager / Operasional & Keuangan"
    t_sign1.rows[2].cells[1].text = "YAN EFFENDI\nDirektur Utama"

    for row in t_sign1.rows:
        for c in row.cells:
            set_cell_margins(c)
            for p in c.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.bold = True
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------
    # DOKUMEN 2: SURAT PERNYATAAN BERMETERAI (LAMPIRAN PER-04/PJ/2020)
    # -------------------------------------------------------------
    doc.add_page_break()

    p_sp_title = doc.add_paragraph()
    p_sp_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sp1 = p_sp_title.add_run("SURAT PERNYATAAN WAJIB PAJAK NON-EFEKTIF\n")
    sp1.font.name = "Arial"
    sp1.font.size = Pt(12.5)
    sp1.font.bold = True
    sp1.font.color.rgb = RGBColor(0, 0, 0)

    sp2 = p_sp_title.add_run("(Sesuai Ketentuan PER-04/PJ/2020)\n\n")
    sp2.font.name = "Arial"
    sp2.font.size = Pt(9.5)
    sp2.font.italic = True
    sp2.font.color.rgb = RGBColor(0, 0, 0)

    p_sp_buka = doc.add_paragraph("Yang bertanda tangan di bawah ini:")
    p_sp_buka.paragraph_format.line_spacing = 1.15
    for r in p_sp_buka.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    t_id_dir = doc.add_table(rows=4, cols=2)
    t_id_dir.alignment = WD_TABLE_ALIGNMENT.CENTER
    dir_data = [
        ("Nama Lengkap", ": YERIKHO ARFENSIAS EFFENDI"),
        ("NIK / No. KTP", ": (Diisi Nomor KTP Bpk. Yerikho)"),
        ("Jabatan", ": General Manager / Penanggung Jawab Keuangan & Ops"),
        ("Bertindak Selaku", ": Wakil / Kuasa Wajib Pajak Badan PT KEDIRI CHEMICAL ABADI")
    ]
    for idx, (label, val) in enumerate(dir_data):
        row = t_id_dir.rows[idx].cells
        row[0].text = label
        row[1].text = val
        for c in row:
            set_cell_margins(c)
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    doc.add_paragraph()
    p_sp_badan = doc.add_paragraph("Dengan ini menyatakan yang sebenarnya mengenai Wajib Pajak:")
    p_sp_badan.paragraph_format.line_spacing = 1.15
    for r in p_sp_badan.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    t_id_pt = doc.add_table(rows=3, cols=2)
    t_id_pt.alignment = WD_TABLE_ALIGNMENT.CENTER
    pt_data = [
        ("Nama Wajib Pajak", ": PT KEDIRI CHEMICAL ABADI"),
        ("NPWP Badan", ": (Diisi Nomor NPWP PT Kediri Chemical Abadi)"),
        ("Alamat Pabrik / Kantor", ": RT.1/RW.6, Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161")
    ]
    for idx, (label, val) in enumerate(pt_data):
        row = t_id_pt.rows[idx].cells
        row[0].text = label
        row[1].text = val
        for c in row:
            set_cell_margins(c)
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    doc.add_paragraph()
    p_sp_isi = doc.add_paragraph(
        "Menyatakan dengan sesungguhnya bahwa:\n\n"
        "1. Wajib Pajak Badan PT Kediri Chemical Abadi SAAT INI BELUM MEMULAI KEGIATAN USAHA / BELUM MELAKUKAN KEGIATAN KOMERSIAL "
        "yang menghasilkan peredaran bruto (omzet nihil) dan belum memiliki pegawai tetap yang dipotong PPh Pasal 21.\n"
        "2. Wajib Pajak Badan tidak melakukan transaksi penjualan maupun pembelian bahan baku yang bernilai komersial selama periode berjalan.\n"
        "3. Berkenaan dengan kondisi tersebut, kami memohon agar Wajib Pajak Badan PT Kediri Chemical Abadi ditetapkan sebagai "
        "WAJIB PAJAK NON-EFEKTIF sehingga dibebaskan dari kewajiban penyampaian Surat Pemberitahuan (SPT) Masa maupun SPT Tahunan "
        "tanpa diterbitkan sanksi denda administrasi perpajakan.\n"
        "4. Apabila di kemudian hari Wajib Pajak Badan telah aktif kembali menjalankan kegiatan usaha dan/atau memperoleh peredaran usaha (omzet), "
        "kami bersedia dan berjanji untuk segera melaporkan diri ke KPP Pratama Kediri guna mengaktifkan kembali (reaktivasi) Nomor Pokok Wajib Pajak.\n\n"
        "Demikian surat pernyataan ini kami buat dengan sebenarnya dan penuh rasa tanggung jawab. Apabila keterangan yang kami berikan "
        "tidak benar, kami bersedia dituntut sesuai dengan ketentuan perundang-undangan perpajakan yang berlaku."
    )
    p_sp_isi.paragraph_format.line_spacing = 1.15
    for r in p_sp_isi.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # Tanda Tangan Bermeterai
    doc.add_paragraph("\n")
    p_tgl_sp = doc.add_paragraph("Kediri, 05 September 2026\nYang membuat pernyataan,")
    p_tgl_sp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for r in p_tgl_sp.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    p_meterai = doc.add_paragraph("\n\n(Meterai Rp 10.000 & Cap PT)\n\n\n")
    p_meterai.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for r in p_meterai.runs:
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0, 0, 0)

    p_nama_sp = doc.add_paragraph("YERIKHO ARFENSIAS EFFENDI\nGeneral Manager / Penanggung Jawab")
    p_nama_sp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for r in p_nama_sp.runs:
        r.font.name = "Arial"
        r.font.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------
    # DOKUMEN 3: PANDUAN RINGKAS PENYERAHAN KE KPP PRATAMA KEDIRI
    # -------------------------------------------------------------
    doc.add_page_break()
    p_guide_title = doc.add_heading("PANDUAN PRAKTIS PENGAJUAN WP NON-EFEKTIF KE KPP PRATAMA KEDIRI", level=2)
    for r in p_guide_title.runs:
        r.font.name = "Arial"
        r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)

    p_guide = doc.add_paragraph(
        "Berikut langkah-langkah praktis dan berkas yang harus dibawa ke Kantor Pelayanan Pajak (KPP) Pratama Kediri:\n\n"
        "A. Lokasi Penyerahan Berkas:\n"
        "   Loket Tempat Pelayanan Terpadu (TPT) KPP Pratama Kediri\n"
        "   Alamat: Jl. Basuki Rahmat No. 10, Kel. Pocanan, Kota Kediri, Jawa Timur 64129\n"
        "   Jam Pelayanan: Senin - Jumat, pukul 08.00 - 16.00 WIB.\n\n"
        "B. Susunan Urutan Berkas (Disatukan dalam 1 Map): \n"
        "   1. Surat Pengantar Permohonan Penetapan WP Non-Efektif (Dokumen 1);\n"
        "   2. Surat Pernyataan Belum Melakukan Kegiatan Usaha bermeterai Rp 10.000 (Dokumen 2);\n"
        "   3. Fotokopi NPWP Badan PT Kediri Chemical Abadi;\n"
        "   4. Fotokopi KTP dan NPWP Bpk. Yerikho Arfensias Effendi & Bpk. Yan Effendi;\n"
        "   5. Fotokopi Akta Pendirian PT dan NIB (Nomor Induk Berusaha) OSS;\n"
        "   6. Surat Permohonan Penghapusan Denda (Pasal 36 UU KUP) beserta salinan STP denda yang kemarin diterima (bisa diserahkan bersamaan).\n\n"
        "C. Keuntungan Setelah Berstatus WP Non-Efektif (NE):\n"
        "   • PT Kediri Chemical Abadi TIDAK LAGI DIWAJIBKAN lapor SPT Masa bulanan maupun SPT Tahunan.\n"
        "   • Sistem DJP TIDAK AKAN PERNAH LAGI menerbitkan denda/STP keterlambatan pelaporan.\n"
        "   • NPWP Badan tetap aktif tersimpan di database DJP dan legalitas PT tetap sah berdiri.\n"
        "   • Begitu pabrik siap beroperasi komersial dan mulai ada penjualan, status NE dapat diaktifkan kembali (Reaktivasi) dalam 1 hari kerja."
    )
    p_guide.paragraph_format.line_spacing = 1.15
    for r in p_guide.runs:
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0, 0, 0)

    doc.save(doc_path)
    
    # Salin ke root folder KCA DOKUMEN jika ada
    ext_path = "/Users/arthur/Documents/KCA DOKUMEN/08_LEGALITAS_HR_PJT_DAN_ADMINISTRASI_MAKLOON/BERKAS_PERMOHONAN_WP_NON_EFEKTIF_NE_KCA.docx"
    if os.path.exists(os.path.dirname(ext_path)):
        doc.save(ext_path)
        sanitize_docx_metadata(ext_path, title="Berkas Permohonan WP Non Efektif NE KCA", author="Yerikho Arfensias Effendi")

    sanitize_docx_metadata(doc_path, title="Berkas Permohonan WP Non Efektif NE KCA", author="Yerikho Arfensias Effendi")
    print("SUCCESS: WP Non-Efektif Documents generated at", doc_path)
    return doc_path

if __name__ == "__main__":
    generate_wp_ne_documents()
