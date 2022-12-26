'''Program Bintang'''

x = "*"
bintang = 0
banyak = int(input("Berapa banyak : "))
for i in range(banyak):
    bintang += 1
    bintang1 = bintang * x
    print(bintang1)
for j in range(banyak):    
    banyak -= 1
    bintang2 = banyak * x
    print(bintang2)

