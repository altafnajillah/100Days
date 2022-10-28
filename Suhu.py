'''Program Konversi Suhu'''

print(80 * "=")
print("Program pengonversi suhu")
print("Silahkan pilih satuan suhu yang akan dikonversi :")
print("1. Celsius\n2. Farenheit\n3. Kelvin\n4. Reamur\n")

satuan = int(input("Masukkan pilihan anda (1/2/3/4)\t: "))

if (satuan < 1 or satuan > 4):
    print("Input Error, Kesalahan dalam memilih satuan asal")
elif (satuan == 1):
    print("Anda memilih konversi dari satuan Celsius")
    nilai = int(input("Masukkan suhu dalam satuan °C\t= "))
    F = nilai * 9 / 5 + 32
    K = nilai + 273
    R = nilai * 4 / 5
    print("konversi", nilai, "°C Sama dengan :\n", F, "°F\n", K, "K\n", R, "°R\n")

elif (satuan == 2):
    print("Anda memilih konversi dari satuan Farenheit")
    nilai = int(input("Masukkan suhu dalam satuan °F\t= "))
    C = 5 / 9 * (nilai - 32)
    K = 5 / 9 * (nilai - 32) + 273
    R = 4 / 9 * (nilai - 32)
    print("konversi", nilai, "°F Sama dengan :\n", C, "°C\n", K, "K\n", R, "°R\n")

elif (satuan == 3):
    print("Anda memilih konversi dari satuan Kelvin")
    nilai = int(input("Masukkan suhu dalam satuan K\t= "))
    C = nilai - 273
    F = 9 / 5 * (nilai - 273) + 32
    R = 4 / 5 * (nilai - 273)
    print("Konversi", nilai, "K sama dengan :\n", C, "°C\n", F, "°F\n", R, "°R\n")

else :
    print("Anda memilih konversi dari satuan Reamur")
    nilai = int(input("Masukkan suhu dalam satuan °R\t= "))
    C = 5 / 4 * nilai
    F = 9 / 4 * nilai + 32
    K = 5 / 4 * nilai + 273
    print("Konversi", nilai, "°R sama dengan :\n", C, "°C\n", F, "°F\n", K, "K\n")