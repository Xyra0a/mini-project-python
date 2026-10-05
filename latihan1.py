belanja = int(input("Masukkan nominal belanja "))
total = 0

if belanja >= 500000:
    diskon = belanja * 0.2
elif belanja >= 200000 and belanja < 500000:
    diskon = belanja * 0.1
else:
    print("Tidak mendapat diskon")

total += belanja - diskon

print(f"Total belanja anda {belanja}")
print(f"Anda mendapat diskon {diskon}")
print(f"Total bayar {total}")
