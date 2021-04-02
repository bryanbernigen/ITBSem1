#2b.2 Lakukan LabelEncoding pada kolom status, kurikulum,
# dan penyelenggaraan, lalu print kolom yang sudah diproses.
# kolom status, kurikulum, dan penyelenggaraan yang awal dapat
# di-drop (dihapus) (Hint: Library Sci-Kit Learn)

#template awal
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")


#mengubah kolom jadi string
df['kurikulum']=df['kurikulum'].astype(str)
df['penyelenggaraan']=df['penyelenggaraan'].astype(str)

#mengubah label menjadi nominal
labelencoder = LabelEncoder()
df['status'] = labelencoder.fit_transform(df['status'])
df['kurikulum'] = labelencoder.fit_transform(df['kurikulum'])
df['penyelenggaraan'] = labelencoder.fit_transform(df['penyelenggaraan'])

#menampilkan di layar
df.loc[:,['status','kurikulum','penyelenggaraan']]
