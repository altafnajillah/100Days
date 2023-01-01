'''Program mengitung permutasi unsur yang sama dari input kata'''

print()
print("Menghitung permutasi unsur yang sama")

def permutasi (kata):
    hitung = {}
    for i in kata :
        if i in hitung :
            hitung[i] += 1
        else :
            hitung[i] = 1
    
    banyak = len(kata)

    nfaktorial = 1
    for j in range(1, banyak + 1):
        nfaktorial = nfaktorial * j

    for k in hitung.values():
        rfaktorial = 1
        for l in range(1, k + 1):
            rfaktorial = rfaktorial * l

        nfaktorial /= rfaktorial

    return int(nfaktorial)

kata = input("Masukkan kata : ")
print(f"Kata \"{kata}\" jika dipermutasikan dapat menghasilkan {permutasi(kata)} permutasi")
print()