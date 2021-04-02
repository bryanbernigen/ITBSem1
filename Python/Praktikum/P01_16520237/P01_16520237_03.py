# NIM/Nama   : 16520237/ Bryan Bernigen
# Tanggal    : 21 Oktober 2020
# Deskripsi  : Mencari Jarak Terpendek

#kamus
#x1,y1,x2,y2,x3,y3,cara_1,cara_2 : integer

#(x1,y1) = rumah Tuan Kin
print('Rumah Tuan Kin:')
x1=int(input('X1: '))
y1=int(input('Y1: '))

#(x2,y2) = rumah Tuan Ryo
print('Rumah Tuan Ryo:')
x2=int(input('X2: '))
y2=int(input('Y2: '))

#(x3,y3) = restoran
print('Restoran:')
x3=int(input('X3: '))
y3=int(input('Y3: '))

#cara1 rumah Tuan Kin -> rumah Tuan Ryo -> restoran
cara_1=abs(x1)+abs(y1)+abs((x2-x1))+abs((y2-y1))+abs((x3-x2))+abs((y3-y2))
print('----------------------------------------------')
print('cara 1:')
print('Rumah Tuan Kin --> Rumah Tuan Kyo --> Restoran')
print('jarak:',cara_1)

#cara2 rumah Tuan Ryo -> rumah Tuan Kin -> restoran

cara_2=abs(x2)+abs(y2)+abs((x1-x2))+abs((y1-y2))+abs((x3-x1))+abs((y3-y1))
print('----------------------------------------------')
print('cara 2:')
print('Rumah Tuan Ryo --> Rumah Tuan Kin --> Restoran')
print('jarak:',cara_2)
print('----------------------------------------------')

if cara_1<cara_2:
    print('Jarak Terpendek dapat ditempuh jika Tuan Mor pergi ke')
    print('Rumah Tuan Kin --> Rumah Tuan Kyo --> Restoran')
    print('dengan jarak',cara_1)
elif cara_1>cara_2:
    print('Jarak Terpendek dapat ditempuh jika Tuan Mor pergi ke')
    print('Rumah Tuan Ryo --> Rumah Tuan Kin --> Restoran')
    print('dengan jarak:',cara_2)
else:
    print('Jarak Rumah Tuan Ryo --> Rumah Tuan Kin --> Restoran')
    print('sama dengan jarak Rumah Tuan Kin --> Rumah Tuan Kyo --> Restoran')
    print('dengan jarak:',cara_1)


