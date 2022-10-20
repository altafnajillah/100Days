'''GLB atau Gerak Lurus Beraturan dapat di gunakan untuk mengkalkulasi berbagai hal
seperti perkiraan ketibaan, kecepatan yang dibutuhkan maupun jarak tempuh dengan anggapan
bahwa kecepatan yang di gunakan selalu konstan'''

print(100*"=")
print("Program estimasi ketibaan")
kecepatan = 60
jarak = 15

print("Saya ingin ke kampus menggunakan motor dengan kecepatan", kecepatan,
      "km/jam dan menempuh jarak", jarak, "km")
print("Maka\t:")
waktuj = jarak / kecepatan
waktum = (jarak / kecepatan) * 60
print("Menempuh Jarak", jarak, "km dengan Kecepatan", kecepatan,
      "km/jam memerlukan waktu", waktuj, "Jam atau", waktum, "menit\n")

print(100*"=")
print("Program jarak tempuh")
kecepatan = 120
waktu = 2.25
jarak = kecepatan * waktu
print("Sebuah kereta melakukan perjalanan dari kota A ke Kota B dengan kecepatan", kecepatan,
      "km/jam selama", waktu, "jam")
print("Maka\t:\nPerjalanan", kecepatan, "km/jam selama", waktu, "jam menempuh jarak", jarak, "km\n")

print(100*"=")
print("Program kecepatan yang dibutuhkan")
jarak = 48
waktu = 1.5
kecepatan = jarak / waktu
print("Sebuah acara akan dimulai dalam waktu", waktu,
      "jam dalam jarak", jarak,"km")
print("Maka\t:\nPerjalanan sejauh", jarak, "km dalam", waktu,
      "jam membutuhkan kecepatan", kecepatan, "km/jam agar sampai tepat waktu")