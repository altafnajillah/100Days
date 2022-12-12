'''Program menghitung Median'''

print('Program Menghitung Median')

Banyak_Data = int(input('Masukkan Banyaknya Data = '))
x = []
for i in range(1, Banyak_Data + 1):
    print('Angka ke-', i, ': ',sep='' ,end='')
    x.append(int(input()))

print()

total = sum(x)

median = total / Banyak_Data
print('Median =', median )

print(50*'=')