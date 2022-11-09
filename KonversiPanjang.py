'''Program konversi panjang dari satuan meter ke beberapa satuan seperti inch, dan kaki'''

print(80*"=")
print("Program mengonversi satuan dari kilometer ke inch dan kaki")
input1 = float(input("Masukkan nilai panjang dalam satuan meter : "))

inch = input1 * 39.3701
feet = input1 * 3.28084

print("Nilai", input1, "m Apabila dikonversi ke inch akan sama dengan", round(inch,2), "inchi")
print("Nilai", input1, "m Apabila dikonversi ke kaki akan sama dengan", round(feet,2), "kaki")