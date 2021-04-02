#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 4 November 2020
#Deskripsi : Menampilkan siap bang jago?

#kamus
#n : integer (jumlah bilangan)
#a : integer (pembagi ke-1)
#b : integer (pembagi ke-1)
#c : integer (pembagi ke-1)

#kamus
#meminta input user
#asumsikan input semuanya benar ( integer > 0)
n=int(input('Masukkan nilai N: '))
a=int(input('Masukkan nilai A: '))
b=int(input('Masukkan nilai B: '))
c=int(input('Masukkan nilai C: '))

#algoritma
#mengulang sebanyak n kali
for i in range (n):
    i+=1
    if i%a!=0 and i%b!=0 and i%c!=0: #jika i tidak habis dibagi manapun
        print(i,end=' ')
    elif i%a==0 and i%b!=0 and i%c!=0: #jika i habis dibagi a
        print('Siap',end=' ')
    elif i%a!=0 and i%b==0 and i%c!=0: #jika i habis dibagi b
        print('Bang',end=' ')
    elif i%a!=0 and i%b!=0 and i%c==0: #jika i habis dibagi c
        print('Jago',end=' ')
    elif i%a==0 and i%b==0 and i%c!=0: #jika i habis dibagi a dan b
        print('SiapBang',end=' ')
    elif i%a==0 and i%b!=0 and i%c==0: #jika i habis dibagi a dan c
        print('SiapJago',end=' ')
    elif i%a!=0 and i%b==0 and i%c==0: #jika i habis dibagi b dan c
        print('BangJago',end=' ')
    else: #i%a==0 and i%b==0 and i%c==0: #jika i habis dibagi ketiganya
        print('SiapBangJago',end=' ')
