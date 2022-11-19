'''Program memperkirakan keadaan benda dalam air (Mengapung/Tenggelam/Melayang) berdasarkan volume dan berat benda'''

print("Memperkirakan keadaan benda dalam air berdasarkan hukum Archimedes dari volume dan berat benda")

rhoair = 1000.0
g = 10
V = float(input("Masukkan nilai volume benda (m³)\t: "))
m = float(input("Masukkan nilai berat benda (kg)\t\t: "))
rhobenda = m / V

print(f"Massa jenis benda adalah {rhobenda} kg/m³")
if (rhobenda < rhoair):
    print("Keadaan benda akan mengapung")
elif (rhobenda == rhoair):
    print("Keadaan benda akan melayang")
else:
    print("Keadaan benda akan tenggelam")