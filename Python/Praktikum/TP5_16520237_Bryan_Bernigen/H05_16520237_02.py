#NIM/Nama : 16520237/Bryan Bernigen
#Tanggal  : Minggu, 13 Desember 2020
#Deskripsi:

#kamus
#import modul yang dibutuhkan
import pandas as pd
df = pd.read_csv("D:\\ITB\\TPB Sem. 1\\Pengenalan Komputasi\\Praktikum\\Tugas pendahuluan\\nilai_uas.csv")

#algoritma
#1. nilai Tuan Mor
nilai_tuan_mor_kal=df['nilai_kal'][df['nama'] == 'Tuan Mor'].values[0]
nilai_tuan_mor_fis=df['nilai_fis'][df['nama'] == 'Tuan Mor'].values[0]
nilai_tuan_mor_kim=df['nilai_kim'][df['nama'] == 'Tuan Mor'].values[0]
print('nilai kalkulus Tuan Mor:',nilai_tuan_mor_kal)
print('nilai fisika Tuan Mor  :',nilai_tuan_mor_fis)
print('nilai kimia Tuan Mor   :',nilai_tuan_mor_kim)
print('')

#2. Mahasiswa dengan nilai fisika tertinggi
fis_tertinggi=df['nilai_fis'].max()
mahasiswa_nilai_fis_tertinggi=df.loc[df['nilai_fis'] == fis_tertinggi][['nama']]
print('Mahasiswa dengan nilai fisika tertinggi('+str(fis_tertinggi)+') adalah')
print(mahasiswa_nilai_fis_tertinggi)
print('')


#3. 10 Mahasiswa dengan nilai kimia tertinggi
print('10 Mahasiswa dengan nilai kimia tertinggi adalah')
urut_kimia_terbalik=df.sort_values(by='nilai_kim',ascending=False)
kimia_10_terbaik=urut_kimia_terbalik.head(10).loc[:,['nama','nilai_kim']]
print(kimia_10_terbaik)
print('')

#4.banyak nilai kalkulus dibawah 50
kalkulus_dibawah_50=len(df[(df['nilai_kal']<50)])
print('banyak mahasiswa dengan nilai kalkulus dibawah 50 adalah',kalkulus_dibawah_50,'orang')
print('')


#5. Banyak mahasiswa FMIPA
banyak_mahasiswa_FMIPA=len(df[(df['fakultas']=='FMIPA')])
print('banyak mahasiswa FMIPA adalah',banyak_mahasiswa_FMIPA,'orang')