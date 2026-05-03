from django.shortcuts import render, get_object_or_404

PRODUK_LIST = [
    {
        'id': 1,
        'nama': 'Nike Air Zoom Pegasus 40',
        'merek': 'Nike',
        'harga': 1450000,
        'kategori': 'Running',
        'ukuran': '39, 40, 41, 42, 43, 44',
        'warna': 'Hitam / Putih',
        'stok': 12,
        'deskripsi': (
            'Nike Air Zoom Pegasus 40 adalah sepatu lari harian yang ringan dan responsif. '
            'Dilengkapi dengan bantalan Zoom Air di bagian depan kaki untuk memberikan '
            'dorongan energi di setiap langkah. Cocok untuk lari jarak menengah hingga jauh.'
        ),
        'fitur': ['Zoom Air cushioning', 'Mesh breathable upper', 'Rubber outsole'],
        'emoji': '👟',
        'badge': 'Best Seller',
    },
    {
        'id': 2,
        'nama': 'Adidas Ultraboost 23',
        'merek': 'Adidas',
        'harga': 1850000,
        'kategori': 'Running',
        'ukuran': '39, 40, 41, 42, 43',
        'warna': 'Putih / Abu-abu',
        'stok': 8,
        'deskripsi': (
            'Adidas Ultraboost 23 hadir dengan teknologi BOOST midsole terbaru yang memberikan '
            'pengembalian energi luar biasa. Upper menggunakan Primeknit+ yang menyesuaikan '
            'bentuk kaki secara natural. Pilihan terbaik untuk pelari yang menginginkan kenyamanan premium.'
        ),
        'fitur': ['BOOST midsole', 'Primeknit+ upper', 'Continental rubber outsole'],
        'emoji': '🏃',
        'badge': 'New',
    },
    {
        'id': 3,
        'nama': 'Puma Softride Premier',
        'merek': 'Puma',
        'harga': 780000,
        'kategori': 'Lifestyle',
        'ukuran': '38, 39, 40, 41, 42, 43, 44',
        'warna': 'Navy / Putih',
        'stok': 20,
        'deskripsi': (
            'Puma Softride Premier dirancang untuk kenyamanan sepanjang hari. '
            'Teknologi SoftFoam+ memberikan bantalan lembut yang nyaman dipakai dari pagi hingga malam. '
            'Desain yang simpel dan elegan cocok untuk aktivitas kasual maupun olahraga ringan.'
        ),
        'fitur': ['SoftFoam+ insole', 'Synthetic upper', 'Rubber traction outsole'],
        'emoji': '⚡',
        'badge': 'Hemat',
    },
    {
        'id': 4,
        'nama': 'New Balance Fresh Foam X 1080v12',
        'merek': 'New Balance',
        'harga': 2100000,
        'kategori': 'Running',
        'ukuran': '40, 41, 42, 43, 44',
        'warna': 'Biru / Putih',
        'stok': 5,
        'deskripsi': (
            'New Balance Fresh Foam X 1080v12 adalah sepatu lari premium dengan bantalan maksimal. '
            'Fresh Foam X midsole menggunakan data-driven design untuk memberikan ride yang halus dan lembut. '
            'Ideal untuk long run dan recovery run.'
        ),
        'fitur': ['Fresh Foam X midsole', 'Hypoknit upper', 'Blown rubber outsole'],
        'emoji': '🌊',
        'badge': 'Premium',
    },
    {
        'id': 5,
        'nama': 'Asics Gel-Kayano 30',
        'merek': 'Asics',
        'harga': 1950000,
        'kategori': 'Running',
        'ukuran': '39, 40, 41, 42, 43',
        'warna': 'Merah / Hitam',
        'stok': 7,
        'deskripsi': (
            'Asics Gel-Kayano 30 adalah sepatu stability running legendaris yang kini hadir dalam generasi ke-30. '
            'Teknologi GEL di heel dan forefoot memberikan perlindungan dari benturan. '
            'Cocok untuk pelari overpronator yang membutuhkan dukungan ekstra.'
        ),
        'fitur': ['GEL technology', 'FF BLAST PLUS ECO foam', 'LITETRUSS support system'],
        'emoji': '🔥',
        'badge': 'Terlaris',
    },
]


def homepage(request):
    featured = PRODUK_LIST[:3]
    return render(request, 'katalog/homepage.html', {'featured': featured})


def daftar_produk(request):
    return render(request, 'katalog/daftar_produk.html', {'produk_list': PRODUK_LIST})


def detail_produk(request, id):
    produk = next((p for p in PRODUK_LIST if p['id'] == id), None)
    if produk is None:
        from django.http import Http404
        raise Http404("Produk tidak ditemukan")
    return render(request, 'katalog/detail_produk.html', {'produk': produk})


def kontak(request):
    return render(request, 'katalog/kontak.html')
