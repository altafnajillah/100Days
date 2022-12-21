'''Program menghitung berat yang terdilatasi berdasarkan teori relativitas khusus'''

print('Program menghitung dilatasi berat')
pilih = input('Mencari berat benda bergerak? [Y/n] : ')

kecepatan = float(input('Kecepatan bergerak (Xc) \t= '))
satuan = input('Satuan (kg/g/dll)\t\t= ')

if pilih.lower() == 'y' :
    massadiam = float(input('Massa benda ketika diam \t= '))
    m = massadiam / (1-(kecepatan)** 2) ** 0.5
    print(f'Berat Bergerak massa adalah {round(m,2)}{satuan}')
elif pilih.lower() == 'n' :
    massabergerak = float(input('Massa benda ketika bergerak \t= '))
    m = massabergerak * (1-(kecepatan)** 2) ** 0.5
    print(f'Berat diam massa adalah {round(m,2)}{satuan}')
else :
    print('Input tidak terdaftar')
