#NIM/Nama  : 16520237/Bryan Bernigen
#Tanggal   : 4 November 2020
#Deskripsi : FPB

#kamus
#bil1 : integer (bilangan ke-1)
#bil2 : integer (bilangan ke-2)
#bil3 : integer (bilangan ke-3)
#bil4 : integer (bilangan ke-4)
#bilmax : integer (nilai maximum dari ke-4 bilangan)
#fpb : integer (FPB keempat bilangan)

#kamus
#input dari user
bil1=int(input('Masukkan bilangan ke-1 :'))
bil2=int(input('Masukkan bilangan ke-2 :'))
bil3=int(input('Masukkan bilangan ke-3 :'))
bil4=int(input('Masukkan bilangan ke-4 :'))

#nilai max keempat bilangan
bilmax=max(bil1,bil2,bil3,bil4)

#menentukan nilai FPB
fpb=1

#algoritma
#keempat bilangan akan dibagi 1,2,3 dst sampai bilmax
#jika keempat bilangan memiliki hasil bagi=0,
#angka tersebut akan di anggap sebagi FPBnya
#jika ada yang lebih besar, maka yang lebih besar akan dianggap sebagai FPBnya
for i in range (bilmax):
    i=i+1
    if bil1%i==0 and bil2%i==0 and bil3%i==0 and bil4%i==0:
        fpb=i
    else:
        fpb=fpb
print('FPB keempat bilangan adalah',fpb)
