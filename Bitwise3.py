'''Program Menjalankan Operasi XOR pada Operator Bitwise'''


print('Operator Bitwise XOR')

print('Masukkan dua angka yang akan dioperasikan')
input1 = int(input('Angka Pertama\t: '))
input2 = int(input('Angka Kedua\t: '))
bitwise = input1 ^ input2

print('Angka', input1, 'memiliki binary : ', format(input1, '08b'))
print('Angka', input2, 'memiliki binary : ', format(input2, '08b'))

print('Hasil Bitwise \"XOR\"')
print('Binary :', format(bitwise, '08b'), ", Angka : ", bitwise)