'''Program Menghitung Gerak Lurus Berubah Bertauran'''
print(80*"=")

print("Anda akan mencari nilai dari percepatan (a).\nInput hal-hal berikut : ")

rumus = input("Apakah anda mengetahui nilai jarak (S)? [Y/N] : ")
if(rumus.lower() == "y"):
    rumus2 = input("Apakah anda mengetahui nilai kecepatan akhir (vt)? [Y/N] : ")
    if (rumus2.lower() == "y"):
        S = int(input("Masukkan nilai jarak tempuh (m) : "))
        vo = int(input("Masukkan nilai kecepatan awal (m/s) : "))
        vt = int(input("Masukkan nilai kecepatan akhir (m/s) : "))
        a = ((vt ** 2) - (vo ** 2)) / (2 * S)

    elif (rumus2.lower() == "n"):
        S = int(input("Masukkan nilai jarak tempuh (m) : "))
        vo = int(input("Masukkan nilai kecepatan awal (m/s) : "))
        t = int(input("Masukkan nilai waktu yang digunakan (detik) : "))
        a = (S - vo * t) / (0.5 * t ** 2)

    else :
        print ("Error, input tidak valid")

elif(rumus.lower() == "n"):    
    vo = int(input("Masukkan nilai kecepatan awal (m/s) : "))
    vt = int(input("Masukkan nilai kecepatan akhir (m/s) : "))
    t = int(input("Masukkan nilai waktu yang digunakan (detik) : "))
    a = (vt - vo) / t

else :
    print ("Error, input tidak valid")

print("Nilai dari percepatan adalah", round(a,2), "m/s²")