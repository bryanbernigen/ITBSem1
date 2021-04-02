'''
cek apakah username dan PIN cocok
jika cocok akan masuk menu ATM
jika tidak cocok akan kembali ke asal
'''

import sqlite3

def cek_pengguna():
    # innitiate connection
    conn = sqlite3.connect('data.db')
    # create a cursor
    c = conn.cursor()
    # cek user valid atau tidak
    from ATM.run import masukkan_username,masukkan_pin
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'"
              "and pin='{}'".format(masukkan_username, masukkan_pin))
    if c.fetchall()==[]:
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
