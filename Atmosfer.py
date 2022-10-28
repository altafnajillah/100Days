'''Penentuan lapisan atmosfer berdasarkan ketinggiannya'''

print("Program penentuan lapisan atmosfer berdasarkan ketinggian")
print("Silahkan masukkan ketinggian (km)")

range1 = 'Troposfer'
range2 = 'Stratosfer'
range3 = 'Mesosfer'
range4 = 'Termosfer'
range5 = 'Ionesfer'
range6 = 'Eksosfer'

ketinggian = int(input("Ketinggian\t: "))
if (0 <= ketinggian <= 12):
    print("Lapisan pada ketinggian", ketinggian, "km adalah", range1)
elif (12 < ketinggian <= 60):
    print("Lapisan pada ketinggian", ketinggian, "km adalah", range2)
elif (60 < ketinggian <= 80):
    print("Lapisan pada ketinggian", ketinggian, "km adalah", range3)
elif (80 < ketinggian <= 100):
    print("Lapisan pada ketinggian", ketinggian, "km adalah", range4)
elif (100 < ketinggian <= 800):
    print("Lapisan pada ketinggian", ketinggian, "km adalah", range5)
elif (800 < ketinggian <= 3260):
    print("Lapisan pada ketinggian", ketinggian, "km adalah", range6)
else :
    print("Ketinggian", ketinggian, "tidak valid, masukkan 0-3260 km")