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

semua_menu = daftar_menu["makanan"] + daftar_menu["minuman"]
pesanan = []

while True:
    choose_menu = input("Masukkan kode menu yang ingin dipesan: ")

    item_ditemukan = []
    for item in semua_menu:
        if item["kode"] == choose_menu:
            item_ditemukan = item
            break

    if item_ditemukan:
        pesanan.append(item_ditemukan)
        print(f"Menu ditambahkan: {item_ditemukan['menu']} - Rp{item_ditemukan['harga']}")
    else:
        print("Kode menu tidak ditemukan, coba lagi.")
        continue

    lanjut = input("Tambah pesanan lagi? (y/n): ").lower()
    if lanjut != "y":
        break

print("\n=== Ringkasan Pesanan ===")
total = 0
for item in pesanan:
    print(f"{item['menu']} - Rp{item['harga']}")
    total += item['harga']

print(f"\nTotal: Rp{total}")

while True:
    pembayaran = int(input("Masukkan jumlah pembayaran : Rp"))
    if pembayaran < total:
        print("Uang anda kurang, silahkan masukkan jumlah yang sesuai.")
    else:
        kembalian = pembayaran - total
        print(f"Pembayaran diterima. Kembalian: Rp{kembalian}")
        break

print("Terima kasih telah memesan di restoran kami!")