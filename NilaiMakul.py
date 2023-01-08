#Bobot Nilai, Setiap penilaian memiliki persentase masing-masing
bobotKehadiran = 15/100
bobotTugas = 45/100
bobotUjian = 20/100

Kehadiran = int(input("Masukkan jumlah kehadiran [1-16]\t: "))
if (0 <= Kehadiran <= 16):
    if (Kehadiran >= 8): 
        nKehadiran = Kehadiran * (15/16)
        Tugas = float(input("Masukkan nilai Tugas\t\t\t: "))
        nTugas = Tugas * bobotTugas 
        UTS = float(input("Masukkan nilai Ujian Tengah Semester\t: "))
        nUTS = UTS * bobotUjian
        UAS = float(input("Masukkan nilai Ujian Akhir Semester\t: "))
        nUAS = UAS * bobotUjian

        print(f'''
        Berikut rekap nilai anda :
        Kehadiran\t: {round(nKehadiran, 3)}/15
        Tugas\t\t: {round(nTugas, 3)}/45
        UTS\t\t: {round(nUTS, 3)}/20
        UAS\t\t: {round(nUAS, 3)}/20
        ''')

        total = nKehadiran + nTugas + nUTS + nUAS
        if (85 < total <= 100) :
            print("Nilai pengetahuan anda A")
        elif (total > 79):
            print("Nilai pengetahuan anda A-")
        elif (total > 74):
            print("Nilai pengetahuan anda B+")
        elif (total > 69):
            print("Nilai pengetahuan anda B")
        elif (total > 64):
            print("Nilai pengetahuan anda B-")
        elif (total > 54):
            print("Nilai pengetahuan anda C")
        elif (total > 39):
            print("Nilai pengetahuan anda D")
        elif (total > 0):
            print("Nilai pengetahuan anda E")
        else :
            print("Tidak Valid")

        print(f"Total nilai anda : {round(total,3)}")

    else :
        print()
        print("Anda Tidak Lulus")
        print()

else :
    print()
    print("Input Tidak Valid")
    print()
