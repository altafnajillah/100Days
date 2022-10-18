#Menghitung Bermacam-macam hal
'''misal dalam suatu soal terdapat satu kubus yang memiliki panjang rusuk 5 cm'''

print("Suatu kubus memiliki panjang rusuk 5 cm, maka :")
panjangrusuk = 5
jumlahsisi = 6
luassisi = panjangrusuk ** 2
volume = luassisi * panjangrusuk
tluaspermukaan = panjangrusuk ** 2 * jumlahsisi
jumlahrusuk = 12
tpanjangrusuk = panjangrusuk * jumlahrusuk
diagonalsisi = ((panjangrusuk ** 2 * 2) ** 0.5)
diagonalruang = ((diagonalsisi ** 2 + panjangrusuk ** 2) ** 0.5)

print("Total panjang rusuk keseluruhan adalah", tpanjangrusuk, "cm")
print("Luas satu sisinya adalah", luassisi, "cm persegi")
print("Total luas permukaannya adalah", tluaspermukaan, "cm persegi")
print("Volumenya adalah", volume, "cm kubik")
print("Panjang diagonal sisinya sekitar", round(diagonalsisi,2), "cm")
print("Panjang diagonal ruangnya sekitar", round(diagonalruang,2), "cm")