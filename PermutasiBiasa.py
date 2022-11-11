'''Program Menghitung Permutasi biasa'''

print(80*"=")
print("Program Menghitung Permutasi Biasa")

n = int(input("Masukkan nilai n : "))
nfakotrial = 1

for i in range(1, n + 1):
    nfakotrial *= i

r = int(input("Masukkan nilai r : "))

p = n - r
pfaktorial = 1

for j in range(1, p + 1):
    pfaktorial *= j

permutasi = int(nfakotrial / pfaktorial)

print(f"Permutasi dari {n,r} adalah {permutasi}")