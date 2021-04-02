#2a.1 Buatlah sebuah histogram untuk kolom 'bentuk'

#template awal
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from collections import Counter
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

#algoritma
jumlah_bentuk = Counter(df['bentuk'])
df = pd.DataFrame.from_dict(jumlah_bentuk, orient='index')
df.plot(kind='bar')
plt.legend('')
plt.xlabel('Bentuk Sekolah')
plt.ylabel('Frekuensi')
plt.title('Histogram Bentuk Sekolah')
plt.show()