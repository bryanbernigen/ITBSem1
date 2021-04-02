#2a.4 Buatlah visualisasi seperti dibawah ini. dengan sumbu x nya
# merupakan kolom 'siswa_laki_laki' dan pembagianya berdasarkan
# 'kurikulum' (pada plot di bawah warna berdasarkan species).
# hint: library seaborn. Jelaskan insight dari plot yang sudah dibuat.

#template awal
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")


meh = df[df.kurikulum == 'KTSP']
sns.distplot(meh['siswa_laki_laki'],  kde=False, label='KTSP',bins=100)
meh = df[df.kurikulum == 'K-13']
sns.distplot(meh['siswa_laki_laki'],  kde=False, label='K-13', bins=100)

plt.legend(prop={'size': 12})
plt.title('Jumlah Seklah dengan Banyak Siswa Tertentu')
plt.xlabel('Jumlah Siswa')
plt.ylabel('Jumlah Sekolah')