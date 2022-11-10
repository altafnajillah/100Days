n = int(input("Masukkan Nilai n : "))
nfaktorial = 1

for i in range(1, n + 1):
    nfaktorial *= i

k = int(input("Masukkan Nilai k : "))
kfaktorial = 1

for x in range(1, k + 1):
    kfaktorial *= x

selisih = int(n - k)
sFaktorial = 1

for z in range(1, selisih + 1):
    sFaktorial *= z

Kombinasi = nfaktorial / (kfaktorial * sFaktorial)

print(f"Total kombinasi yang ada adalah : {Kombinasi} Kombinasi")