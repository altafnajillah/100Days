'''Program menghitung belanjaan dan kembalian'''
print('Program menghitung total belanjaan dan kembalian')

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

print('Sabun\t\t= 1\t\t\t\tParfum\t\t= 6')
print('Shampo\t\t= 2\t\t\t\tPewangi\t\t= 7')
print('Pasta Gigi\t= 3\t\t\t\tHandsanitizer\t= 8')
print('Sikat Gigi\t= 4\t\t\t\tLotion\t\t= 9')
print('Sabun Wajah\t= 5\t\t\t\tListerin\t= 10')

#Menghitung
def menghitung (namabarang, jumlah):
    harga = namabarang * jumlah
    print(f'Harga = {harga}')
    x.append(harga)
    print(50*'=')
    
Barang = 0
Jawab = 'y'

x = []
while Jawab.lower() == 'y':
    pilih = int(input('Masukkan Kode Barang : '))
    jumlah = int(input('Jumlah : '))

    if pilih == 1:
        print(f'Anda akan membeli Sabun sebanyak {jumlah} buah')
        namabarang = Sabun
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 2:
        print(f'Anda akan membeli Shampo sebanyak {jumlah} buah')
        namabarang = Shampo
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 3:
        print(f'Anda akan membeli Pasta Gigi sebanyak {jumlah} buah')
        namabarang = PastaGigi
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 4:
        print(f'Anda akan membeli Sikat Gigi sebanyak {jumlah} buah')
        namabarang = SikatGigi
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 5:
        print(f'Anda akan membeli Sabun Wajah sebanyak {jumlah} buah')
        namabarang = Sabun_Wajah
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 6:
        print(f'Anda akan membeli Parfum sebanyak {jumlah} buah')
        namabarang = Parfum
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 7:
        print(f'Anda akan membeli Pewangi sebanyak {jumlah} buah')
        namabarang = Pewangi
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 8:
        print(f'Anda akan membeli Handsanitizer sebanyak {jumlah} buah')
        namabarang = Handsanitizer
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 9:
        print(f'Anda akan membeli Lotion sebanyak {jumlah} buah')
        namabarang = Lotion
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    elif pilih == 10:
        print(f'Anda akan membeli Listerin sebanyak {jumlah} buah')
        namabarang = Listerin
        menghitung(namabarang, jumlah)
        Jawab = input('Ingin Menambahkan? [Y/n] : ')
        Barang += 1
        
    else:
        print('Barang tidak terdaftar')
    
total = sum(x)
print(f'Anda membeli {Barang} jenis barang.')
print(f'Total harga yang harus dibayar adalah Rp.{total}')
bayar = int(input('Jumlah yang dibayarkan Rp.'))
SisaUang = bayar - total
if SisaUang > 0:
    print(f'Terimakasih, Kembalian anda Rp.{SisaUang}')
elif SisaUang == 0:
    print(f'Uang anda pas, Terimakasih')
else :
    print(f'Uang anda kurang dari seharusnya, sisa yang harus dibayarkan adalah Rp.{abs(SisaUang)}')
print(50*'=')