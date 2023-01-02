'''Program menghitung IP dari input nilai'''
print()
print("Program menghitung IP")

print('''Program ini menggunakan bobot penilaian sebagai berikut :
A\t= 4.00\t\t\tC\t= 2.00
A-\t= 3.75\t\t\tD\t= 1.00
B+\t= 3.50\t\t\tE\t= 0.00
B\t= 3.00\t\t\t
B-\t= 2.75\t\t\t

Note : Mungkin dapat berbeda-beda tergantung ketentuan yang berlaku
''')
x = []
y = []
banyakMakul = int(input("Berapa banyak mata kuliah yang diambil? : "))
print()

for i in range(1, banyakMakul + 1):
  print(f"Matakuliah ke-{i}")
  nilai = input("Masukkan nilai [A, A-, B+ dst]\t: ") #nilai yang di input berupa huruf. A, A-, B+, B, B- dan seterusnya
  sks = int(input(f"Masukkan bobot SKS makul ke-{i}\t: "))
  if (nilai.upper() == "A"):
      muatan = 4.00
  elif (nilai.upper() == "A-"):
      muatan = 3.75
  elif (nilai.upper() == "B+"):
      muatan = 3.50
  elif (nilai.upper() == "B"):
      muatan = 3.00
  elif (nilai.upper() == "B-"):
      muatan = 2.75
  elif (nilai.upper() == "C"):
      muatan = 2.00
  elif (nilai.upper() == "D"):
      muatan = 1.00
  elif (nilai.upper() == "E"):
      muatan = 0.00
  else :
      print("Input salah")
      break
  tNilai = muatan * sks  
  x.append(tNilai)
  y.append(sks)
  print()


totalSKS = sum(y)
total = sum(x)
print(f"Banyak matakuliah yang diambil : {banyakMakul}")
print(f"Total SKS\t: {totalSKS}")

ipk = total / totalSKS
print(f"IP anda\t\t: {round(ipk,2)}")
print()