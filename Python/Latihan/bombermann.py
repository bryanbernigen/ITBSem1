#program bomberman

#kamus
detik=1
# input user
baris=int(input('masukkan banyak baris(y): '))
kolom=int(input('masukkan banyak kolom(x): '))
waktu=int(input('masukkan banyaknya detik: '))
if waktu%2==1:
    waktu=int((waktu-1)/2)
    waktu_tambahan=0
else:
    waktu=int((waktu/2)-1)
    waktu_tambahan=1
#inisialisasi array
arr=[[0 for j in range(baris+2)] for i in range(kolom+2)]
#menampilkan array awal yang sudah diperbesar


#input keadaan awal
for j in range(baris):
    for i in range(kolom):
        arr[j+1][i+1]=int(input(('masukkan keadaan di['+str(j+1)+']['+str(i+1)+']: ')))

#menampilkan keadaan awal
print('detik ke',str(detik))
for j in range(baris):
    for i in range(kolom):
        print(arr[i+1][j+1],end=' ')
    print('')

#algoritma
for i in range(waktu):
    #mengisi slot kosong
    for j in range(baris):
        for i in range(kolom):
            if arr[j+1][i+1]==0:
                arr[j+1][i+1]=1
            else:
                arr[j+1][i+1]=2

    #menampilkan keadaan setelah diisi
    detik+=1
    print('detik ke-'+str(detik))
    for j in range(baris):
        for i in range(kolom):
            print(1, end=' ')
        print('')


    #menghancurkan block sekitarnya
    for j in range(baris):
        for i in range(kolom):
            if arr[j+1][i+1]==2:
                #arr sendiri
                arr[j+1][i+1]=0
                #atas
                if arr[j][i+1]!=[]:
                    arr[j][i+1]=0
                #bawah
                if arr[j+2][i+1]!=[]:
                    arr[j+2][i+1]=0
                #kiri
                if arr[j+1][i]!=[]:
                    arr[j+1][i]=0
                #kanan
                if arr[j+1][i+2]!=[]:
                    arr[j+1][i+2]=0

    #menampilkan keadaan
    detik+=1
    print('detik ke-'+str(detik))
    for j in range(baris):
        for i in range(kolom):
            print(arr[i+1][j+1], end=' ')
        print('')

#waktu tambahan
if waktu_tambahan==1:
    detik+=1
    print('detik ke-'+str(detik))
    for j in range(baris):
        for i in range(kolom):
            print(1, end=' ')
        print('')