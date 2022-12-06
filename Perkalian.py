'''Program menampilkan perkalian yang diminta'''

awal = int(input('Masukkan perkalian dimulai\t: '))
akhir = int(input('Masukkan perkalian berakhir\t: '))

for i in range(awal, akhir+1):
    print('\n', 20*'=','Perkalian', i, 20*'=')
    for j in range(1, 11):
        print(f'{j} x {i} = {i * j}')
        if j == 10:
            print(55*'=')