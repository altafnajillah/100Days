# NIM D0222528
nama = "Sadly"
status = False
gajipokok = 1000000
gajilembur = 5000
lamalembur = 28
tgajilembur = gajilembur * lamalembur
gajikotor = gajipokok + tgajilembur
pajak = 10/100
tpajak = int(gajikotor * pajak)
gajibersih = int(gajikotor - tpajak)

print("Nama\t\t\t\t:", nama)
print("Status Pernikahan\t:", status)

print("\nInfo Gaji")
print("Gaji Pokok\t= Rp.", gajipokok)
print("Gaji Lembur\t= Rp.", gajilembur, "Perjam")
print("Gaji Kotor\t= Rp.", gajikotor)
print("Pajak\t\t= Rp.", tpajak)
print("Gaji Total\t= Rp.", gajibersih)

