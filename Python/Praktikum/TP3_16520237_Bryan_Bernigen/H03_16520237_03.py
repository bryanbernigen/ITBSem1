#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 15 November 2020
#Deskripsi: Cek Palindrom

#kamus
'''
#kata: string (kata masukan user yang akan di cek)
#panjang_kata: integer (panjang kata hasil input user)
#array_kata: string (array berisi huruf per huruf dari kata inputan user)
#array_kata_terbalik: string (array berisi huruf per huruf
                             dari kata inputan user secara terbalik)
#a: integer (bantuan untuk membalik kata)
'''

#kamus
a=0
#inputan user
panjang_kata=int(input('Masukkan panjang kata (jumlah huruf): '))
kata=str(input('Masukkan kata yang akan di cek: '))

#inisialisasi array
array_kata=list(kata)
array_kata_terbalik=['a' for i in range(panjang_kata)]
#pengisian array kata secara terbalik
for i in range(panjang_kata-1,-1,-1):
    a=a+1
    array_kata_terbalik[a-1]=array_kata[i]

#algoritma cek apakah kata tersebut merupakan palindrom
if array_kata==array_kata_terbalik:
    print(kata,'adalah palindrom')
else:
    print(kata,'bukan palindrom')