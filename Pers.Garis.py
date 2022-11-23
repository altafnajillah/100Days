'''Program menentukan pesamaan garis lurus dari input titik dan gradien'''

print(80*'=')
print("Menentukan persamaan garis lurus.\nMasukkan nilai : ")

x1 = int(input("Masukkan nilai x dari titik \t: "))
y1 = int(input("Masukkan nilai y dari titik \t: "))
m = float(input("Masukkan nilai gradien \t\t: "))

print(f'Titik (x1, y1) = ({x1, y1}) dengan gradien {m}')

a = round(m, 1)
c = round((m * (-x1) + (y1)),1)

print(80*'#')
print('Hasil :')
print(f'y = {a}x + {c}, atau')
print(f'{a}x - y + {c} = 0')