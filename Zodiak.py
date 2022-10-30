'''Program menentukan zodiak dari input tanggal lahir'''

print(80 * "=")
print("Silahkan masukkan tanggal lahir : ")
tanggal = int(input("Tanggal lahir (1-31)\t:"))
bulan = int(input("Bulan kelahiran (1-12)\t:"))

if (tanggal > 31 or tanggal < 1 or bulan > 12 or tanggal < 1 or (tanggal > 29 and bulan == 2)):
    print("Error input")
elif((tanggal >= 21 and bulan == 3) or (tanggal <= 19 and bulan == 4)):
    print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Aries\n")
elif ((tanggal >= 20 and bulan == 4) or (tanggal <= 20 and bulan == 5)):
    print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Taurus\n")
elif ((tanggal >= 21 and bulan == 5) or (tanggal <= 20 and bulan == 6)):
    print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Gemini\n")
elif ((tanggal >= 21 and bulan == 6) or (tanggal <= 22 and bulan == 7)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Cancer\n")
elif ((tanggal >= 23 and bulan == 7) or (tanggal <= 22 and bulan == 8)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Leo\n")
elif ((tanggal >= 23 and bulan == 8) or (tanggal <= 22 and bulan == 9)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Virgo\n")
elif ((tanggal >= 23 and bulan == 9) or (tanggal <= 22 and bulan == 10)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Libra\n")
elif ((tanggal >= 23 and bulan == 10) or (tanggal <= 21 and bulan == 11)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Scorpio\n")
elif ((tanggal >= 22 and bulan == 11) or (tanggal <= 21 and bulan == 12)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Sagitarius\n")
elif ((tanggal >= 22 and bulan == 12) or (tanggal <= 19 and bulan == 1)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Capricorn\n")
elif ((tanggal >= 20 and bulan == 1) or (tanggal <= 18 and bulan == 2)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Aquarius\n")
elif ((tanggal >= 19 and bulan == 2) or (tanggal <= 20 and bulan ==3)):
	print("Tanggal", +tanggal, "bulan", +bulan,", Zodiak anda Pisces\n")
else:
    print("Error input")