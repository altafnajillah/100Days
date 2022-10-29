'''Program menghitung luas lingkaran, keliling lingkaran, luas permukaan Tabung, 
volume tabung dan diagonal ruang tabung'''

print("Masukkan nilai-nilai dari komponen berikut :")
jari2 = int(input("Jari-jari (cm)\t\t:"))
tinggi = int(input("Tinggi tabung (cm)\t:"))
p = 3.14

luasalas = p * jari2 ** 2
keliling = 2 * p * jari2
luasperm = 2 * luasalas + keliling * tinggi
voltabung = luasalas * tinggi
diagtabung = ((jari2 * 2) ** 2 + tinggi ** 2) ** 0.5

print("Luas alas dari tabung adalah", round(luasalas,2), "cm²")
print("Keliling dari tabung adalah", round(keliling,2), "cm")
print("Luas permukaan tabung adalah", round(luasperm,2), "cm²")
print("Volume maksimal tabung adalah", round(voltabung,2), "cm³")
print("Panjang diagonal ruang adalah", round(diagtabung,2), "cm")