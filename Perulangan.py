'''operasi perulangan pada python'''

#print satu persatu secara vertikal
kata = 'RPL'
for x in kata:
    print(x)

#print angka ganjil dengan operasi for
print("\n", 80 * "=")
print("Menampilkan angka ganjil secara vertikal")
for y in range(1,10,2):
    print(y)

#While
print("\n", 80 * "=")
hitung = 0
jawab = input("Apakah anda ingin memulai operasi?\n")
jawaban1 = "ya"
jawaban2 = "tidak"

while (jawab.lower() == jawaban1.lower()):
    hitung += 1
    jawab = input("Apakah anda ingin mengulang operasi?\n")
    if jawab == jawaban2:
        print("Hitungan Selesai")
        break
    elif jawab == jawaban1:
        print("Operasi diulangi")
    else :
        print("Periksa input")

print("Perulangan yang dihitung sebanyak :", hitung, "Kali")