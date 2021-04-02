#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 2 Desember 2020
#Deskripsi : mine sweeper

'''
#kamus
baris: integer(benyaknya baris dalam matriks)
kolom: integer(banyaknya kolom dalam matriks)
arr: matriks
bom: integer(banyaknya bom disekitar)
'''

#kamus
#input user
baris=int(input('Masukkan jumlah baris: '))
kolom=int(input('Masukkan jumlah kolom: '))

#inisialisasi matriks yang dibesarkan di semua sisinya
arr=[[0 for j in range(kolom+2)] for i in range(baris+2)]

#mendefinisikan fungsi menanpilkan matriks
def show():
    for j in range(baris):
        for i in range(kolom):
            print(arr[j+1][i+1],end=' ')
        print('')

#mengisi matriks tersebut
for j in range(baris):
    for i in range(kolom):
        arr[j+1][i+1]=str(input(('masukan elemen baris '+str(j+1)+' kolom '+str(i+1)+' : ')))
#menampilkan tampilan awal matriks
print('')
print('matriks awal')
show()

#algoritma
#mengecek banykanya bom di sekitar
for j in range(baris):
    for i in range(kolom):
        if arr[j + 1][i + 1] =='.':
            bom = 0
            #cek sekitarnya jika ada bom maka indikator akan bertambah
            #atas
            if arr[j][i+1]=='*':
                bom+=1
            #kanan atas
            if arr[j][i+2]=='*':
                bom+=1
            #kanan
            if arr[j+1][i+2]=='*':
                bom+=1
            #kanan bawah
            if arr[j+2][i+2]=='*':
                bom+=1
            #bawah
            if arr[j+2][i+1]=='*':
                bom+=1
            #bawah kiri
            if arr[j+2][i]=='*':
                bom+=1
            #kiri
            if arr[j+1][i]=='*':
                bom+=1
            #kiri atas
            if arr[j][i]=='*':
                bom+=1
            #mengubah array menjadi jumlah bom
            arr[j + 1][i + 1] = bom

#mengubah bom dari * menjadi #
for j in range(baris):
    for i in range(kolom):
        if arr[j + 1][i + 1] =='*':
            arr[j + 1][i + 1] = '#'

#menampilkan keadaan akhir
print('')
print('matriks angka')
show()
