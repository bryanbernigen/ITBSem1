#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 15 November 2020
#Deskripsi: kotak pascal

'''
#kamus
#ukuran: integer (besarnya matriks)
#arr: matriksnya
'''

#kamus
#input user
ukuran= int(input('Masukkan ukuran segitiga pascall: '))
#inisialisasi matriks
arr=[[1 for j in range (ukuran)] for i in range (ukuran)]

#algoritma
for j in range(ukuran-1):
    for i in range(ukuran):
        for k in range(i):
            arr[j+1][i] += arr[j][k+1]

#menampilkan ke layar
for j in range(ukuran):
    for i in range(ukuran):
        print(arr[j][i],end=' ')
    print('')