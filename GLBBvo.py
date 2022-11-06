'''Program menghitung kecepatan awal dari suatu gerak GLBB'''

print(80*"=")
print("Anda akan mencari nilai dari kecepatan awal (vo).\nInput hal-hal berikut : ")
rumus = input("Apakah anda mengetahui nilai jarak (S)? [Y/N] : ")
if(rumus.lower() == "y"):
    S = float(input("Masukkan nilai jarak yang ditempuh (S) dalam satuan m : "))
    a = float(input("Masukkan nilai percepatan (a) dalam satuan m/s² : "))
    vt = float(input("Masukkan nilai kecepatan akhir (vt) dalam satuan m/s : "))
    vo = ((vt ** 2) - (2 * a * S)) ** 0.5

elif(rumus.lower() == "n"):
    vt = float(input("Masukkan nilai kecepatan akhir (vt) dalam satuan m/s : "))
    a = float(input("Masukkan nilai percepatan (a) dalam satuan m/s² : "))
    t = float(input("Masukkan nilai waktu yang dibutuhkan (t) dalam satuan detik : "))
    vo = vt - (a * t)

else:
    print("Input Error!. Silahkan periksa kembali")

print("Kecepatan awalnya adalah", round(vo,2), "m/s")