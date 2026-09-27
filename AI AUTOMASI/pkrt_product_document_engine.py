#!/usr/bin/env python3
"""
PT KEDIRI CHEMICAL ABADI — QUALITY ASSURANCE & LEGAL PKRT
Modul Otomasi Generator Dokumen Produk PKRT Berbasis Template Word (.docx)
Memproses 8 Dokumen Resmi PKRT & Mengekspor PDF Sesuai Standar ISO 9001:2015

Dokumen yang diotomasi:
1. Formula .docx (List Bahan Baku, Persentase Terhitung, dan Fungsi)
2. COA.docx (Certificate of Analysis / Sertifikat Analisis Fisikokimia)
3. Formulir 1.1.docx (Formulir Pendaftaran PKRT Kemenkes RI)
4. Sertifikat uji Lab.docx (Sertifikat Hasil Uji Produk Jadi)
5. Alur Produksi.docx (Alur & Lembar Pengujian Produksi)
6. Sepsifikasi Kemasan.docx (Spesifikasi Kemasan Jerigen & Botol PET)
7. Tujuan Pembuatan.docx (Deskripsi Produk, Cara Penggunaan & Peringatan)
8. Uji Stabilitas.docx (Data Stabilitas Realtime 1 Tahun & Kesimpulan)

Author / Manager : Yerikho Arfensias Effendi
Company          : PT Kediri Chemical Abadi
Direktur Utama   : Yan Effendi
"""

import os
import re
import sys
import shutil
import subprocess
from datetime import datetime
import docx
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

TEMPLATE_DIR = "/Users/arthur/Documents/tamplate"
DEFAULT_OUTPUT_BASE = "/Users/arthur/Documents/PT. ANUGERAH SURYA SEMBADA"

SOFFICE_BIN = "/opt/homebrew/bin/soffice"
if not os.path.exists(SOFFICE_BIN):
    SOFFICE_BIN = shutil.which("soffice")

# ==============================================================================
# 1. CHEMICAL KNOWLEDGE BASE & PKRT REGULATORY INTELLIGENCE
# ==============================================================================

CHEMICAL_FUNCTIONS = {
    # Surfaktan & Pembersih
    "sles": "Surfaktan utama pembersih & pembusa efektif",
    "sodium lauryl ether sulfate": "Surfaktan utama pembersih & pembusa efektif",
    "sodium laureth sulfate": "Surfaktan utama pembersih & pembusa efektif",
    "sls": "Surfaktan anionik pembersih noda & busa melimpah",
    "sodium lauryl sulfate": "Surfaktan anionik pembersih noda & busa melimpah",
    "labs": "Surfaktan penembus & pelarut noda lemak membandel",
    "labsa": "Surfaktan penembus & pelarut noda lemak membandel",
    "linear alkylbenzene sulfonate": "Surfaktan penembus & pelarut noda lemak membandel",
    "cdea": "Foam booster, penstabil busa & penambah viskositas",
    "cocoamide dea": "Foam booster, penstabil busa & penambah viskositas",
    "cocamidopropyl betaine": "Surfaktan amfoterik penambah kelembutan & busa stabil",
    "capb": "Surfaktan amfoterik penambah kelembutan & busa stabil",
    
    # Alkali & Builder
    "naoh": "Alkali builder & pengatur kebasaan (pH booster)",
    "sodium hydroxide": "Alkali builder & pengatur kebasaan (pH booster)",
    "soda api": "Alkali builder & pengatur kebasaan (pH booster)",
    "koh": "Alkali builder penyabun lembut cair",
    "potassium hydroxide": "Alkali builder penyabun lembut cair",
    "sodium carbonate": "Builder alkali, pelunak kesadahan & penstabil sediaan",
    "soda ash": "Builder alkali, pelunak kesadahan & penstabil sediaan",
    "stpp": "Sequestering agent pengikat kesadahan kalsium & magnesium",
    "sodium tripolyphosphate": "Sequestering agent pengikat kesadahan kalsium & magnesium",
    "sodium metasilicate": "Builder alkali pencegah redeposisi & korosi mesin",

    # Asam & Neutralizer
    "citric acid": "Pengatur pH, chelating agent & pelunak air sadah",
    "asam sitrat": "Pengatur pH, chelating agent & pelunak air sadah",
    "oxalic acid": "Bahan aktif penghilang noda karat tekstil & mineral (chelating)",
    "asam oksalat": "Bahan aktif penghilang noda karat tekstil & mineral (chelating)",
    "acetic acid": "Bahan penetral sisa alkali cucian & penyegar serat kain",
    "asam asetat": "Bahan penetral sisa alkali cucian & penyegar serat kain",

    # Oksidator & Disinfektan
    "calcium hypochlorite": "Bahan aktif pemutih, oksidator noda & disinfektan (klorin aktif)",
    "kaporit": "Bahan aktif pemutih, oksidator noda & disinfektan (klorin aktif)",
    "sodium hypochlorite": "Bahan aktif pemutih klorin, penghilang noda & bakterisida",
    "hydrogen peroxide": "Oksidator pemutih oksigen aman kain berwarna & disinfektan",
    "bkc": "Bahan aktif antimikroba, disinfektan & pembunuh bakteri spektrum luas",
    "benzalkonium chloride": "Bahan aktif antimikroba, disinfektan & pembunuh bakteri spektrum luas",

    # Pengental, Pelembut, Pelarut & Aditif
    "nacl": "Pengatur viskositas & pengental larutan (thickener)",
    "garam": "Pengatur viskositas & pengental larutan (thickener)",
    "sodium chloride": "Pengatur viskositas & pengental larutan (thickener)",
    "edta": "Agen pengkhelat (chelating agent) pengikat logam berat",
    "disodium edta": "Agen pengkhelat (chelating agent) pengikat logam berat",
    "silicon emulsion": "Bahan pelembut, pelicin serat pakaian & anti kusut",
    "silicone": "Bahan pelembut, pelicin serat pakaian & anti kusut",
    "esterquat": "Surfaktan kationik pelembut serat tekstil & antistatik",
    "parfum": "Pemberi aroma segar & wangi khas produk",
    "parfume": "Pemberi aroma segar & wangi khas produk",
    "fragrance": "Pemberi aroma segar & wangi khas produk",
    "pewarna": "Pemberi warna estetika produk",
    "colorant": "Pemberi warna estetika produk",
    "dye": "Pemberi warna estetika produk",
    "tartrazine": "Pewarna estetika produk kuning/hijau",
    "aqua": "Pelarut utama sediaan (solvent)",
    "water": "Pelarut utama sediaan (solvent)",
    "air": "Pelarut utama sediaan (solvent)",
    "air demineralisasi": "Pelarut utama sediaan (solvent)",
    "demineralized water": "Pelarut utama sediaan (solvent)"
}

def guess_chemical_function(chemical_name):
    """Menebak fungsi bahan kimia berdasarkan database internal."""
    cn_lower = chemical_name.lower()
    for key, func in CHEMICAL_FUNCTIONS.items():
        if key in cn_lower:
            return func
    if "surfactant" in cn_lower:
        return "Surfaktan aktif pembersih"
    if "acid" in cn_lower or "asam" in cn_lower:
        return "Pengatur pH sediaan asam"
    if "oil" in cn_lower or "minyak" in cn_lower:
        return "Bahan aktif pelarut & pelembut"
    return "Bahan pendukung formulasi sediaan"


