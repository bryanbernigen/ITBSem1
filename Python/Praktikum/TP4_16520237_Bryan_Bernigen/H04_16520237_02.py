#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 15 November 2020
#Deskripsi: Matriks baris x kolom

'''
#kamus
#baris: integer(jumlah baris)
#kolom: integer(jumlah kolom)
#arr: matriksnya
#positif: integer(banyak bilangan positif)
'''

#kamus
positif=0
#inputan user
baris=int(input('Masukkan jumlah baris: '))
kolom=int(input('Masukkan jumlah kolom: '))
#inisialisasi matriks
arr=[[0 for i in range(kolom)] for j in range (baris)]
#pengisian matriks
for j in range(baris):
    for i in range(kolom):
        arr[j][i]=int(input(('Masukkan elemen matriks['+str(j+1))+']['+str(i+1)+']: '))

#algoritma
#cek banyaknya bilangan positif
#sekalian menanpilkan matriksnya
for j in range(baris):
    for i in range(kolom):
        #cek bilangan positif
        if arr[j][i]>0:
            positif+=1
        print(arr[j][i],end=' ')
    print('')
print('Ada',positif,'bilangan positif di matriks')