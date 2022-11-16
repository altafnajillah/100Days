#Program Menentukan memunculkan Index

print("Index Ibukota Provinsi di Sulawesi")

kota = ['Makassar','Kendari','Palu','Gorontalo','Manado','Mamuju']
dicari = input('Ketik kota yang anda cari :')

for i, namakota in enumerate (kota):
    if namakota.lower() == dicari.lower():
        print("Kota yang anda cari ada di indeks", i)
        break
else:
    print("Maaf, kota yang anda cari tidak ada dalam list")