'''Program menghitung total jumlah suku ke-n dari suatu deret aritmatika'''

print('Menghitung jumlah total deret aritmatika\nMencari nilai suku ke-n, Masukkan input :')

n = int(input('Masukkan nilai n \t: '))
a = int(input('Masukkan nilai awal \t: '))
b = int(input('Masukkan nilai beda \t: '))

Un = a + (n - 1) * b

Sn = 0.5 * n * (a + Un)

print(f'Nilai Suku ke-{n} adalah {Un}')
print(f'Jumlah total dari suku pertama sampai dengan suku ke-{n} adalah {Sn}')