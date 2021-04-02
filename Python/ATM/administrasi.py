'''
Daftar user baru
'''

secret_key=int(input())
if secret_key!=123456:
    exit()
def start():
    import sqlite3

    # innitiate connection
    conn = sqlite3.connect('data.db')

    # create a cursor
    c = conn.cursor()

    # create a tabel
    '''c.execute(""" create table data_pelanggan (
            username text,
            pin integer,
            saldo real
        )""")
    '''

    # input data
    username = input('Masukkan Username: ')
    pin = int(input('Masukkan PIN: '))
    saldo = int(input('Masukkan Saldo Awal: '))

    # execute into database
    c.execute("INSERT INTO data_pelanggan VALUES('{}','{}','{}')".format(username, pin, saldo))

    # commit command
    conn.commit()

    # close connection
    conn.close()
start()