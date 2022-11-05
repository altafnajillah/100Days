'''Program menghitung kecepatan akhir dari suatu gerak GLBB'''

print(80*"=")

print("Anda akan mencari nilai dari kecepatan akhir (vt).\nInput hal-hal berikut : ")
rumus = input("Apakah anda mengetahui nilai jarak (S)? [Y/N] : ")
if(rumus.lower() == "y"):
    S = float(input("Masukkan nilai jarak yang ditempuh (S) dalam satuan m : "))
    a = float(input("Masukkan nilai percepatan (a) dalam satuan m/s² : "))
    vo = float(input("Masukkan nilai kecepatan awal (vo) dalam satuan m/s : "))
    vt = ((vo ** 2) + (2 * a * S)) ** 0.5

elif(rumus.lower() == "n"):
    vo = float(input("Masukkan nilai kecepatan awal (vo) dalam satuan m/s : "))
    a = float(input("Masukkan nilai percepatan (a) dalam satuan m/s² : "))
    t = float(input("Masukkan nilai waktu yang dibutuhkan (t) dalam satuan detik : "))
    vt = vo + (a * t)

else:
    print("Input Error!. Silahkan periksa kembali")

print("Kecepatan akhirnya adalah", round(vt,2), "m/s")