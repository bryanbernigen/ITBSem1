#1.6 Tunjukan kurikulum apa yang memiliki rata rata akreditasi
# paling baik (semakin kecil nilai akreditasi, semakin baik)

#template awal
import pandas as pd
import numpy as np
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

#algoritma

print(df.groupby(['kurikulum']).mean().sort_values(by='akreditasi',ascending=True).loc[:,'akreditasi'])
kurikulum_1=df.groupby(['kurikulum']).mean().sort_values(by='akreditasi',ascending=True).index[0]
akreditasi_1= df.groupby(['kurikulum']).mean().sort_values(by='akreditasi',ascending=True).loc[:,'akreditasi'].values[0]
print(kurikulum_1,'merupakan kurikulum terbaik dengan rata-rata akreditasi sekolah', akreditasi_1)
