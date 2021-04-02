#program luas permukaan

#kamus
#input user
baris=int(input('masukkan banyak baris(y): '))
kolom=int(input('masukkan banyak kolom(x): '))
#inisialisasi array
arr=[[0 for j in range(baris+2)] for i in range(kolom+2)]
luas_permukaan=0
#menampilkan array awal yang sudah diperbesar
for j in range(baris+2):
    for i in range(kolom+2):
        print(arr[i][j],end=' ')
    print('')

#input user mengisi ketinggian tiap lokasi
for j in range(baris):
    for i in range(kolom):
        arr[j+1][i+1]=int(input(('masukkan tinggi daerah['+str(j+1)+']['+str(i+1)+']: ')))
#menampilkan isian user
for j in range(baris+2):
    for i in range(kolom+2):
        print(arr[i][j],end=' ')
    print('')

#algoritma
#mengecek tinggi sekitarnya jika lebih tinggi
#luas permukaan akan ditambah sesuai perbedaan tingginya
for j in range(baris):
    for i in range(kolom):
        #atas
        if arr[j+1][i+1]>arr[j][i+1]:
            luas_permukaan+=arr[j+1][i+1]-arr[j][i+1]
        #bawah
        if arr[j+1][i+1]>arr[j+2][i+1]:
            luas_permukaan+=arr[j+1][i+1]-arr[j+2][i+1]
        #kiri
        if arr[j+1][i+1]>arr[j+1][i]:
            luas_permukaan+=arr[j+1][i+1]-arr[j+1][i]
        #kanan
        if arr[j+1][i+1]>arr[j+1][i+2]:
            luas_permukaan+=arr[j+1][i+1]-arr[j+1][i+2]
#atas dan bawah:
luas_permukaan+=2*baris*kolom

#menampilkan hasil
print('luas permukaan: ',luas_permukaan)