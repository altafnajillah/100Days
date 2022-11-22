'''Program menghitung Volume benda yang berbentuk Limas Segi Empat'''

print('Menghitung luas permukaan limas segi empat')

PAlas = float(input('Masukkan nilai panjang rusuk alas \t: '))
Tinggi = float(input('Masukkan nilai tinggi limas \t\t: '))

LAlas = PAlas * PAlas

def volume(LAlas, Tinggi):
    v = LAlas * Tinggi / 3
    print(f'Volume\t\t= {v} satuan³')

volume (LAlas, Tinggi)