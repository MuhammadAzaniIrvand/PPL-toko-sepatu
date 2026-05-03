# SoleStore - Website Katalog Sepatu Olahraga

## Informasi Mahasiswa
- Nama : Muhammad Azani Irvand
- NIM  : 2308107010026
- Framework: Django (Python)

---

## Deskripsi Program

**SoleStore** adalah website katalog produk sepatu olahraga sederhana yang dibangun menggunakan framework Django. Website ini menampilkan daftar produk sepatu dari berbagai brand ternama (Nike, Adidas, Puma, New Balance, Asics) beserta detail spesifikasinya.

### Halaman yang Tersedia

| URL | Halaman | Keterangan |
|-----|---------|------------|
| `/` | Homepage | Halaman utama dengan hero section dan produk pilihan |
| `/produk/` | Daftar Produk | Grid katalog semua produk (5 produk) |
| `/produk/<id>/` | Detail Produk | Detail lengkap satu produk berdasarkan ID |
| `/kontak/` | Kontak | Informasi kontak dan jam operasional toko |

### Fitur
- Routing menggunakan `urls.py` Django
- Template HTML menggunakan Django Template Language (DTL)
- Data produk hardcoded (tanpa database)
- Desain responsif dengan CSS murni
- Navigasi aktif otomatis sesuai halaman

---

## Cara Menjalankan

### 1. Pastikan Python dan Django sudah terinstall
```bash
pip install django
```


### 2. Masuk ke folder proyek
```bash
cd toko_sepatu
```

### 3. Jalankan development server
```bash
python manage.py runserver
```

### 4. Buka browser
```
http://127.0.0.1:8000/
```

---

## Struktur Folder

```
toko_sepatu/
├── manage.py
├── README.md
├── toko_sepatu/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── katalog/
    ├── __init__.py
    ├── urls.py
    ├── views.py
    ├── static/
    │   └── katalog/
    │       └── css/
    │           └── style.css
    └── templates/
        └── katalog/
            ├── base.html
            ├── homepage.html
            ├── daftar_produk.html
            ├── detail_produk.html
            └── kontak.html
```
# PPL-toko-sepatu
