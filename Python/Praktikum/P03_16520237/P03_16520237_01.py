#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 18 November 2020
#Deskripsi : Pembagian mobil

'''
#kamus
#jumlah_mobil: integer (banyaknya mobil)
#jumlah_anak: integer (banyaknya anak)
#array_mobil: integer (array plat mobil)
#array_anak: integer (jumlah yang didapat anak)
'''

#kamus
#meminta input user
jumlah_mobil=int(input('Masukkan jumlah mobil: '))
#inisialisasi array
array_mobil=[0 for i in range (jumlah_mobil)]
#input plat mobil
for i in range (jumlah_mobil):
    array_mobil[i]=int(input('Masukkan plat mobil: ke-'+str(i+1)+': '))

#meminta input user
jumlah_anak=int(input('Masukkan jumlah anak: '))
#inisialisasi array jumlah yang didapat oleh anak
array_anak=[0 for i in range (jumlah_anak)]

#algoritma
#pembagian per anak
for i  in range(jumlah_mobil):
    array_anak[array_mobil[i]%jumlah_anak] += 1

#menampilkan ke layar
for i in range (jumlah_anak):
    print('Anak ke-'+str(i+1)+' mendapat',array_anak[i],'mobil')