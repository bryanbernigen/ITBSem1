#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 15 November 2020
#Deskripsi: Anagram 2 buah array

#kamus:
'''
#jumlah_array_a: integer (banyaknya isi array a)
#jumlah_array_b: integer (banyaknya isi array b)
#array_a: integer (isi array a)
#array_b: integer (isis array b)
#tabel_frekuensi_a: integer (tabel frekuensi dari a)
#tabel_frekuensi_b: integer (tabel frekuensi dari b)
#a: integer (bantuan untuk mempercantik tampilan "elemen ke-")
#b: integer (bantuan untuk mempercantik tampilan "elemen ke-")
'''

#cara 1 dengan tabel frekuensi
#inisialisasi array dan konstanta
a=0
b=0
tabel_frekuensi_a=[0 for i in range (11)] #0-10
tabel_frekuensi_b=[0 for i in range (11)] #0-10

#meminta input user untuk mengisi banyaknya elemen array a
jumlah_array_a=int(input('Masukkan banyaknya elemen A: '))
#inisialisasi array a
array_a=[0 for i in range(jumlah_array_a)]
#meminta user mengisi array A
for i in range(jumlah_array_a):
    a=a+1
    array_a[i]=int(input('Masukkan elemen ke-'+str(a)+': '))

#meminta input user untuk mengisi banyaknya elemen array b
jumlah_array_b=int(input('Masukkan banyaknya elemen B: '))
#inisialisasi array b
array_b=[0 for i in range(jumlah_array_b)]
#meminta user mengisi array B
for i in range(jumlah_array_b):
    b=b+1
    array_b[i]=int(input('Masukkan elemen ke-'+str(b)+': '))

#mengisi tabel frekuensi A
for i in range (11):
    c=0
    for j in range (jumlah_array_a):
        if array_a[j]==i:
            c=c+1
    tabel_frekuensi_a[i]=c

#mengisi tabel frekuensi b
for i in range (11):
    c=0
    for j in range (jumlah_array_b):
        if array_b[j]==i:
            c=c+1
    tabel_frekuensi_b[i]=c

#cek apakah tabel frekuensi a == tabel frekuensi b
if tabel_frekuensi_a==tabel_frekuensi_b:
    print('B adalah anagram dari A')
else:
    print('B bukan anagram dari A')

#cara 2 tanpa tabel frekuensi
'''#kamus:
a=0
b=0
#meminta input user untuk mengisi array a
jumlah_array_a=int(input('Masukkan banyaknya elemen A: '))
#inisialisasi array a
array_a=[0 for i in range(jumlah_array_a)]
#meminta user mengisi array A
for i in range(jumlah_array_a):
    a=a+1
    array_a[i]=int(input('Masukkan elemen ke-'+str(a)+': '))

#meminta input user untuk mengisi array b
jumlah_array_b=int(input('Masukkan banyaknya elemen B: '))
#inisialisasi array b
array_b=[0 for i in range(jumlah_array_b)]
#meminta user mengisi array B
for i in range(jumlah_array_b):
    b=b+1
    array_b[i]=int(input('Masukkan elemen ke-'+str(b)+': '))

#algoritma
#cek apakah jumlah array a == jumlah array b
if jumlah_array_a==jumlah_array_b:
    #cek apakah B dapat membentuk A
    array_a.sort()
    array_b.sort()
    if array_a==array_b:
        print('B adalah anagram dari A')
    else:
        print('B bukan anagram dari A')
else:
    print('B bukan Anagram dari A')'''