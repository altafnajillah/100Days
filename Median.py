'''Program menghitung Mean'''

print('Program Menghitung Mean')

def nilai_tengah (Data):
    Data.sort()
    banyak_data = len(Data)
    nilai_tengah = banyak_data // 2
    if banyak_data % 2 == 1:
        return Data[nilai_tengah]
    else :
        return (Data[nilai_tengah - 1] + Data[nilai_tengah]) / 2

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
Data = []

for bilangan in inputan.split(','):
    Data.append(int(bilangan))

print(f'Data yang di input adalah {Data}')
print(f'Median dari data tersebut adalah {nilai_tengah(Data)}')

print(60*'=')