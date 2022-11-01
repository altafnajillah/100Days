'''Program menghitung luas alas, total luas permukaan dan volume prisma segitiga sama sisi'''

print("Masukkan nilai dari prisma segitiga sama sisi yang akan dihitung:")
satuan = input("Masukkan satuan yang ingin dipakai (km/m/cm/mm)\t:")
sisialas = int(input("panjang sisi miring alas\t:"))
height = int(input("Tinggi prisma\t:"))

halas = (sisialas ** 2) - ((sisialas * 0.5) ** 2)
sisitegak = 3

luasalas = 0.5 * sisialas * halas
tluasperm = luasalas * 2 + sisialas * height * sisitegak
volume = luasalas * height

print("Tinggi dari segitiga sama sisi\t", halas, satuan)
print("Luas alas\t=", luasalas, satuan,"²")
print("Total luas permukaan\t=", tluasperm, satuan,"²")
print("Volume dari prisma segitiga sama sisi\t=", volume, satuan,"³")