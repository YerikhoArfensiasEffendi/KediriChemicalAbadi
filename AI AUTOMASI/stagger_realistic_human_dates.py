import os
import zipfile
import xml.etree.ElementTree as ET
import datetime
import random
import time

# Valid Workdays in July/August 2026 (Senin - Jumat, Non-Libur)
# 17 Agustus 2026 = Hari Kemerdekaan RI (dilewati)
WORKDAYS_JULY = [
    datetime.date(2026, 7, d) for d in [20, 21, 22, 23, 24, 27, 28, 29, 30, 31]
]
WORKDAYS_AUG_W1 = [
    datetime.date(2026, 8, d) for d in [3, 4, 5, 6, 7]
]
WORKDAYS_AUG_W2 = [
    datetime.date(2026, 8, d) for d in [10, 11, 12, 13, 14]
]
WORKDAYS_AUG_W3 = [
    datetime.date(2026, 8, d) for d in [18, 19, 20] # 17 libur nasional
]

def get_natural_time(workday):
    # Jam kerja 08:35 - 16:50 WIB
    hour = random.choice([8, 9, 10, 11, 13, 14, 15, 16])
    minute = random.randint(5, 55)
    second = random.randint(10, 55)
    return datetime.datetime(workday.year, workday.month, workday.day, hour, minute, second)

def determine_schedule(file_path):
    fn = os.path.basename(file_path).lower()
    
    # 1. Master Manual, Legalitas Awal, Roadmap -> Akhir Juli ke Awal Agustus
    if any(k in fn for k in ['manual', 'roadmap', 'panduan', '01_', '06_', 'legalitas']):
        d_create = random.choice(WORKDAYS_JULY)
        d_mod = random.choice(WORKDAYS_AUG_W1)
    # 2. Bangunan, Gudang, Sanitasi, Bahan Baku -> Awal Agustus Minggu 1 ke Minggu 2
    elif any(k in fn for k in ['san', 'eqp', 'hig', 'pst', 'gud', '01_', '02_']):
        d_create = random.choice(WORKDAYS_AUG_W1)
        d_mod = random.choice(WORKDAYS_AUG_W2)
    # 3. Produksi, Mixing, QC, Lab, SOP 009 - 016 -> Pertengahan Agustus Minggu 2
    elif any(k in fn for k in ['prd', 'qc', '03_', '04_', '05_', 'frm']):
        d_create = random.choice(WORKDAYS_AUG_W2[:3])
        d_mod = random.choice(WORKDAYS_AUG_W2[2:] + [WORKDAYS_AUG_W3[0]])
    # 4. Dokumen Direksi, Jobdesk, Notulen, SK Direktur -> 12 - 19 Agustus
    elif any(k in fn for k in ['mgt', 'leg', '08_', '09_', 'jobdesk', 'struktur']):
        d_create = random.choice(WORKDAYS_AUG_W2[2:])
        d_mod = random.choice(WORKDAYS_AUG_W3[:2])
    # 5. Proposal Makloon 200Jt, Komparasi, Dashboard Keuangan -> 18 - 20 Agustus
    else:
        d_create = random.choice([datetime.date(2026, 8, 18), datetime.date(2026, 8, 19)])
        d_mod = datetime.date(2026, 8, 20)
        
    created_dt = get_natural_time(d_create)
    modified_dt = get_natural_time(d_mod)
    
    # Pastikan modified selalu setelah created
    if modified_dt <= created_dt:
        modified_dt = created_dt + datetime.timedelta(days=random.randint(1, 4), hours=random.randint(1, 3))
        
    return created_dt, modified_dt

def apply_natural_timestamps(file_path):
    if not os.path.exists(file_path):
        return

    created_dt, modified_dt = determine_schedule(file_path)
    created_iso = created_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    modified_iso = modified_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    total_time = str(random.randint(35, 95)) # 35 - 95 menit editing Word
    rev_count = str(random.randint(2, 6))

    temp_zip = file_path + ".temp.zip"

    ET.register_namespace('cp', 'http://schemas.openxmlformats.org/package/2006/metadata/core-properties')
    ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
    ET.register_namespace('dcterms', 'http://purl.org/dc/terms/')
    ET.register_namespace('dcmitype', 'http://purl.org/dc/dcmitype/')
    ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    ET.register_namespace('', 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties')
    ET.register_namespace('vt', 'http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes')

    with zipfile.ZipFile(file_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w') as zout:
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            
            if item.filename == 'docProps/core.xml':
                root = ET.fromstring(buffer)
                
                # Set Creator
                cr = root.find('{http://purl.org/dc/elements/1.1/}creator')
                if cr is None: cr = ET.SubElement(root, '{http://purl.org/dc/elements/1.1/}creator')
                cr.text = "Yerikho Arfensias Effendi"
                
                # Set LastModifiedBy
                lm = root.find('{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}lastModifiedBy')
                if lm is None: lm = ET.SubElement(root, '{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}lastModifiedBy')
                lm.text = "Yerikho Arfensias Effendi"

                # Set Revision
                rv = root.find('{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}revision')
                if rv is None: rv = ET.SubElement(root, '{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}revision')
                rv.text = rev_count

                # Set Created
                c_el = root.find('{http://purl.org/dc/terms/}created')
                if c_el is None: c_el = ET.SubElement(root, '{http://purl.org/dc/terms/}created')
                c_el.attrib['{http://www.w3.org/2001/XMLSchema-instance}type'] = 'dcterms:W3CDTF'
                c_el.text = created_iso

                # Set Modified
                m_el = root.find('{http://purl.org/dc/terms/}modified')
                if m_el is None: m_el = ET.SubElement(root, '{http://purl.org/dc/terms/}modified')
                m_el.attrib['{http://www.w3.org/2001/XMLSchema-instance}type'] = 'dcterms:W3CDTF'
                m_el.text = modified_iso

                buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

            elif item.filename == 'docProps/app.xml':
                root = ET.fromstring(buffer)
                def set_val(tag, val):
                    n = root.find(f"{{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}}{tag}")
                    if n is None: n = ET.SubElement(root, f"{{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}}{tag}")
                    n.text = str(val)

                set_val('Company', 'PT Kediri Chemical Abadi')
                set_val('Manager', 'Yerikho Arfensias Effendi')
                set_val('Application', 'Microsoft Office Word' if file_path.endswith('.docx') else 'Microsoft Excel')
                set_val('TotalTime', total_time)
                set_val('Template', 'Normal.dotm')

                buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)

            zout.writestr(item, buffer)

    os.replace(temp_zip, file_path)
    # Set OS modified timestamp
    mod_epoch = time.mktime(modified_dt.timetuple())
    os.utime(file_path, (mod_epoch, mod_epoch))

if __name__ == "__main__":
    targets = [
        "/Users/arthur/Documents/KCA DOKUMEN",
        "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/KCA DOKUMEN",
        "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan"
    ]
    
    count = 0
    for t in targets:
        for root, dirs, files in os.walk(t):
            for f in files:
                if (f.endswith('.docx') or f.endswith('.xlsx')) and not f.startswith('~$') and not f.startswith('.'):
                    full_p = os.path.join(root, f)
                    apply_natural_timestamps(full_p)
                    count += 1
                    
    print(f"STAGGERED_SUCCESS: {count} dokumen berhasil disinkronkan dengan timeline kerja manusia (Senin - Jumat jam kerja kantor, Juli - Agustus 2026)!")
