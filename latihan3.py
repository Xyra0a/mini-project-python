bilangan = int(input("Masukkan bilangan bulat positif "))

genap = 0
ganjil = 0

for item in range(1, bilangan + 1):
    if item % 2 == 0:               #4 % 2 = 0
                    #5 % 2 = 1 
                    #6 % 2 = 0
        print(f"{item} = genap")    
        genap += 1
    else:
        print(f"{item} = ganjil")    
        ganjil += 1

print(f"Jumlah bilangan genap {genap}") 
print(f"Jumlah bilangan ganjil {ganjil}") 




