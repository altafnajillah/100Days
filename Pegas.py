'''Program menentukan nilai konstanta pegas dari input beban dan pertambahan panjang'''

print('Masukkan nilai dari beberapa hal berikut :')

w = float(input('Masukkan nilai beban (kg)\t\t: '))
x = float(input('Masukkan nilai panjang pegas (m)\t: '))
g = 10
f = w * g
k = f / x
print(f'Konstanta dari pegas tersebut adalah {k} N/m')