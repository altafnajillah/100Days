'''Program menghitung gaji bersih dengan perbedaan pekerjaan'''

print()
print("Menghitung gaji bersih dengan perbedaan pekerjaan")
pekerjaan = input("Apakah Pekerjaannya PNS? [Y/n]\t: ")
gaji = int(input("Masukkan nilai gaji\t\t: "))

pajak = 0

if (pekerjaan.lower() == "y"):
    pajak += 5
else :
    pajak = pajak

if (gaji >= 5000000):
    pajak += 10
elif (gaji >= 3000000):
    pajak += 5
else :
    pajak = pajak * 0

nilaiPajak = int(gaji * pajak / 100)
gajiBersih = gaji - nilaiPajak

print()
print(f"""Rekap\t:
    Gaji\t: Rp.{gaji}
    Pajak\t: {pajak}%
    Nilai Pajak\t: Rp.{nilaiPajak}
    Gaji Bersih\t: Rp.{gajiBersih}
    """)