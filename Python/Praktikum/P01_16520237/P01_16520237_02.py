# NIM/Nama   : 16520237/ Bryan Bernigen
# Tanggal    : 21 Oktober 2020
# Deskripsi  : Integral

#kamus
#a,b: integer

print('Program akan menghitung hasil integral f(x)=ax+b')
a=int(input('Masukkan nilai a: '))
b=int(input('Masukkan nilai b: '))
#operasi
a=a/2
if a==0 and b==0:
    print('integral dari f(x) adalah 0')
elif a==0:
    print('integral dari f(x) adalah', b, 'x + C')
elif b==0:
    print('integral dari f(x) adalah', a, 'x^2 + C')
elif a==1:
    print('integral dari f(x) adalah x^2 +', b, 'x + C')
elif b==1:
    print('integral dari f(x) adalah', a, 'x^2 + x + C')
else:
    print('integral dari f(x) adalah',a,'x^2 +',b,'x + C')