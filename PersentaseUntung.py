'''Program Menghitung Persentase keuntungan melalui input harga beli dan harga jual'''

print('Program menghitung persentase untung')
print('Masukkan nilai-nilai berikut\t: ')

harga_beli = int(input('Masukkan nilai harga beli\t: '))
harga_jual = int(input('Masukkan nilai harga jual\t: '))

persen = ((harga_jual - harga_beli)/harga_jual) * 100
print(f'Hasil jika harga beli {harga_beli} dan harga jual {harga_jual}')
print(f'Persentase keuntungan adalah {round(persen,2)}%')

print(60*'=')