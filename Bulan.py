'''Program menentukan nama bulan dari input angka ataupun singkatan'''

print("Masukkan angka ataupun singkatan\t:")

input = input("Angka atau singkatan\t:")

if (input == "1" or input == "01" or input == "Jan" or input == "jan"):
    print("Nama bulan : Januari")
elif (input == "2" or input == "02" or input == "Feb" or input == "feb"):
    print("Nama bulan : Februari")
elif (input == "3" or input == "03" or input == "Mar" or input == "mar"):
    print("Nama bulan : Maret")
elif (input == "4" or input == "04" or input == "Apr" or input == "apr"):
    print("Nama bulan : April")
elif (input == "5" or input == "05" or input == "Mei" or input == "mei"):
    print("Nama bulan : Mei")
elif (input == "6" or input == "06" or input == "Jun" or input == "jun"):
    print("Nama bulan : Juni")
elif (input == "7" or input == "07" or input == "Jul" or input == "jul"):
    print("Nama bulan : Juli")
elif (input == "8" or input == "08" or input == "Agu" or input == "agu"):
    print("Nama bulan : Agustus")
elif (input == "9" or input == "09" or input == "Sep" or input == "sep"):
    print("Nama bulan : September")
elif (input == "10" or input == "Okt" or input == "okt"):
    print("Nama bulan : Oktober")
elif (input == "11" or input == "Nov" or input == "nov"):
    print("Nama bulan : November")
elif (input == "12" or input == "Des" or input == "des"):
    print("Nama bulan : Desember")
else :
    print("Input tidak Valid")
