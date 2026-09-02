import os
import zipfile
import xml.etree.ElementTree as ET
import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor

def sanitize_docx_metadata(doc_path, title="Dokumen Resmi PT Kediri Chemical Abadi", author="Yerikho Arfensias Effendi"):
    if not os.path.exists(doc_path):
        return
    
    doc = Document(doc_path)
    # 1. Update Core Properties
    core = doc.core_properties
    core.author = author
    core.last_modified_by = author
    core.title = title
    core.subject = "Sistem Manajemen Mutu ISO 9001:2015 & Operasional Bisnis"
    core.comments = "Dokumen Terkendali PT Kediri Chemical Abadi"
    core.category = "Dokumen Manajemen KCA"
    core.keywords = "PT Kediri Chemical Abadi, ISO 9001, CPKRT, SOP, Manajemen"
    core.modified = datetime.datetime.now()
    doc.save(doc_path)

    # 2. Update docProps/app.xml via zipfile to ensure Company & Manager are set to KCA & Yerikho
    temp_zip = doc_path + ".temp.zip"
    ET.register_namespace('', 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties')
    ET.register_namespace('vt', 'http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes')

    with zipfile.ZipFile(doc_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w') as zout:
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            if item.filename == 'docProps/app.xml':
                root = ET.fromstring(buffer)
                
                def set_or_create(tag_name, val):
                    node = root.find(f"{{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}}{tag_name}")
                    if node is None:
                        node = ET.SubElement(root, f"{{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}}{tag_name}")
                    node.text = val

                set_or_create('Company', 'PT Kediri Chemical Abadi')
                set_or_create('Manager', author)
                set_or_create('Application', 'Microsoft Office Word')
                buffer = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            zout.writestr(item, buffer)
    os.replace(temp_zip, doc_path)
    print(f"METADATA_SANITIZED: {doc_path} (Author: {author}, Company: PT Kediri Chemical Abadi)")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sanitize_docx_metadata(sys.argv[1])
    else:
        # Sanitize recent docs
        p1 = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Proposal/PROPOSAL_KERJASAMA_MAKLOON_CAPEX_200JT_KCA.docx"
        p2 = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/KCA DOKUMEN/06_MASTER_MANUAL_DAN_LEGALITAS/PROPOSAL_KERJASAMA_MAKLOON_CAPEX_200JT_KCA.docx"
        p3 = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Laporan Bulanan/LAPORAN_KEUANGAN_BULANAN_KCA_SEPTEMBER_2026.docx"
        for p in [p1, p2, p3]:
            sanitize_docx_metadata(p)
