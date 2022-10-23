'''Program menentukan tinggi suatu gedung berdasarkan input jarak dan sudut yang diapit
dari bidang horizontal'''
import math

halfcir = 180
phi = 3.14

print("Program menentukan tinggi gedung melalui trigonometri")
print("Silahkan masukkan data-data berikut\t:")

sudut =float(input("Besar sudut (°)\t\t\t: "))
jarak =float(input("Jarak dari gedung (m)\t: "))

tsudut = sudut * phi / halfcir

tinggi = jarak * math.tan(tsudut)

print("Ketinggian gedung tersebut adalah : ", round(tinggi,3), "meter")