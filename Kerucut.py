'''Program menghitung volume kerucut menggunakan fuction'''

print("Menghitung volume kerucut menggunakan function")

pi = 22/7

def volume(jari2, tinggi):
    volume = 1/3*pi*(jari2 ** 2) *tinggi
    print(f"volume dari kerucut tersebut adalah {volume}")

jari2 = float(input("Masukkan nilai jari-jari : "))
tinggi = float(input("Masukkan nilai tinggi : "))

volume(jari2, tinggi)
