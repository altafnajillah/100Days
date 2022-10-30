'''Program pemberian Izin berdasarkan status True or False'''

print(80*"=")
print("Masukkan input biodata berikut")

nama = input("Masukkan nama anda\t\t:")
usia = int(input("Masukkan usia anda\t\t:"))
status = input("Masukkan status (True/False)\t:")

print("Hai, nama anda", nama)
print("Usia anda :", usia, "Tahun")
print("Status anda", status)

if (usia <= 0):
    print("Data error, input salah")
elif (usia >= 18 and (status == "True" or status == "true")):
    print("Selamat, izin diberikan. Anda memenuhi kedua syarat")
elif (usia >= 18 or (status == "True" or status == "true")):
    print("Selamat, izin diberikan. Anda telah memenuhi salah satu syarat")
elif (usia < 18 and (status == "False" or status =="false")):
    print("Maaf, Permohonan izin ditolak")
else:
    print("Input error, periksa kembali")