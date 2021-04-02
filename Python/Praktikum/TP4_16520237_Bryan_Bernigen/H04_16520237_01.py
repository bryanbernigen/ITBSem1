#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 29 November 2020
#Deskripsi: f(a) sampai f(b)

'''
#kamus
#a: integer(batas bawah)
#b: integer(batas atas)
#c: tambahan
'''

#kamus
#input user
print('f(x)= x^2 - 2x + 5')
a=int(input('Masukkan batas bawah: '))
b=int(input('Masukkan batas atas : '))

#definisi fungsi
def kuadrat(x):
    return x*x

#algoritma
for i in range(b-a+1):
    c=a+i
    print('f('+str(c)+') =',(kuadrat(c) - 2*c +5))