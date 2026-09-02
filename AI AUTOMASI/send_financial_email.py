import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_financial_report(month="September", year="2026", docx_path=None):
    recipient = "kdrchemicals@gmail.com"
    subject = f"📊 [LAPORAN KEUANGAN BULANAN] PT Kediri Chemical Abadi - Periode {month} {year}"
    
    body = f"""Kepada Yth.
Direktur Utama: Bpk. Yan Effendi
General Manager: Bpk. Yerikho Arfensias Effendi
PT Kediri Chemical Abadi

Berikut terlampir Laporan Keuangan & Posisi Kas Bulanan PT Kediri Chemical Abadi untuk periode {month} {year}.

══════════════════════════════════════════════════════════
RINGKASAN EKSEKUTIF KEUANGAN KCA ({month.upper()} {year}):
══════════════════════════════════════════════════════════
• Beban Gaji Karyawan (Payroll)   : Rp 7.500.000,- (3 Tim)
• Biaya Operasional Pabrik (OPEX) : Rp 4.500.000,- (Listrik, BBM, Konsumsi, Sanitasi, ATK)
• Total Beban Tetap Operasional    : Rp 12.000.000,- / bulan (Target BEP ~600 Jerigen 5L)
• Total Nilai Aset Pabrik          : Rp 260.000.000,- (Xenia 2012, 2 Mixer Manual, Bangunan)
• Sisa Hutang Restrukturisasi      : Rp 700.000.000,- (Tercatat di skedul pembayaran bertahap)

Dokumen lengkap ISO / Direksi terlampir dan telah diarsipkan secara rapi di:
Keuangan/Laporan Bulanan/LAPORAN_KEUANGAN_BULANAN_KCA_{month.upper()}_{year}.docx

Dibuat secara otomatis oleh Sistem Akuntansi & Finance AI PT Kediri Chemical Abadi.
"""

    smtp_user = os.environ.get("SMTP_USER")
    smtp_pass = os.environ.get("SMTP_PASSWORD")
    
    if smtp_user and smtp_pass:
        try:
            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            if docx_path and os.path.exists(docx_path):
                with open(docx_path, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(docx_path)}"')
                    msg.attach(part)
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
            server.quit()
            print(f"EMAIL_SENT_SUCCESS: Laporan berhasil dikirim ke {recipient}")
            return True
        except Exception as e:
            print(f"EMAIL_ERROR: {e}")
            return False
    else:
        print(f"EMAIL_DRAFT_READY: Laporan siap dikirim ke {recipient}")
        print("\n--- FORMAT RINGKASAN EMAIL ---")
        print(f"To: {recipient}")
        print(f"Subject: {subject}\n")
        print(body)
        return True

if __name__ == "__main__":
    m = sys.argv[1] if len(sys.argv) > 1 else "September"
    y = sys.argv[2] if len(sys.argv) > 2 else "2026"
    doc = f"/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Laporan Bulanan/LAPORAN_KEUANGAN_BULANAN_KCA_{m.upper()}_{y}.docx"
    send_financial_report(m, y, doc)
