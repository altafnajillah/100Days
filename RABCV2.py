#Penyelesaian Rumus ABC menggunakan function dan berasal dari input

print("Program mencari akar-akar persamaan dari fungsi kuadrat : ")

def RumusABC(a, b, c):
    x1 = int((-(b) + (b ** 2 - 4 * a * c) ** 0.5)/ 2 * a)
    x2 = int((-(b) - (b ** 2 - 4 * a * c) ** 0.5)/ 2 * a)
    print("Akar Persamaan yang sesuai adalah :")
    print(f"Pertama = {x1}\nKedua = {x2}")

print("Masukkan nilai-nilai berikut : ")
na = float(input("Nilai a : "))
nb = float(input("Nilai b : "))
nc = float(input("Nilai c : "))

RumusABC(na, nb, nc)