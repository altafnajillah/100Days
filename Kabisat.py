'''Program menentukan tahun kabisat dari input'''

print("="*80)
print("Menentukan Tahun Kabisat")

tahun = int(input("Masukkan nilai tahun : "))

if tahun % 4 == 0 :
    print(f"{tahun} Masehi merupakan tahun kabisat")

else:
    print(f"{tahun} Masehi BUKAN merupakan tahun kabisat")