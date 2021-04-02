# Program NilaiKuliah
# Pengolahan N nilai mahasiswa

# Kamus
import os
# n, uts, uas, prak, i : int
# akhir : float
# nama, indeks : string

#kamus
#input banyak data
n=int(input('Masukkan jumlah siswa: '))

#inisialisasi array
array_nama=[0 for i in range (n)]
array_praktikum=[0 for i in range (n)]
array_uts=[0 for i in range (n)]
array_uas=[0 for i in range (n)]
array_akhir=[0 for i in range (n)]
array_indeks=[0 for i in range (n)]

#input data siswa
for i in range (n):
    array_nama[i]=input('Nama     : ')
    array_praktikum[i] = int(input('Praktikum: '))
    array_uts[i] = int(input('UTS      : '))
    array_uas[i] = int(input('UAS      : '))
    # Algoritma
    array_akhir[i]=(2*array_praktikum[i]+4*array_uts[i]+4*array_uas[i])/10
    if array_akhir[i]>=85:
        array_indeks[i]='A'
    elif array_akhir[i]<85 and array_akhir[i]>=75:
        array_indeks[i]='AB'
    elif array_akhir[i]<75 and array_akhir[i]>=70:
        array_indeks[i]='B'
    elif array_akhir[i]<70 and array_akhir[i]>=60:
        array_indeks[i]='BC'
    elif array_akhir[i]<60 and array_akhir[i]>=50:
        array_indeks[i]='C'
    elif array_akhir[i]<50 and array_akhir[i]>=40:
        array_indeks[i]='D'
    else:
        array_indeks[i]='E'

#menampilkan ke layar
print('nama | praktikum | uts | uas | akhir | indeks')
for i in range (n):
    print(array_nama[i],end=' | ')
    print(array_praktikum[i], end=' | ')
    print(array_uts[i], end=' | ')
    print(array_uas[i], end=' | ')
    print(array_akhir[i], end=' | ')
    print(array_indeks[i])