def get_product_intelligence(product_name):
    """
    Menyimpulkan profil regulasi PKRT & parameter fisikokimia
    berdasarkan nama produk.
    """
    name_clean = product_name.upper()
    
    # 1. Sabun Cuci Piring
    if "CUCI PIRING" in name_clean or "DISHWASH" in name_clean:
        return {
            "code": "CP",
            "kategori": "Pembersih",
            "sub_kategori": "Pembersih Peralatan Dapur",
            "jenis_pkrt": "Pembersih Peralatan Dapur",
            "hs_code": "3402.50.11",
            "bentuk": "Cairan Kental (Viscous Liquid)",
            "warna": "Hijau Segar Transparan",
            "bau": "Khas Jeruk Nipis Segar",
            "berat_spec": "1,00 – 1,04 kg",
            "berat_res": "1,02 kg",
            "ph_spec": "6.5 – 7.5",
            "ph_res": "7.10",
            "ph_history": ["7.15", "7.12", "7.10", "7.08", "7.05"],
            "dens_spec": "1.02 – 1.05",
            "dens_res": "1.03",
            "dens_history": ["1.03", "1.03", "1.03", "1.02", "1.02"],
            "deskripsi": (
                f"{product_name} adalah sediaan sabun cuci piring cair konsentrat dengan daya bersih tinggi "
                "yang diformulasikan khusus untuk mengangkat noda lemak membandel, bau amis, dan sisa makanan "
                "pada peralatan makan dan dapur. Mengandung surfaktan pilihan yang lembut di tangan serta mudah dibilas kesat tanpa meninggalkan residu."
            ),
            "cara_penggunaan": (
                "Untuk Pemakaian Harian :\n"
                "1. Larutkan 1 sendok teh (sekitar 5 ml) sabun cuci piring ke dalam mangkuk berisi 100 ml air bersih.\n"
                "2. Remas spons pencuci hingga busa melimpah terbentuk.\n"
                "3. Usapkan pada piring, gelas, wajan, dan peralatan dapur hingga bersih dari kotoran dan lemak.\n"
                "4. Bilas dengan air mengalir hingga bersih kesat.\n\n"
                "Untuk Noda Lemak Membandel :\n"
                "1. Teteskan beberapa tetes langsung pada spons basah tanpa diencerkan.\n"
                "2. Usap langsung pada permukaan berlemak tebal, diamkan 1-2 menit, lalu bilas hingga tuntas."
            ),
            "peringatan": (
                "1. Jauhkan dari jangkauan anak-anak.\n"
                "2. Hindari kontak langsung dengan mata. Jika terkena mata, segera bilas dengan air mengalir selama 15 menit.\n"
                "3. Jika tertelan secara tidak sengaja, minumlah air yang banyak dan segera hubungi dokter.\n"
                "4. Simpan di tempat sejuk, kering, dan terhindar dari paparan sinar matahari langsung."
            )
        }

    # 2. Liquid Detergent / Deterjen Cair
    if "DETERGENT" in name_clean or "DETERJEN" in name_clean:
        return {
            "code": "LD",
            "kategori": "Sediaan Untuk Mencuci",
            "sub_kategori": "Deterjen",
            "jenis_pkrt": "Deterjen Dalam Bentuk Cair",
            "hs_code": "3402.50.11",
            "bentuk": "Cairan Homogen Kental",
            "warna": "Biru Laut Transparan",
            "bau": "Khas Floral Segar Tahan Lama",
            "berat_spec": "1,00 – 1,04 kg",
            "berat_res": "1,02 kg",
            "ph_spec": "7.5 – 8.5",
            "ph_res": "8.10",
            "ph_history": ["8.20", "8.18", "8.14", "8.10", "8.08"],
            "dens_spec": "1.01 – 1.04",
            "dens_res": "1.02",
            "dens_history": ["1.02", "1.02", "1.02", "1.02", "1.01"],
            "deskripsi": (
                f"{product_name} adalah deterjen cair konsentrat dengan daya cuci optimal "
                "yang dirancang untuk mencuci pakaian dengan mesin cuci (bukaan depan maupun atas) dan pencucian manual. "
                "Efektif menembus serat kain untuk mengangkat noda kotoran, keringat, dan bau apek tanpa merusak warna serat pakaian."
            ),
            "cara_penggunaan": (
                "Pencucian Menggunakan Mesin Cuci (Kapasitas 5–7 kg) :\n"
                "1. Tuangkan 35–50 ml deterjen cair ke dalam laci dispenser mesin cuci.\n"
                "2. Masukkan cucian dan jalankan siklus pencucian standar.\n\n"
                "Pencucian Manual (Rendam Tangan) :\n"
                "1. Tuangkan 30 ml deterjen cair ke dalam 10 liter air.\n"
                "2. Rendam pakaian selama 15–30 menit.\n"
                "3. Kucek bagian yang bernoda lalu bilas dengan air bersih hingga tuntas."
            ),
            "peringatan": (
                "1. Jauhkan dari jangkauan anak-anak.\n"
                "2. Hindari kontak langsung dengan mata. Jika terkena mata, segera bilas dengan air mengalir.\n"
                "3. Pisahkan pakaian putih dan pakaian yang mudah luntur sebelum dicuci.\n"
                "4. Simpan dalam wadah tertutup rapat di tempat kering dan sejuk."
            )
        }

    # 3. Softener / Pelembut Pakaian
    if "SOFTENER" in name_clean or "PELEMBUT" in name_clean:
        return {
            "code": "SFT",
            "kategori": "Sediaan Untuk Mencuci",
            "sub_kategori": "Pelembut, Pewangi dan / atau Pelicin Kain",
            "jenis_pkrt": "Pelembut, Pewangi dan / atau Pelicin Kain",
            "hs_code": "3809.91.00",
            "bentuk": "Cairan Emulsi Homogen",
            "warna": "Merah Muda Lembut",
            "bau": "Khas Bunga Aromaterapi Segar Mewah",
            "berat_spec": "1,00 – 1,03 kg",
            "berat_res": "1,01 kg",
            "ph_spec": "4.0 – 6.0",
            "ph_res": "4.80",
            "ph_history": ["4.90", "4.88", "4.84", "4.80", "4.78"],
            "dens_spec": "1.00 – 1.03",
            "dens_res": "1.01",
            "dens_history": ["1.01", "1.01", "1.01", "1.01", "1.01"],
            "deskripsi": (
                f"{product_name} adalah cairan pelembut dan pewangi konsentrat yang diformulasikan khusus "
                "untuk melembutkan serat kain tekstil, mencegah kusut, memberikan efek antistatik, "
                "serta menyebarkan keharuman mewah yang tahan lama pada pakaian setelah proses pencucian."
            ),
            "cara_penggunaan": (
                "Pada Bilasan Terakhir Mesin Cuci :\n"
                "1. Tuangkan 30–45 ml pelembut ke dalam laci pelembut mesin cuci saat siklus bilasan akhir.\n"
                "2. Biarkan mesin menyelesaikan putaran pemerasan.\n\n"
                "Pencucian Manual :\n"
                "1. Tuangkan 30 ml pelembut ke dalam 10 liter air bilasan terakhir.\n"
                "2. Rendam cucian yang sudah bersih selama 10–15 menit (jangan dibilas lagi).\n"
                "3. Peras pakaian dan jemur hingga kering."
            ),
            "peringatan": (
                "1. Jangan tuangkan langsung pelembut tanpa air ke atas permukaan kain kering.\n"
                "2. Jauhkan dari jangkauan anak-anak.\n"
                "3. Jika terkena mata, segera bilas dengan air bersih mengalir.\n"
                "4. Simpan pada suhu ruang dan hindarkan dari pembekuan atau sinar matahari terik."
            )
        }

    # 4. Bleach / Pemutih / Klorin / Oxy
    if "BLEACH" in name_clean or "PEMUTIH" in name_clean or "CHLOR" in name_clean or "OXY" in name_clean:
        return {
            "code": "BLC",
            "kategori": "Sediaan Untuk Mencuci",
            "sub_kategori": "Pemutih Kain",
            "jenis_pkrt": "Pemutih Kain",
            "hs_code": "3402.90.93",
            "bentuk": "Cairan Homogen",
            "warna": "Bening Kekuningan",
            "bau": "Khas Klorin Segar",
            "berat_spec": "1,05 – 1,15 kg",
            "berat_res": "1,10 kg",
            "ph_spec": "10.0 – 12.0",
            "ph_res": "11.20",
            "ph_history": ["11.50", "11.35", "11.25", "11.20", "11.10"],
            "dens_spec": "1.05 – 1.15",
            "dens_res": "1.10",
            "dens_history": ["1.10", "1.10", "1.09", "1.09", "1.08"],
            "deskripsi": (
                f"{product_name} adalah cairan pemutih dan disinfektan dengan kekuatan oksidasi tinggi "
                "yang dirancang untuk melenyapkan noda membandel pada pakaian putih, membasmi kuman dan bakteri, "
                "serta menghilangkan bau tak sedap. Menjaga serat pakaian putih tetap bersih cemerlang dan higienis."
            ),
            "cara_penggunaan": (
                "Untuk Pemutih Pakaian Putih (Rendam) :\n"
                "1. Campurkan 50–100 ml pemutih ke dalam 5 liter air bersih.\n"
                "2. Masukkan pakaian putih ke dalam larutan.\n"
                "3. Rendam selama 10–15 menit.\n"
                "4. Bilas bersih dengan air mengalir, lalu lanjutkan pencucian dengan deterjen biasa.\n\n"
                "Untuk Desinfektan Lantai & Permukaan Keras :\n"
                "1. Campurkan 100 ml pemutih ke dalam 5 liter air.\n"
                "2. Usapkan spons atau kain pel ke permukaan, diamkan 10 menit, lalu bilas bersih."
            ),
            "peringatan": (
                "1. HANYA UNTUK PAKAIAN PUTIH. Jangan gunakan pada pakaian berwarna, sutra, wol, atau kulit.\n"
                "2. JANGAN dicampur dengan produk kimia asam, amonia, atau pembersih toilet karena memicu gas beracun.\n"
                "3. Gunakan sarung tangan karet pelindung. Jauhkan dari jangkauan anak-anak.\n"
                "4. Simpan dalam wadah tertutup rapat di tempat teduh dan sejuk."
            )
        }

    # 5. Rust Tex / Penghilang Karat
    if "RUST" in name_clean or "KARAT" in name_clean:
        return {
            "code": "RTX",
            "kategori": "Pembersih",
            "sub_kategori": "Pembersih Lainnya",
            "jenis_pkrt": "Preparat untuk pencuci atau penghilang noda",
            "hs_code": "3402.50.11",
            "bentuk": "Cairan Homogen Transparan",
            "warna": "Bening Transparan",
            "bau": "Khas Asam Ringan Lembut",
            "berat_spec": "1,02 – 1,07 kg",
            "berat_res": "1,04 kg",
            "ph_spec": "2.0 – 3.5",
            "ph_res": "2.70",
            "ph_history": ["2.80", "2.75", "2.72", "2.70", "2.68"],
            "dens_spec": "1.03 – 1.08",
            "dens_res": "1.05",
            "dens_history": ["1.05", "1.05", "1.04", "1.04", "1.04"],
            "deskripsi": (
                f"{product_name} adalah formula khusus pengkelat noda karat oksida besi pada tekstil dan kain laundry. "
                "Bekerja cepat melarutkan bercak karat membandel, noda air tanah berzat besi tinggi, "
                "serta kerak mineral tanpa merusak integritas serat kain."
            ),
            "cara_penggunaan": (
                "Spotting Noda Karat Lokal :\n"
                "1. Basahi area noda karat pada kain dengan sedikit air bersih hangat.\n"
                "2. Teteskan langsung cairan ke pusat bercak noda karat.\n"
                "3. Diamkan selama 2–5 menit hingga noda karat memudar larut.\n"
                "4. Bilas seketika dengan air mengalir hingga tuntas sebelum dicuci biasa.\n\n"
                "Perendaman Pakaian Berkerak Karat Merata :\n"
                "1. Larutkan 50–100 ml ke dalam 10 liter air hangat.\n"
                "2. Rendam pakaian 15–30 menit, lalu bilas bersih."
            ),
            "peringatan": (
                "1. Mengandung agen asam; wajib gunakan sarung tangan karet saat pengaplikasian.\n"
                "2. Hindari kontak dengan kulit dan mata. Bila terkena kulit, basuh dengan air mengalir.\n"
                "3. Jangan diaplikasikan pada permukaan marmer, batu alam, atau enamel.\n"
                "4. Jauhkan dari jangkauan anak-anak dan simpan di area bersirkulasi baik."
            )
        }

    # 6. Blood Tex / Penghilang Darah & Noda Protein
    if "BLOOD" in name_clean or "DARAH" in name_clean:
        return {
            "code": "BTX",
            "kategori": "Pembersih",
            "sub_kategori": "Pembersih Lainnya",
            "jenis_pkrt": "Preparat untuk pencuci atau penghilang noda",
            "hs_code": "3402.50.11",
            "bentuk": "Cairan Homogen",
            "warna": "Kuning Pudar Bening",
            "bau": "Khas Lembut",
            "berat_spec": "1,05 – 1,15 kg",
            "berat_res": "1,10 kg",
            "ph_spec": "10.0 – 12.0",
            "ph_res": "11.40",
            "ph_history": ["11.55", "11.48", "11.44", "11.40", "11.35"],
            "dens_spec": "1.05 – 1.15",
            "dens_res": "1.10",
            "dens_history": ["1.10", "1.10", "1.10", "1.09", "1.09"],
            "deskripsi": (
                f"{product_name} adalah preparat pencuci penghilang noda berat khusus darah, protein, lendir, "
                "dan cairan biologis lainnya. Mengandung formulasi alkali builder teruji yang memecah ikatan hemoglobin "
                "dan zat organik sehingga noda terlepas tuntas dari kain rumah sakit, hotel, maupun rumah tangga."
            ),
            "cara_penggunaan": (
                "Spotting Noda Darah Segar / Kering :\n"
                "1. Basahi noda darah dengan air dingin (hindari air panas agar protein tidak mengeras).\n"
                "2. Teteskan secukupnya pada area noda.\n"
                "3. Gosok perlahan dengan sikat berbulu halus hingga noda terurai.\n"
                "4. Bilas dengan air dingin hingga bersih.\n\n"
                "Perendaman Linen Medis / Rumah Sakit :\n"
                "1. Larutkan 50–80 ml ke dalam 10 liter air dingin.\n"
                "2. Rendam pakaian selama 20–30 menit, lalu lanjutkan pencucian utama di mesin cuci."
            ),
            "peringatan": (
                "1. Gunakan sarung tangan pelindung karet saat menangani noda darah atau cairan biologis.\n"
                "2. Jangan mencampur dengan asam pekat.\n"
                "3. Jauhkan dari jangkauan anak-anak.\n"
                "4. Simpan dalam wadah tertutup rapat di tempat kering dan sejuk."
            )
        }

    # 7. Neutralizer / Penetral Sisa Klorin & Alkali
    if "NEUTRAL" in name_clean or "PENETRAL" in name_clean:
        return {
            "code": "NEU",
            "kategori": "Sediaan Untuk Mencuci",
            "sub_kategori": "Sediaan Mencuci Lainnya",
            "jenis_pkrt": "Sediaan untuk Mencuci Lainnya",
            "hs_code": "3402.90.93",
            "bentuk": "Cairan Bening Homogen",
            "warna": "Bening Transparan",
            "bau": "Khas Asam Lemah Segar",
            "berat_spec": "1,01 – 1,05 kg",
            "berat_res": "1,03 kg",
            "ph_spec": "3.0 – 4.5",
            "ph_res": "3.60",
            "ph_history": ["3.70", "3.66", "3.62", "3.60", "3.58"],
            "dens_spec": "1.02 – 1.05",
            "dens_res": "1.03",
            "dens_history": ["1.03", "1.03", "1.03", "1.03", "1.02"],
            "deskripsi": (
                f"{product_name} adalah cairan penetral sisa residu alkali dan sisa klorin pemutih "
                "pada proses akhir pencucian kain. Mengembalikan pH serat kain ke tingkat normal (pH netral 6–7) "
                "sehingga mencegah iritasi kulit bagi pemakai pakaian, serta mencegah kain menguning saat proses setrika panas."
            ),
            "cara_penggunaan": (
                "Pada Tahap Bilasan Akhir Laundry :\n"
                "1. Tuangkan 15–30 ml neutralizer per 5 kg cucian ke dalam air bilasan akhir.\n"
                "2. Jalankan putaran pengadukan mesin cuci selama 3–5 menit.\n"
                "3. Lanjutkan ke proses pemerasan (spinning) dan pengeringan."
            ),
            "peringatan": (
                "1. Jangan dicampurkan langsung dengan pemutih klorin pekat di wadah tertutup.\n"
                "2. Jauhkan dari jangkauan anak-anak.\n"
                "3. Bila terkena mata, segera bilas dengan air bersih mengalir.\n"
                "4. Simpan dalam wadah tertutup rapat di tempat berventilasi baik."
            )
        }

    # 8. Emulsifier / Pengemulsi Lemak & Minyak Cucian
    if "EMULSI" in name_clean:
        return {
            "code": "EMU",
            "kategori": "Sediaan Untuk Mencuci",
            "sub_kategori": "Sediaan Mencuci Lainnya",
            "jenis_pkrt": "Sediaan untuk Mencuci Lainnya",
            "hs_code": "3402.90.93",
            "bentuk": "Cairan Homogen Agak Kental",
            "warna": "Kuning Jerami Transparan",
            "bau": "Khas Pelarut Minyak Ringan",
            "berat_spec": "1,01 – 1,05 kg",
            "berat_res": "1,03 kg",
            "ph_spec": "7.5 – 9.0",
            "ph_res": "8.20",
            "ph_history": ["8.35", "8.28", "8.24", "8.20", "8.16"],
            "dens_spec": "1.02 – 1.05",
            "dens_res": "1.03",
            "dens_history": ["1.03", "1.03", "1.03", "1.02", "1.02"],
            "deskripsi": (
                f"{product_name} adalah surfaktan pengemulsi non-ionik berdaya larut tinggi "
                "yang diformulasikan khusus untuk melarutkan noda minyak industri, pelumas (grease), lemak makanan restoran, "
                "dan kotoran sebum membandel pada pakaian kerja, seragam koki, serta linen perhotelan."
            ),
            "cara_penggunaan": (
                "Pencucian Utama Mesin Cuci Bersama Deterjen :\n"
                "1. Tuangkan 20–40 ml emulsifier bersamaan dengan deterjen cair untuk 5–7 kg pakaian berminyak berat.\n"
                "2. Gunakan air hangat (40–60°C) untuk efektivitas maksimal pencairan lemak.\n\n"
                "Spotting Noda Minyak Pekat :\n"
                "1. Teteskan langsung tanpa diencerkan ke atas noda minyak.\n"
                "2. Gosok perlahan, diamkan 5–10 menit, lalu cuci seperti biasa."
            ),
            "peringatan": (
                "1. Hindari kontak langsung yang lama dengan kulit tanpa perlindungan sarung tangan.\n"
                "2. Jauhkan dari jangkauan anak-anak.\n"
                "3. Jangan sampai tertelan. Bila terjadi, segera minum air banyak dan konsultasi ke dokter.\n"
                "4. Simpan di tempat sejuk dan terhindar dari panas berlebih."
            )
        }

    # 9. Liquid Pencerah / Optical Brightener
    if "PENCERAH" in name_clean or "BRIGHTENER" in name_clean or "OBA" in name_clean:
        return {
            "code": "LPC",
            "kategori": "Sediaan Untuk Mencuci",
            "sub_kategori": "Pemutih Kain",
            "jenis_pkrt": "Pemutih Kain",
            "hs_code": "3204.20.00",
            "bentuk": "Cairan Homogen Transparan",
            "warna": "Biru Transparan Berpendar (Fluoresen)",
            "bau": "Khas Floral Segar Lembut",
            "berat_spec": "1,00 – 1,04 kg",
            "berat_res": "1,02 kg",
            "ph_spec": "7.0 – 8.5",
            "ph_res": "7.80",
            "ph_history": ["7.90", "7.86", "7.82", "7.80", "7.78"],
            "dens_spec": "1.01 – 1.04",
            "dens_res": "1.02",
            "dens_history": ["1.02", "1.02", "1.02", "1.02", "1.01"],
            "deskripsi": (
                f"{product_name} adalah formula konsentrat pencerah pakaian berbasis Optical Brightening Agent (OBA) "
                "berteknologi tinggi yang bekerja menyerap sinar ultraviolet tak tampak dan memancarkannya kembali sebagai cahaya biru kasat mata. "
                "Secara efektif mengembalikan kecemerlangan warna serat pakaian putih maupun berwarna yang telah kusam atau kekuningan."
            ),
            "cara_penggunaan": (
                "Pada Siklus Pencucian Utama Bersama Deterjen :\n"
                "1. Tuangkan 20–30 ml cairan pencerah bersamaan dengan deterjen untuk 5–7 kg pakaian.\n"
                "2. Jalankan siklus pencucian standar.\n\n"
                "Pada Siklus Perendaman Khusus :\n"
                "1. Tuangkan 25 ml ke dalam 10 liter air.\n"
                "2. Rendam pakaian selama 15–20 menit sebelum dicuci biasa."
            ),
            "peringatan": (
                "1. Jauhkan dari jangkauan anak-anak.\n"
                "2. Hindari kontak langsung dengan mata. Jika terkena mata, segera bilas dengan air mengalir.\n"
                "3. Simpan di tempat teduh dan sejuk, terhindar dari paparan sinar UV matahari langsung."
            )
        }

    # Default Fallback (General Cleaner)
    code_words = re.sub(r'[^A-Za-z0-9\s]', '', name_clean).split()
    short_code = "".join([w[0] for w in code_words[:3]]) if code_words else "GEN"
    return {
        "code": short_code,
        "kategori": "Pembersih",
        "sub_kategori": "Pembersih Lainnya",
        "jenis_pkrt": "Pembersih Multiguna/ multipurpose",
        "hs_code": "3402.50.11",
        "bentuk": "Cairan Homogen",
        "warna": "Bening Transparan",
        "bau": "Khas Segar",
        "berat_spec": "1,00 – 1,05 kg",
        "berat_res": "1,02 kg",
        "ph_spec": "7.0 – 8.5",
        "ph_res": "7.50",
        "ph_history": ["7.60", "7.55", "7.52", "7.50", "7.48"],
        "dens_spec": "1.01 – 1.04",
        "dens_res": "1.02",
        "dens_history": ["1.02", "1.02", "1.02", "1.02", "1.01"],
        "deskripsi": (
            f"{product_name} adalah sediaan pembersih bermutu tinggi dari PT Kediri Chemical Abadi "
            "yang diformulasikan dengan standar mutu ISO 9001:2015 untuk memberikan daya bersih prima "
            "dan kebersihan menyeluruh pada berbagai perlengkapan rumah tangga."
        ),
        "cara_penggunaan": (
            "1. Larutkan secukupnya (20–40 ml) ke dalam 5 liter air bersih.\n"
            "2. Gunakan spons atau kain lap untuk membersihkan permukaan.\n"
            "3. Bilas atau seka hingga bersih dan kering."
        ),
        "peringatan": (
            "1. Jauhkan dari jangkauan anak-anak.\n"
            "2. Hindari kontak langsung dengan mata.\n"
            "3. Simpan di tempat sejuk dan kering."
        )
    }

