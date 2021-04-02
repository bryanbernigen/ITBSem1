#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 18 November 2020
#Deskripsi : substring

'''
#kamus:
#panjang: integer (panjang bilangan)
#kata: string (kata yang akan di cek)
#array: string (array kata)
'''

#kamus
#meminta input user
panjang=int(input('Masukkan panjang string: '))
kata=str(input('Masukkan string: '))

#inisialisasi array
array=['' for i in range(panjang)]
#inisialisasi cara
palindrom=0

#algoritma
for i in range (panjang):
    for j in range(panjang-i):
        if kata[j]==kata[j+i]:
            c = 0
            for k in range(i+1):
                if kata[j+k]==kata[j+i-k]:
                    c=c+1
            if c==i+1:
                palindrom=c
print('Panjang palindrom: ', palindrom)

