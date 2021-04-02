#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 1 November 2020
#Deskripsi: Program bilangan Prima

#kamus
#n,a,b,c: integer

a=0 #hasil bagi
b=0 #counter hasil bagi
c=0 #pembagi bilangan yang diinput
n=int(input('Masukkan angka: ')) #angka yang akan dicari prima atau bukan
for i in range(n): #melakukan hasil bagi sebanyak n kali
    c=c+1 #perintah agar pembagi akan terus bertambah sebanyak 1 selama n kali
    a=n%c #perintah untuk melakukan hasil bagi
    if a==0: #jika hasil bagi=0
        b=b+1 #counter hasil bagi akan bertambah 1
if b==2: #jika counter hasil bagi=2
         # (mengingat bilangan prima hanya akan habis dibagi 1 dan bilangan itu sendri)
    print(n,'adalah bilangan prima')
else:
    print(n,'bukan bilangan prima')