'''Program Menghitung Permutasi Siklis'''

print("Program Permutasi Siklis")

nilai = int(input("Masukkan nilai n : "))
n = nilai - 1
nfaktorial = 1

for i in range(1, n + 1):
    nfaktorial *= i

print(f"Permutasi siklis dari {nilai} adalah {nfaktorial}")