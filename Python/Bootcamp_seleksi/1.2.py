#1.2 Tunjukan provinsi mana yang memiliki rata-rata perbandingan
# jumlah guru per jumlah siswa yang paling rendah dibanding provinsi
# yang lain dan tunjukkan jumlahnya

# template awal
import pandas as pd
import numpy as np
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

# algoritma

#grup berdasarkan provinsi
df.groupby(['provinsi']).mean()

# jumlah data
jumlah_data = df.count().values[0]

# tambah kolom gur per murid
df.insert(47, "guru_per_siswa", [0.0 for i in range(jumlah_data)], True)

# mengisi guru per murid
for i in range(jumlah_data):
    if df['jumlah_siswa'][i] == 0:
        pass
    else:
        df['guru_per_siswa'][i] = df['jumlah_guru_sertifikasi'][i] / df['jumlah_siswa'][i]

# menampilkan di layar
print(df.groupby(['provinsi']).mean().sort_values(by='guru_per_siswa', ascending=True).loc[:, 'guru_per_siswa'])
provinsi_terendah=df.groupby(['provinsi']).mean().sort_values(by='guru_per_siswa', ascending=True).index[0]
nilai_terendah=df.groupby(['provinsi']).mean().sort_values(by='guru_per_siswa', ascending=True).loc[1, 'guru_per_siswa']
print('provinsi',provinsi_terendah,'memiliki nilai guru per murid yang paling rendah')
print('dengan nilai '+str(nilai_terendah))
