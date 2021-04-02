#2a.2 Buatlah sebuah boxplot untuk kolom 'siswa_perempuan'

#template awal
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

sns.boxplot(df.siswa_perempuan)