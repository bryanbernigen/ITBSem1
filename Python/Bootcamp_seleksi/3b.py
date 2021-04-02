'''
3.b. Seorang kepala sekolah di sebuah Sekolah Menengah Atas pada provinsi 28
ingin meningkatkan status akreditasinya, diketahui sekolah ini masih menerapkan
kurikulum KTSP sebagai standar pengajarannya. Apa saran yang dapat anda berikan
kepada kepala sekolah untuk dapat meningkatkan akreditasi sekolahnya?
(insight yang diberikan bisa dalam bentuk visualisasi atau deskripsi dari
saran yang anda berikan)

Parameter penilaian :

Kejelasan dari breakdown masalah yang akan diselesaikan
Solusi yang diberikan memiliki alasan yang jelas (Data-driven solution):
Solusi yang diberikan berdasarkan analisis data (boleh juga data eksternal), atau
Solusi tidak secara langsung berdasarkan analisis data, namun dapat diketahui
cara-cara mendapatkan solusi bila ada suatu data

'''

#template awal
import pandas as pd
import numpy as np
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")

#hapus data yang bukan SMA
df.drop(df[ df['bentuk'] != 'SMA'].index , inplace=True)

#algoritma
print('akreditasi keseluruhan SMA')
print(df.groupby(['kurikulum']).mean().loc[:,'akreditasi'])

#hapus data dengan provinsi bukan 28
df.drop(df[ df['provinsi'] == 28].index , inplace=True)
print('\nakreditasi provinsi 28')
print(df.groupby(['kurikulum']).mean().loc[:,'akreditasi'])

print('Dari data tersebut diketahui bahwa seluruh SMA di 34 provinsi di Indonesia'
     ' menggunakan kurikulum KTSP sehingga tidak dapat diambil kesimpulan apakah'
      ' penggunaan kurikulum lain akan memperbaiki akreditasi. Tidak diketahui juga apakah'
      ' ada kurikulum lain selain KTSP sehingga kurikulum KTSP bukanlah sebuah masalah.'
     ' Rata-rata akreditasi sekolah di provinsi 28 juga hanya sedikit berbeda dengan'
     ' rata-rata provinsi secara nasional')


#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
df = pd.read_csv("D:\\data_pandas\\data_sekolah.csv")
#hapus data yang bukan SMA
df.drop(df[ df['bentuk'] != 'SMA'].index , inplace=True)
df.drop(df[ df['provinsi'] != 28].index , inplace=True)

print(df.groupby(['status']).mean().loc[:,'akreditasi'])
print('Diketahui rata-rata SMA negri memiliki rata-rata akreditasi yang'
     ' lebih baik dibandingkan dengan SMA swasta di provinsi 28.\n')

print(df.groupby(['status']).mean().loc[:,'guru_status_pns':'guru_sertifikasi_sudah'])

print('dari seluruh data, perbedaan paling signifikan antara SMA Negri dengan akreditasi'
     ' lebih baik dibandingkan dengan SMA Swasta dengan akreditasi lebih rendah terdapat'
     ' di banyak guru. Dapat dilihat bahwa jumlah guru cukup mempengaruhi akreditasi.'
     ' Sehingga jika ingin memperbaiki akreditasi sekolah, maka harus menambah jumlah guru.')