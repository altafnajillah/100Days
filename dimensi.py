'''Program menentukan dimensi besaran pokok'''
print("Program menentukan dimensi besaran pokok")

isian = input("Masukkan satuan yang akan dicari dimensinya\t:")
m = "[L]"
kg = "[M]"
s = "[T]"
A = "[I]"
K = "[θ]"
cd = "[J]"
mol = ["N"]

if (isian == "m" or isian.lower() == "panjang"):
    print("dimensi dari", isian, "adalah", m)
elif (isian == "kg" or isian.lower() == "massa"):
    print("dimensi dari", isian, "adalah", kg)
elif (isian == "s" or isian.lower() == "waktu"):
    print("dimensi dari", isian, "adalah", s)
elif (isian == "A" or isian.lower() == "kuat arus listrik"):
    print("dimensi dari", isian, "adalah", A)
elif (isian == "K" or isian.lower() == "suhu"):
    print("dimensi dari", isian, "adalah", K)
elif (isian == "cd" or isian.lower() == "intensitas cahaya"):
    print("dimensi dari", isian, "adalah", cd)
elif (isian == "mol" or isian.lower() == "jumlah zat"):
    print("dimensi dari", isian, "adalah", mol)
else:
    print("Error, ada yang salah dengan input. Periksa kembali!!")
