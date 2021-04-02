#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 2 Desember 2020
#Deskripsi : diagonal dan matriks

'''
#kamus
baris: integer(benyaknya baris dalam matriks)
kolom: integer(banyaknya kolom dalam matriks)
arr: matriks
'''

#kamus
#input user
baris=int(input('Masukkan jumlah baris: '))
kolom=int(input('Masukkan jumlah kolom: '))
#inisialisasi matriks
arr=[[0 for j in range(kolom)] for i in range(baris)]

#algoritma
for j in range(baris):
    for i in range(kolom):
        #mengecek apakah sudut matriks ada diatas dan dibawah garis
        if (baris*i+kolom*j-baris*kolom<0 and baris*(i+1)+kolom*(j+1)-baris*kolom>0):
            arr[j][i]=1

#mencetak ke layar secara kordinat kartesius ( (0,0) nya di bawah kiri bukan atas kiri)
for j in range(baris-1,-1,-1):
        for i in range(kolom):
            print(arr[j][i],end=' ')
        print('')