'''Program menentukan hari dari kode input'''
print("Program Menentukan Hari")
hari0 = "Ahad"
hari1 = "Senin"
hari2 = "Selasa"
hari3 = "Rabu"
hari4 = "Kamis"
hari5 = "Jumat"
hari6 = "Sabtu"

hari = int(input("Masukkan Kode (0-6)\t:"))
if(hari == 0):
    print("Hari dari kode tersebut adalah", hari0)
elif(hari == 1):
    print("Hari dari kode tersebut adalah", hari1)
elif (hari == 2):
    print("Hari dari kode tersebut adalah", hari2)
elif(hari == 3):
    print("Hari dari kode tersebut adalah", hari3)
elif(hari == 4):
    print("Hari dari kode tersebut adalah", hari4)
elif(hari == 5):
    print("Hari dari kode tersebut adalah", hari5)
elif(hari == 6):
    print("Hari dari kode tersebut adalah", hari6)
else:
    print("Kode tidak valid")