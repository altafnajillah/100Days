'''Mengitung frekuensi ayunan bandul sederhana di bumi dengan menginput panjang tali bandul'''

print('Menghitung frekuensi bandul sederhana')

g = 10
pi = 3.14
l = float(input('Masukkan nilai tali : '))

f = (1/(2*pi)) * (g / l) ** 0.5
T = 1/f

print(f'Apabila panjang tali bandul adalah {l} m, dan gravitasi bumi adalah {g} m/s²') 
print(f'maka frekuensi ayunannya adalah {round(f,2)} Hz atau {round((f * 60), 2)} kali permenit')
print(f'Sedangkan Periode (T) atau waktu agar menyelesaikan satu getarannya adalah {T} detik')