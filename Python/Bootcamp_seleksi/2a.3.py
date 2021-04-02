#2a.3 Buatlah distribution plot untuk kolom 'rombongan_belajar'
# dengan menggunakan library seaborn. Berikan label pada kedua
# sumbu (x dan y). dan berikan judul pada plot yang dibuat.

#template awal
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")


sns.displot(df.rombongan_belajar, binwidth=2, kde=True).set(xlabel='Banyaknya Siswa dalam Rombongan',
           ylabel='Frekuensi', title='Distribution Plot Rombongan Belajar')