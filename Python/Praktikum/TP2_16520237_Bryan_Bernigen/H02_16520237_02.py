#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 1 November 2020
#Deskripsi: program yang menerima bilangan n dan menuliskan bilangan 10^x terkecil yang lebih dari n.

#kamus
#n,a,b: integer

n=int(input('Masukkan Angka: '))
a=n
#bilangan bantuan
b=10
while a>=10: #selama angka yang diinput lebih besar sama dengan 10 maka:
    a=a/10 #angka tersebut akan dibagi dengan 10
    b=b*10 #dan bilangan bantuan akan dikali 10
#menampilkan besar bilangan bantuan
print('Bilangan 10^x terkecil yang lebih besar dari',n,'adalah',b)