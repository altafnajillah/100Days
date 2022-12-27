'''Program menghitung nilai investasi dalam jangka waktu'''

print("Menghitung nilai investasi : ")
persen = 5/100
modal = int(input("Masukkan modal : "))
lama = int(input("Lama modal : "))

for i in range(lama):
    print(modal)
    untung = modal * persen
    modal = modal + untung

print()