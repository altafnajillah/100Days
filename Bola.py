'''Menghitung Volume dan Luas Permukaan Bola'''

print("Menghitung Volume dan Luas Permukaan Bola")

pi = 22/7

def LuasPerm(r):
    LuasPerm = 4 * pi * r ** 2
    print(f"Luas Permukaan Bola  adalah : {round(LuasPerm,2)} satuan²")

def Volume(r):
    Volume = 4/3 * pi * r ** 3
    print(f"Volume dari Bola adalah : {round(Volume,2)} satuan³")

r = float(input("Masukkan nilai jari-jari : "))

print(f"Dengan Jari-jari {r} satuan, akan diperoleh : ")
LuasPerm(r)
Volume(r)