'''program menghitung banyak angka anggota perkalian dalam suatu range bilangan'''

print("Menghitung banyak anggota perkalian dalam suatu range bilangan")

batasAtas = int(input("Masukkan nilai batas atas : "))
perkalian = int(input("Mencari anggota dari perkalian : "))

anggota = 0
for i in range(1, batasAtas + 1):
    if i % 3 == 0 :
        anggota += 1

print(f"Jumlah anggota perkalian {perkalian} dalam range 1-{batasAtas} adalah {anggota}")    