daftar_menu = {
    "makanan" :[
        {"kode":"1", "menu":"nasi goreng", "harga":15000},
        {"kode":"2", "menu":"mie goreng", "harga":10000}
    ],

    "minuman":[
        {"kode":"3", "menu":"air putih", "harga":5000},
        {"kode":"4", "menu":"es jeruk", "harga":7000}
    ]
}

recap_menu = daftar_menu["makanan"] + daftar_menu["minuman"]
pesanan = []

while True:
    pilih_menu = input("Masukkan kode menu yang ingin dipesan : ")

    item_ditemukan = []

    for item in recap_menu:
        if item["kode"] == pilih_menu:
            item_ditemukan = item
            break

    if item_ditemukan:
        pesanan.append(item_ditemukan)
        print(f"Menu ditambahkan : {item_ditemukan["menu"]} - Rp{item_ditemukan["harga"]}")
    else:
        print("Kode tidak ditemukan, coba lagi!")
        continue

    tambah_pesanan = input("Tambah pesanan? y/n)").lower()
    if tambah_pesanan != "y":
        break

print("\n=== Ringkasan Pesanan ===")
total = 0

for item in pesanan:
    print(f"{item['menu']} - Rp{item['harga']}")
    total += item['harga']

print(f"\nTotal: Rp{total}")

while True:
    bayar = int(input("Masukkan nominal uang"))

    if bayar > total:
        kembalian = bayar - total
        print(f"Kembalian {kembalian}")
        break
    else:
        print("Masukin duit yang bener!!")
        continue







