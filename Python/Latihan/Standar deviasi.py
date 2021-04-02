# Program StandarDeviasi
# menghitung standar deviasi data tinggi sample mahasiswa sebanyak 50 orang

# Kamus
# n, i, x, sum : integer
# s, mean, s1 : float
# array : array of integer

#kamus
n=50
sum1=0
sum2=0
avg=0
std=0
#inisialisasi array
array=[0 for i in range(n)]
#input user:
for i in range (n):
    array[i]=int(input('Masukkan data ke-'+str(i+1)+': '))
    sum1 = sum1 + array[i]

#rata-rata
avg=sum1/n

#jumlah (x-xaverage)^2
for i in range (n):
    array[i]= (array[i]-avg)**2
    sum2=array[i]+sum2

#standar deviasi
std=(1/(n-1) * sum2)**0.5

print('Standar Deviasi: ',std)