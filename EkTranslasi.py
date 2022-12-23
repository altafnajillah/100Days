'''Program menghitung momentum translasi suatu benda'''

print("Program Menghitung Momentum Translasi")
print("Masukkan nilai-nilai berikut :")

#Variabel
m = float(input("Berat (kg)\t= "))
v = float(input("Kecepatan (m/s)\t= "))

#Rumus / operasi aritmatika
Ekt = 0.5 * m * v ** 2

print("Energi kinetik translasi dari benda bermassa {} kg dengan kecepatan {} m/s".format(m, v))
#Penyesuaian
if Ekt < 1000 :
    hasil = Ekt
    print("adalah {} J".format(hasil))
    
else :
    hasil = Ekt / 1000
    print("adalah {} kJ".format(hasil))

print(80*'=')