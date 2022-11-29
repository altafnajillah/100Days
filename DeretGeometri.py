'''Program menghitung panjang semula tali yang dipotong dengan 
deret aritmatika'''

print('Menghitung panjang semula tali')
print('Masukkan nilai-nilai berikut :')

a = int(input('Barisan pertama (U1) \t: '))
r = int(input('Rasio (r) \t\t: '))
n = int(input('Urutan Deret \t\t: '))

Un = a * r ** (n-1)

print(f'Nilai dari suku ke-{n} adalah {Un}')