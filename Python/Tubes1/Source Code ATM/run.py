'''
Menjalankan Program
cek apakah username dan PIN cocok
jika cocok akan masuk menu ATM
dan user bisa memilih layanan ATM
'''
import sqlite3
import os
import time

#KAMUS
#username = string
#pin, NIK, lahir = int
#saldo = float
#conn = deklarasi koneksi kedatabase
#c = cursor untuk database
#sqlite3, os = Library


#Algoritma
#Memulai koneksi ke database
conn = sqlite3.connect('data.db')
# Membuat kursor
c = conn.cursor()

#cek login user
os.system('cls')
print('------------------Selamat Datang------------------')
print('--------Silahkan Masukkan Username dan PIN--------')
masukkan_username = input('Username: ')
masukkan_pin = int(input('PIN: '))
c.execute("SELECT * FROM data_pelanggan WHERE username='{}'"
          "and pin='{}'".format(masukkan_username, masukkan_pin))
if c.fetchall() == []:
    print('Mohon Maaf, Username dan atau PIN salah')
    print('Jika belum memiliki akun, mohon hubungi staff kami')
    exit()
else:
    print('Anda berhasil Login')
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'"
              "and pin='{}'".format(masukkan_username, masukkan_pin))
    login_user = c.fetchall()
    for login_user in login_user:
        pengguna_saat_ini = login_user[0]
        pin_saat_ini = login_user[1]
        saldo_saat_ini = login_user[2]

#mendefinisikan fungsi
def menu():
    os.system('cls')
    print('------------------Selamat Datang------------------')
    print('--------------Silahkan Pilih Layanan--------------')
    print('1)Informasi Akun             Transfer Antar Akun(4')
    print('')
    print('2)Tarik Tunai                          Ganti PIN(5')
    print('')
    print('3)Setor Tunai                             Keluar(6')
    print('')
    pilihan_layanan = int(input('Pilih Menu :'))
    os.system('cls')
    if pilihan_layanan == 1:
        layanan_1()
    if pilihan_layanan==2:
        layanan_2()
    elif pilihan_layanan==3:
        layanan_3()
    elif pilihan_layanan==4:
        layanan_4()
    elif pilihan_layanan==5:
        layanan_5()
    else:
        keluar()
def layanan_1():
    os.system('cls')
    print('Mohon Masukkan PIN Anda')
    print('Masukkan PIN: 0 untuk membatalkan transaksi')
    pin=int(input('PIN: '))
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'"
              "and pin='{}'".format(masukkan_username, pin))
    login_user = c.fetchall()
    for login_user in login_user:
        pengguna_saat_ini = login_user[0]
        pin_saat_ini = login_user[1]
        saldo_saat_ini = login_user[2]
        if pin==0:
           menu()
        elif pin==pin_saat_ini:
            os.system('cls')
            print('--------------------Akun Anda---------------------')
            print('Username :',pengguna_saat_ini)
            print('PIN      :',pin_saat_ini)
            print('Saldo    : Rp'+str(saldo_saat_ini))
            print('--------------------------------------------------')
            print('---Apakah Anda ingin melakukan transaksi lain??---')
            print('1)Ya')
            print('2)Tidak')
            pilihan=int(input('(1/2): '))
            if pilihan==1:
                menu()
            else:
                keluar()
    os.system('cls')
    print('Mohon Maaf PIN Anda salah')
    print('Apakah Anda ingin kembali ke menu?')
    print('1)Ya')
    print('2)Tidak')
    pilihan = int(input('(1/2): '))
    if pilihan == 1:
        menu()
    else:
        keluar()
