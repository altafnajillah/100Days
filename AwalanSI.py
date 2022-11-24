'''Program menentukan awalan Satuan internasional'''

print('Program menentukan awalan Satuan internasional')

simbol = input('Masukkan simbol : ')

if simbol == 'Y' :
    print('yotta-')
elif simbol == 'Z':
    print('zetta-')
elif simbol == 'E' :
    print('eksa-')
elif simbol == 'P':
    print('peta-')
elif simbol == 'T':
    print('tera-')
elif simbol == 'G':
    print('giga-')
elif simbol == 'M':
    print('mega-')
elif simbol == 'k':
    print('kilo-')
elif simbol == 'h':
    print('hekto-')
elif simbol == 'da':
    print('deka-')
elif simbol == 'd':
    print('desi-')
elif simbol == 'c':
    print('centi-')
elif simbol == 'm':
    print('mili-')
elif simbol == 'miu' or simbol == 'µ':
    print('micro-')
elif simbol == 'n':
    print('nano-')
elif simbol == 'p':
    print('piko-')
elif simbol == 'f':
    print('femto-')
elif simbol == 'a':
    print('atto-')
elif simbol == 'z':
    print('zepto-')
elif simbol == 'y':
    print('yokto-')
else:
    print('Tidak Terdaftar')