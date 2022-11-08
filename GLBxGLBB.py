'''Program menghitung waktu jatuh dan jarak maksimal jatuh suatu objek yang sebelumnya bergerak lurus beraturan'''

print(80 * "=")
print("Program menghitung waktu jatuh dan jarak maksimal jatuh suatu objek")
print("1. Waktu Jatuh\n2. Jarak jatuh terjauh")
rumus = input("Pilih program yang anda inginkan [1/2] : ")
g = 10

if (rumus == "1"):
    print("Menghitung waktu saat jatuh ke tanah")
    def waktujatuh(h):
        tjatuh = (2 * h / g) ** 0.5
        print("Waktu jatuhnya ke bidang horizontal adalah", round(tjatuh,2), "s")

    waktujatuh(float(input("Masukkan nilai Ketinggian (h) dalam meter :")))

elif (rumus == "2"):
    print("Menghitung jarak terjauh benda sampai ke tanah")
    def jarakjatuh(h, v):
        Sjatuh = v * ((2 * h / g) ** 0.5)
        print("Jarak jatuhnya benda tersebut dalam bidang horizontal adalah", round(Sjatuh,2), "m")

    h = float(input("Masukkan nilai ketinggian (h) dalam meter : "))
    v = float(input("Masukkan nilai dari kecepatan horizontal awal (vo) dalam m/s : "))
    jarakjatuh(h, v)

else:
    print("Input Error. Silahkan periksa kembali")
   
