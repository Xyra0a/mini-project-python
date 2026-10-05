saldo = 0

def setor():
    global saldo

    uang = int(input("Masukkan jumlah uang : "))
    saldo += uang

    print(f"Berhasil setor Rp{uang}")
    print(f"Saldo sekarang: Rp{saldo}")

def tarik():
    global saldo

    uang = int(input("Masukkan jumlah uang : "))

    if uang > saldo:
        print("Saldo tidak cukup")
    else:
        saldo -= uang
        print(f"Berhasil menarik Rp{uang}")
        print(f"Saldo sekarang: Rp{saldo}")


def lihat_saldo():
     print(f"Saldo Anda: Rp{saldo}")


while True:
    print("\n=== TABUNGAN SEDERHANA ===")
    print("1. Setor Uang")
    print("2. Tarik Uang")
    print("3. Lihat Saldo")
    print("4. Keluar")

    pilihan = int(input("Masukkan Pilihan Menu: "))

    if pilihan == 1:
        setor()

    elif pilihan == 2:
        tarik()

    elif pilihan == 3:
        lihat_saldo()

    elif pilihan == 4:
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")