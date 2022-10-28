'''Penggunaan rumus ABC dalam penyelesaian soal persamaan kuadrat'''

print("Diketahui Persamaan\nx² + 8x + 7 = 0")

a = 1
b = 8
c = 7

x1 = int((-(b) + (b ** 2 - 4 * a * c) ** 0.5)/ 2 * a)
x2 = int((-(b) - (b ** 2 - 4 * a * c) ** 0.5)/ 2 * a)

print("Maka :\na =", a, "\nb =", b,"\nc =", c)

print("akar-akar persamaan yang sesuai adalah :")
print("x =", x1, "atau x =", x2)

print("=================================================================")
print("\nSalah satu akar persamaan dari x² + 3x + c = 0 adalah 4")
print("Akar Selanjutnya adalah ...")
a = 1
b = 3
x1 = 4
c = -a * x1 ** 2 - 3 * x1
x2 = int((-(b) - (b ** 2 - 4 * a * c) ** 0.5)/ 2 * a)

print("Diketahu :")
print("a =", a, "\nb =", b, "\nAkar pertama =", x1)
print("c =", c)
print("Akar kedua =", x2)
