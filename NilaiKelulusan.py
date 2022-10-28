'''Program menentukan kelulusan berdasarkan input dua nilai. Pengetahuan dan Keterampilan'''

nilai1 = int(input("Nilai Pengetahuan\t: "))
nilai2 = int(input("Nilai Keterampilan\t: "))

nilai1 <= 100
nilai2 <= 100

print(80 * "=")

if (85 < nilai1 <= 100) :
    print("Nilai pengetahuan anda A")
elif (79 < nilai1 <= 85):
    print("Nilai pengetahuan anda A-")
elif (74 < nilai1 <= 79):
    print("Nilai pengetahuan anda B+")
elif (69 < nilai1 <= 74):
    print("Nilai pengetahuan anda B")
elif (64 < nilai1 <= 69):
    print("Nilai pengetahuan anda B-")
elif (54 < nilai1 <= 64):
    print("Nilai pengetahuan anda C")
elif (39 < nilai1 <= 54):
    print("Nilai pengetahuan anda D")
elif (0 < nilai1 <= 39):
    print("Nilai pengetahuan anda E")
else :
    print("Tidak Valid")

if (nilai1 > 39 and nilai2 > 39) :
    print("Selamat anda lulus")
else:
    print("Maaf, anda tidak lulus")


if (85 < nilai2 <= 100) :
    print("Nilai pengetahuan anda A")
elif (79 < nilai2 <= 85):
    print("Nilai pengetahuan anda A-")
elif (74 < nilai2 <= 79):
    print("Nilai pengetahuan anda B+")
elif (69 < nilai2 <= 74):
    print("Nilai pengetahuan anda B")
elif (64 < nilai2 <= 69):
    print("Nilai pengetahuan anda B-")
elif (54 < nilai2 <= 64):
    print("Nilai pengetahuan anda C")
elif (39 < nilai2 <= 54):
    print("Nilai pengetahuan anda D")
elif (0 < nilai2 <= 39):
    print("Nilai pengetahuan anda E")
else :
    print("Tidak Valid")

if (nilai1 > 39 and nilai2 > 39) :
    print("Selamat anda lulus")
else:
    print("Maaf, anda tidak lulus")
