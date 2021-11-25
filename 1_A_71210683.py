def calculator():
    A = ("======== Calculator sederhana ========\n")
    B = ("1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Perpangkatan")
    return(A+B)
def tambah():
    Bilangan1 = int(input("Masukkan bilangan 1: "))
    Bilangan2 = int(input("Masukkan bilangan 2: "))
    return Bilangan1 + Bilangan2 
def kurang():
    Bilangan1 = int(input("Masukkan bilangan 1: "))
    Bilangan2 = int(input("Masukkan bilangan 2: "))
    return Bilangan1 - Bilangan2 
def kali():
    Bilangan1 = int(input("Masukkan bilangan 1: "))
    Bilangan2 = int(input("Masukkan bilangan 2: "))
    return Bilangan1 * Bilangan2    
def bagi():
    Bilangan1 = int(input("Masukkan bilangan 1: "))
    Bilangan2 = int(input("Masukkan bilangan 2: "))
    return Bilangan1 / Bilangan2 
def pangkat():
    Bilangan1 = int(input("Masukkan bilangan 1: "))
    Bilangan2 = int(input("Masukkan bilangan 2: "))
    return Bilangan1 ** Bilangan2

print(calculator())
Input = int(input("Masukkan pilihan: "))
if Input == 1:
    Hasil = tambah()
    print("Hasilnya:",Hasil)
elif Input == 2:
    Hasil = kurang()
    print("Hasilnya:",Hasil)
elif Input == 3:
    Hasil = kali()
    print("Hasilnya:",Hasil)
elif Input == 4:
    Hasil = bagi()
    print("Hasilnya:",Hasil)
elif Input == 5:
    Hasil = pangkat()
    print("Hasilnya:",Hasil)
else:
    print("Maaf input operasi antara A-E")