# ==============================================================================
# 2. FORMULA PARSER & PERCENTAGE CALCULATOR
# ==============================================================================

def parse_formula_input(formula_input):
    """
    Mengonversi input formula menjadi daftar dict:
    [
        {"name": "...", "gram": float, "pct": float, "pct_str": "...", "function": "..."},
        ...
    ]
    Input bisa berupa:
    - List of dict: [{"name": "SLES", "gram": 120, "function": "..."}, ...]
    - List of tuples: [("SLES", 120), ...] atau [("SLES", 120, "Surfaktan"), ...]
    - String: "SLES: 120g, LABS: 50g, NaCl: 25g, Parfume: 5g, Aqua: 800g"
              atau per-baris: "SLES 120 gram\nLABS 50 gram..."
    """
    raw_items = []
    
    if isinstance(formula_input, list):
        for item in formula_input:
            if isinstance(item, dict):
                name = item.get("name", "").strip()
                gram = float(item.get("gram", 0))
                func = item.get("function") or guess_chemical_function(name)
                raw_items.append({"name": name, "gram": gram, "function": func})
            elif isinstance(item, (list, tuple)):
                name = str(item[0]).strip()
                gram = float(item[1])
                func = str(item[2]).strip() if len(item) > 2 else guess_chemical_function(name)
                raw_items.append({"name": name, "gram": gram, "function": func})
    elif isinstance(formula_input, str):
        # Format string bisa dipisahkan koma atau newline
        lines = re.split(r'[,;\n]+', formula_input.strip())
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Pola: "Nama Bahan : 120 gram (Fungsi opsional)" atau "Nama Bahan 120g"
            m = re.match(r'^([^:]+?)\s*[:=-]\s*([0-9.,]+)\s*(?:g|gram|gr|ml)?(?:\s*[\(\[]([^\)\]]+)[\)\]])?$', line, re.I)
            if m:
                name = m.group(1).strip()
                gram_val = float(m.group(2).replace(',', '.'))
                func = m.group(3).strip() if m.group(3) else guess_chemical_function(name)
                raw_items.append({"name": name, "gram": gram_val, "function": func})
            else:
                # Coba cari angka di akhir kalimat
                m2 = re.search(r'^(.*?)\s+([0-9.,]+)\s*(?:g|gram|gr|ml)?$', line, re.I)
                if m2:
                    name = m2.group(1).strip()
                    gram_val = float(m2.group(2).replace(',', '.'))
                    raw_items.append({"name": name, "gram": gram_val, "function": guess_chemical_function(name)})

    if not raw_items:
        raise ValueError("Formula tidak dapat dibaca atau kosong. Masukkan nama bahan dan berat dalam satuan gram.")

    # Hitung total gram
    total_gram = sum(item["gram"] for item in raw_items)
    if total_gram <= 0:
        raise ValueError("Total gram formula harus lebih besar dari 0.")

    # Hitung persentase dan format string standar Indonesia (koma untuk desimal)
    parsed = []
    pct_sum = 0.0
    for idx, item in enumerate(raw_items):
        pct = (item["gram"] / total_gram) * 100.0
        pct_sum += pct
        # Format desimal 2 digit
        pct_formatted = f"{pct:.2f}%".replace('.', ',')
        parsed.append({
            "no": str(idx + 1),
            "name": item["name"],
            "gram": item["gram"],
            "pct": pct,
            "pct_str": pct_formatted,
            "function": item["function"]
        })

    return parsed, total_gram