def layanan_2():
    c.execute("SELECT * FROM data_pelanggan WHERE "
              "username='{}'".format(masukkan_username))
    login_user = c.fetchall()
    # mengambil data dari database dengan menggunakan loop dan memanfaatkan array
    for login_user in login_user:
        pengguna_saat_ini = login_user[0]
        pin_saat_ini = login_user[1]
        saldo_saat_ini = login_user[2]
    print('-------------Pilih Jumlah Paket Tunai-------------')
    print('1)Rp50.000                           Rp1.000.000(4')
    print('')
    print('2)Rp100.000                          Rp1.500.000(5')
    print('')
    print('3)Rp500.000                              Kembali(6')
    print('')
    print('Saldo Anda Rp',saldo_saat_ini)
    pilihan_tunai = int(input('Pilih jumlah yang akan Anda tarik: '))
    #kondisional untuk saldo
    if pilihan_tunai == 1:
        tarikan=50000
    elif pilihan_tunai ==2:
        tarikan=100000
    elif pilihan_tunai ==3:
        tarikan=500000
    elif pilihan_tunai ==4:
        tarikan=1000000
    elif pilihan_tunai ==5:
        tarikan=1500000
    elif pilihan_tunai == 6:
        menu()
    else:
        menu()
    if saldo_saat_ini < tarikan:
        os.system('cls')
        print('Mohon maaf saldo Anda tidak mencukupi')
        print('Saldo Anda: Rp' + str(saldo_saat_ini))
        print('Apakah Anda ingin melakukan transaksi lainnya?')
        print('1)Ya')
        print('2)Tidak')
        pilihan = int(input('(1/2): '))
        if pilihan == 1:
            menu()
        else:
            keluar()
    os.system('cls')
    print('Saldo Anda: Rp'+str(saldo_saat_ini))
    print('Anda akan menarik Rp'+str(tarikan))
    print('Saldo akhir Anda akan menjadi Rp'+str(saldo_saat_ini-tarikan))
    print('Mohon Masukkan PIN Anda')
    print('Masukkan PIN: 0 untuk membatalkan transaksi')
    pin = int(input('PIN: '))
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'"
              "and pin='{}'".format(masukkan_username, pin))
    login_user = c.fetchall()
    for login_user in login_user:
        pengguna_saat_ini = login_user[0]
        pin_saat_ini = login_user[1]
        saldo_saat_ini = login_user[2]
        if pin == 0:
            menu()
        elif pin == pin_saat_ini:
            os.system('cls')
        if saldo_saat_ini >= tarikan:
            saldo_now = saldo_saat_ini - tarikan
            c.execute("UPDATE data_pelanggan SET saldo='{}' WHERE username='{}'".format(saldo_now, pengguna_saat_ini))
            conn.commit()
            print('Anda berhasil menarik Rp'+str(tarikan))
            print('Username  :', pengguna_saat_ini)
            print('Sisa Saldo: Rp' + str(saldo_now))
            print('Apakah Anda ingin melakukan transaksi lainnya?')
            print('1)Ya')
            print('2)Tidak')
            pilihan = int(input('(1/2): '))
            if pilihan == 1:
                menu()
            else:
                keluar()
        else:
            print('Saldo Kurang')
    if pin == 0:
        menu()
    os.system('cls')
    print('Mohon Maaf PIN Anda salah')
    print('Apakah Anda ingin kembali ke menu?')
    print('1)Ya')
    print('2)Tidak')
    pilihan = int(input('(1/2): '))
    if pilihan == 1:
        menu()
    else:
        keluar()
def layanan_3():
    os.system('cls')
    #Mengambil data dengan format username
    c.execute("SELECT * FROM data_pelanggan WHERE "
              "username='{}'".format(masukkan_username))
    login_user = c.fetchall()
    for login_user in login_user:
        pengguna_saat_ini = login_user[0]
        pin_saat_ini = login_user[1]
        saldo_saat_ini = login_user[2]
    print('Saldo Anda saat ini Rp'+str(saldo_saat_ini))
    print('Setoran Tunai')
    print('Silahkan Masukkan Uang Yang Akan Disetor')
    print('Masukkan 0 & 0 untuk kembali ke menu')
    print('Nominal yang diterima: ')
    print('- Rp 50000')
    print('- Rp 100000')
    isisaldo1=int(input('Masukan jumlah lembar Rp 50000 : '))
    isisaldo2=int(input('Masukan jumlah lembar Rp 100000: '))
    total = (50000*isisaldo1) + (100000*isisaldo2)
    print('Sedang menghitung, mohon tunggu sebentar')
    time.sleep(3)
    if isisaldo1==0 and isisaldo2==0:
        menu()
    print('Transaksi Setoran Tunai')
    print('Rp  50000 x ' + str(isisaldo1) + ' = ' + str(isisaldo1*50000))
    print('Rp 100000 x ' + str(isisaldo2) + ' = ' + str(isisaldo2*100000))
    print('Total         = ' + str(total) )
    print('Setor?')
    print('1)Ya')
    print('2)Batalkan')
    pilihan=int(input('(1/2): '))
    if pilihan==2:
        layanan_3()
    saldo_now=total+saldo_saat_ini
    #Mengeksekusi data setalah saldo ditambahkan yang dideklarasikan dengan variabel saldo_now
    c.execute("UPDATE data_pelanggan SET saldo='{}' WHERE username='{}'".format(saldo_now,pengguna_saat_ini))
    conn.commit()
    os.system('cls')
    print('---------Saldo Anda berhasil ditambah---------')
    print('Username :',pengguna_saat_ini)
    print('Saldo    : Rp'+str(saldo_now))
    print('')
    print('Apakah Anda ingin melakukan transaksi lainnya?')
    print('1)Ya')
    print('2)Tidak')
    pilihan = int(input('(1/2): '))
    if pilihan == 1:
        menu()
    else:
        keluar()
