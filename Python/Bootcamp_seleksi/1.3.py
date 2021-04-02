#1.3 Tunjukan lab apa yang paling banyak jumlahnya pada sekolah jenjang SMK

# template awal
import pandas as pd
import numpy as np

df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

# algoritma

# hapus data dengan id bukan SMK
df.drop(df[df['bentuk'] != 'SMK'].index, inplace=True)

lab_terbanyak = 'a'
jumlah = 0

jumlah_ipa = df['jumlah_lab_ipa'].sum()
print('jumlah lab ipa adalah', jumlah_ipa)
if jumlah_ipa > jumlah:
    lab_terbanyak = 'ipa'
    jumlah = jumlah_ipa

jumlah_bio = df['jumlah_lab_biologi'].sum()
print('jumlah lab biologi adalah', jumlah_bio)
if jumlah_bio > jumlah:
    lab_terbanyak = 'biologi'
    jumlah = jumlah_bio

jumlah_kim = df['jumlah_lab_kimia'].sum()
print('jumlah lab kimia adalah', jumlah_kim)
if jumlah_kim > jumlah:
    lab_terbanyak = 'kimia'
    jumlah = jumlah_kim

jumlah_fis = df['jumlah_lab_fisika'].sum()
print('jumlah lab fisika adalah', jumlah_fis)
if jumlah_fis > jumlah:
    lab_terbanyak = 'fisika'
    jumlah = jumlah_fis

jumlah_bahasa = df['jumlah_lab_bahasa'].sum()
print('jumlah lab bahasa adalah', jumlah_bahasa)
if jumlah_bahasa > jumlah:
    lab_terbanyak = 'bahasa'
    jumlah = jumlah_bahasa

jumlah_ips = df['jumlah_lab_ips'].sum()
print('jumlah lab ips adalah', jumlah_ips)
if jumlah_ips > jumlah:
    lab_terbanyak = 'ips'
    jumlah = jumlah_ips

jumlah_kom = df['jumlah_lab_komputer'].sum()
print('jumlah lab komputer adalah', jumlah_kom)
if jumlah_kom > jumlah:
    lab_terbanyak = 'komputer'
    jumlah = jumlah_kom

print('lab terbanyak adalah lab', lab_terbanyak, 'sebanyak', jumlah, 'buah')