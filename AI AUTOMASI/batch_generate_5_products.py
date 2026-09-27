#!/usr/bin/env python3
"""
PT KEDIRI CHEMICAL ABADI — QUALITY ASSURANCE & LEGAL PKRT
Batch Generator untuk 5 Produk PKRT PT Anugerah Surya Sembada:
1. ALBERN Liquid Detergent
2. ALBERN Neutralizer
3. ALBERN Softener
4. ALBERN Emulsifier
5. ALBERN Liquid Pencerah

Mengonversi nama dagang pasar menjadi nomenklatur kimia resmi (IUPAC / INCI),
menghitung persentase presisi total 100%, menghasilkan 8 berkas Word + 8 berkas PDF,
dan mensanitasi metadata resmi PT Kediri Chemical Abadi.

Author / Manager : Yerikho Arfensias Effendi
Company          : PT Kediri Chemical Abadi
Direktur Utama   : Yan Effendi
"""

import os
import sys

# Tambahkan direktori saat ini ke sys.path
sys.path.append(os.path.dirname(__file__))

from pkrt_product_document_engine import generate_complete_product_suite

BASE_DIR = "/Users/arthur/Documents/PT. ANUGERAH SURYA SEMBADA"

PRODUCTS = [
    # 1. ALBERN Liquid Detergent
    {
        "name": "ALBERN Liquid Detergent",
        "output_dir": os.path.join(BASE_DIR, "Liquid Detergent"),
        "formula": [
            {
                "name": "Sodium Lauryl Ether Sulfate (SLES)",
                "gram": 4000.0,
                "function": "Surfaktan anionik pembersih noda, lemak & pembusa aktif"
            },
            {
                "name": "Natrium Klorida (Sodium Chloride / NaCl)",
                "gram": 6000.0,
                "function": "Pengatur viskositas, pengental larutan sediaan & penstabil surfaktan"
            },
            {
                "name": "Asam Fluorida (Hydrofluoric Acid)",
                "gram": 250.0,
                "function": "Bahan aktif pembersih noda anorganik membandel & pencerah serat"
            },
            {
                "name": "Natrium Karbonat (Sodium Carbonate / Soda Ash Dense)",
                "gram": 30.0,
                "function": "Alkali builder pengatur pH basa & pelunak kesadahan air"
            },
            {
                "name": "Asam Sitrat (Citric Acid)",
                "gram": 30.0,
                "function": "Buffer penyeimbang kestabilan pH sediaan"
            },
            {
                "name": "Disodium EDTA (Ethylenediaminetetraacetic Acid)",
                "gram": 20.0,
                "function": "Agen pengkhelat (chelating agent) pengikat ion logam berat dalam air"
            },
            {
                "name": "Fragrance / Parfume",
                "gram": 75.0,
                "function": "Pemberi aroma kesegaran floral khas cucian tahan lama"
            },
            {
                "name": "Air Demineralisasi (Aqua Demineralisata)",
                "gram": 60000.0,
                "function": "Pelarut utama sediaan (solvent) & media homogenisasi"
            }
        ]
    },

    # 2. ALBERN Neutralizer
    {
        "name": "ALBERN Neutralizer",
        "output_dir": os.path.join(BASE_DIR, "Neutralizer"),
        "formula": [
            {
                "name": "Natrium Metabisulfit (Sodium Metabisulfite)",
                "gram": 1000.0,
                "function": "Bahan aktif penetral sisa klorin/pemutih & anti-klorin (dechlorinating agent)"
            },
            {
                "name": "Fragrance / Parfume",
                "gram": 15.0,
                "function": "Pemberi aroma kesegaran ringan pada bilasan akhir laundry"
            },
            {
                "name": "Air Demineralisasi (Aqua Demineralisata)",
                "gram": 5000.0,
                "function": "Pelarut utama sediaan (solvent)"
            }
        ]
    },

    # 3. ALBERN Softener
    {
        "name": "ALBERN Softener",
        "output_dir": os.path.join(BASE_DIR, "Softener"),
        "formula": [
            {
                "name": "Esterquat (Dialkyl Ester Ammonium Methosulfate / Tetranil)",
                "gram": 1000.0,
                "function": "Surfaktan kationik pelembut serat tekstil, pelicin kain & anti-statis"
            },
            {
                "name": "Disodium EDTA (Ethylenediaminetetraacetic Acid)",
                "gram": 10.0,
                "function": "Pengkhelat ion logam untuk menjaga kestabilan emulsi pelembut"
            },
            {
                "name": "Fragrance / Parfume",
                "gram": 100.0,
                "function": "Pemberi aroma wangi floral mewah tahan lama pada serat pakaian"
            },
            {
                "name": "Air Demineralisasi (Aqua Demineralisata)",
                "gram": 5000.0,
                "function": "Pelarut utama sediaan & media dispersi emulsi kationik"
            }
        ]
    },

    # 4. ALBERN Emulsifier
    {
        "name": "ALBERN Emulsifier",
        "output_dir": os.path.join(BASE_DIR, "Emulsifier"),
        "formula": [
            {
                "name": "Sodium Lauryl Ether Sulfate (SLES)",
                "gram": 4000.0,
                "function": "Surfaktan pengemulsi lemak & pembersih noda minyak"
            },
            {
                "name": "Natrium Klorida (Sodium Chloride / NaCl)",
                "gram": 5000.0,
                "function": "Pengatur viskositas & penstabil larutan sediaan"
            },
            {
                "name": "Natrium Karbonat (Sodium Carbonate / Soda Ash Dense)",
                "gram": 2000.0,
                "function": "Alkali builder penyabun asam lemak & pelarut gemuk/minyak berat"
            },
            {
                "name": "Asam Sitrat (Citric Acid)",
                "gram": 2000.0,
                "function": "Pengatur kestabilan pH & chelating builder"
            },
            {
                "name": "Enzim Anti-Redeposisi (Enzyme Anti-Redeposition Agent / Protease-Lipase)",
                "gram": 1000.0,
                "function": "Katalisator pemecah protein & lemak serta pencegah kotoran menempel kembali"
            },
            {
                "name": "Optical Brightening Agent (Disodium 4,4'-bis(2-sulfostyryl)biphenyl / CBS-X)",
                "gram": 1000.0,
                "function": "Pencerah serat optik pakaian kusam akibat noda minyak"
            },
            {
                "name": "Disodium EDTA (Ethylenediaminetetraacetic Acid)",
                "gram": 30.0,
                "function": "Agen pengkhelat ion logam pencegah oksidasi noda minyak"
            },
            {
                "name": "Fragrance / Parfume",
                "gram": 75.0,
                "function": "Pemberi aroma segar penetral bau minyak"
            },
            {
                "name": "Colorant / Pewarna Tekstil (Dye)",
                "gram": 15.0,
                "function": "Pemberi warna estetika sediaan"
            },
            {
                "name": "Air Demineralisasi (Aqua Demineralisata)",
                "gram": 60000.0,
                "function": "Pelarut utama sediaan (solvent)"
            }
        ]
    },

    # 5. ALBERN Liquid Pencerah
    {
        "name": "ALBERN Liquid Pencerah",
        "output_dir": os.path.join(BASE_DIR, "Liquid Pencerah"),
        "formula": [
            {
                "name": "Sodium Lauryl Ether Sulfate (SLES)",
                "gram": 4000.0,
                "function": "Surfaktan pembersih kotoran mikro & pembawa zat pencerah optik"
            },
            {
                "name": "Optical Brightening Agent (Disodium 4,4'-bis(2-sulfostyryl)biphenyl / CBS-X)",
                "gram": 3000.0,
                "function": "Zat aktif pencerah optik pakaian putih & berwarna (mencegah kusam dan menguning)"
            },
            {
                "name": "Natrium Klorida (Sodium Chloride / NaCl)",
                "gram": 5000.0,
                "function": "Pengatur viskositas & penstabil dispersi cairan pencerah"
            },
            {
                "name": "Disodium EDTA (Ethylenediaminetetraacetic Acid)",
                "gram": 30.0,
                "function": "Agen pengkelat ion sadah untuk mencegah penumpukan mineral pada kain"
            },
            {
                "name": "Fragrance / Parfume",
                "gram": 75.0,
                "function": "Pemberi aroma wangi segar pada pakaian"
            },
            {
                "name": "Colorant / Pewarna Tekstil (Dye)",
                "gram": 15.0,
                "function": "Pemberi warna estetika sediaan"
            },
            {
                "name": "Air Demineralisasi (Aqua Demineralisata)",
                "gram": 60000.0,
                "function": "Pelarut utama sediaan (solvent)"
            }
        ]
    }
]

def main():
    print("=" * 80)
    print("EKSEKUSI BATCH GENERATOR DOKUMEN PKRT (5 PRODUK)")
    print("PT KEDIRI CHEMICAL ABADI — YERIKHO ARFENSIAS EFFENDI")
    print("=" * 80)

    results = []
    for prod in PRODUCTS:
        print(f"\n>>> MEMPROSES: {prod['name']} -> Folder: {prod['output_dir']}")
        res = generate_complete_product_suite(
            product_name=prod["name"],
            formula_input=prod["formula"],
            output_dir=prod["output_dir"],
            export_pdf=True
        )
        results.append(res)

    print("\n" + "=" * 80)
    print("BATCH SELESAI DENGAN SUKSES!")
    print("Ringkasan Folder yang Terbuat & Terisi Lengkap:")
    for r in results:
        print(f" - {r['output_dir']} ({len(r['docx_files'])} DOCX, {len(r['pdf_files'])} PDF)")
    print("=" * 80)

if __name__ == "__main__":
    main()
