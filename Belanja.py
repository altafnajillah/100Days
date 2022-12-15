'''Program menghitung belanjaan'''

print('Program menghitung belanjaan dan kembalian')

#Daftar Harga
Sabun = 3000
Shampo = 1000
PastaGigi = 6000
SikatGigi = 3500
Sabun_Wajah = 15000
Parfum = 20000
Pewangi = 12000
Handsanitizer = 15000
Lotion = 25000
Listerin = 18000

print('Masukkan jumlah dari barang-barang berikut : ')
input0 = int(input('Sabun\t\t: '))
input1 = int(input('Shampo\t\t: '))
input2 = int(input('Pasta Gigi\t: '))
input3 = int(input('Sikat Gigi\t: '))
input4 = int(input('Sabun Wajah\t: '))
input5 = int(input('Parfum\t\t: '))
input6 = int(input('Pewangi\t\t: '))
input7 = int(input('Handsanitizer\t: '))
input8 = int(input('Lotion\t\t: '))
input9 = int(input('Listerin\t: '))

total0 = Sabun * input0
total1 = Shampo * input1
total2 = PastaGigi * input2
total3 = SikatGigi * input3
total4 = Sabun_Wajah * input4
total5 = Parfum * input5
total6 = Pewangi * input6
total7 = Handsanitizer * input7
total8 = Lotion * input8
total9 = Listerin * input9

Total = total0 + total1  + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9
print(f'Total Belanja anda adalah : Rp.{Total}')

input10 = int(input('Uang yang dibayarkan : Rp.'))
SisaUang = input10 - Total
if SisaUang > 0:
    print(f'Terimakasih, Kembalian anda Rp.{SisaUang}')
elif SisaUang == 0:
    print(f'Uang anda pas, Terimakasih')
else :
    print(f'Uang anda kurang dari seharusnya, sisah yang harus dibayarkan adalah Rp.{SisaUang}')