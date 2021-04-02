#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 18 Oktober 2020
#Deskripsi: Program kalkulator sederhana

#tampilan awal kalkulator
print('Ini adalah program kalkulator sederhana yang mengoperasikan dua buah angka')
print('Operasi yang dapat dilakukan kalkulator:')
print('Tambah                    (+)')
print('Kurang                    (-)')
print('Kali                      (*)')
print('Bagi                      (/)')
print('Bagi dibulatkan ke bawah (//)')
print('Sisa bagi                 (%)')
#pemasukkan angka yang akan dioperasikan
angka_pertama=int(input('Masukkan angka pertama :'))
angka_kedua=int(input('Masukkan angka kedua   :'))
#pemilihan jenis operasi yang akan dilakukan
operator=input('Masukkan operator      :')
#jika memilih tambah
if operator=='+':
    #penerapan operator
    hasil_operasi = angka_pertama + angka_kedua
    #pengubahan bentuk data dari integer menjadi string agar dapat ditampilkan dalam satu baris
    angka_pertama = str(angka_pertama)
    angka_kedua = str(angka_kedua)
    hasil_operasi = str(hasil_operasi)
    #menampilkan hasil akhir
    print(angka_pertama+' + '+angka_kedua+' = '+hasil_operasi)
#jika memilih kurang
elif operator=='-':
    # penerapan operator
    hasil_operasi = angka_pertama - angka_kedua
    # pengubahan bentuk data dari integer menjadi string agar dapat ditampilkan dalam satu baris
    angka_pertama = str(angka_pertama)
    angka_kedua = str(angka_kedua)
    hasil_operasi = str(hasil_operasi)
    # menampilkan hasil akhir
    print(angka_pertama+' - '+angka_kedua+' = '+hasil_operasi)
#jika memilih kali
elif operator=='*':
    # penerapan operator
    hasil_operasi = angka_pertama * angka_kedua
    # pengubahan bentuk data dari integer menjadi string agar dapat ditampilkan dalam satu baris
    angka_pertama = str(angka_pertama)
    angka_kedua = str(angka_kedua)
    hasil_operasi = str(hasil_operasi)
    # menampilkan hasil akhir
    print(angka_pertama+' * '+angka_kedua+' = '+hasil_operasi)
#jika memilih bagi
elif operator=='/':
    # penerapan operator
    hasil_operasi = angka_pertama / angka_kedua
    # pengubahan bentuk data dari integer menjadi string agar dapat ditampilkan dalam satu baris
    angka_pertama = str(angka_pertama)
    angka_kedua = str(angka_kedua)
    hasil_operasi = str(hasil_operasi)
    # menampilkan hasil akhir
    print(angka_pertama+' / '+angka_kedua+' = '+hasil_operasi)
#jika memilih bagi pembulatan ke bawah
elif operator=='//':
    # penerapan operator
    hasil_operasi = angka_pertama // angka_kedua
    # pengubahan bentuk data dari integer menjadi string agar dapat ditampilkan dalam satu baris
    angka_pertama = str(angka_pertama)
    angka_kedua = str(angka_kedua)
    hasil_operasi = str(hasil_operasi)
    # menampilkan hasil akhir
    print(angka_pertama+' // '+angka_kedua+' = '+hasil_operasi)
#jika memilih sisa bagi
elif operator=='%':
    # penerapan operator
    hasil_operasi = angka_pertama % angka_kedua
    # pengubahan bentuk data dari integer menjadi string agar dapat ditampilkan dalam satu baris
    angka_pertama = str(angka_pertama)
    angka_kedua = str(angka_kedua)
    hasil_operasi = str(hasil_operasi)
    # menampilkan hasil akhir
    print(angka_pertama+' % '+angka_kedua+' = '+hasil_operasi)
#jika memilih operasi selain yang tertera di tampilan awal
else:
    exit('Error, Operasi tidak terdaftar')