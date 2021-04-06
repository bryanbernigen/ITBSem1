'''
Cari user berdasarkan kategori tertentu
'''

#KAMUS LOKAL
#user = string
# sqlite3, os = library


#ALGORITMA
def start():
    import os
    import sqlite3
    # Memulai koneksi ke database
    conn = sqlite3.connect('data.db')
    #Membua cursor di database
    c = conn.cursor()
    os.system('cls')
    user=input('Masukkan Username yang akan dicari: ')
    #Mengeksekusi data sesuai dengan inputan user
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'".format(user))
    #Mengambil data dan menampilkannya jika ada
    if c.fetchall()==[]:
        print('Akun tidak terdaftar')
    else:
        print('Akun',user,'terdaftar')
start()