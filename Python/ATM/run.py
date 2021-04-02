'''
menjalankan seluruh program ATM
'''

import sqlite3
from ATM.cek_pengguna import cek_pengguna

masukkan_username = input('Masukkan Username: ')
masukkan_pin = int(input('Masukkan PIN: '))
cek_pengguna()
