def calculator():
    A = ("======== Calculator sederhana ========\n")
    B = ("1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Perpangkatan")
    return(A+B)
print(calculator())

def tambah():
    Data1 = int(input("Masukkan bilangan 1: "))
    Data2 = int(input("Masukkan bilangan 2: "))
    return Data1 + Data2 
def kurang():
    Data1 = int(input("Masukkan bilangan 1: "))
    Data2 = int(input("Masukkan bilangan 2: "))
    return Data1 - Data2 
def kali():
    Data1 = int(input("Masukkan bilangan 1: "))
    Data2 = int(input("Masukkan bilangan 2: "))
    return Data1 * Data2 
def bagi():
    Data1 = int(input("Masukkan bilangan 1: "))
    Data2 = int(input("Masukkan bilangan 2: "))
    return Data1 / Data2 
def pangkat():
    Data1 = int(input("Masukkan bilangan 1: "))
    Data2 = int(input("Masukkan bilangan 2: "))
    return Data1 ** Data2 

Data = int(input("Masukkan pilihan: "))
if Data == 5:
    Hasil = pangkat()
    print("Hasilnya:",Hasil)
elif Data == 4:
    Hasil = bagi()
    print("Hasilnya:",Hasil)
elif Data == 3:
    Hasil = kali()
    print("Hasilnya:",Hasil)
elif Data == 2:
    Hasil = kurang()
    print("Hasilnya:",Hasil)
elif Data == 1:
    Hasil = tambah()
    print("Hasilnya:",Hasil)
else:
    print("Maaf input operasi antara 1-5")