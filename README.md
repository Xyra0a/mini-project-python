PENJELASAN KODE

daftar_menu = {
    "makanan": [
        {"kode": "1", "menu": "Nasi Goreng", "harga": 15000},
        {"kode": "2", "menu": "Mie Goreng", "harga": 12000},
    ],
    "minuman": [
        {"kode": "3", "menu": "Es Teh", "harga": 5000},
        {"kode": "4", "menu": "Es Jeruk", "harga": 7000},
    ]
}

KODE DI ATAS BERFUNGSI SEBAGAI PENAMPUNG SEMUA MENU YANG TERSEDIA DI SINI SAYA MENGGUNAKAN METHOD OBJECT + ARRAY
daftar_menu{

}

INI ADALAH OBJECT

"makanan" :[

]

INI ADALAH ARRAY

LALU DALAM MASING-MASING KATEGORI SAYA BUAT OBJECT LAGI

==================================================================

semua_menu = daftar_menu["makanan"] + daftar_menu["minuman"]
pesanan = []

VARIABEL PESANAN DIGUNAKAN SEBAGAI PENAMPUNG DI LOOPING KODE SELANJUTNYA


