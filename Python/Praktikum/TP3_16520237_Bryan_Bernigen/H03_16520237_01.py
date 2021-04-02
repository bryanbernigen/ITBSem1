#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 15 November 2020
#Deskripsi: Print angka terbalik

#kamus
#n: interger (banyak bilangan(

#kamus
#meminta input user
n=int(input('Masukkan banyaknya angka: '))

#inisialisasi array
angka=[0 for i in range (n)]

#algoritma1
#meminta user menginput angka sebanyak n kali
for i in range(n):
    angka[i]=int(input())

#mencetak secara terbalik
for i in range(n-1,-1,-1):
    print(angka[i])