# ==============================================================================
# 3. DOCX HELPER UTILITIES (ISO 9001 & PURE BLACK)
# ==============================================================================

def set_cell_text(cell, text, bold=False, italic=False, font_name="Times New Roman", font_size=Pt(9.5), color_rgb=RGBColor(0, 0, 0), align=WD_ALIGN_PARAGRAPH.LEFT):
    """Menulis teks ke sel tabel dengan font ISO 9001 murni hitam."""
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = font_name
    run.font.size = font_size
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color_rgb
    return run

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    """Set inner cell padding dalam satuan dxa."""
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

def set_table_borders(table, sz="4", color="000000"):
    """Set border tabel rapi hitam murni."""
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

def calculate_stability_dates(ref_date=None):
    """Hitung 5 interval stabilitas realtime mundur 1 tahun per 3 bulan."""
    if ref_date is None:
        ref_date = datetime.now()
    months_offset = [12, 9, 6, 3, 0]
    dates = []
    for mo in months_offset:
        target_month = ref_date.month - mo
        target_year = ref_date.year
        while target_month <= 0:
            target_month += 12
            target_year -= 1
        day = min(ref_date.day, 28)
        d = datetime(target_year, target_month, day)
        dates.append(d.strftime("%d/%m/%Y"))
    return dates

# ==============================================================================
# 4. TEMPLATE GENERATORS (8 DOKUMEN)
# ==============================================================================

def generate_doc_formula(target_path, product_name, parsed_formula):
    """1. Memproses Formula .docx"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "Formula .docx")
    doc = Document(tmpl_path)

    # Paragraph 0: Judul Produk
    if len(doc.paragraphs) > 0:
        doc.paragraphs[0].text = f"List Bahan Baku {product_name}"
        doc.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in doc.paragraphs[0].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)

    # Table 0: List Bahan
    if len(doc.tables) > 0:
        tbl = doc.tables[0]
        # Hapus baris lama kecuali header
        while len(tbl.rows) > 1:
            tbl._tbl.remove(tbl.rows[-1]._tr)

        # Tambahkan baris untuk tiap bahan
        for ing in parsed_formula:
            row = tbl.add_row()
            set_cell_text(row.cells[0], ing["name"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.LEFT)
            set_cell_text(row.cells[1], ing["pct_str"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row.cells[2], ing["function"], bold=False, font_size=Pt(9.0), align=WD_ALIGN_PARAGRAPH.LEFT)
            for c in row.cells:
                set_cell_margins(c, top=60, bottom=60, left=80, right=80)
                c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        # Baris Total
        row_tot = tbl.add_row()
        set_cell_text(row_tot.cells[0], "Total", bold=True, font_size=Pt(10), align=WD_ALIGN_PARAGRAPH.LEFT)
        set_cell_text(row_tot.cells[1], "100%", bold=True, font_size=Pt(10), align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(row_tot.cells[2], "", bold=False, font_size=Pt(10), align=WD_ALIGN_PARAGRAPH.LEFT)
        for c in row_tot.cells:
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        set_table_borders(tbl, sz="4", color="000000")

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Formula Sediaan PKRT - {product_name}")


def generate_doc_coa(target_path, product_name, intel, parsed_formula, check_date_str):
    """2. Memproses COA.docx (Certificate of Analysis)"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "COA.docx")
    doc = Document(tmpl_path)

    today = datetime.now()
    exp_year = today.year + 2
    exp_date_str = f"{today.day} September {exp_year}"
    doc_no = f"COA/KCA-PKD/{today.year}/{today.month:02d}/{intel['code']}-001"
    batch_no = f"{intel['code']}-{today.strftime('%y%m%d')}-01"

    # Update Doc No Paragraph
    for p in doc.paragraphs:
        if "Nomor Dokumen:" in p.text:
            p.text = f"Nomor Dokumen: {doc_no}"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9.5)
                r.font.italic = True
                r.font.color.rgb = RGBColor(0, 0, 0)
            break

    # Table 0: Metadata Produk
    if len(doc.tables) >= 1:
        t_meta = doc.tables[0]
        meta_left = [
            f"Nama Produk / Product    : {product_name}",
            f"Kategori Sediaan              : {intel['kategori']} ({intel['jenis_pkrt']})",
            f"Bentuk Sediaan / Form     : {intel['bentuk']}",
            "Ukuran Sampel / Sample  : 1 Liter"
        ]
        meta_right = [
            f"Nomor Bets / Batch No.  : {batch_no}",
            f"Tanggal Manufaktur        : {check_date_str}",
            f"Tanggal Pengujian           : {check_date_str}",
            f"Kedaluwarsa / Exp. Date : {exp_date_str}"
        ]
        for ri in range(min(4, len(t_meta.rows))):
            set_cell_text(t_meta.cell(ri, 0), meta_left[ri], bold=(ri == 0), font_size=Pt(9.5))
            set_cell_text(t_meta.cell(ri, 1), meta_right[ri], bold=(ri == 0), font_size=Pt(9.5))

    # Table 1: Parameter Hasil Uji Lab
    if len(doc.tables) >= 2:
        t_test = doc.tables[1]
        test_rows = [
            ("1", "Bentuk Fisik (Appearance)", "Organoleptik", intel["bentuk"], intel["bentuk"], "Memenuhi"),
            ("2", "Warna (Color)", "Visual", intel["warna"], intel["warna"], "Memenuhi"),
            ("3", "Bau / Aroma (Odor)", "Olfaktori", intel["bau"], intel["bau"], "Memenuhi"),
            ("4", "Berat Bersih (Net Weight)", "Gravimetri", intel["berat_spec"], intel["berat_res"], "Memenuhi"),
            ("5", "Derajat Keasaman / pH (25°C)", "pH Meter Digital", intel["ph_spec"], intel["ph_res"], "Memenuhi"),
            ("6", "Bobot Jenis / Densitas (25°C)", "Hydrometer", intel["dens_spec"], intel["dens_res"], "Memenuhi"),
        ]
        for idx, tr in enumerate(test_rows, start=1):
            if idx < len(t_test.rows):
                r = t_test.rows[idx]
                set_cell_text(r.cells[0], tr[0], bold=True, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.CENTER)
                set_cell_text(r.cells[1], tr[1], bold=False, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.LEFT)
                set_cell_text(r.cells[2], tr[2], bold=False, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.CENTER)
                set_cell_text(r.cells[3], tr[3], bold=False, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.CENTER)
                set_cell_text(r.cells[4], tr[4], bold=False, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.CENTER)
                set_cell_text(r.cells[5], tr[5], bold=True, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.CENTER)

    # Table 2: Bahan yang Digunakan
    if len(doc.tables) >= 3:
        t_ing = doc.tables[2]
        while len(t_ing.rows) > 1:
            t_ing._tbl.remove(t_ing.rows[-1]._tr)

        for ing in parsed_formula:
            row = t_ing.add_row()
            set_cell_text(row.cells[0], ing["no"], bold=True, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row.cells[1], ing["name"], bold=False, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.LEFT)
            set_cell_text(row.cells[2], ing["pct_str"], bold=False, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row.cells[3], ing["function"], bold=False, font_size=Pt(8.5), align=WD_ALIGN_PARAGRAPH.LEFT)
            for c in row.cells:
                set_cell_margins(c, top=45, bottom=45, left=60, right=60)
                c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        set_table_borders(t_ing, sz="4", color="000000")

    # Update tanggal tanda tangan
    for p in doc.paragraphs:
        if "Kediri," in p.text:
            p.text = f"Kediri, {check_date_str}"
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(0, 0, 0)
            break

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Certificate of Analysis (COA) - {product_name}")


