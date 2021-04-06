import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import sqlite3
import csv
import os

#KAMUS (Kamus lokal tidak kami masukkan)
# tkinter, sqlite3, csv, os = Library
# q, w, t1 = string
# t2, t4, t5 = int
# t2 = float


#ALGORITMA
#Membuat array kosong untuk menyimpan data sementara 
mydata = []

conn = sqlite3.connect('data.db')
c = conn.cursor()

#Fungsi untuk menampilkan data terbaru setelah dilakukan perubahan
def update(rows):
    global mydata
    mydata = rows
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)

def search():
    q2 = q.get()
    query = "SELECT username, pin, saldo, nik, lahir from data_pelanggan WHERE username LIKE '%" + q2 + "%'"
    c.execute(query)
    rows = c.fetchall()
    update(rows)

def search_nik():
    w2 = w.get()
    query = "SELECT username, pin, saldo, nik, lahir from data_pelanggan WHERE nik LIKE '%" + w2 + "%'"
    c.execute(query)
    rows = c.fetchall()
    update(rows)

def clear():
    ent.delete(0, END)
    entt.delete(0, END)
    query = "SELECT username, pin, saldo, nik, lahir from data_pelanggan"
    c.execute(query)
    rows = c.fetchall()
    update(rows)

def getrow(event):
    #memanfaatkan library trv untuk mengambil data dari tabel dan meunculkannya langsung di textbox
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])

def update_user():
    user_name = t1.get()
    pas_user = t2.get()
    sal_do = t3.get()
    n_ik = t4.get()
    lah_ir = t5.get()
    c.execute("SELECT * FROM data_pelanggan WHERE NIK='{}'".format(n_ik))
    #Kondisional untuk menentukan apakah data yang akan diperbarui sudah sesuai ketentuans
    if len(str(pas_user)) != 6:
        messagebox.showerror("ERROR", "Mohon Maaf, PIN harus 6 angka")
        return False
    else:
        if len(str(lah_ir)) != 8:
            messagebox.showerror("ERROR", "Mohon masukkan tanggal lahir yang benar (ddmmyyyy)")
            return False
        else:
            if messagebox.askyesno("UPDATE", "Perbarui data pelanggan ini?"):
                query = "UPDATE data_pelanggan SET pin='{}' WHERE username='{}'".format(pas_user, user_name)
                query1 = "UPDATE data_pelanggan SET nik='{}' WHERE username='{}'".format(n_ik, user_name)
                query2 = "UPDATE data_pelanggan SET lahir='{}' WHERE username='{}'".format(lah_ir, user_name)
                #Mengeksekusi query yang telah dideklarasikan
                c.execute(query)
                c.execute(query1)
                c.execute(query2)
                #Mengcommit perubahan ke database agar perubahannya bersifat permanen
                conn.commit()
                clear()
                print("Success!")
            else:
                return True
    #Membersihkan textbox setelah dilakukan perubahan
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)

def sort_username_dsc():
    # Mengurutkan berdasarkan username secara menurun (A-Z)
    c.execute("SELECT * from data_pelanggan ORDER BY username DESC")
    rows = c.fetchall()
    update(rows)

def sort_username_asc():
    # Mengurutkan berdasarkan username secara menaik (Z-A)
    c.execute("SELECT * from data_pelanggan ORDER BY username")
    rows = c.fetchall()
    update(rows)

def sort_nik_asc():
    # Mengurutkan berdasarkan NIK secara menurun (0-9)
    c.execute("SELECT * from data_pelanggan ORDER BY nik ASC")
    rows = c.fetchall()
    update(rows)

def sort_nik_dsc():
    # Mengurutkan berdasarkan NIK secara menurun (9-0)
    c.execute("SELECT * from data_pelanggan ORDER BY nik DESC")
    rows = c.fetchall()
    update(rows)

def add_user():
    user_name = t1.get()
    pas_user = t2.get()
    sal_do = t3.get()
    n_ik = t4.get()
    lah_ir = t5.get()
    #Mengeksekusi database dengan keyword username
    c.execute("SELECT * FROM data_pelanggan WHERE username='{}'".format(user_name))
    #Kondisional untuk menentukan apakah data yang diisikan sesuai dengan aturan
    if c.fetchall() != []:  #kondisional bila username tidak valid/sudah terpakai
        messagebox.showerror("ERROR", "Mohon Maaf, Username tidak valid atau sudah terpakai")
        return False
    else:
        if len(str(pas_user)) != 6:
            messagebox.showerror("ERROR", "Mohon Maaf, PIN harus 6 angka")
            return False
        else:
            if sal_do < 10000:
                messagebox.showerror("ERROR", "Mohon maaf, saldo awal minimal Rp10.000")
                return False
            elif sal_do > 10000000:
                messagebox.showerror("ERROR", "Mohon maaf, saldo awal maksimal Rp10.000.000")
                return False
            else:
                c.execute("SELECT * FROM data_pelanggan WHERE NIK='{}'".format(n_ik))
                if c.fetchall() != []:
                    messagebox.showerror("ERROR", "Mohon Maaf, NIK sudah terdaftar")
                    return False
                else:
                    if len(str(lah_ir)) != 8:
                        messagebox.showerror("ERROR", "Mohon masukkan tanggal lahir yang benar (ddmmyyyy)")
                        return False
                    else:
                        query = "INSERT INTO data_pelanggan(username, pin, saldo, nik, lahir) VALUES('{}', '{}', '{}', '{}', '{}')".format(
                            user_name, pas_user, sal_do, n_ik, lah_ir)
                        # Mengeksekusi query yang sudah didekalrasikan
                        c.execute(query)
                        #Mengcommit perubahan ke database agar perubahannya bersifat permanen
                        conn.commit()
                        clear()
                        ent1.delete(0, END)
                        ent2.delete(0, END)
                        ent3.delete(0, END)
                        ent4.delete(0, END)
                        ent5.delete(0, END)

