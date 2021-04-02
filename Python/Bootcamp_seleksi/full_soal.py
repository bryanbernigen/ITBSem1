'''
cara menjalankan kode:
1. buat folder bernama data_pandas di drive (D:)
2. masukkan data_sekolah ke dalam folder tersebut
3. masukkan kode di bawah ke terminal (Di laptop pembuat kode, ini rootnya)
    cd C:/Users/Asus/PycharmProjects/pythonProject/Bootcamp_seleksi/
4. ketik: python
5. masukkan judul yang akan di run:
    ____.py (____ berisi judul yang akan di run *cth 1.1.py)
'''


#1.1 Tunjukan rata-rata jumlah lab
# (semua jenis lab, baik lab biologi,kimia,dll)
# pada semua sekolah di provinsi 11


#1.2 Tunjukan provinsi mana yang memiliki rata-rata perbandingan
# jumlah guru per jumlah siswa yang paling rendah dibanding provinsi
# yang lain dan tunjukkan jumlahnya


#1.3 Tunjukan lab apa yang paling banyak jumlahnya pada sekolah jenjang SMK


#1.4 Tunjukan jumlah SMA yang semua ruang kelas dan laboratorium memiliki kondisi baik


#1.5 Dari semua sekolah jenjang SMK, provinsi mana yang memiliki
# akses internet paling susah dan paling baik (ditunjukan dengan
#persentase jumlah sekolah dengan akses internet / jumlah sekolah )?


#1.6 Tunjukan kurikulum apa yang memiliki rata rata akreditasi
# paling baik (semakin kecil nilai akreditasi, semakin baik)


#2a.1 Buatlah sebuah histogram untuk kolom 'bentuk'


#2a.2 Buatlah sebuah boxplot untuk kolom 'siswa_perempuan'


#2a.3 Buatlah distribution plot untuk kolom 'rombongan_belajar'
# dengan menggunakan library seaborn. Berikan label pada kedua
# sumbu (x dan y). dan berikan judul pada plot yang dibuat.


#2a.4 Buatlah visualisasi seperti dibawah ini. dengan sumbu x nya
# merupakan kolom 'siswa_laki_laki' dan pembagianya berdasarkan
# 'kurikulum' (pada plot di bawah warna berdasarkan species).
# hint: library seaborn. Jelaskan insight dari plot yang sudah dibuat.


#2b.1 Drop (hapus) semua baris yang mempunyai nilai null, lalu print
# jumlah baris dan kolom yang ada (Hint: Library Pandas).


#2b.2 Lakukan LabelEncoding pada kolom status, kurikulum,
# dan penyelenggaraan, lalu print kolom yang sudah diproses.
# kolom status, kurikulum, dan penyelenggaraan yang awal dapat
# di-drop (dihapus) (Hint: Library Sci-Kit Learn)


#2b.3 Lakukan OneHotEncoding pada kolom bentuk. Kolom bentuk yang
# belum diproses dapat dihapus (Hint: Library Sci-Kit Learn)


#2c.1. Lakukan training pada model LogisticRegression
# untuk memprediksi nilai kolom akreditasi (Hint: Library Sci-Kit Learn)


#2c.2. Lakukan prediksi untuk variabel akreditasi
# menggunakan data training (data awal, dengan kolom
# akreditasi yang di-drop) (Hint: Library Sci-Kit Learn)


#3a wawasan tentang ordinal, nominal, numeral


#3b case study