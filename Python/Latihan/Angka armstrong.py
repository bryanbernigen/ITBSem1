# Program Angka Armstrong
# Menentukan apakah sebuah angka 3 digit angka armstrong atau bukan

# Kamus
# angka: integer (3 angka yang akan di cek)
#str_angka: string ( string dari angka yang akan di cek)
# array_angka: interger (array dari anga tersebut)

#kamus
#inisialisasi array
array_angka=[0 for i in range (3)]
#meminta input user
a=0
while a==0:
    angka= int(input('Masukkan angka yang akan di cek:'))
    str_angka=str(angka)
    if len(str_angka)==3:
        a=1

# Algoritma
#pemasukkan angka ke array
array_angka[0]=int(str_angka[0])
array_angka[1]=int(str_angka[1])
array_angka[2]=int(str_angka[2])

#cek bilangan armstrong
if angka==(array_angka[0]**3 + array_angka[1]**3 + array_angka[2]**3):
    print(angka,'merupakan bilangan armstrong')
else:
    print(angka,'bukan bilangan armstrong')