#1.1 Tunjukan rata-rata jumlah lab
# (semua jenis lab, baik lab biologi,kimia,dll)
# pada semua sekolah di provinsi 11

#template awal
import pandas as pd
import numpy as np
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

#algoritma
print('rata-rata jumlah lab ipa provinsi 11 adalah',
      df.groupby(['provinsi']).mean().iloc[11:12,31].values[0])
print('rata-rata jumlah lab biologi provinsi 11 adalah',
      df.groupby(['provinsi']).mean().iloc[11:12,32].values[0])
print('rata-rata jumlah lab kimia provinsi 11 adalah',
      df.groupby(['provinsi']).mean().iloc[11:12,33].values[0])
print('rata-rata jumlah lab fisika provinsi 11 adalah',
      df.groupby(['provinsi']).mean().iloc[11:12,34].values[0])
print('rata-rata jumlah lab ips provinsi 11 adalah',
      df.groupby(['provinsi']).mean().iloc[11:12,35].values[0])
print('rata-rata jumlah lab komputer provinsi 11 adalah',
      df.groupby(['provinsi']).mean().iloc[11:12,36].values[0])
