'''Program menghitung jam kerja dengan input jam masuk dan jam pulang'''
print()
print("Program menghitung jam kerja")

jamMasuk = int(input("Masukkan jam masuk [1-12]\t: "))
jamPulang = int(input("Masukkan jam pulang [1-12]\t: "))

if (0 < jamPulang <= 12 and 0 < jamMasuk <= 12):
    totalJam = jamPulang - jamMasuk

    if totalJam <= 0 :
        totalJam = totalJam + 12

    print()
    if (totalJam <= 12):
        print(f"""Rekap\t:
        Masuk pukul\t: {jamMasuk}:00
        Pulang pukul\t: {jamPulang}:00
        Total Jam kerja\t: {totalJam} jam""")
    else:
        print()
        print("Total jam kerja anda berlebihan")
    
else :
    print("Input error")
print()