#1.4 Tunjukan jumlah SMA yang semua ruang kelas dan laboratorium
# memiliki kondisi baik

#template awal
import pandas as pd
import numpy as np
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

#algoritma

#hapus data dengan id bukan SMA
df.drop(df[ df['bentuk'] != 'SMA'].index , inplace=True)
#hapus SMA tanpa kelas dengan kondisi baik
df.drop(df[ df['jumlah_ruang_kelas_baik'] == 0].index , inplace=True)
#hapus SMA dengan kondisi buruk
df.drop(df[ df['jumlah_ruang_kelas_rusak_ringan'] != 0].index , inplace=True)
df.drop(df[ df['jumlah_ruang_kelas_rusak_sedang'] != 0].index , inplace=True)
df.drop(df[ df['jumlah_ruang_kelas_rusak_berat'] != 0].index , inplace=True)

jumlah=df.count().values[0]
print('jumlah SMA dengan seluruh kelas dan laboratorium dalam kondisi baik adalah',jumlah,'buah')