#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 2 Desember 2020
#Deskripsi : jarak total

'''
#kamus
banyak_kota: integer(banyaknya kota yang akan dikunjungi)
arr: matriks(berisi x,y dari kota tujuan)
jarak total: float(total jarak dari tiap kota ke kota)
'''

#kamus
total_jarak=0
#input user
banyak_kota=int(input('Masukkan banyaknya kota: '))
#inisialiasasi array
arr=[[0 for i in range(2)] for j in range(banyak_kota)]
#memasukkan lokasi kota
for j in range(banyak_kota):
        arr[j][0]=int(input(('masukkan kordinat x kota ke-'+str(j+1)+': ')))
        arr[j][1] = int(input(('masukkan kordinat y kota ke-' + str(j + 1)+': ')))
print(arr)

#definisi fungsi jarak
def jarak(x1,y1,x2,y2):
    #kamus lokal
    #x dan y merupakan kordinat kota
    jarak=(((x1-x2)**2) + ((y1-y2)**2))**0.5
    return jarak

#algoritma
for i in range(banyak_kota-1):
    total_jarak+=jarak(arr[i][0],arr[i][1],arr[i+1][0],arr[i+1][1])
    print(total_jarak)
#menampilkan ke layar
print('total jarak adalah',total_jarak)