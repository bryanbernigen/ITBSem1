#2b.3 Lakukan OneHotEncoding pada kolom bentuk. Kolom bentuk yang
# belum diproses dapat dihapus (Hint: Library Sci-Kit Learn)


#template awal
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,LabelBinarizer
from sklearn import preprocessing
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

df['bentuk_encoded'] = LabelEncoder().fit_transform(df.bentuk)
X = OneHotEncoder().fit_transform(df.bentuk_encoded.values.reshape(-1,1)).toarray()
dfOneHot = pd.DataFrame(X, columns = ["Bentuk_"+str(int(i)+1) for i in range(X.shape[1])])
df = pd.concat([df, dfOneHot], axis=1)

print(df.loc[:,'Bentuk_1':'Bentuk_4'])
print('Bentuk_1: SD')
print('Bentuk_2: SMA')
print('Bentuk_3: SMK')
print('Bentuk_4: SMP')