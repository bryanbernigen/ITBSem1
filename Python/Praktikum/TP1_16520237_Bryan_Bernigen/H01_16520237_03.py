#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 18 Oktober 2020
#Deskripsi: Program menentukan sebuah bilangan positif (ganjil/genap), nol, atau negatif

#tampilan awal
print('Ini adalah program untuk menentukan bilangan yang dinput merupakan bilangan')
print('1)Positif (Genap/Ganjil)')
print('2)Nol')
print('3)Negatif')
#memasukan bilangan yang akan di cek
bilangan_yang_akan_di_cek=int(input('Masukkan bilangan yang akan di cek :'))
if bilangan_yang_akan_di_cek > 0:#jika bilangan_yang_akan_di_cek lebih besar dari 0
    if bilangan_yang_akan_di_cek % 2 == 0: #jika sisa bagi sama dengan 0
        #mengubah data bilangan_yang_akan_di_cek menjadi string agar dapat di tampilkan sebaris
        bilangan_yang_akan_di_cek = str(bilangan_yang_akan_di_cek)
        #menampilkan tampilan akhir
        print(bilangan_yang_akan_di_cek + ' adalah bilangan positif genap')
    else: #jika sisa bagi tidak sama dengan 0
        # mengubah data bilangan_yang_akan_di_cek menjadi string agar dapat di tampilkan sebaris
        bilangan_yang_akan_di_cek = str(bilangan_yang_akan_di_cek)
        # menampilkan tampilan akhir
        print(bilangan_yang_akan_di_cek + ' adalah bilangan positif ganjil')
elif bilangan_yang_akan_di_cek < 0:#jika bilangan_yang_akan_di_cek lebih kecil dari 0
    # mengubah data bilangan_yang_akan_di_cek menjadi string agar dapat di tampilkan sebaris
    bilangan_yang_akan_di_cek = str(bilangan_yang_akan_di_cek)
    # menampilkan tampilan akhir
    print(bilangan_yang_akan_di_cek + ' adalah bilangan negatif')
else: #jika bilangan_yang_akan_di_cek sama dengan 0
    # mengubah data bilangan_yang_akan_di_cek menjadi string agar dapat di tampilkan sebaris
    bilangan_yang_akan_di_cek = str(bilangan_yang_akan_di_cek)
    # menampilkan tampilan akhir
    print(bilangan_yang_akan_di_cek + ' adalah bilangan nol')