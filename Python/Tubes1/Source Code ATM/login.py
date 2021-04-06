import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

#KAMUS
# tkinter, sqlite3, os = Library
# e1 = string
# e2 = int




#ALGORITMA
#Bagian ini untuk mengkoneksikan ke database, membuat cursor, dan mengambil data
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("SELECT * from data_pelanggan")
rows = c.fetchall()

conn = sqlite3.connect('data.db')
c = conn.cursor()

#Fungsi Ok
def Ok():
    #Mendeklarasikan variabel untuk mengambil inputan user
    uname = e1.get()
    password = e2.get()

    #Kondisional untuk mengecek apakah inputan user sesuai dengan username dan password yang sudah diset
    if uname == "" or password == "":
        messagebox.showinfo("", "Please fill the required field")

    elif(uname == "admin" and password == "123456"):
        #Menampilkan messagebox
        messagebox.showinfo("", "Login Succes")
        root.destroy()
        os.system('python admin.py')
        
    else:
        messagebox.showinfo("", "Incorrect username or password!")

#GUI/Interface untuk bagian login
root = Tk()
root.title("Admin Panel")
root.geometry("300x300")
root.resizable(False, False)
#Mendeklarasikan variabel global
global e1
global e2
global e3
global e4
#Membuat label untuk textbox
Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

#Membuat textbox untuk menerima inputan pengguna
e1 = Entry(root)
e1.place(x=140, y=10)


e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=Ok, height=2, width=10).place(x=100,y=80)

#Memulai program
root.mainloop()
  
