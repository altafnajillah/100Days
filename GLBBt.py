'''Program menghitung waktu dari suatu gerak GLBB'''

print(80*"=")
print("Anda akan mencari nilai dari waktu (t).\nInput hal-hal berikut : ")
rumus = input("Apakah anda mengetahui nilai jarak (S)? [Y/N] : ")
if(rumus.lower() == "y"):
    vo = float (input("MAsukkan nilai dari kecepatan awal (vo) dalam satuan m/s : "))
    a1 = float(input("Masukkan nilai percepatan (a) dalam satuan m/s² : "))
    S = float(input("Masukkan nilai jarak yang ditempuh (S) dalam satuan m : "))
    
    a = (0.5) * a1
    b = vo
    c = (-(S))
    
    t1 = int((-(b) + (b ** 2 - 4 * a * c) ** 0.5)/ 2 * a)
    t2 = int((-(b) - (b ** 2 - 4 * a * c) ** 0.5)/ 2 * a)

    if (t1 > 0):
        print("Waktu yang diperlukan adalah ", t1, "s")
    elif (t1 < 0 and t2 > 0):
        print("Waktu yang diperlukan adalah ", t2, "s")
    else:
        print("Hasil tidak ditemukan")

elif(rumus.lower() == "n"):
    vo = float (input("MAsukkan nilai dari kecepatan awal (vo) dalam satuan m/s : "))
    vt = float(input("Masukkan nilai kecepatan akhir (vt) dalam satuan m/s : "))
    a = float(input("Masukkan nilai percepatan (a) dalam satuan m/s² : "))
    t = (vt - vo) / a

    print("Waktu yang diperlukan adalah ", t, "s")
else:
    print("Input Error!. Silahkan periksa kembali")