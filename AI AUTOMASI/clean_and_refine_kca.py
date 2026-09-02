import zipfile
import xml.etree.ElementTree as ET
import shutil

xlsx_path = '/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Dashboard Keuangan PT Kediri Chemical Abadi.xlsx'
temp_zip = xlsx_path + '.temp.zip'

ET.register_namespace('', 'http://schemas.openxmlformats.org/spreadsheetml/2006/main')
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')

def clean_cell_if_contains(row_elem, col_letter, dummy_keywords):
    r_num = row_elem.attrib.get('r')
    cell_ref = f"{col_letter}{r_num}"
    for c in list(row_elem.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')):
        if c.attrib.get('r') == cell_ref:
            row_elem.remove(c)

with zipfile.ZipFile(xlsx_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w') as zout:
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if item.filename == 'xl/worksheets/sheet29.xml':
            root = ET.fromstring(buffer)
            for r in root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                r_num = int(r.attrib.get('r'))
                # Bersihkan dummy karyawan > row 9
                if r_num >= 10:
                    clean_cell_if_contains(r, 'S', [])
                    clean_cell_if_contains(r, 'T', [])
                # Bersihkan dummy aset > row 9
                if r_num >= 10:
                    clean_cell_if_contains(r, 'X', [])
                    clean_cell_if_contains(r, 'Y', [])
                    clean_cell_if_contains(r, 'V', [])
                # Bersihkan dummy bank > row 7
                if r_num >= 8:
                    clean_cell_if_contains(r, 'AP', [])
                # Bersihkan dummy toko > row 8
                if r_num >= 9:
                    clean_cell_if_contains(r, 'AH', [])
                    clean_cell_if_contains(r, 'AI', [])
                    clean_cell_if_contains(r, 'AK', [])
            buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)
        zout.writestr(item, buffer)

shutil.move(temp_zip, xlsx_path)
print("Dummy data di sheet SETUP berhasil dibersihkan total!")
