# NIM/Nama   : 16520237/ Bryan Bernigen
# Tanggal    : 21 Oktober 2020
# Deskripsi  : Membagi permen kepad 4 anak secara adil

#kamus
#permen_anak_1,permen_anak_2,permen_anak_3,permen_anak_4,jumlah_permen,jumlah_permen_per_anak : integer

permen_anak_1=int(input('Jumlah Permen Anak Ke-1 :'))
permen_anak_2=int(input('Jumlah Permen Anak Ke-2 :'))
permen_anak_3=int(input('Jumlah Permen Anak Ke-3 :'))
permen_anak_4=int(input('Jumlah Permen Anak Ke-4 :'))
jumlah_permen=permen_anak_1+permen_anak_2+permen_anak_3+permen_anak_4
print('Jumlah Permen=',jumlah_permen)
if jumlah_permen%4==1:
    jumlah_permen = jumlah_permen - 2
    jumlah_permen_per_anak = jumlah_permen / 4
    jumlah_permen_per_anak=int(jumlah_permen_per_anak)
    print('Setiap anak mendapat', jumlah_permen_per_anak, 'permen')
elif jumlah_permen%4==2:
    jumlah_permen = jumlah_permen - 2
    jumlah_permen_per_anak = jumlah_permen / 4
    jumlah_permen_per_anak = int(jumlah_permen_per_anak)
    print('Setiap anak mendapat', jumlah_permen_per_anak, 'permen')
elif jumlah_permen%4==3:
    jumlah_permen = jumlah_permen - 3
    jumlah_permen_per_anak = jumlah_permen / 4
    jumlah_permen_per_anak = int(jumlah_permen_per_anak)
    print('Setiap anak mendapat', jumlah_permen_per_anak, 'permen')
else:
    jumlah_permen_per_anak = jumlah_permen / 4
    jumlah_permen_per_anak = int(jumlah_permen_per_anak)
    print('Setiap anak mendapat', jumlah_permen_per_anak, 'permen')