'''Program menampilkan rumus momen inersia berdasarkan bentuk bedanya'''

print(60*("="))
print("Program rumus inersia")
print()
print("Pilih salah satu :")
print('''
Benda Titik\t= 1
Benda Panjang\t= 2
Bola\t\t= 3
Silinder\t= 4
''')

pilihan1 = input("Masukkan pilihan : ")
if (pilihan1 == "1"):
    print("\nInersia = mR²\n")
elif (pilihan1 == "2"):
    print('''
    Pilih salah satu :
    Diputar disalah satu ujung\t= 1
    Diputar tepat di tengah\t= 2
    ''')
    pilihan2 = input("Masukkan pilihan : ")
    if (pilihan2 == "1"):
        print("\nInersia = (1/3)mL²\n")
    elif (pilihan2 == "2"):
        print("\nInersia = (1/12)mL²\n")
    else :
        print("\nInput Tidak Valid\n")
elif (pilihan1 == "3"):
    print('''
    Pilih salah satu :
    Bola Berongga\t= 1
    Bola Pejal\t\t= 2
    ''')
    pilihan2 = input("Masukkan pilihan : ")
    if (pilihan2 == "1"):
        print("\nInersia = (2/3)mR²\n")
    elif (pilihan2 == "2"):
        print("\nInersia = (2/5)mR²\n")
    else :
        print("\nInput Tidak Valid\n")
elif (pilihan1 == "4"):
    print('''
    Pilih salah satu :
    Silinder Berongga Tipis\t\t= 1
    Silinder Pejal\t\t\t= 2
    Silinder Berongga Tidak Tipis\t= 3
    ''')
    pilihan2 = input("Masukkan pilihan : ")
    if (pilihan2 == "1"):
        print("\nInersia = mR²\n")
    elif (pilihan2 == "2"):
        print("\nInersia = (1/2)mR²\n")
    elif (pilihan2 == "3"):
        print("\nInersia = (1/2)m(R1² + R2²)\n")
    else :
        print("\nInput Tidak Valid\n")
else :
    print("\nInput Tidak Valid\n")
