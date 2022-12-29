'''Program index suatu nilai dalam list'''

myList = ["Ahad", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

hari = input("Masukkan nama hari : ")

for i, namahari in enumerate(myList):
    if namahari.lower() == hari.lower():
        print(f"Hari {hari} ada di indeks {i}")
        break
else :
    print("Maaf, hari yang anda cari tidak ada dalam list")