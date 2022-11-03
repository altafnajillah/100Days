'''Program menghitung Gerak jatuh bebas (GJB)'''

print(80*"=")
a = g = 10
dicari = input("Masukkan nilai yang ingin dicari (vt/t/ht) : ")

if (dicari == "vt" or dicari == "v"):
    print("Anda akan mencari nilai kecepatan akhir.\nMasukkan hal-hal berikut :")
    rumus = input("Apakah anda mengetahui nilai waktu (t)? [Y/N] : ")
    if (rumus.lower() == "y"):
        t = float(input("Masukkan nilai waktu (t) dalam s : "))
        vt = a * t
        print("Kecepatan setelah", t, "detik adalah :", round(vt,2), "m/s")
    elif (rumus.lower() == "n"):
        ht = float(input("Masukkan nilai ketinggian (ht) dalam m : "))
        vt = (2 * g * ht) ** 0.5
        print("Kecepatan setelah", ht, "m adalah :", round(vt,2), "m/s")
    else :
        print ("Error, input tidak valid")

elif (dicari == "t"):
    print("Anda akan mencari nilai waktu untuk sampai dipermukaan.\nMasukkan hal-hal berikut :")
    rumus = input("Apakah anda mengetahui nilai kecepatan akhir? [Y/N] : ")
    if (rumus.lower() == "y"):
        vt = float(input("Masukkan nilai kecepatan akhir (vt) dalam m/s : "))
        t = vt / g
        print("Waktu yang ditempuh adalah", round(t,2), "s")
    elif(rumus.lower() == "n"):
        ht = float(input("Masukkan nilai dari ketinggian (ht) dalam m : "))
        t = (2 * ht / g) ** 0.5
        print("Waktu yang ditempuh adalah", round(t,2), "s")
    else :
        print ("Error, input tidak valid")

elif (dicari == "ht" or dicari == "h"):
    print("Anda akan mencari nilai ketinggian.\nMasukkan hal-hal berikut :")
    t = float(input("Masukkan nilai waktu (t) dalam s : "))
    ht = 0.5 * g * t ** 2
    print("Ketinggian benda jatuh adalah", round(ht,2), "m")

else:
    print("Error, Kesalahan input silahkan periksa kembali")