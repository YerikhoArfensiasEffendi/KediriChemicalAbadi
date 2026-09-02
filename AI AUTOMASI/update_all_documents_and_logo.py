import zipfile
import xml.etree.ElementTree as ET
import shutil
import os

xlsx_path = '/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Dashboard Keuangan PT Kediri Chemical Abadi.xlsx'
temp_zip = xlsx_path + '.temp.zip'

ET.register_namespace('', 'http://schemas.openxmlformats.org/spreadsheetml/2006/main')
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')

# Baca Logo KCA PNG dan SVG
kca_png_path = '/tmp/favicon.svg.png'
kca_svg_path = '/Users/arthur/Documents/WebsiteKCA/kediri-chemical/public/favicon.svg'

with open(kca_png_path, 'rb') as f:
    kca_png_bytes = f.read()

with open(kca_svg_path, 'rb') as f:
    kca_svg_bytes = f.read()

def set_cell(row_elem, col_letter, val):
    r_num = row_elem.attrib.get('r')
    cell_ref = f"{col_letter}{r_num}"
    
    c = None
    for child in row_elem.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
        if child.attrib.get('r') == cell_ref:
            c = child
            break
    if c is None:
        c = ET.Element('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')
        c.attrib['r'] = cell_ref
        row_elem.append(c)
        
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
    sheet_data = sheet_root.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheetData')
    r = ET.SubElement(sheet_data, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row')
    r.attrib['r'] = str(row_num)
    return r

with zipfile.ZipFile(xlsx_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w') as zout:
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        
        # 1. Update Logo di xl/media/
        if item.filename.startswith('xl/media/'):
            if item.filename.endswith('.png'):
                buffer = kca_png_bytes
            elif item.filename.endswith('.svg'):
                buffer = kca_svg_bytes

        # 2. Update INVOICE (sheet26.xml)
        elif item.filename == 'xl/worksheets/sheet26.xml':
            root = ET.fromstring(buffer)
            r17 = get_row(root, 17)
            set_cell(r17, 'D', 'PT. Kediri Chemical Abadi will supply the following products:')
            r35 = get_row(root, 35)
            set_cell(r35, 'D', 'Pembayaran dapat ditransfer ke rekening resmi PT Kediri Chemical Abadi:')
            r36 = get_row(root, 36)
            set_cell(r36, 'D', 'Bank Mandiri No. Rekening: 1710066990006 a/n PT Kediri Chemical Abadi')
            r46 = get_row(root, 46)
            set_cell(r46, 'J', 'Yan Effendi')
            r47 = get_row(root, 47)
            set_cell(r47, 'J', 'Direktur Utama')
            r51 = get_row(root, 51)
            set_cell(r51, 'D', 'PT KEDIRI CHEMICAL ABADI - Solusi Kimia Pembersih & Makloon Berkualitas')
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 3. Update QUOTATION (sheet21.xml)
        elif item.filename == 'xl/worksheets/sheet21.xml':
            root = ET.fromstring(buffer)
            r7 = get_row(root, 7)
            set_cell(r7, 'F', 'RT.1/RW.6, Pagung, Kec. Semen, Kediri, Jawa Timur 64161')
            r8 = get_row(root, 8)
            set_cell(r8, 'F', 'Phone/WA: 0822-4400-6699 | Email: kdrchemicals@gmail.com')
            r52 = get_row(root, 52)
            set_cell(r52, 'D', 'Yan Effendi')
            r53 = get_row(root, 53)
            set_cell(r53, 'D', 'Direktur Utama')
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 4. Update PURCHASE ORDER (sheet23.xml)
        elif item.filename == 'xl/worksheets/sheet23.xml':
            root = ET.fromstring(buffer)
            r46 = get_row(root, 46)
            set_cell(r46, 'K', 'Yerikho Arfensias Effendi')
            r47 = get_row(root, 47)
            set_cell(r47, 'K', 'General Manager / Operasional')
            r56 = get_row(root, 56)
            set_cell(r56, 'D', 'PT KEDIRI CHEMICAL ABADI - Solusi Kimia Pembersih Berkualitas')
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 5. Update PURCHASE REQUEST (sheet22.xml)
        elif item.filename == 'xl/worksheets/sheet22.xml':
            root = ET.fromstring(buffer)
            r54 = get_row(root, 54)
            set_cell(r54, 'D', 'PT KEDIRI CHEMICAL ABADI - Solusi Kimia Pembersih Berkualitas')
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 6. Update SALES ORDER (sheet24.xml)
        elif item.filename == 'xl/worksheets/sheet24.xml':
            root = ET.fromstring(buffer)
            r60 = get_row(root, 60)
            set_cell(r60, 'D', 'PT KEDIRI CHEMICAL ABADI - Solusi Kimia Pembersih Berkualitas')
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 7. Update DELIVERY ORDER (sheet25.xml)
        elif item.filename == 'xl/worksheets/sheet25.xml':
            root = ET.fromstring(buffer)
            r33 = get_row(root, 33)
            set_cell(r33, 'E', 'Barang telah diperiksa dan diterima dalam kondisi baik & tersegel utuh.')
            r54 = get_row(root, 54)
            set_cell(r54, 'D', 'PT KEDIRI CHEMICAL ABADI - Solusi Kimia Pembersih Berkualitas')
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # 8. Update SLIP GAJI (sheet11.xml)
        elif item.filename == 'xl/worksheets/sheet11.xml':
            root = ET.fromstring(buffer)
            r10 = get_row(root, 10)
            set_cell(r10, 'D', 'RT.1/RW.6, Pagung, Kec. Semen')
            set_cell(r10, 'J', 'Yerikho Arfensias Effendi')
            r11 = get_row(root, 11)
            set_cell(r11, 'D', 'Kabupaten Kediri, Jawa Timur 64161')
            r12 = get_row(root, 12)
            set_cell(r12, 'D', 'Phone/WA: 0822-4400-6699')
            r34 = get_row(root, 34)
            set_cell(r34, 'D', 'PT KEDIRI CHEMICAL ABADI')
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        zout.writestr(item, buffer)

shutil.move(temp_zip, xlsx_path)
print("SUCCESS! Seluruh dokumen resmi (Invoice, Quotation, PO, SO, DO, Slip Gaji) & Logo KCA telah 100% diperbarui!")
