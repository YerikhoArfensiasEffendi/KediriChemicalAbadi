import zipfile
import xml.etree.ElementTree as ET
import shutil
import os

xlsx_path = '/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Dashboard Keuangan PT Kediri Chemical Abadi.xlsx'
temp_zip = xlsx_path + '.temp.zip'

ET.register_namespace('', 'http://schemas.openxmlformats.org/spreadsheetml/2006/main')
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')

def set_cell(row_elem, col_letter, val, cell_type=None):
    r_num = row_elem.attrib.get('r')
    cell_ref = f"{col_letter}{r_num}"
    
    # Cari cell yang sudah ada atau buat baru
    c = None
    for child in row_elem.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
        if child.attrib.get('r') == cell_ref:
            c = child
            break
    if c is None:
        c = ET.Element('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')
        c.attrib['r'] = cell_ref
        row_elem.append(c)
        
    # Bersihkan isi lama
    for child in list(c):
        c.remove(child)
        
    if val is None or str(val).strip() == '':
        c.attrib.pop('t', None)
        return

    if isinstance(val, (int, float)):
        c.attrib['t'] = 'n'
        v = ET.SubElement(c, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
        v.text = str(val)
    elif str(val).startswith('='):
        c.attrib.pop('t', None)
        f = ET.SubElement(c, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}f')
        f.text = str(val)[1:]
    else:
        c.attrib['t'] = 'inlineStr'
        is_elem = ET.SubElement(c, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}is')
        t_elem = ET.SubElement(is_elem, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
        t_elem.text = str(val)

def get_row(sheet_root, row_num):
    for r in sheet_root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
        if int(r.attrib.get('r')) == row_num:
            return r
    # jika belum ada, buat di dalam sheetData
    sheet_data = sheet_root.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheetData')
    r = ET.SubElement(sheet_data, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row')
    r.attrib['r'] = str(row_num)
    return r

with zipfile.ZipFile(xlsx_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w') as zout:
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        
        # 1. Update sharedStrings.xml untuk identitas perusahaan & default teks
        if item.filename == 'xl/sharedStrings.xml':
            sst = ET.fromstring(buffer)
            si_list = list(sst.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'))
            def set_text(si_elem, val):
                t = si_elem.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                if t is not None:
                    t.text = val
                else:
                    r_elem = si_elem.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}r')
                    if r_elem is not None:
                        rt = r_elem.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                        if rt is not None:
                            rt.text = val
            set_text(si_list[15], 'PT KEDIRI CHEMICAL ABADI')
            set_text(si_list[533], 'RT.1/RW.6, Pagung, Kec. Semen')
            set_text(si_list[534], 'Kabupaten Kediri, Jawa Timur 64161')
            set_text(si_list[535], 'Phone/WA: 0822-4400-6699 | Email: kdrchemicals@gmail.com')
            buffer = ET.tostring(sst, encoding='utf-8', xml_declaration=True)

        # 2. Update sheet29.xml (SETUP)
        elif item.filename == 'xl/worksheets/sheet29.xml':
            root = ET.fromstring(buffer)
            
            # Produk
            products = [
                ('KCA-PR-001', 'Laundry Care', 'Liquid Detergent (1L, 5L, 20L)'),
                ('KCA-PR-002', 'Kitchen Care', 'Liquid DishWasher (1L, 5L, 20L)'),
                ('KCA-PR-003', 'Laundry Specialty', 'Pencerah Warna / Oxygen Bleach (1L-20L)'),
                ('KCA-PR-004', 'Laundry Specialty', 'Emulsifier Pengangkat Lemak (1L-20L)'),
                ('KCA-PR-005', 'Laundry Specialty', 'Bleach Pemutih Klorin (1L-20L)'),
                ('KCA-PR-006', 'Spotting Agent', 'Rust Tex Perontok Noda Karat (1L-20L)'),
                ('KCA-PR-007', 'Spotting Agent', 'Blood Tex Perontok Noda Darah (1L-20L)'),
                ('KCA-PR-008', 'Spa Specialty', 'Peluruh Noda Minyak SPA (10 kg Pail)'),
            ]
            for idx, (code, cat, name) in enumerate(products, 6):
                r = get_row(root, idx)
                set_cell(r, 'G', code)
                set_cell(r, 'H', cat)
                set_cell(r, 'I', name)

            # Karyawan & Status
            employees = [
                ('Yerikho Arfensias Effendi', 'TETAP'),
                ('Operator Produksi', 'TETAP'),
                ('Operasional Freelance', 'FREELANCE'),
                ('Yan Effendi', 'DIREKTUR UTAMA'),
            ]
            for idx, (name, status) in enumerate(employees, 6):
                r = get_row(root, idx)
                set_cell(r, 'S', name)
                set_cell(r, 'T', status)

            # Aset
            assets = [
                ('AS001', 'Mobil Daihatsu Xenia 2012 Bekas', 'Kendaraan Operasional'),
                ('AS002', 'Mesin Pengaduk Manual 1', 'Mesin Produksi'),
                ('AS003', 'Mesin Pengaduk Manual 2', 'Mesin Produksi'),
                ('AS004', 'Pabrik Home Industri Pagung', 'Bangunan'),
            ]
            for idx, (code, name, jenis) in enumerate(assets, 6):
                r = get_row(root, idx)
                set_cell(r, 'X', code)
                set_cell(r, 'Y', name)
                set_cell(r, 'V', jenis)

            # Bank
            banks = ['Bank Mandiri (1710066990006)', 'Kas Tunai (Cash)']
            for idx, bank in enumerate(banks, 6):
                r = get_row(root, idx)
                set_cell(r, 'AP', bank)

            # Toko Offline
            channels = ['Pabrik Kediri KCA', 'Distributor / B2B KCA', 'Mitra Makloon KCA']
            for idx, ch in enumerate(channels, 6):
                r = get_row(root, idx)
                set_cell(r, 'AH', ch)

            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 3. Update sheet10.xml (GAJI KARYAWAN)
        elif item.filename == 'xl/worksheets/sheet10.xml':
            root = ET.fromstring(buffer)
            salaries = [
                (1, '2026-09-25', 'September', '2026', 'Yerikho Arfensias Effendi', 'TETAP', 2500000),
                (2, '2026-09-25', 'September', '2026', 'Operator Produksi', 'TETAP', 2500000),
                (3, '2026-09-25', 'September', '2026', 'Operasional Freelance', 'FREELANCE', 2500000),
            ]
            for idx, (no, tgl, bln, thn, nama, status, gapok) in enumerate(salaries, 6):
                r = get_row(root, idx)
                set_cell(r, 'C', no)
                set_cell(r, 'D', tgl)
                set_cell(r, 'E', bln)
                set_cell(r, 'F', thn)
                set_cell(r, 'G', nama)
                set_cell(r, 'H', status)
                set_cell(r, 'I', gapok)
                set_cell(r, 'J', 0) # Lembur
                set_cell(r, 'K', 0) # Tunjangan
                set_cell(r, 'L', 0) # Potongan
                set_cell(r, 'M', gapok) # Total
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 4. Update sheet9.xml (ASET & DEPRESIASI)
        elif item.filename == 'xl/worksheets/sheet9.xml':
            root = ET.fromstring(buffer)
            assets_data = [
                (1, 'AS001', 'Mobil Daihatsu Xenia 2012 Bekas', 'Kendaraan Operasional', 'September', '2026-09-01', 'September', '2026', 150000000, 5, 30000000, 24000000, 0, 0, 150000000),
                (2, 'AS002', 'Mesin Pengaduk Manual 1', 'Mesin Produksi', 'September', '2026-09-01', 'September', '2026', 5000000, 4, 0, 1250000, 0, 0, 5000000),
                (3, 'AS003', 'Mesin Pengaduk Manual 2', 'Mesin Produksi', 'September', '2026-09-01', 'September', '2026', 5000000, 4, 0, 1250000, 0, 0, 5000000),
                (4, 'AS004', 'Pabrik Home Industri Pagung', 'Bangunan', 'September', '2026-09-01', 'September', '2026', 100000000, 20, 0, 5000000, 0, 0, 100000000),
            ]
            for idx, (no, kode, nama, jenis, bln_lap, tgl_beli, bln, thn, nominal, umur, residu, dep_thn, umur_jalan, akum_dep, nilai_buku) in enumerate(assets_data, 6):
                r = get_row(root, idx)
                set_cell(r, 'C', no)
                set_cell(r, 'D', kode)
                set_cell(r, 'E', nama)
                set_cell(r, 'F', jenis)
                set_cell(r, 'G', bln_lap)
                set_cell(r, 'H', tgl_beli)
                set_cell(r, 'I', bln)
                set_cell(r, 'J', thn)
                set_cell(r, 'K', nominal)
                set_cell(r, 'L', umur)
                set_cell(r, 'M', residu)
                set_cell(r, 'N', dep_thn)
                set_cell(r, 'O', umur_jalan)
                set_cell(r, 'P', akum_dep)
                set_cell(r, 'Q', nilai_buku)
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 5. Update sheet8.xml (HUTANG)
        elif item.filename == 'xl/worksheets/sheet8.xml':
            root = ET.fromstring(buffer)
            # H-001 | 2026-09-01 | September | 2026 | H-001 | Utang Usaha | Kreditur Restrukturisasi | Hutang Restrukturisasi Usaha Masa Lalu | - | 700000000 | 0 | 700000000
            r = get_row(root, 6)
            set_cell(r, 'C', 1)
            set_cell(r, 'D', '2026-09-01')
            set_cell(r, 'E', 'September')
            set_cell(r, 'F', '2026')
            set_cell(r, 'G', 'H-001')
            set_cell(r, 'H', 'Utang Usaha')
            set_cell(r, 'I', 'Kreditur Restrukturisasi Bisnis')
            set_cell(r, 'J', 'Hutang Restrukturisasi Usaha Masa Lalu (Turnaround KCA)')
            set_cell(r, 'K', '2028-12-31')
            set_cell(r, 'L', 700000000)
            set_cell(r, 'M', 0)
            set_cell(r, 'N', 700000000)
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 6. Update sheet17.xml (HARGA JUAL)
        elif item.filename == 'xl/worksheets/sheet17.xml':
            root = ET.fromstring(buffer)
            products_catalog = [
                (1, 'Liquid Detergent (1L, 5L, 20L)', 'Laundry Care', 'KCA-PR-001', 1, 'Jerigen/Pcs'),
                (2, 'Liquid DishWasher (1L, 5L, 20L)', 'Kitchen Care', 'KCA-PR-002', 1, 'Jerigen/Pcs'),
                (3, 'Pencerah Warna / Oxygen Bleach (1L-20L)', 'Laundry Specialty', 'KCA-PR-003', 1, 'Jerigen/Pcs'),
                (4, 'Emulsifier Pengangkat Lemak (1L-20L)', 'Laundry Specialty', 'KCA-PR-004', 1, 'Jerigen/Pcs'),
                (5, 'Bleach Pemutih Klorin (1L-20L)', 'Laundry Specialty', 'KCA-PR-005', 1, 'Jerigen/Pcs'),
                (6, 'Rust Tex Perontok Noda Karat (1L-20L)', 'Spotting Agent', 'KCA-PR-006', 1, 'Jerigen/Pcs'),
                (7, 'Blood Tex Perontok Noda Darah (1L-20L)', 'Spotting Agent', 'KCA-PR-007', 1, 'Jerigen/Pcs'),
                (8, 'Peluruh Noda Minyak SPA (10 kg Pail)', 'Spa Specialty', 'KCA-PR-008', 1, 'Pail'),
            ]
            for idx, (no, nama, cat, kode, qty, sat) in enumerate(products_catalog, 6):
                r = get_row(root, idx)
                set_cell(r, 'C', no)
                set_cell(r, 'D', nama)
                set_cell(r, 'E', cat)
                set_cell(r, 'F', kode)
                set_cell(r, 'G', qty)
                set_cell(r, 'H', sat)
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        zout.writestr(item, buffer)

shutil.move(temp_zip, xlsx_path)
print("SUCCESS! Seluruh data PT Kediri Chemical Abadi telah diisikan ke dalam file Excel!")
