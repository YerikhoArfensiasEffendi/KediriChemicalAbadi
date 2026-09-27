import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from kca_doc_humanizer import sanitize_docx_metadata

def set_cell_margins(cell, top=40, bottom=40, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def generate_direct_director_tax_docs():
    base_dir = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical"
    output_dir = os.path.join(base_dir, "KCA DOKUMEN/08_LEGALITAS_HR_PJT_DAN_ADMINISTRASI_MAKLOON")
    ext_dir = "/Users/arthur/Documents/KCA DOKUMEN/08_LEGALITAS_HR_PJT_DAN_ADMINISTRASI_MAKLOON"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(ext_dir, exist_ok=True)

    # =========================================================================
    # DOKUMEN 1: BERKAS WP NON-EFEKTIF (DIRANCANG PAS 1 HALAMAN PER SURAT = TOTAL 2 HALAMAN)
    # =========================================================================
    doc1_path = os.path.join(output_dir, "BERKAS_PERMOHONAN_WP_NON_EFEKTIF_DIRECT_DIREKTUR_KCA.docx")
    doc1 = Document()
    for s in doc1.sections:
        s.top_margin = Inches(0.65)
        s.bottom_margin = Inches(0.65)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)

    # ------------------ HALAMAN 1: SURAT PENGANTAR ------------------
    kop1 = doc1.add_paragraph()
    kop1.paragraph_format.space_after = Pt(2)
    kop1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    k1 = kop1.add_run("PT KEDIRI CHEMICAL ABADI\n")
    k1.font.name = "Arial"
    k1.font.size = Pt(13.5)
    k1.font.bold = True
    k1.font.color.rgb = RGBColor(0, 0, 0)

    k2 = kop1.add_run("Pabrik: RT.1/RW.6, Pagung, Kec. Semen, Kab. Kediri, Jawa Timur 64161 | Telp: 0822-4400-6699\n")
    k2.font.name = "Arial"
    k2.font.size = Pt(8.5)
    k2.font.color.rgb = RGBColor(0, 0, 0)

    p_line1 = doc1.add_paragraph("═" * 65)
    p_line1.paragraph_format.space_after = Pt(4)
    p_line1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p_line1.runs:
        r.font.color.rgb = RGBColor(0, 0, 0)

    p_meta1 = doc1.add_paragraph()
    p_meta1.paragraph_format.space_after = Pt(4)
    p_meta1.paragraph_format.line_spacing = 1.05
    m_run1 = p_meta1.add_run(
        "Nomor    : 017/KCA-DIR/TAX-NE/IX/2026\n"
        "Lampiran : 1 (Satu) Berkas Lengkap\n"
        "Perihal  : Permohonan Penetapan Wajib Pajak Non-Efektif (WP NE) - PER-04/PJ/2020\n\n"
        "Kepada Yth.: Kepala Kantor Pelayanan Pajak (KPP) Pratama Kediri\n"
        "Jl. Basuki Rahmat No. 10, Kota Kediri, Jawa Timur 64129\n"
    )
    m_run1.font.name = "Arial"
    m_run1.font.size = Pt(9)
    m_run1.font.color.rgb = RGBColor(0, 0, 0)

    p_isi1 = doc1.add_paragraph(
        "Dengan hormat, sehubungan dengan operasional PT Kediri Chemical Abadi yang saat ini masih dalam fase persiapan pabrik dan restrukturisasi internal, saya bertindak selaku Direktur Utama dan Penanggung Jawab sah Wajib Pajak Badan:"
    )
    p_isi1.paragraph_format.space_after = Pt(3)
    p_isi1.paragraph_format.line_spacing = 1.05
    for r in p_isi1.runs:
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0, 0, 0)

    t_dir = doc1.add_table(rows=5, cols=2)
    t_dir.alignment = WD_TABLE_ALIGNMENT.CENTER
    dir_info = [
        ("Nama Direktur Utama", ": YAN EFFENDI"),
        ("Nama Wajib Pajak", ": PT KEDIRI CHEMICAL ABADI"),
        ("NPWP Badan (16 Digit)", ": (Diisi Nomor NPWP 16 Digit PT Kediri Chemical Abadi)"),
        ("Alamat Terdaftar", ": RT.1/RW.6, Pagung, Kec. Semen, Kab. Kediri, Jawa Timur 64161"),
        ("Kontak / Email", ": 0822-4400-6699 / kdrchemicals@gmail.com")
    ]
    for idx, (label, val) in enumerate(dir_info):
        row = t_dir.rows[idx].cells
        row[0].text = label
        row[1].text = val
        for c in row:
            set_cell_margins(c, top=20, bottom=20, left=60, right=60)
            for p in c.paragraphs:
                p.paragraph_format.space_after = Pt(1)
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.size = Pt(8.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    p_isi1_2 = doc1.add_paragraph(
        "Mengajukan permohonan kepada Kepala KPP Pratama Kediri agar PT KEDIRI CHEMICAL ABADI dapat ditetapkan sebagai WAJIB PAJAK NON-EFEKTIF (WP NE), dengan pertimbangan bahwa:\n"
        "1. Perusahaan belum melakukan kegiatan usaha komersial secara aktif dan peredaran bruto (omzet penjualan) berstatus NIHIL, serta belum memiliki karyawan tetap kena pajak.\n"
        "2. Perusahaan saat ini masih dalam tahap penyiapan sarana pabrik Pagung sehingga belum terjadi transaksi komersial aktif.\n"
        "Hal ini sesuai Pasal 24 Ayat (2) Huruf d PER-04/PJ/2020 tentang penetapan WP Non-Efektif bagi Badan yang belum melakukan kegiatan usaha tetapi belum dibubarkan.\n"
        "Bersama surat ini dilampirkan: (1) Surat Pernyataan WP Non-Efektif bermeterai Rp 10.000; (2) Salinan NPWP Badan; (3) Salinan KTP Direktur Utama; (4) Salinan NIB & Akta PT."
    )
    p_isi1_2.paragraph_format.space_after = Pt(4)
    p_isi1_2.paragraph_format.line_spacing = 1.05
    for r in p_isi1_2.runs:
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0, 0, 0)

    p_ttd_box1 = doc1.add_paragraph(
        "Kediri, 05 September 2026\n"
        "Hormat saya,\n"
        "PT KEDIRI CHEMICAL ABADI\n\n\n"
        "(Tanda Tangan & Cap PT)\n\n\n"
        "YAN EFFENDI\n"
        "Direktur Utama"
    )
    p_ttd_box1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd_box1.paragraph_format.space_after = Pt(0)
    p_ttd_box1.paragraph_format.line_spacing = 1.0
    for r in p_ttd_box1.runs:
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        if "YAN EFFENDI" in r.text:
            r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)

    # ------------------ HALAMAN 2: SURAT PERNYATAAN BERMETERAI ------------------
    doc1.add_page_break()

    p_sp_t = doc1.add_paragraph()
    p_sp_t.paragraph_format.space_after = Pt(3)
    p_sp_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sp_t1 = p_sp_t.add_run("SURAT PERNYATAAN WAJIB PAJAK NON-EFEKTIF\n")
    sp_t1.font.name = "Arial"
    sp_t1.font.size = Pt(12)
    sp_t1.font.bold = True
    sp_t1.font.color.rgb = RGBColor(0, 0, 0)

    sp_t2 = p_sp_t.add_run("(Sesuai Format Lampiran PER-04/PJ/2020)\n")
    sp_t2.font.name = "Arial"
    sp_t2.font.size = Pt(8.5)
    sp_t2.font.italic = True
    sp_t2.font.color.rgb = RGBColor(0, 0, 0)

    p_sp_b = doc1.add_paragraph("Yang bertanda tangan di bawah ini:")
    p_sp_b.paragraph_format.space_after = Pt(2)
    for r in p_sp_b.runs:
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0, 0, 0)

    t_id_dir2 = doc1.add_table(rows=7, cols=2)
    t_id_dir2.alignment = WD_TABLE_ALIGNMENT.CENTER
    dir2_data = [
        ("Nama Lengkap", ": YAN EFFENDI"),
        ("NIK / No. KTP", ": (Diisi Nomor KTP Bpk. Yan Effendi)"),
        ("Jabatan", ": Direktur Utama dan Penanggung Jawab Sah"),
        ("Bertindak Atas Nama", ": PT KEDIRI CHEMICAL ABADI"),
        ("NPWP Badan (16 Digit)", ": (Diisi Nomor NPWP 16 Digit PT Kediri Chemical Abadi)"),
        ("Alamat Pabrik", ": RT.1/RW.6, Pagung, Kec. Semen, Kab. Kediri, Jawa Timur 64161"),
        ("Nomor Kontak", ": 0822-4400-6699 / kdrchemicals@gmail.com")
    ]
    for idx, (label, val) in enumerate(dir2_data):
        row = t_id_dir2.rows[idx].cells
        row[0].text = label
        row[1].text = val
        for c in row:
            set_cell_margins(c, top=20, bottom=20, left=60, right=60)
            for p in c.paragraphs:
                p.paragraph_format.space_after = Pt(1)
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.size = Pt(8.5)
                    r.font.color.rgb = RGBColor(0, 0, 0)

    p_sp_content = doc1.add_paragraph(
        "\nMenyatakan dengan sesungguhnya bahwa:\n"
        "1. Wajib Pajak Badan PT Kediri Chemical Abadi SAAT INI BELUM MEMULAI KEGIATAN USAHA / KEGIATAN KOMERSIAL yang menghasilkan peredaran bruto (omzet berstatus NIHIL) dan belum mempekerjakan karyawan tetap yang dipotong PPh Pasal 21.\n"
        "2. Wajib Pajak Badan tidak melakukan transaksi operasional komersial selama periode berjalan sehubungan fasilitas pabrik masih dalam persiapan sarana produksi.\n"
        "3. Berkenaan dengan kondisi tersebut, kami memohon agar Wajib Pajak Badan PT Kediri Chemical Abadi ditetapkan sebagai WAJIB PAJAK NON-EFEKTIF (WP NE), sehingga dibebaskan dari kewajiban penyampaian SPT Masa maupun SPT Tahunan tanpa diterbitkan sanksi denda administrasi perpajakan.\n"
        "4. Apabila di kemudian hari Wajib Pajak Badan telah siap dan aktif kembali menjalankan kegiatan usaha dan/atau memperoleh omzet penjualan, kami bersedia dan berjanji untuk segera melaporkan diri ke KPP Pratama Kediri guna mengaktifkan kembali (reaktivasi) status Wajib Pajak.\n\n"
        "Demikian surat pernyataan ini saya buat dengan sebenarnya dan penuh rasa tanggung jawab. Apabila keterangan ini tidak benar, saya bersedia dituntut sesuai ketentuan perundang-undangan perpajakan yang berlaku."
    )
    p_sp_content.paragraph_format.space_after = Pt(4)
    p_sp_content.paragraph_format.line_spacing = 1.05
    for r in p_sp_content.runs:
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0, 0, 0)

    p_ttd_box2 = doc1.add_paragraph(
        "Kediri, 05 September 2026\n"
        "Yang membuat pernyataan,\n"
        "Direktur Utama PT KEDIRI CHEMICAL ABADI\n\n"
        "(Meterai Rp 10.000 & Cap PT)\n\n\n\n"
        "YAN EFFENDI\n"
        "Direktur Utama"
    )
    p_ttd_box2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd_box2.paragraph_format.space_after = Pt(0)
    p_ttd_box2.paragraph_format.line_spacing = 1.0
    for r in p_ttd_box2.runs:
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        if "YAN EFFENDI" in r.text:
            r.font.bold = True
        r.font.color.rgb = RGBColor(0, 0, 0)

    doc1.save(doc1_path)
    doc1.save(os.path.join(ext_dir, "BERKAS_PERMOHONAN_WP_NON_EFEKTIF_DIRECT_DIREKTUR_KCA.docx"))
    sanitize_docx_metadata(doc1_path, title="Berkas Permohonan WP Non Efektif Direct Direktur KCA", author="Yerikho Arfensias Effendi")
    sanitize_docx_metadata(os.path.join(ext_dir, "BERKAS_PERMOHONAN_WP_NON_EFEKTIF_DIRECT_DIREKTUR_KCA.docx"), title="Berkas Permohonan WP Non Efektif Direct Direktur KCA", author="Yerikho Arfensias Effendi")
    print("SUCCESS: 2-Page exact layout saved!")

if __name__ == "__main__":
    generate_direct_director_tax_docs()
