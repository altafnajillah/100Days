'''Program menentukan arah mata angin dari input derajat'''

print('Program menentukan arah mata angin')

print('Masukkan input (0-359) : ')
derajat = float(input('Masukkan nilai derajat : '))

if 0 <= derajat < 359 :
    if derajat <= 11.25 or derajat >= 348.75 :
        print(f'arah {derajat} derajat Mengarah ke-U (Utara)')
    elif 11.25 < derajat <= 33.75 :
        print(f'arah {derajat} derajat Mengarah ke-UTL (Utara Timur Laut)')
    elif 33.75 < derajat <= 56.25 :
        print(f'arah {derajat} derajat Mengarah ke-TL (Timur Laut)')
    elif 56.25 < derajat <= 78.75 :
        print(f'arah {derajat} derajat Mengarah ke-TTL (Timur Timur Laut)')
    elif 78.75 < derajat <= 101.25 :
        print(f'arah {derajat} derajat Mengarah ke-T (Timur)')
    elif 101.25 < derajat <= 123.75 :
        print(f'arah {derajat} derajat Mengarah ke-TTG (Timur Menenggara)')
    elif 123.75 < derajat <= 146.25 :
        print(f'arah {derajat} derajat Mengarah ke-TG (Tenggara)')
    elif 146.25 < derajat <= 168.75 :
        print(f'arah {derajat} derajat Mengarah ke-STG (Selatan Menenggara)')
    elif 168.75 < derajat <= 191.25 :
        print(f'arah {derajat} derajat Mengarah ke-S (Selatan)')
    elif 191.25 < derajat <= 213.75 :
        print(f'arah {derajat} derajat Mengarah ke-SBD (Selatan Barat Daya)')
    elif 213.75 < derajat <= 236.25 :
        print(f'arah {derajat} derajat Mengarah ke-BD (Barat Daya)')
    elif 236.25 < derajat <= 258.75 :
        print(f'arah {derajat} derajat Mengarah ke-BBD (Barat Barat Daya)')
    elif 258.75 < derajat <= 281.25 :
        print(f'arah {derajat} derajat Mengarah ke-B (Barat)')
    elif 281.25 < derajat <= 303.75 :
        print(f'arah {derajat} derajat Mengarah ke-BBL (Barat Barat Laut)')
    elif 303.75 < derajat <= 326.25 :
        print(f'arah {derajat} derajat Mengarah ke-BL (Barat Laut)')
    elif 326.25 < derajat <= 348.75 :
        print(f'arah {derajat} derajat Mengarah ke-UTB (Utara Barat Laut)')
    else :
        ('Input Error, Periksa kembali')
else:
    print('Error input tidak sesuai')
print (60*'=')