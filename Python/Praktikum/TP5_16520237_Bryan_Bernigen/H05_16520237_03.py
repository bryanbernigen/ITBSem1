#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 13 Desember 2020
#Deskripsi:

#kamus
#import modul yang dibutuhkan
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
df = pd.read_csv("D:\\ITB\\TPB Sem. 1\\Pengenalan Komputasi\\Praktikum\\Tugas pendahuluan\\nilai_uas.csv")

#algoritma
#1.histogram nilai kalkulus
df['nilai_kal'].plot(kind='hist', bins=[0,10,20,30,40,50,60,70,80,90,100],rwidth=0.8)
plt.xticks(np.arange(0,101,10))
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Histogram Nilai Kalkulus')
plt.show()


#2. batang horisontal banyaknya mahasiswa per fakultas
df.groupby(['fakultas']).count().plot(kind='bar',y='nama')
plt.legend('')
plt.xlabel('Fakultas')
plt.ylabel('Frekuensi')
plt.title('Banyaknya Mahasiswa per Fakultas')
plt.show()



#3. pie banyaknya mahasiswa per fakultas
df.groupby(['fakultas']).count().plot(kind='pie',y='nama',autopct='%1.1f%%')
plt.legend('')
plt.xlabel('')
plt.ylabel('')
plt.title('Banyaknya Mahasiswa per Fakultas')
plt.show()


#4. Berdasarkan diagram pie dan batang horizontal, manakah fakultas dengan mahasiswa terbanyak? Manakah
#diagram yang lebih baik dalam menampilkan fakultas dengan mahasiswa terbanyak dan mengapa
print('keduanya dapat menampilkan fakultas mana yang memiliki mahasiswa terbanyak.')
print('Namun bar lebih baik dibanding pie karena dengan bar, dapat diketahui perkiraan')
print('jumlah mahasiswa per fakultas. sedangkan dalam pie, hanya diketahui fakultas')
print('mana yang memiliki jumlah terbanyak, namun tidak dengan jumlahnya.')


#Scatter plot dengan nilai kimia sebagai x dan fisika sebagai y
df.plot(kind='scatter',x='nilai_kim',y='nilai_fis')
plt.xlabel('Nilai Kimia')
plt.ylabel('Nilai Fisika')
plt.show()