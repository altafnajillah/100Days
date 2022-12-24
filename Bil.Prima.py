'''program mengecek apakah suatu bilangan merupakan bilangan prima atau bukan'''

print(60*"=")
print("Program mengecek bilangan prima")

angka = int(input("Masukkan sebuah bilangan bulat : "))

if (angka == 1 or angka == 2 or angka == 3 or angka == 5 or angka % 2 != 0 and angka % 3 != 0 and angka % 5 != 0 and angka % 7 != 0):
    print("Bilangan {} merupakan bilangan prima".format(angka))
else :
    print("Bilangan {} BUKAN merupakan bilangan prima".format(angka))

print(60*"=")
print()