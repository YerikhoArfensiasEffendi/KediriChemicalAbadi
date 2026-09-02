# 🚀 PANDUAN DEPLOYMENT WEBSITE KE HOSTINGER
## PROYEK: PT KEDIRI CHEMICAL ABADI

```
TARGET HOSTING : Hostinger Business Web Hosting / Cloud Hosting
FRAMEWORK      : React 19 + Vite 8
OUTPUT BUILD   : folder 'dist/' (Static Production Build)
```

---

## 🛠️ 1. CARA BUILD PRODUCTION STATIC FILE

Jalankan perintah berikut di terminal:
```bash
npm run build
```
Perintah ini akan mengompilasi seluruh kode React, Tailwind CSS, dan gambar ke dalam folder `dist/` yang super ringan, ter-minifikasi, dan siap diunggah.

---

## 🌐 2. KONFIGURASI `.htaccess` UNTUK HOSTINGER (SPA ROUTING)

Karena website ini menggunakan **React Router (Single Page Application)**, kita wajib menyertakan file `.htaccess` di dalam folder `public/` (agar otomatis tersalin ke `dist/` saat di-build).

File `.htaccess` memastikan ketika pengunjung membuka langsung URL seperti `kedirichemical.com/about` atau `kedirichemical.com/products`, server Hostinger tidak memunculkan error **404 Not Found**.

Isi file `.htaccess`:
```apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
</IfModule>
```

---

## 📤 3. CARA UPLOAD KE HOSTINGER (FILE MANAGER / GIT)

### Opsi A: Melalui File Manager hPanel Hostinger
1. Buka **hPanel Hostinger** $\rightarrow$ Pilih Domain $\rightarrow$ Buka **File Manager**.
2. Masuk ke folder `public_html/`.
3. Kompres seluruh isi folder `dist/` Anda menjadi file `.zip`.
4. Unggah file `.zip` ke dalam `public_html/` dan lakukan **Extract**.
5. Pastikan file `index.html` dan folder `assets/` berada langsung di dalam `public_html/`.

### Opsi B: Melalui Git Auto-Deploy Hostinger
1. Masukkan repository GitHub/GitLab ke menu **Git** di hPanel Hostinger.
2. Atur branch: `main`.
3. Set build directory ke: `dist`.

---

## 🔒 4. PENGATURAN SSL & DOMAIN RESMI
1. Pastikan fitur **Free Unlimited SSL** diaktifkan di hPanel Hostinger.
2. Aktifkan opsi **Force HTTPS** agar seluruh pengunjung otomatis diarahkan ke koneksi aman `https://`.