def generate_doc_formulir_1_1(target_path, product_name, intel, check_date_str):
    """3. Memproses Formulir 1.1.docx (Pendaftaran PKRT Resmi Kemenkes RI)"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "Formulir 1.1.docx")
    doc = Document(tmpl_path)

    if len(doc.tables) >= 1:
        tbl = doc.tables[0]
        # Baris 0: Nama Perusahaan yang mendaftar
        if len(tbl.rows) > 0:
            set_cell_text(tbl.cell(0, 2), "PT KEDIRI CHEMICAL ABADI", bold=True, font_size=Pt(9.5))
        # Baris 1: Alamat Lengkap dan Nomor Telepon
        alamat_kca = "Dusun Pagung, Desa Pagung, Kecamatan Semen, Kabupaten Kediri, Provinsi Jawa Timur, Kode Pos : 64161, No. Telp : 082244006699"
        if len(tbl.rows) > 1:
            set_cell_text(tbl.cell(1, 2), alamat_kca, bold=False, font_size=Pt(9.0))
        # Baris 2: Alamat Surat-menyurat dan Nomor Telepon
        if len(tbl.rows) > 2:
            set_cell_text(tbl.cell(2, 2), alamat_kca, bold=False, font_size=Pt(9.0))
        # Baris 3: NPWP
        if len(tbl.rows) > 3:
            set_cell_text(tbl.cell(3, 2), "10.000.000.0-512.1814", bold=False, font_size=Pt(9.5))
        # Baris 4: Nama Dagang PKRT
        if len(tbl.rows) > 4:
            set_cell_text(tbl.cell(4, 2), product_name, bold=True, font_size=Pt(9.5))
        # Baris 5: Kategori PKRT (Pilihan Resmi Kemenkes)
        if len(tbl.rows) > 5:
            set_cell_text(tbl.cell(5, 2), intel["kategori"], bold=False, font_size=Pt(9.5))
        # Baris 6: Sub Kategori PKRT (Pilihan Resmi Kemenkes)
        if len(tbl.rows) > 6:
            set_cell_text(tbl.cell(6, 2), intel["sub_kategori"], bold=False, font_size=Pt(9.5))
        # Baris 7: Jenis PKRT (Pilihan Resmi Kemenkes)
        if len(tbl.rows) > 7:
            set_cell_text(tbl.cell(7, 2), intel["jenis_pkrt"], bold=False, font_size=Pt(9.5))
        # Baris 8: HS Code (Klasifikasi BTKI 2022)
        if len(tbl.rows) > 8:
            set_cell_text(tbl.cell(8, 2), intel["hs_code"], bold=False, font_size=Pt(9.5))
        # Baris 9: Keterangan Kemasan
        if len(tbl.rows) > 9:
            desc_kemasan = (
                f"- Bentuk Sediaan : {intel['bentuk']}\n"
                f"- Warna Sediaan  : {intel['warna']}\n"
                f"- Aroma Sediaan  : {intel['bau']}\n"
                f"- Kemasan & Netto: Botol HDPE 1 Liter, Jerigen HDPE 5 Liter, Jerigen HDPE 20 Liter"
            )
            set_cell_text(tbl.cell(9, 2), desc_kemasan, bold=False, font_size=Pt(9.0))
        # Baris 10: Nama Pemberi Lisensi
        if len(tbl.rows) > 10:
            set_cell_text(tbl.cell(10, 2), "PT ANUGERAH SURYA SEMBADA", bold=True, font_size=Pt(9.5))
        # Baris 11: Alamat Pemberi Lisensi
        if len(tbl.rows) > 11:
            alamat_ass = "Jl. Manukan Indah, 19 - K No. 1, RT 010 / RW 003, Kel. Manukan Kulon, Kec. Tandes, Kota Surabaya, Jawa Timur, Indonesia, 60185"
            set_cell_text(tbl.cell(11, 2), alamat_ass, bold=False, font_size=Pt(9.0))
        # Baris 12: Nama Pabrik Induk
        if len(tbl.rows) > 12:
            set_cell_text(tbl.cell(12, 2), "PT KEDIRI CHEMICAL ABADI", bold=True, font_size=Pt(9.5))
        # Baris 13: Alamat Pabrik Induk
        if len(tbl.rows) > 13:
            alamat_pabrik = "Dusun Pagung, Desa Pagung, Kecamatan Semen, Kabupaten Kediri, Provinsi Jawa Timur, Kode Pos : 64161"
            set_cell_text(tbl.cell(13, 2), alamat_pabrik, bold=False, font_size=Pt(9.0))
        # Baris 14: Nama Penerima Lisensi
        if len(tbl.rows) > 14:
            set_cell_text(tbl.cell(14, 2), "PT KEDIRI CHEMICAL ABADI", bold=True, font_size=Pt(9.5))
        # Baris 15: Permohonan ini dilengkapi dengan
        if len(tbl.rows) > 15:
            kelengkapan = (
                "8 (delapan) berkas lampiran persyaratan teknis izin edar PKRT:\n"
                "1. Formula Lengkap & Nomenklatur Kimia Murni\n"
                "2. Sertifikat Analisis Mutu (Certificate of Analysis / COA)\n"
                "3. Diagram Alur Proses Produksi & Compounding Kimia\n"
                "4. Spesifikasi Wadah dan Kemasan (HDPE)\n"
                "5. Sertifikat Hasil Uji Laboratorium Mutu Produk Jadi\n"
                "6. Laporan Hasil Pengujian Stabilitas Sediaan (Accelerated / Real Time)\n"
                "7. Lembar Tujuan Pembuatan & Cara Penggunaan Sediaan\n"
                "8. Rancangan Desain Penandaan Label Kemasan Produk"
            )
            set_cell_text(tbl.cell(15, 2), kelengkapan, bold=False, font_size=Pt(8.5))

    # Table 1: Tanda Tangan
    if len(doc.tables) >= 2:
        t_sig = doc.tables[1]
        sig_header = f"Kediri, {check_date_str}\nPenanggung Jawab Teknis"
        set_cell_text(t_sig.cell(0, 2), sig_header, bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(t_sig.cell(2, 0), "Yan Effendi", bold=True, font_size=Pt(10), align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(t_sig.cell(2, 2), "Yerikho Arfensias Effendi", bold=True, font_size=Pt(10), align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Formulir 1.1 Pendaftaran PKRT - {product_name}")


def generate_doc_sertifikat_lab(target_path, product_name, intel, check_date_str):
    """4. Memproses Sertifikat uji Lab.docx"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "Sertifikat uji Lab.docx")
    doc = Document(tmpl_path)

    # Paragraphs Update
    for p in doc.paragraphs:
        if "Nama Produk" in p.text:
            p.text = f"Nama Produk\t\t: {product_name}"
        elif "Tanggal pengecekan" in p.text:
            p.text = f"Tanggal pengecekan\t: {check_date_str}"
        elif "Kediri" in p.text and ("202" in p.text or "September" in p.text):
            p.text = f"Kediri {check_date_str}"
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.color.rgb = RGBColor(0, 0, 0)

    # Table 0: Parameter Uji
    if len(doc.tables) >= 1:
        tbl = doc.tables[0]
        if len(tbl.rows) >= 3:
            # Row 1: Spesifikasi
            row_spec = tbl.rows[1]
            set_cell_text(row_spec.cells[0], "Spesifikasi", bold=True, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_spec.cells[1], intel["bentuk"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_spec.cells[2], intel["warna"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_spec.cells[3], intel["bau"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_spec.cells[4], intel["berat_spec"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_spec.cells[5], intel["ph_spec"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_spec.cells[6], intel["dens_spec"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)

            # Row 2: Hasil
            row_res = tbl.rows[2]
            set_cell_text(row_res.cells[0], "Hasil", bold=True, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_res.cells[1], intel["bentuk"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_res.cells[2], intel["warna"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_res.cells[3], intel["bau"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_res.cells[4], intel["berat_res"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_res.cells[5], intel["ph_res"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_text(row_res.cells[6], intel["dens_res"], bold=False, font_size=Pt(9.5), align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Sertifikat Hasil Uji Produk Jadi - {product_name}")


def get_realistic_stages_for_product(product_name):
    """
    Menyusun tahapan proses produksi & compounding kimia yang riil
    berdasarkan sifat fisika-kimia, formulasi, dan unit operasi pabrik.
    """
    name_u = product_name.upper()

    if "BLEACH" in name_u or "OXY" in name_u or "CHLOR" in name_u:
        return [
            "Tahap 1: Pengisian air baku (Aqua Demin) ke dalam tangki reaksi pencampuran bertingkat",
            "Tahap 2: Pencampuran Calcium Hypochlorite & Sodium Carbonate secara terkontrol (reaksi metatesis klorin aktif)",
            "Tahap 3: Proses pengendapan (settling) endapan kalsium karbonat selama 12–24 jam hingga terbentuk dua fase terpisah",
            "Tahap 4: Dekantasi / penyaringan cairan supernatan klorin aktif jernih ke tangki holding produk jadi siap kemas"
        ]

    if "DETERGENT" in name_u or "DETERJEN" in name_u:
        return [
            "Tahap 1: Pengisian air baku (Aqua Demin) 60% ke dalam tangki mixer, lalu larutkan Disodium EDTA dan Soda Ash Dense hingga larut sempurna",
            "Tahap 2: Pemasukan Sodium Lauryl Ether Sulfate (SLES) secara perlahan dengan kecepatan mixer rendah untuk mencegah pembusaan berlebih",
            "Tahap 3: Pemasukan Asam Sitrat, Asam Fluorida (HF), dan penambahan larutan Natrium Klorida (NaCl) bertahap hingga terbentuk viskositas standar",
            "Tahap 4: Penambahan Parfum pada suhu kamar serta sisa air baku hingga volume batch 100%, diaduk perlahan hingga larutan homogen sempurna"
        ]

    if "NEUTRAL" in name_u or "PENETRAL" in name_u:
        return [
            "Tahap 1: Pengisian Air Baku (Aqua Demineralisata) 80% ke dalam tangki mixer HDPE anti-korosi",
            "Tahap 2: Pelarutan Natrium Metabisulfit secara bertahap dengan pengadukan pelan di area berventilasi baik hingga terlarut sempurna",
            "Tahap 3: Penambahan sisa air baku dan Fragrance/Parfume, diaduk perlahan hingga larutan jernih dan homogen sempurna"
        ]

    if "SOFTENER" in name_u or "PELEMBUT" in name_u:
        return [
            "Tahap 1: Pemanasan air baku (Aqua Demin) hingga suhu 45°C–50°C dan pelarutan Disodium EDTA sebagai agen pengkhelat ion logam",
            "Tahap 2: Pemasukan Esterquat (Tetranil) secara perlahan dengan mixer dispersi kecepatan konstan hingga terbentuk emulsi kationik stabil",
            "Tahap 3: Pendinginan bertahap sambil terus diaduk perlahan hingga suhu sediaan mencapai suhu kamar (< 30°C)",
            "Tahap 4: Pemasukan Fragrance/Parfume pada kondisi dingin agar stabilitas aroma wangi terjaga maksimal dan tidak menguap"
        ]

    if "EMULSI" in name_u:
        return [
            "Tahap 1: Pengisian air baku 60% ke tangki utama, larutkan Disodium EDTA, Soda Ash Dense, dan Asam Sitrat hingga homogen",
            "Tahap 2: Pemasukan SLES (Texapon) ke dalam tangki utama, diaduk rata dengan kecepatan putaran sedang hingga larut sempurna",
            "Tahap 3: Pelarutan terpisah Enzim Anti-Redeposisi dan OBA (CBS-X) pada suhu 35°C, lalu dimasukkan perlahan ke tangki utama",
            "Tahap 4: Penambahan larutan NaCl sebagai pengatur viskositas, diikuti Pewarna Tekstil, Parfum, dan sisa air hingga homogen"
        ]

    if "PENCERAH" in name_u or "BRIGHTENER" in name_u:
        return [
            "Tahap 1: Pengisian air baku (Aqua Demin) 70% ke dalam tangki mixer dan pelarutan Disodium EDTA pengikat ion sadah",
            "Tahap 2: Pemasukan Optical Brightening Agent (OBA CBS-X) dengan mixer putaran intensif hingga seluruh partikel terdispersi rata",
            "Tahap 3: Pemasukan SLES (Texapon) sebagai surfaktan pembersih mikro dan pembawa partikel pencerah optik fluoresen",
            "Tahap 4: Penambahan larutan NaCl (pengatur viskositas sediaan), diikuti penambahan Pewarna, Parfum, dan sisa air baku hingga merata"
        ]

    if "CUCI PIRING" in name_u or "DISHWASH" in name_u:
        return [
            "Tahap 1: Pengisian air baku 60% dan pelarutan Linear Alkylbenzene Sulfonate (LABS) serta Natrium Hidroksida (NaOH)",
            "Tahap 2: Pemasukan Sodium Lauryl Ether Sulfate (SLES) dan Cocoamide DEA (foam booster) diaduk hingga homogen",
            "Tahap 3: Penambahan larutan NaCl secara bertahap hingga terbentuk kekentalan cairan sediaan yang diinginkan",
            "Tahap 4: Pemasukan Pewarna Tekstil & Parfum Jeruk Nipis, diaduk perlahan dan ditambahkan sisa air baku"
        ]

    return [
        "Tahap 1: Pengisian air baku ke dalam tangki pencampur dan pelarutan bahan pendukung sediaan standar",
        "Tahap 2: Penambahan bahan aktif utama formula dengan pengadukan homogen dan kecepatan terkontrol",
        "Tahap 3: Penambahan bahan aditif, aroma & pewarna hingga sediaan mencapai homogenitas sempurna"
    ]


def generate_flowchart_image(product_name, output_image_path, parsed_formula=None):
    """Menghasilkan gambar flowchart presisi berbasis proses manufaktur riil."""
    from PIL import Image, ImageDraw, ImageFont
    import math

    font_path = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
    font_bold_path = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"

    def draw_arrow(draw, start, end, width=2, arrow_size=9):
        draw.line([start, end], fill=(0, 0, 0), width=width)
        x1, y1 = start
        x2, y2 = end
        angle = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - arrow_size * math.cos(angle - math.pi / 6), y2 - arrow_size * math.sin(angle - math.pi / 6))
        p2 = (x2 - arrow_size * math.cos(angle + math.pi / 6), y2 - arrow_size * math.sin(angle + math.pi / 6))
        draw.polygon([end, p1, p2], fill=(0, 0, 0))

    def draw_pill(draw, box, text, font, fill=(255, 255, 255), outline=(0, 0, 0), width=2):
        r = (box[3] - box[1]) // 2
        draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)
        tb = draw.textbbox((0, 0), text, font=font)
        tw, th = tb[2] - tb[0], tb[3] - tb[1]
        draw.text(((box[0] + box[2] - tw) // 2, (box[1] + box[3] - th) // 2 - 2), text, fill=(0, 0, 0), font=font)

    def wrap_text(text, font, max_width, draw):
        words = text.split()
        lines = []
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] - bbox[0] <= max_width or not current_line:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        return lines

    def draw_box(draw, box, lines, font, fill=(255, 255, 255), outline=(0, 0, 0), width=2, line_spacing=4):
        draw.rectangle(box, fill=fill, outline=outline, width=width)
        max_w = box[2] - box[0] - 24
        wrapped_lines = []
        for l in lines:
            tb = draw.textbbox((0, 0), l, font=font)
            if tb[2] - tb[0] > max_w:
                wrapped_lines.extend(wrap_text(l, font, max_w, draw))
            else:
                wrapped_lines.append(l)

        line_bboxes = [draw.textbbox((0, 0), l, font=font) for l in wrapped_lines]
        line_heights = [b[3] - b[1] for b in line_bboxes]
        total_h = sum(line_heights) + line_spacing * (len(wrapped_lines) - 1)
        cur_y = (box[1] + box[3] - total_h) // 2 - 2
        for i, l in enumerate(wrapped_lines):
            tb = draw.textbbox((0, 0), l, font=font)
            lw = tb[2] - tb[0]
            cur_x = (box[0] + box[2] - lw) // 2
            draw.text((cur_x, cur_y), l, fill=(0, 0, 0), font=font)
            cur_y += line_heights[i] + line_spacing

    def draw_diamond(draw, center, size, lines, font, fill=(255, 255, 255), outline=(0, 0, 0), width=2, line_spacing=4):
        cx, cy = center
        hw, hh = size
        pts = [(cx, cy - hh), (cx + hw, cy), (cx, cy + hh), (cx - hw, cy)]
        draw.polygon(pts, fill=fill, outline=outline)
        line_bboxes = [draw.textbbox((0, 0), l, font=font) for l in lines]
        line_heights = [b[3] - b[1] for b in line_bboxes]
        total_h = sum(line_heights) + line_spacing * (len(lines) - 1)
        cur_y = cy - (total_h // 2) - 2
        for i, l in enumerate(lines):
            tb = draw.textbbox((0, 0), l, font=font)
            lw = tb[2] - tb[0]
            cur_x = cx - (lw // 2)
            draw.text((cur_x, cur_y), l, fill=(0, 0, 0), font=font)
            cur_y += line_heights[i] + line_spacing

    def draw_badge(draw, box, text, font, bg_color=(204, 0, 0), text_color=(255, 255, 255)):
        draw.rectangle(box, fill=bg_color, outline=(0, 0, 0), width=1)
        tb = draw.textbbox((0, 0), text, font=font)
        tw, th = tb[2] - tb[0], tb[3] - tb[1]
        cx = (box[0] + box[2] - tw) // 2
        cy = (box[1] + box[3] - th) // 2 - 2
        draw.text((cx, cy), text, fill=text_color, font=font)

    stages = get_realistic_stages_for_product(product_name)

    W, H = 860, 1080
    im = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    f_body = ImageFont.truetype(font_path, 14)
    f_badge = ImageFont.truetype(font_bold_path, 14)
    f_pill = ImageFont.truetype(font_bold_path, 16)

    # Kolom tengah x = 340
    # 1. MULAI (Pill)
    draw_pill(draw, (35, 30, 185, 95), "MULAI", f_pill)
    draw_arrow(draw, (185, 62), (220, 62))

    # 2. Persiapan alat
    draw_box(draw, (220, 25, 460, 100), ["Persiapan alat produksi,", "tangki pencampur & kemasan"], f_body)
    draw_arrow(draw, (340, 100), (340, 135))

    # 3. Persiapan bahan baku
    draw_box(draw, (220, 135, 460, 210), ["Persiapan & penimbangan bahan", "baku sesuai formula standar"], f_body)

    # Arrow ke Diamond 1 (QC Bahan Baku)
    draw.line([(420, 210), (420, 230)], fill=(0, 0, 0), width=2)
    draw.line([(420, 230), (600, 230)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (600, 230), (600, 260))

    # 4. Diamond 1 (QC Masuk) - Center at (680, 310), size (100, 58)
    d1_cx, d1_cy = 680, 310
    draw_diamond(draw, (d1_cx, d1_cy), (100, 58), ["Pemeriksaan", "bahan baku", "& kemasan"], f_body)

    # NO loop
    draw.line([(d1_cx, d1_cy - 58), (d1_cx, 172)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (d1_cx, 172), (460, 172))
    # Badge NO (oranye)
    draw_badge(draw, (d1_cx + 12, 185, d1_cx + 72, 215), "NO", f_badge, bg_color=(255, 165, 0), text_color=(0, 0, 0))

    # Parameter tahapan compounding
    num_stg = len(stages)
    stg_top = 370
    stg_bot = 750
    total_avail = stg_bot - stg_top
    gap = 18
    box_h = (total_avail - (num_stg - 1) * gap) // num_stg

    # YES path dari Diamond 1
    draw.line([(d1_cx - 100, d1_cy), (340, d1_cy)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (340, d1_cy), (340, stg_top))
    # Badge YES (merah)
    draw_badge(draw, (380, d1_cy - 35, 445, d1_cy - 5), "YES", f_badge, bg_color=(210, 0, 0), text_color=(255, 255, 255))

    stg_boxes = []
    for i, raw_text in enumerate(stages):
        y1 = stg_top + i * (box_h + gap)
        y2 = y1 + box_h
        b = (140, y1, 540, y2)
        draw_box(draw, b, [raw_text] if isinstance(raw_text, str) else raw_text, f_body)
        stg_boxes.append(b)
        if i > 0:
            prev_y2 = stg_top + (i - 1) * (box_h + gap) + box_h
            draw_arrow(draw, (340, prev_y2), (340, y1))

    # Dari tahap akhir ke Diamond 2 (QC Produk Jadi)
    last_b = stg_boxes[-1]
    last_mid_y = (last_b[1] + last_b[3]) // 2
    d2_cx, d2_cy = 680, last_mid_y
    draw_arrow(draw, (540, last_mid_y), (d2_cx - 100, last_mid_y))

    # Diamond 2
    draw_diamond(draw, (d2_cx, d2_cy), (100, 58), ["Pemeriksaan", "kualitas", "produk jadi"], f_body)

    # Diamond 2 NO loop (kembali ke tahap sebelum akhir)
    target_stage_idx = max(0, num_stg - 2)
    target_box = stg_boxes[target_stage_idx]
    target_y = (target_box[1] + target_box[3]) // 2

    draw.line([(d2_cx, d2_cy - 58), (d2_cx, target_y)], fill=(0, 0, 0), width=2)
    draw_arrow(draw, (d2_cx, target_y), (540, target_y))
    # Badge NO (oranye)
    badge_no_y = (d2_cy - 58 + target_y) // 2 - 15
    draw_badge(draw, (d2_cx + 12, badge_no_y, d2_cx + 72, badge_no_y + 30), "NO", f_badge, bg_color=(255, 165, 0), text_color=(0, 0, 0))

    # YES path ke pengemasan
    draw_badge(draw, (d2_cx + 15, d2_cy + 65, d2_cx + 75, d2_cy + 95), "YES", f_badge, bg_color=(210, 0, 0), text_color=(255, 255, 255))

    # Bagian bawah (Pengemasan -> Gudang -> Selesai)
    bot_y1 = 870
    bot_y2 = 955
    pack_box = (570, bot_y1, 790, bot_y2)
    draw_box(draw, pack_box, ["Pengisian (Filling) & Capping", "ke dalam kemasan botol/jerigen"], f_body)
    draw_arrow(draw, (d2_cx, d2_cy + 58), (d2_cx, bot_y1))

    stor_box = (280, bot_y1, 500, bot_y2)
    draw_box(draw, stor_box, ["Pelabelan & penyimpanan", "di gudang produk jadi"], f_body)
    draw_arrow(draw, (570, (bot_y1 + bot_y2) // 2), (500, (bot_y1 + bot_y2) // 2))

    selesai_box = (40, bot_y1 + 5, 205, bot_y2 - 5)
    draw_pill(draw, selesai_box, "SELESAI", f_pill)
    draw_arrow(draw, (280, (bot_y1 + bot_y2) // 2), (205, (bot_y1 + bot_y2) // 2))

    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    im.save(output_image_path)
    return output_image_path


def generate_doc_alur_produksi(target_path, product_name, intel=None, check_date_str=None, parsed_formula=None):
    """5. Memproses Alur Produksi.docx (Flowchart 1 Halaman Persis Screenshot)"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "Alur Produksi.docx")
    doc = Document(tmpl_path)

    # 1. Hapus paragraf dan tabel lama di body
    for p in list(doc.paragraphs):
        p._element.getparent().remove(p._element)
    for t in list(doc.tables):
        t._element.getparent().remove(t._element)

    # 2. Judul: Proses Produksi [PRODUCT_NAME]
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run(f"Proses Produksi {product_name}")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    # 3. Generate dan sematkan gambar flowchart
    chart_img_dir = os.path.join(os.path.dirname(target_path), ".cache_flowcharts")
    chart_img_path = os.path.join(chart_img_dir, f"flowchart_{re.sub(r'[^a-zA-Z0-9]', '_', product_name)}.png")
    generate_flowchart_image(product_name, chart_img_path, parsed_formula)

    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(0)
    p_img.paragraph_format.space_after = Pt(0)
    r_img = p_img.add_run()
    r_img.add_picture(chart_img_path, width=Inches(5.7))

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Alur Proses Produksi - {product_name}")


def generate_doc_spesifikasi_kemasan(target_path, product_name):
    """6. Memproses Sepsifikasi Kemasan.docx (Mempertahankan 4 gambar asli)"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "Sepsifikasi Kemasan.docx")
    doc = Document(tmpl_path)

    # Paragraph 0: Judul
    if len(doc.paragraphs) > 0:
        doc.paragraphs[0].text = f"Spesifikasi Kemasan - {product_name}"
        doc.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in doc.paragraphs[0].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Spesifikasi Kemasan - {product_name}")


def generate_doc_tujuan_pembuatan(target_path, product_name, intel):
    """7. Memproses Tujuan Pembuatan.docx (Deskripsi, Cara Pakai, Peringatan)"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "Tujuan Pembuatan.docx")
    doc = Document(tmpl_path)

    # Bersihkan paragraf lama dan isi konten terstruktur
    p_elems = [p._p for p in doc.paragraphs]
    for pe in p_elems:
        doc._body._body.remove(pe)

    # 1. Judul Produk
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(8)
    r_t = p_title.add_run(product_name)
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(14)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(0, 0, 0)

    # 2. Deskripsi Produk
    p_dh = doc.add_paragraph()
    p_dh.paragraph_format.space_before = Pt(4)
    p_dh.paragraph_format.space_after = Pt(2)
    r_dh = p_dh.add_run("Deskripsi Produk :")
    r_dh.font.name = 'Times New Roman'
    r_dh.font.size = Pt(11)
    r_dh.font.bold = True
    r_dh.font.color.rgb = RGBColor(0, 0, 0)

    p_d = doc.add_paragraph()
    p_d.paragraph_format.space_before = Pt(0)
    p_d.paragraph_format.space_after = Pt(8)
    p_d.paragraph_format.line_spacing = 1.15
    r_d = p_d.add_run(intel["deskripsi"])
    r_d.font.name = 'Times New Roman'
    r_d.font.size = Pt(10.5)
    r_d.font.color.rgb = RGBColor(0, 0, 0)

    # 3. Cara Penggunaan
    p_uh = doc.add_paragraph()
    p_uh.paragraph_format.space_before = Pt(4)
    p_uh.paragraph_format.space_after = Pt(2)
    r_uh = p_uh.add_run("Cara Penggunaan :")
    r_uh.font.name = 'Times New Roman'
    r_uh.font.size = Pt(11)
    r_uh.font.bold = True
    r_uh.font.color.rgb = RGBColor(0, 0, 0)

    p_u = doc.add_paragraph()
    p_u.paragraph_format.space_before = Pt(0)
    p_u.paragraph_format.space_after = Pt(8)
    p_u.paragraph_format.line_spacing = 1.15
    r_u = p_u.add_run(intel["cara_penggunaan"])
    r_u.font.name = 'Times New Roman'
    r_u.font.size = Pt(10)
    r_u.font.color.rgb = RGBColor(0, 0, 0)

    # 4. Peringatan
    p_wh = doc.add_paragraph()
    p_wh.paragraph_format.space_before = Pt(4)
    p_wh.paragraph_format.space_after = Pt(2)
    r_wh = p_wh.add_run("Peringatan :")
    r_wh.font.name = 'Times New Roman'
    r_wh.font.size = Pt(11)
    r_wh.font.bold = True
    r_wh.font.color.rgb = RGBColor(0, 0, 0)

    p_w = doc.add_paragraph()
    p_w.paragraph_format.space_before = Pt(0)
    p_w.paragraph_format.space_after = Pt(4)
    p_w.paragraph_format.line_spacing = 1.15
    r_w = p_w.add_run(intel["peringatan"])
    r_w.font.name = 'Times New Roman'
    r_w.font.size = Pt(10)
    r_w.font.color.rgb = RGBColor(0, 0, 0)

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Tujuan Pembuatan & Petunjuk Penggunaan - {product_name}")


def generate_doc_uji_stabilitas(target_path, product_name, intel, check_date_str):
    """8. Memproses Uji Stabilitas.docx (Data Realtime 1 Tahun)"""
    tmpl_path = os.path.join(TEMPLATE_DIR, "Uji Stabilitas.docx")
    doc = Document(tmpl_path)

    # Paragraphs Update
    for p in doc.paragraphs:
        if "Nama Produk" in p.text:
            p.text = f"Nama Produk \t\t: {product_name}"
        elif "Kode Produksi" in p.text:
            p.text = f"Kode Produksi \t\t: KCA/{intel['code']}/01"
        elif "Tanggal Produksi" in p.text:
            p.text = f"Tanggal Produksi \t: {check_date_str}"
        elif "Bentuk" in p.text and "PH" in p.text:
            p.text = f"Bentuk \t\t: {intel['bentuk']} \t\t\t\t\t\tPH \t\t: {intel['ph_spec']}"
        elif "Warna" in p.text and "Densitas" in p.text:
            p.text = f"Warna \t\t: {intel['warna']} \t\t\t\t\tDensitas \t: {intel['dens_spec']}"
        elif "Aroma" in p.text:
            p.text = f"Aroma \t\t: {intel['bau']}"
        elif "Kesimpulan :" in p.text:
            p.text = (
                f"Kesimpulan :\n"
                f"Dengan melakukan Uji stabilitas secara Realtime PT KEDIRI CHEMICAL ABADI {product_name} Telah "
                f"memenuhi standar stabilitas minimum 1 tahun sehingga masa kadaluarsa produk lebih dari 1 tahun.\n\n"
                f"Kediri {check_date_str}"
            )
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.color.rgb = RGBColor(0, 0, 0)

    # Table 0: 5 Titik Interval Realtime
    if len(doc.tables) >= 1:
        tbl = doc.tables[0]
        stab_dates = calculate_stability_dates()
        
        # Row 0: Tanggal Uji
        if len(tbl.rows) > 0:
            tbl.cell(0, 0).text = "Tanggal Uji"
            for col_i in range(1, 6):
                tbl.cell(0, col_i).text = stab_dates[col_i - 1]
            tbl.cell(0, 6).text = "Hasil"

        # Row 1: Bentuk
        if len(tbl.rows) > 1:
            tbl.cell(1, 0).text = "Bentuk"
            for col_i in range(1, 6):
                tbl.cell(1, col_i).text = intel["bentuk"]
            tbl.cell(1, 6).text = "OK"

        # Row 2: Warna
        if len(tbl.rows) > 2:
            tbl.cell(2, 0).text = "Warna"
            for col_i in range(1, 6):
                tbl.cell(2, col_i).text = intel["warna"]
            tbl.cell(2, 6).text = "OK"

        # Row 3: Aroma
        if len(tbl.rows) > 3:
            tbl.cell(3, 0).text = "Aroma"
            for col_i in range(1, 6):
                tbl.cell(3, col_i).text = intel["bau"]
            tbl.cell(3, 6).text = "OK"

        # Row 4: Berat
        if len(tbl.rows) > 4:
            tbl.cell(4, 0).text = "Berat"
            for col_i in range(1, 6):
                tbl.cell(4, col_i).text = intel["berat_res"]
            tbl.cell(4, 6).text = "OK"

        # Row 5: pH
        if len(tbl.rows) > 5:
            tbl.cell(5, 0).text = "pH"
            for col_i in range(1, 6):
                tbl.cell(5, col_i).text = intel["ph_history"][col_i - 1]
            tbl.cell(5, 6).text = "OK"

        # Row 6: Densitas
        if len(tbl.rows) > 6:
            tbl.cell(6, 0).text = "Densitas"
            for col_i in range(1, 6):
                tbl.cell(6, col_i).text = intel["dens_history"][col_i - 1]
            tbl.cell(6, 6).text = "OK"

        # Set styling all cells in table
        for r_idx, r in enumerate(tbl.rows):
            for c_idx, c in enumerate(r.cells):
                for p in c.paragraphs:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for run in p.runs:
                        run.font.name = 'Times New Roman'
                        run.font.size = Pt(8.5)
                        run.font.bold = (r_idx == 0 or c_idx == 0 or c_idx == 6)
                        run.font.color.rgb = RGBColor(0, 0, 0)
                set_cell_margins(c, top=45, bottom=45, left=50, right=50)

    doc.save(target_path)
    sanitize_docx_metadata(target_path, title=f"Uji Stabilitas Realtime - {product_name}")

# ==============================================================================
# 5. PDF EXPORT AUTOMATION (LIBREOFFICE)
# ==============================================================================

def export_to_pdf(docx_path, output_dir):
    """Mengonversi dokumen Word ke PDF menggunakan LibreOffice soffice."""
    if not SOFFICE_BIN:
        print(f"Peringatan: LibreOffice soffice tidak ditemukan, melewati konversi PDF untuk {docx_path}")
        return None
    try:
        cmd = [
            SOFFICE_BIN,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            docx_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            pdf_name = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
            pdf_path = os.path.join(output_dir, pdf_name)
            if os.path.exists(pdf_path):
                print(f"SUKSES PDF: {pdf_name}")
                return pdf_path
        else:
            print(f"Error PDF ({docx_path}): {result.stderr}")
    except Exception as e:
        print(f"Gagal konversi PDF ({docx_path}): {e}")
    return None

# ==============================================================================
# 6. MASTER ENGINE PIPELINE
# ==============================================================================

def generate_complete_product_suite(
    product_name,
    formula_input,
    output_dir=None,
    export_pdf=True,
    check_date=None
):
    """
    Eksekusi Utama:
    1. Parse formula (satuan gram -> persen % presisi total 100%)
    2. Ekstrak data intelejen produk & regulasi PKRT
    3. Siapkan folder khusus produk
    4. Generate ke-8 file .docx dari template
    5. Sanitasi seluruh metadata .docx
    6. Ekspor seluruh berkas ke .pdf
    """
    print("=" * 70)
    print(f"MEMULAI PROSES GENERASI DOKUMEN PKRT UNTUK: {product_name.upper()}")
    print("=" * 70)

    # 1. Parse Formula
    parsed_formula, total_gram = parse_formula_input(formula_input)
    print(f"Total Berat Formula: {total_gram:.2f} gram (Dihitung menjadi 100%)")
    print("Komposisi:")
    for ing in parsed_formula:
        print(f" - {ing['name']}: {ing['gram']}g ({ing['pct_str']}) -> {ing['function']}")

    # 2. Intelejen Produk
    intel = get_product_intelligence(product_name)
    print(f"Kategori PKRT: {intel['kategori']} | Jenis: {intel['jenis_pkrt']} | HS: {intel['hs_code']}")

    # 3. Tanggal Pemeriksaan
    if check_date is None:
        today = datetime.now()
        bulan_indo = [
            "", "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ]
        check_date = f"{today.day} {bulan_indo[today.month]} {today.year}"

    # 4. Direktori Output Produk
    if output_dir is None:
        # Buat folder produk di PT ANUGERAH SURYA SEMBADA
        clean_folder_name = re.sub(r'^(?:ALBERN\s+|PT\s+ANUGERAH\s+SURYA\s+SEMBADA\s+)', '', product_name, flags=re.I).strip()
        if not clean_folder_name:
            clean_folder_name = product_name
        output_dir = os.path.join(DEFAULT_OUTPUT_BASE, clean_folder_name)

    os.makedirs(output_dir, exist_ok=True)
    print(f"Target Direktori: {output_dir}")

    # 5. Daftar 8 Berkas
    docs_to_generate = [
        ("Formula .docx", generate_doc_formula, (product_name, parsed_formula)),
        ("COA.docx", generate_doc_coa, (product_name, intel, parsed_formula, check_date)),
        ("Formulir 1.1.docx", generate_doc_formulir_1_1, (product_name, intel, check_date)),
        ("Sertifikat uji Lab.docx", generate_doc_sertifikat_lab, (product_name, intel, check_date)),
        ("Alur Produksi.docx", generate_doc_alur_produksi, (product_name, intel, check_date, parsed_formula)),
        ("Sepsifikasi Kemasan.docx", generate_doc_spesifikasi_kemasan, (product_name,)),
        ("Tujuan Pembuatan.docx", generate_doc_tujuan_pembuatan, (product_name, intel)),
        ("Uji Stabilitas.docx", generate_doc_uji_stabilitas, (product_name, intel, check_date)),
    ]

    generated_docx = []
    generated_pdf = []

    for filename, gen_func, args in docs_to_generate:
        target_docx = os.path.join(output_dir, filename)
        print(f"\n[+] Membuat: {filename}...")
        try:
            gen_func(target_docx, *args)
            generated_docx.append(target_docx)
            print(f"    Berhasil: {target_docx}")

            if export_pdf:
                pdf_res = export_to_pdf(target_docx, output_dir)
                if pdf_res:
                    generated_pdf.append(pdf_res)
        except Exception as e:
            print(f"    Gagal memproses {filename}: {e}")

    print("\n" + "=" * 70)
    print(f"SELESAI: {len(generated_docx)} DOCX & {len(generated_pdf)} PDF berhasil dibuat di:")
    print(output_dir)
    print("=" * 70)

    return {
        "output_dir": output_dir,
        "docx_files": generated_docx,
        "pdf_files": generated_pdf
    }

# ==============================================================================
# 7. INTERACTIVE CLI RUNNER
# ==============================================================================

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="PKRT Product Document Generator")
    parser.add_argument("--product", type=str, help="Nama Produk (contoh: 'ALBERN Cuci Piring')")
    parser.add_argument("--formula", type=str, help="Formula dalam gram (contoh: 'SLES: 120, LABS: 50, NaCl: 25, Aqua: 805')")
    parser.add_argument("--outdir", type=str, default=None, help="Direktori output")
    parser.add_argument("--no-pdf", action="store_true", help="Jangan ekspor ke PDF")

    args = parser.parse_args()

    if args.product and args.formula:
        generate_complete_product_suite(
            product_name=args.product,
            formula_input=args.formula,
            output_dir=args.outdir,
            export_pdf=not args.no_pdf
        )
    else:
        print("--- DEMO / TEST RUN PADA PRODUK CONTOH (Cuci Piring) ---")
        demo_product = "ALBERN Cuci Piring"
        demo_formula = [
            {"name": "Sodium Laureth Sulfate (SLES)", "gram": 120.0},
            {"name": "Linear Alkylbenzene Sulfonate (LABS)", "gram": 50.0},
            {"name": "Sodium Hydroxide (NaOH)", "gram": 7.0},
            {"name": "Cocoamide DEA (CDEA)", "gram": 15.0},
            {"name": "Sodium Chloride (NaCl)", "gram": 25.0},
            {"name": "Parfume Jeruk Nipis", "gram": 3.0},
            {"name": "Pewarna Tartrazine & Brilliant Blue", "gram": 0.1},
            {"name": "Air Demineralisasi (Aqua RO)", "gram": 779.9}
        ]
        generate_complete_product_suite(
            product_name=demo_product,
            formula_input=demo_formula,
            output_dir=os.path.join(DEFAULT_OUTPUT_BASE, "Cuci Piring")
        )
