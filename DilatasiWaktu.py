'''Program menghitung perbedaan selang waktu yang terasa oleh keadaan diam dan 
keadaan bergerak mendekati kecepatan cahaya berdasarkan teori dilatasi waktu'''

print('Program menghitung perbedaan waktu (Dilatasi Waktu) dari sudut pandang orang diam')
print('Silahkan masukkan input-input berikut :')

pilih = input('Apakah pengamat bergerak? [Y/n] : ')
v1 = float(input('Kecepatan pengamat bergerak (kecepatan cahaya (c))\t: ')) #contoh 0.8c ditulis 0.8
satuan = input('Masukkan satuan Waktu (detik/jam/hari/tahun/dll)\t: ')

if pilih.lower() == 'n':
    t0 = float(input('Waktu yang dialami pengamat yang diam\t\t\t: '))
    t1 = t0 * (1 - v1 ** 2) ** 0.5
    print(60*'=')
    print(f'Pengamat yang bergerak dengan kecepatan {v1}c merasakan kejadian dalam {round(t1,2)} {satuan}')
    print(f'Pengamat yang diam merasakan kejadian dalam {round(t0,2)} {satuan}')
elif pilih.lower() == 'y':
    t1 = float(input('Waktu yang diamati pengamat bergerak\t\t\t: '))
    t0 = t1 / (1 - v1 ** 2) ** 0.5
    print(60*'=')
    print(f'Pengamat yang bergerak dengan kecepatan {v1}c merasakan kejadian dalam {round(t1,2)} {satuan}')
    print(f'Pengamat yang diam merasakan kejadian dalam {round(t0,2)} {satuan}')
else:
    print('Pilihan tidak ditemukan')

print(60*'=')