'''Program Menghitung jumlah karakter dalam suatu input'''

print('Menghitung jumlah karakter dalam suatu input')

input1 = input('Masukkan kata atau kalimat : ').lower()
input2 = input('Masukkan karakter atau huruf yang akan dihitung : ').lower()

hasil = input1.count(input2)

print('Hasil : ')
print(f'Jumlah karakter {input2} dalam kata atau kalimat {input1} adalah {hasil}')
print(50*'=')