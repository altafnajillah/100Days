'''Program menentukan angka yang sering muncul dari suatu input'''

import statistics

print('Program Menentukan Modus')
Bilangan = input('Masukkan Bilangan-bilangan (Pisahkan dengan koma) : ')
data = []

for i in Bilangan.split(','):
    data.append(int(i))

hasil = statistics.mode(data)
print('Hasil')
print(f'Modus dari deret {data}, adalah {hasil}')
print(60*'=')