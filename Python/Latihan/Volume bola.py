# Program VolumeBola
# Menghitung volume bola berdasarkan masukan jari-jari

# Kamus
# pi = 3.1416 - konstanta
# r, V : float

#kamus
pi=3.1416
#meminta input user
r=float(input('Masukkan jari-jari bola (dalam meter): '))

#Algortima
v=4/3 * pi * r * r
print('Volume bola: ',v,'m^3')