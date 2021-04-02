#program fibonnaci

#kamus
#input user
a1=int(input('ke-1: '))
a2=int(input('ke-2: '))
a3=int(input('ke-3: '))
n=int(input('angka ke-n: '))
#inisialisasi array
arr=[0 for i in range (n)]
arr[0]=a1
arr[1]=a2
arr[2]=a3

#algoritma
#magisi array sampai array ke-n
for i in range(n-3):
    arr[i+3]+=arr[i]+arr[i+1]+arr[i+2]
#menampilkan ke layar
print(arr)
print(arr[n-1])