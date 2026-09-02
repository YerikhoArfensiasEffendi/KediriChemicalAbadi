import os
import subprocess
import shutil

base_dir = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical"
template_path = os.path.join(base_dir, "Keuangan/Dashboard Keuangan Usaha Produksi PRO/5. Dashboard Usaha Produksi PRO (Data Kosong).xlsx")
target_path = os.path.join(base_dir, "Keuangan/Dashboard Keuangan PT Kediri Chemical Abadi.xlsx")

# 1. Copy clean template to target
shutil.copy2(template_path, target_path)

# 2. Use AppleScript to populate data cleanly via Microsoft Excel engine
applescript = f'''
tell application "Microsoft Excel"
    set display alerts to false
    open POSIX file "{target_path}"
    set wb to active workbook
    
    -- 1. SETUP SHEET
    tell worksheet "SETUP" of wb
        -- Info Perusahaan
        set value of range "C6" to "PT KEDIRI CHEMICAL ABADI"
        set value of range "C7" to "RT.1/RW.6, Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161"
        set value of range "C8" to "082244006699"
        set value of range "C9" to "kdrchemicals@gmail.com"
        
        -- Bank & Akun Kas
        set value of range "C13" to "Bank Mandiri"
        set value of range "D13" to "1710066990006"
        set value of range "E13" to "PT Kediri Chemical Abadi"
        set value of range "F13" to 0
        
        set value of range "C14" to "Kas Tunai (Cash)"
        set value of range "D14" to "-"
        set value of range "E14" to "Kas Operasional Pabrik"
        set value of range "F14" to 0
        
        -- Daftar 8 Produk
        set prodCodes to {{"KCA-PR-001", "KCA-PR-002", "KCA-PR-003", "KCA-PR-004", "KCA-PR-005", "KCA-PR-006", "KCA-PR-007", "KCA-PR-008"}}
        set prodCats to {{"Laundry Care", "Kitchen Care", "Laundry Specialty", "Laundry Specialty", "Laundry Specialty", "Spotting Agent", "Spotting Agent", "Spa Specialty"}}
        set prodNames to {{"Liquid Detergent (1L, 5L, 20L)", "Liquid DishWasher (1L, 5L, 20L)", "Pencerah Warna / Oxygen Bleach (1L-20L)", "Emulsifier Pengangkat Lemak (1L-20L)", "Bleach Pemutih Klorin (1L-20L)", "Rust Tex Perontok Noda Karat (1L-20L)", "Blood Tex Perontok Noda Darah (1L-20L)", "Peluruh Noda Minyak SPA (10 kg Pail)"}}
        set prodUnits to {{"Jerigen / Pcs", "Jerigen / Pcs", "Jerigen / Pcs", "Jerigen / Pcs", "Jerigen / Pcs", "Jerigen / Pcs", "Jerigen / Pcs", "Pail"}}
        
        repeat with i from 1 to 8
            set rowIdx to (5 + i) as text
            set value of range ("G" & rowIdx) to (item i of prodCodes)
            set value of range ("H" & rowIdx) to (item i of prodCats)
            set value of range ("I" & rowIdx) to (item i of prodNames)
            set value of range ("J" & rowIdx) to (item i of prodUnits)
        end repeat
    end tell
    
    -- 2. GAJI KARYAWAN SHEET
    tell worksheet "GAJI KARYAWAN" of wb
        set staffNames to {{"Yerikho Arfensias Effendi", "Operator Produksi Pabrik", "Tenaga Operasional & Delivery"}}
        set staffDepts to {{"Manajemen Umum & Finance", "Produksi & Mixing", "Operasional & Logistik"}}
        set staffStatus to {{"Karyawan Tetap", "Karyawan Tetap", "Freelance / Lapangan"}}
        
        repeat with i from 1 to 3
            set rIdx to (5 + i) as text
            set value of range ("E" & rIdx) to "September"
            set value of range ("F" & rIdx) to 2026
            set value of range ("G" & rIdx) to (item i of staffNames)
            set value of range ("H" & rIdx) to (item i of staffStatus)
            set value of range ("I" & rIdx) to (item i of staffDepts)
            set value of range ("J" & rIdx) to 2500000
            set value of range ("K" & rIdx) to 0
            set value of range ("L" & rIdx) to 0
        end repeat
    end tell
    
    -- 3. ASET & DEPRESIASI SHEET
    tell worksheet "ASET & DEPRESIASI" of wb
        set assetCodes to {{"AS001", "AS002", "AS003", "AS004"}}
        set assetNames to {{"Daihatsu Xenia 2012 Bekas", "Mesin Pengaduk Manual Unit 1", "Mesin Pengaduk Manual Unit 2", "Bangunan Pabrik Pagung Kediri"}}
        set assetCats to {{"Kendaraan Operasional", "Mesin & Peralatan", "Mesin & Peralatan", "Bangunan Pabrik"}}
        set assetCosts to {{150000000, 5000000, 5000000, 100000000}}
        set assetLifes to {{8, 5, 5, 20}}
        
        repeat with i from 1 to 4
            set rIdx to (5 + i) as text
            set value of range ("D" & rIdx) to (item i of assetCodes)
            set value of range ("E" & rIdx) to (item i of assetNames)
            set value of range ("F" & rIdx) to (item i of assetCats)
            set value of range ("G" & rIdx) to "1 September 2026"
            set value of range ("H" & rIdx) to "September"
            set value of range ("I" & rIdx) to 2026
            set value of range ("J" & rIdx) to 1
            set value of range ("K" & rIdx) to (item i of assetCosts)
            set value of range ("L" & rIdx) to 0
            set value of range ("M" & rIdx) to (item i of assetLifes)
        end repeat
    end tell
    
    -- 4. HUTANG SHEET
    tell worksheet "HUTANG" of wb
        set value of range "D6" to "1 September 2026"
        set value of range "E6" to "September"
        set value of range "F6" to 2026
        set value of range "G6" to "H-001"
        set value of range "H6" to "Hutang Usaha Restrukturisasi Bisnis"
        set value of range "I6" to "Hutang Restrukturisasi Usaha"
        set value of range "J6" to 700000000
        set value of range "K6" to 0
        set value of range "L6" to 0
        set value of range "M6" to 0
        set value of range "N6" to 700000000
        set value of range "O6" to "Restrukturisasi Bertahap"
    end tell
    
    -- 5. HARGA JUAL SHEET
    tell worksheet "HARGA JUAL" of wb
        repeat with i from 1 to 8
            set rIdx to (5 + i) as text
            set value of range ("D" & rIdx) to (item i of prodCodes)
            set value of range ("E" & rIdx) to (item i of prodNames)
            set value of range ("F" & rIdx) to (item i of prodCats)
        end repeat
    end tell

    save wb
    close wb
    set display alerts to true
end tell
'''

res = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
print("AppleScript Output:", res.stdout)
if res.stderr:
    print("AppleScript Error:", res.stderr)
