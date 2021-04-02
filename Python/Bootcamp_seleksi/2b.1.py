#2b.1 Drop (hapus) semua baris yang mempunyai nilai null, lalu print
# jumlah baris dan kolom yang ada (Hint: Library Pandas).

#template awal
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")


#algoritma
print('-------------------Sebelum-------------------')
print(df.isnull().sum())
print(df.shape)
print('\n\n\n\n')

print('-------------------Sesudah-------------------')
print(df.dropna().isnull().sum())
print(df.dropna().shape)
