'''Peogram Menjalankan Operasi OR di Operator Bitwise'''

print('Operator Bitwise')

print('Masukkan dua angka yang akan dioperasikan')
angka1 = int(input('Angka Pertama\t: '))
angka2 = int(input('Angka Kedua\t: '))
Bitwise = angka1 | angka2

print('Angka', angka1, 'memiliki binary : ', format(angka1, '08b'))
print('Angka', angka2, 'memiliki binaty : ', format(angka2, '08b'))

print('Hasil Bitwise \"OR\"')
print('Binary :', format(Bitwise, '08b'), ", Angka : ", Bitwise)