def layanan_4():
    c.execute("SELECT * FROM data_pelanggan WHERE "
              "username='{}'".format(masukkan_username))
    login_user = c.fetchall()
    for login_user in login_user:
        pengguna_saat_ini = login_user[0]
        pin_saat_ini = login_user[1]
        saldo_saat_ini = login_user[2]
    print('Masukan transfer: 0 untuk kembali ke menu')
    tujuan=input('Masukkan akun yang akan di transfer: ')
    if tujuan=='0':
        menu()
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'".format(tujuan))
    hasil=c.fetchall()
    if hasil==[]:
        os.system('cls')
        print('Akun tidak ditemukan')
        layanan_4()
    for item in hasil:
        akun_tujuan=item[0]
        saldo_tujuan=item[2]
    if akun_tujuan==pengguna_saat_ini:
        os.system('cls')
        print('Tidak diperbolehkan transfer ke akun sendiri')
        layanan_4()
    os.system('cls')
    a=0
    while a==0:
        print('Penerima:', akun_tujuan)
        print('Masukkan transfer: Rp0 untuk membatalkan transaksi')
        jumlah_transfer=int(input('Masukkan Jumlah yang akan di transfer: Rp'))
        if jumlah_transfer==0:
            os.system('cls')
            layanan_4()
        elif jumlah_transfer<10000:
            os.system('cls')
            print('Minimal transfer Rp10.000')
        elif jumlah_transfer>saldo_saat_ini:
            os.system('cls')
            print('Transfer tidak bisa melebihi saldo Anda')
            print('Sado Anda: Rp'+str(saldo_saat_ini))
        else:
            a=1
    os.system('cls')
    print('Pengirim:',pengguna_saat_ini)
    print('Penerima:',akun_tujuan)
    print('Jumlah  : Rp'+str(jumlah_transfer))
    print('Apakah Anda akan melakukan transfer?')
    print('1)Ya')
    print('2)Tidak')
    pilihan=int(input('(1/2): '))
    if pilihan!=1:
        os.system('cls')
        layanan_4()
    pin=int(input('Masukkan PIN Anda: '))
    if pin!=pin_saat_ini:
        os.system('cls')
        print('PIN Anda salah')
        layanan_4()
    saldo_tujuan_akhir=saldo_tujuan+jumlah_transfer
    saldo_akhir=saldo_saat_ini-jumlah_transfer
    #Mengeksekusi data sesuai perintah transfer
    c.execute("UPDATE data_pelanggan SET saldo='{}' WHERE username='{}'".format(saldo_akhir, pengguna_saat_ini))
    c.execute("UPDATE data_pelanggan SET saldo='{}' WHERE username='{}'".format(saldo_tujuan_akhir, akun_tujuan))
    conn.commit()
    os.system('cls')
    print('Selamat transaksi Anda berhasil')
    print('Sisa saldo Anda Rp'+str(saldo_akhir))
    print('')
    print('Apakah Anda ingin melakukan transaksi lainnya?')
    print('1)Ya')
    print('2)Tidak')
    pilihan = int(input('(1/2): '))
    if pilihan == 1:
        menu()
    else:
        keluar()
def layanan_5():
    konfirmasi_pin=int(input('Masukkan PIN Anda: '))
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'"
              "and pin='{}'".format(masukkan_username, konfirmasi_pin))
    login_user = c.fetchall()
    for login_user in login_user:
        pengguna_saat_ini = login_user[0]
        pin_saat_ini = login_user[1]
        saldo_saat_ini = login_user[2]
        if konfirmasi_pin!=pin_saat_ini:
            print('Mohon maaf, PIN Anda salah')
            print('Anda akan kembali ke menu')
            menu()
        os.system('cls')
        a=1
        while a == 1:
            print('Masukkan PIN Anda:',konfirmasi_pin)
            print('Masukkan PIN: 0 untuk membatalkan perubahan PIN')
            pin_baru = int(input('Masukkan PIN baru Anda: '))
            if pin_baru==0:
                menu()
            elif len(str(pin_baru)) != 6:
                os.system('cls')
                print('Mohon maaf, PIN harus 6 angka')
            elif pin_baru==pin_saat_ini:
                os.system('cls')
                print('Mohon Maaf, PIN baru tidak boleh sama dengan PIN lama')
            else:
                a = 2
        konfirmasi_pin_baru=int(input('Konfirmasi PIN baru Anda:'))
        if konfirmasi_pin_baru!=pin_baru:
            os.system('cls')
            print('Mohon maaf, Konfirmasi PIN Anda salah')
            layanan_5()
        #mengupdate data sesuai pin yang dimasukkan
        c.execute("UPDATE data_pelanggan SET pin='{}' WHERE username='{}'".format(pin_baru,pengguna_saat_ini))
        conn.commit()
        os.system('cls')
        print('     Selamat PIN Anda berhasil di ubah!     ')
        print('Apakah Anda ingin melakukan transaksi lainnya?')
        print('1)Ya')
        print('2)Tidak')
        pilihan=int(input('(1/2): '))
        if pilihan==1:
            menu()
        else:
            keluar()
    os.system('cls')
    print('Mohon Maaf PIN Anda salah')
    print('Apakah Anda ingin kembali ke menu?')
    print('1)Ya')
    print('2)Tidak')
    pilihan = int(input('(1/2): '))
    if pilihan == 1:
        menu()
    else:
        keluar()
def keluar():
    os.system('cls')
    print('  Terima Kasih telah menggunakan layanan kami')
    exit('Mohon untuk selalu menjaga kerahasiaan PIN Anda')

#menjalankan program
menu()

