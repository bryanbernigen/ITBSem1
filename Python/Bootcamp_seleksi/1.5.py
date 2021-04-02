#1.5 Dari semua sekolah jenjang SMK, provinsi mana yang memiliki
# akses internet paling susah dan paling baik (ditunjukan dengan
#persentase jumlah sekolah dengan akses internet / jumlah sekolah )?

#template awal
import pandas as pd
import numpy as np
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")


#algoritma

#hapus data dengan id bukan SMK
df.drop(df[ df['bentuk'] != 'SMK'].index , inplace=True)

#jumlah data
jumlah_data=df.count().values[0]

#tambah kolom akses internet dengan angka
df.insert(47, "aksesinternet", [0 for i in range(jumlah_data)], True)
for i in range(jumlah_data):
    df['aksesinternet'] = np.where(df['akses_internet'] == True, 1, 0)


print(df.groupby(['provinsi']).mean().sort_values(by='aksesinternet',ascending=True).loc[:,'aksesinternet'])
internet_baik=df.groupby(['provinsi']).mean().sort_values(by='aksesinternet',ascending=True).loc[:,'aksesinternet'].values[0]
internet_buruk=df.groupby(['provinsi']).mean().sort_values(by='aksesinternet',ascending=False).loc[:,'aksesinternet'].values[0]
provinsi_baik=df.groupby(['provinsi']).mean().sort_values(by='aksesinternet',ascending=True).index[0]
provinsi_buruk=df.groupby(['provinsi']).mean().sort_values(by='aksesinternet',ascending=False).index[0]


print('provinsi',provinsi_baik,'merupakan provinsi dengan akses internet terburuk dengan nilai',internet_baik)
print('provinsi',provinsi_buruk,'merupakan provinsi dengan akses internet terbaik dengan nilai',internet_buruk)