def delete_user():
    user_name = t1.get()
    if messagebox.askyesno("DELETE", "Hapus pelanggan ini?"):
        query = "DELETE FROM data_pelanggan WHERE username='{}'".format(user_name)
        c.execute(query)
        #Mengcommit perubahan ke database agar perubahannya bersifat permanen
        conn.commit()
        clear()
    else:
        return True
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)

def export():
    if len(mydata) < 1:
        messagebox.showerror("ERROR", "Tidak ada data yang bisa di export")
        return False
    #Membuat file menjadi file csv
    fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                       filetypes=(("CSV FILE", "*.csv"), ("All Files", "*.")))
    #Mengeksport data dalam bentuk file csv
    with open(fln, mode='w') as myfile:
        exp_writer = csv.writer(myfile, delimiter=',')
        for i in mydata:
            exp_writer.writerow(i)

    messagebox.showinfo("Data Exported", "Data berhasil di eksport ke file: " + os.path.basename(fln))

def clear_data():
    #Fungsi untuk mengclear data setelah diisi
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)


#Program GUI
root = Tk()
q = StringVar()
w = StringVar()
t1 = StringVar()
t2 = IntVar()
t3 = DoubleVar()
t4 = IntVar()
t5 = IntVar()

#Mengeset ukuran default interface
root.minsize(width=1000,height=700)

#Membuat wrapper yang terdiri dari 3 buah
wrapper1 = LabelFrame(root, text="Database table")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="User Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5), show="headings", height="6")
trv.pack()

trv.heading(1, text="Username")
trv.heading(2, text="Pin")
trv.heading(3, text="Saldo")
trv.heading(4, text="NIK")
trv.heading(5, text="Tanggal Lahir")

trv.bind('<Double 1>', getrow)

#mengambil data pelanggan berdasarkan username
c.execute("SELECT * from data_pelanggan ORDER BY username")
rows = c.fetchall()
update(rows)

expbtn = Button(wrapper1, text="Export CSV", command=export)
expbtn.pack(side=tk.LEFT, padx=10, pady=10)
updatebtn = Button(wrapper1, text="Update", command=clear)
updatebtn.pack(side=tk.LEFT, padx=10, pady=10)

# Search section
space = Label(wrapper2, text='').grid(row=0)

lbl = Label(wrapper2, text="Search Username")
lbl.grid(row=1, column=0, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.grid(row=1, column=1, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.grid(row=1, column=2, padx=6)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.grid(row=1, column=3, padx=6)

space1 = Label(wrapper2, text='').grid(row=2)

lbl = Label(wrapper2, text="Search NIK")
lbl.grid(row=3, column=0, padx=10)
entt = Entry(wrapper2, textvariable=w)
entt.grid(row=3, column=1, padx=6)
btn = Button(wrapper2, text="Search", command=search_nik)
btn.grid(row=3, column=2, padx=6)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.grid(row=3, column=3, padx=6)

sort_username_asc_btn = Button(wrapper2, text="Sort Username Ascending", command=sort_username_asc)
sort_username_asc_btn.grid(row=1, column=4, padx=10, pady=10)
sort_username_dsc_btn = Button(wrapper2, text="Sort Username Descending", command=sort_username_dsc)
sort_username_dsc_btn.grid(row=1, column=5, padx=10, pady=10)
sort_nik_asc_btn = Button(wrapper2, text="Sort NIK Ascending", command=sort_nik_asc)
sort_nik_asc_btn.grid(row=3, column=4, padx=10, pady=10)
sort_nik_dsc_btn = Button(wrapper2, text="Sort NIK Descending", command=sort_nik_dsc)
sort_nik_dsc_btn.grid(row=3, column=5, padx=10, pady=10)

# User Data section
lbl1 = Label(wrapper3, text="Username")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="PIN")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="Saldo")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="NIK")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5 = Label(wrapper3, text="Tanggal Lahir")
lbl5.grid(row=4, column=0, padx=5, pady=3)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=3)

btn_up = Button(wrapper3, text="Update", command=update_user)
add_btn = Button(wrapper3, text="Add", command=add_user)
delete_btn = Button(wrapper3, text="Delete", command=delete_user)
clear_btn = Button(wrapper3, text="Clear", command=clear_data)

add_btn.grid(row=5, column=0, padx=5, pady=3)
btn_up.grid(row=5, column=1, padx=5, pady=3)
delete_btn.grid(row=5, column=2, padx=5, pady=3)
clear_btn.grid(row=5, column=3, padx=5, pady=3)

ent1.delete(0, END)
ent2.delete(0, END)
ent3.delete(0, END)
ent4.delete(0, END)
ent5.delete(0, END)

#Memulai program utama
root.title("Database Management System")
root.geometry("800x700")
root.mainloop()

