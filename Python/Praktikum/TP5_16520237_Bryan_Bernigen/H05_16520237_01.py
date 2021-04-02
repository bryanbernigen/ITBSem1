#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 13 Desember 2020
#Deskripsi:

#kamus
#import modul yang dibutuhkan
import pandas as pd
df = pd.read_csv("D:\\ITB\\TPB Sem. 1\\Pengenalan Komputasi\\Praktikum\\Tugas pendahuluan\\nilai_uas.csv")

#algoritma
#1. Banyaknya data
banyak_data=df.count()+1
print('Banyaknya data:')
print(banyak_data)
print('')


#2. 10 data pertama
sepuluh_data_pertama=df.head(10)
print('sepuluh data pertama:')
print(sepuluh_data_pertama)
print('')


#Data ke-50 sampai 60
print('data ke-50 sampai ke-60:')
data_50_sampai_60=df.loc[50:60,:]
print(data_50_sampai_60)
print('')


#Banyaknya mahasiswa per fakultas
print('banyaknya mahasiswa per fakultas:')
banyak_mahasiswa_per_fakultas=df.groupby(['fakultas']).count().loc[:,"nama"]
print(banyak_mahasiswa_per_fakultas)
print('')


#korelasi antara nilai kalkulus dan nilai fisika
print('korelasi antara nilai kalkulus dan nilai fisika')
korelasi_kal_fis=df['nilai_kal'].corr(df['nilai_fis'])
print('korelasi: ',korelasi_kal_fis)
print('terdapat korelasi positif yang tinggi antara nilai kalkulus dan nilai fisika')
print('sehingga nilai kalkulus  kemungkinan besar akan diikuti oleh nilai')
print('fisika yang tidak berbeda jauh (tinggi-tinggi/ rendah-rendah)')