'''
Daftar user baru
'''


#KAMUS
#username = string
#pin, NIK, lahir = int
#saldo = float
#conn = deklarasi koneksi kedatabase
#c = cursor untuk database


#ALGORITMA
def start():
    import os
    import sqlite3
    import time

    # innitiate connection
    conn = sqlite3.connect('data.db')

    # create a cursor
    c = conn.cursor()

    # create a tabel
    #c.execute(""" create table data_pelanggan (
    #         username text,
    #        pin integer,
    #        saldo real,
    #        nik integer,
    #        lahir integer
    #    )""")


    # input data
    a = 0
    os.system('cls')
    #buat Username (harus beda dr user laen)
    while a == 0:
        username = input('Masukkan Username yang akan dibuat: ')
        c.execute("SELECT * FROM data_pelanggan WHERE username='{}'".format(username))
        if c.fetchall() != []:
            os.system('cls')
            print('Mohon Maaf, Username tidak valid atau sudah terpakai')
            a = 0
        else:
            if len(username)<=12:
                os.system('cls')
                a = 1
            else:
                os.system('cls')
                print('Mohon Maaf, Username tidak valid atau sudah terpakai')
                a=0
    #buat PIN (harus 6 angka)
    while a == 1:
        print('Username Berhasil dibuat')
        pin = int(input('Masukkan PIN yang akan dibuat: '))
        if len(str(pin)) != 6:
            os.system('cls')
            print('Mohon maaf, PIN harus 6 angka')
        else:
            os.system('cls')
            a = 2
    #setoran saldo awal (harus antara 10rb - 10juta)
    while a == 2:
        print('Username Berhasil dibuat')
        print('PIN berhasil dibuat')
        print('Setorkan saldo awal')
        isisaldo1 = int(input('Masukan jumlah lembar Rp 50000 : '))
        isisaldo2 = int(input('Masukan jumlah lembar Rp 100000: '))
        saldo = (50000 * isisaldo1) + (100000 * isisaldo2)
        print('Sedang menghitung, mohon tunggu sebentar')
        time.sleep(3)
        if saldo < 10000:
            os.system('cls')
            print('Mohon maaf, saldo awal minimal Rp10.000')
        elif saldo > 10000000:
            os.system('cls')
            print('Mohon maaf, saldo awal maksimal Rp10.000.000')
        else:
            os.system('cls')
            a = 3
    os.system('cls')
    print('Username   :',username)
    print('PIN        :',pin)
    print('Saldo awal : Rp'+str(saldo))
    konfirmasi=input('Apakah data diatas sudah benar?(y/n): ')
    if konfirmasi=='n':
        #Pemanggilan fungsi start agar kembali ke awal
        start()
    print('Masukan data untuk keperluan recovery')
    print('Masukan data sesuai KTP/kartu keluarga')
    nik = int(input('Masukkan NIK:'))
    c.execute("SELECT * FROM data_pelanggan WHERE nik='{}'".format(nik))
    if c.fetchall() != []:
        os.system('cls')
        print('Mohon Maaf, NIK sudah terdaftar')
        exit()
    os.system('cls')
    while a==3:
        print('Username   :', username)
        print('PIN        :', pin)
        print('Saldo awal : Rp' + str(saldo))
        print('NIK        :', nik)
        lahir=int(input('Masukkan tanggal lahir(ddmmyyyy): '))
        if len(str(lahir))!=8:
            os.system('cls')
            print('Mohon masukkan tanggal lahir yang benar (ddmmyyyy)')
        else:
            os.system('cls')
            a=4
    os.system('cls')
    print('Username     :', username)
    print('PIN          :', pin)
    print('Saldo awal   : Rp' + str(saldo))
    print('NIK          :',nik)
    print('Tanggal lahir:',lahir)
    pilihan=input('Apakah data sudah benar?(y/n): ')
    if pilihan=='n':
        start()
    #Mengeksekusi perubahan data ke database
    c.execute("INSERT INTO data_pelanggan VALUES('{}','{}','{}','{}','{}')".format(username, pin, saldo,nik,lahir))

    #Mengcommit perubahan ke database agar perubahannya bersifat permanen
    conn.commit()

    # Menutup/mematikan koneksi database
    conn.close()

    lanjut=input('Lagi? (y/n): ')
    if lanjut=='y':
        start()
    else:
        os.system('cls')
        exit()

start()