'''Program menghitung Mean'''

print('Program Menghitung Mean')

Banyak_Data = int(input('Masukkan Banyaknya Data = '))
x = []
for i in range(1, Banyak_Data + 1):
    print('Angka ke-', i, ': ',sep='' ,end='')
    x.append(int(input()))

print()

total = sum(x)

Mean = total / Banyak_Data
print('Mean =', Mean )

print(50*'=')