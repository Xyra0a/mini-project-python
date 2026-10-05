def LuasLingkaran():
    r = int(input("Masukan r : ")) 
    p = 22/7
    luas = p * (r**2)

    print(f"Luas lingkaran adalah {luas} cm")

def KelilingLingkaran():
    r = int(input("Masukan r : ")) 
    p = 22/7
    keliling = 2 * (p * r)
    
    print(f"Keliling lingkaran adalah {keliling} cm")


while True:
    print("1. Luas Lingkaran")
    print("2. Keliling Lingkaran")

    pilihan = int(input("Masukkan pilihan operasi : "))

    if pilihan == 1:
        LuasLingkaran()
    elif pilihan == 2:
        KelilingLingkaran()
    else:
        print("Tidak valid")

