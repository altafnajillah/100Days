'''Program menghitung pekerja berdasarkan perbedaan estimasi waktu'''

print("Program mencari jumlah pekerja dengan estimasi waktu")

def pekerja(p0, w0, w1):
    p1 = (w0 * p0) / w1
    print(f"Jumlah Pekerja baru adalah {p1} orang")

p0 = int(input("Masukkan banyak pekerja awal : "))
w0 = int(input("Masukkan lama waktu pengerjaan awal : "))
w1 = int(input("Masukkan target lama waktu pengerjaan baru : "))

pekerja(p0, w0, w1)