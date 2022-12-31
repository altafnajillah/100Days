'''Program memprint inputan string mulai dari huruf pertama sampai terakhir kemudian kembali'''

print("Memprint string seperti Bintang")

nama = input("Masukkan kata / nama : ")

print()
for i in range(len(nama)):
    for j in range(i + 1):
        print(nama[j], end=" ")

    print()

for i in range(len(nama)-2, -1, -1):
    for j in range(i + 1):
        print(nama[j], end=" ")

    print()
print()