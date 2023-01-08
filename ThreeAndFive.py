'''Program pride of three, pride of five or Master class dari input'''

angka = int(input("Masukkan angka : "))

if (angka % 3 == 0 and angka % 5 == 0):
    print("Master Class")
elif (angka % 3 == 0):
    print("Pride of Three")
elif (angka % 5 == 0):
    print("Pride of Five")
else :
    print("Nothing")
print()