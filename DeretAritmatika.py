'''Rumus mencari nilai ke-n dari deret aritmatika melalui input nilai
awal, jumlah suku dan beda'''

print('Mencari nilai dari suku ke-n deret aritmatika')

n = int(input('Masukkan nilai n \t: '))
a = int(input('Masukkan nilai awal \t: '))
b = int(input('Masukkan nilai beda \t: '))

U = a + (n - 1) * b

print(f'Nilai dari suku ke-{n} dari deret aritmatika tersebut adalah {U}')