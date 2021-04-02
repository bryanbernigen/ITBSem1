#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 18 November 2020
#Deskripsi : Harta Karun ITB

'''
#kamus:
#kode: string (array berisi kode)
#panjang_kode: integer (banyaknya bilangan)
#kode_angka: integer (kode dalam angka)
'''

#kamus
#inisialisasi kode
kode=[' ','A','B','E','I','K','L','R','T','U']
#input user
panjang_kode=int(input('Masukkan banykanya bilangan: '))
kode_angka=input('Masukkan bilangan: ')

#algoritma
for i in range (panjang_kode):
    print(kode[int(kode_angka[i])],end='')