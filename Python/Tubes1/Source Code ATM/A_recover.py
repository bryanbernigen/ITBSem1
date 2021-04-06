import os
import sqlite3
os.system('cls')



#KAMUS
# nik, lahir, pin = int
# saldo = float
# username = string
#conn = deklarasi koneksi kedatabase
#c = cursor untuk database
#os, sqlite3 = library

# Memulai koneksi ke database
conn = sqlite3.connect('data.db')

#membuat cursor
c = conn.cursor()

#ALGORITMA 
#Merupakan algoritma dari recovery akun yang terdir dari syntax-syntax database dan percabangan
print('Masukan Akun yang akan di recover:')
nik=int(input('Masukkan NIK: '))
lahir=int(input('Masukkan tanggal lahir (yyyymmdd): '))
c.execute("SELECT * FROM data_pelanggan WHERE nik='{}' and lahir='{}'".format(nik,lahir))
if c.fetchall() == []:
    print('Mohon maaf, Akun tidak terdaftar')
    exit()
c.execute("SELECT * FROM data_pelanggan WHERE nik='{}' and lahir='{}'".format(nik,lahir))
items=c.fetchall()
for item in items:
    print('Username     :',item[0])
    print('PIN          :',item[1])
    print('Saldo        : Rp'+str(item[2]))
    print('NIK          :',item[3])
    print('Tanggal lahir:',item[4])
pilihan=input('Ubah PIN?(y/n): ')
if pilihan=='n':
    os.system('cls')
    exit()
a=1
#Loop untuk membuat PIN baru
while a == 1:
    os.system('cls')
    print('Username     :', item[0])
    print('PIN          :', item[1])
    print('Saldo        : Rp' + str(item[2]))
    print('NIK          :', item[3])
    print('Tanggal lahir:', item[4])
    print('')
    pin = int(input('Masukkan PIN baru: '))
    if len(str(pin)) != 6:
        print('Mohon maaf, PIN harus 6 angka')
    else:
        a = 2
print('Anda akan mengubah PIN Anda dari')
print(item[1],'menjadi',pin)
pilihan1=input('Ubah?(y/n)')
if pilihan1=='n':
    os.system('cls')
    exit()
#Meengeksekusi perubahan pin di database sesuai input user
c.execute("UPDATE data_pelanggan SET pin='{}' WHERE username='{}' and "
          "nik='{}' and lahir='{}'".format(pin,item[0],nik,lahir))
conn.commit()
os.system('cls')
print('Akun Anda berhasil di recover')
print('Username     :', item[0])
print('PIN          :', pin)
print('Saldo        : Rp' + str(item[2]))
print('NIK          :', item[3])
print('Tanggal lahir:', item[4])