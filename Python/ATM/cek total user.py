import sqlite3
secret_key=int(input())
if secret_key!=123456:
    exit()

# innitiate connection
conn = sqlite3.connect('data.db')
# create a cursor
c = conn.cursor()

c.execute("SELECT * FROM data_pelanggan")
print(c.fetchall())