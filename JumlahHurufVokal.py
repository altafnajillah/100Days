'''Program menghitung banyaknya huruf vokal dalam suatu input'''

print('Menghitung banyak huruf vokal')
Kata = input('Masukkan kata : ')

jumlah = 0
for i in Kata.lower():
    if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
        jumlah += 1
if jumlah > 0:
    print(f'Jumlah huruf vokal dalam {Kata} adalah {jumlah}')
else :
    print('Tidak ditemukan huruf vokal')

print(50*'=')    