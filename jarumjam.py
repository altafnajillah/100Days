'''Program menghitung sudut terkecil yang diapit oleh kedua jarum jam'''

print(100 * "=")
print("Program menghitung sudut terkecil yang diapit oleh kedua jarum jam")
input1 = int(input("Masukkan angka jam (0-12)\t: "))
input2 = int(input("Masukkan angka menit (0-60)\t: "))

if (0 <= input1 <= 12 and 0 <= input2 <= 60):
    derajat1 = (input1 + (1/60 * input2)) * 30 
    derajat2 = input2 * 6

    print("Jam", +input1, "Lewat", +input2, "Menit")

    tderajat = abs(derajat1 - derajat2)
    if (tderajat < 180):
        print("Sudut yang diapit adalah :", tderajat, "Derajat") 
    else:
        print("Sudut yang diapit adalah :", 360-tderajat, "Derajat" )
else:
    print("Input tidak Valid, Sesuaikan berdasarkan satuan yang telah ditentukan!")
