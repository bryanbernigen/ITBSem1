#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 4 November 2020
#Deskripsi : membuat kotak

#kamus
#n : integer banyaknya kotak (2n x 2n)
#i : integer
#j : integer
#k : integer (ixj)

#kamus
n=int(input('Masukkan n ( membentuk kotak 2nx2n):'))

#algoritma
for i in range(n):
    for j in range(n):
        print(j,end='')
    for j in range(n-1,-1,-1):
        print(j,end='')
    print('')
for i in range(n-1,-1,-1):
    for j in range(n):
        print(j,end='')
    for j in range(n-1,-1,-1):
        print(j,end='')
    print('')

#harusnya:
#kenapa ide datang terlambat T_T

'''for j in range (n):
    for i in range (j):
        print(i,end='')
    for i in range (n-j):
        print(j,end='')
    for i in range (n-j):
        print(j,end='')
    for i in range(j,0,-1):
        print(i-1,end='')
    print('')
for j in range (n-1,-1,-1): 
    for i in range (j):
        print(i,end='')
    for i in range (n-j):
        print(j,end='')
    for i in range (n-j):
        print(j,end='')
    for i in range(j,0,-1):
        print(i-1,end='')
    print('')
'''