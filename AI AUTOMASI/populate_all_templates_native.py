import subprocess

applescript = '''
tell application "Microsoft Excel"
    set display alerts to false
    set targetPath to "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Dashboard Keuangan PT Kediri Chemical Abadi.xlsx"
    open POSIX file targetPath
    set wb to active workbook
    
    set tmplSheets to {"INVOICE", "QUOTATION", "PURCHASE ORDER", "SALES ORDER", "DELIVERY ORDER", "PURCHASE REQUEST"}
    repeat with shName in tmplSheets
        try
            tell worksheet shName of wb
                set value of range "D6" to "PT KEDIRI CHEMICAL ABADI"
                set value of range "D7" to "RT.1/RW.6, Pagung, Kec. Semen, Kabupaten Kediri, Jawa Timur 64161"
                set value of range "D8" to "0822-4400-6699 | kdrchemicals@gmail.com"
            end tell
        end try
    end repeat
    
    try
        tell worksheet "SLIP GAJI" of wb
            set value of range "C6" to "PT KEDIRI CHEMICAL ABADI"
            set value of range "C7" to "RT.1/RW.6, Pagung, Kec. Semen, Kediri, Jawa Timur"
        end tell
    end try
    
    save wb
    close wb
    set display alerts to true
    return "TEMPLATES POPULATED SUCCESSFULLY"
end tell
'''

res = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Error:", res.stderr)
