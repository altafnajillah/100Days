'''Program mengurutkan nama dari inputan'''

print('Mengurutkan nama berdasarkan abjad')

huruf = input('Masukkan Nama-nama yang akan diurutkan : ')

urutan = huruf.split() 
urutan.sort()

print('Hasil Pengurutan : ')
for i in urutan:
    print(i)