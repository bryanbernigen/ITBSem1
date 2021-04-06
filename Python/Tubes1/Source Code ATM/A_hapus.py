'''
Menghapus User dari database
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
    os.system('cls')
    # Memulai Koneksi
    conn = sqlite3.connect('data.db')

    # Membuat cursir
    c = conn.cursor()
    print('Masukkan Akun yang akan dihapus')
    username = input('Username: ')
    pin = int(input('PIN :'))
    #Mengeksekusi pengambilan data dengan keyword username dan pin inputan user
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}' and pin='{}'".format(username, pin))
    #Mengambil(fetch) data dari database
    items = c.fetchall()
    if items == []:
        exit('Akun tidak terdaftar')
    os.system('cls')
    print('Anda akan menghapus Akun')
    for item in items:
        print('Username: ', item[0])
        print('PIN     : ', item[1])
        print('Saldo   : Rp' + str(item[2]))
    print('Apakah Anda yakin akan menghapus akan tersebut?')
    print('Akun yang sudah terhapus tidak dapat dikembalikan')
    print('1)Ya')
    print('2)Tidak')
    pilihan = int(input('(1/2): '))
    if pilihan != 1:
        os.system('cls')
        exit()
    # Mendelete data akun sesudah user mengkonfirmasi untuk mendelete akunnya dengan syntax database
    c.execute("DELETE from data_pelanggan WHERE username='{}' and pin='{}'".format(username, pin))
    #Mengcommit perubahan ke database agar perubahannya bersifat permanen
    conn.commit()
    #Mengclear tampilan layar
    os.system('cls')
    print('           Akun berhasil dihapus           ')
    print('Terima Kasih telah menggunakan layanan kami')
start()
