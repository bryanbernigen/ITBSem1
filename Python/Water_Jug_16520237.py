#NIM/Nama : 16520237/Bryan Bernigen
#Tantangan Water Jug

#kamus
#ember_1,ember_2,_ember_tambahan:integer
#coba_lagi, bantuan: string

import os #untuk warna??? entah kenapa ketika dihapus warnanya tidak keluar
import pyautogui #untuk clear screen.

#definisikan start sebagai awal mulai sistem
def start():
    ember_1 = 0
    ember_2 = 0
    cara = 0
    while ember_2 != 4:
        pyautogui.hotkey('ctrl','l') #untuk clear screen. Sesuaikan dengan command hotkeys clear screen
                                     #hot keys pada system saya adalah control + l
        os.system('cls') #mengeluarkan warna?? aneh juga commandnya saya pikir untuk clear screen
        cara = cara + 1
        print('-------------------------------------------------')
        print('-------------------------------------------------')
        print('Tantangan membuat salah satu ember berisi 4 liter')
        print('Ember 1 -> 3 liter dan Ember 2 -> 5 liter')
        print('Kondisi Saat Ini:')
        print('Ember 1:\033[1;33m', ember_1, '\033[0mliter')
        print('Ember 2:\033[1;33m', ember_2, '\033[0mliter')
        print('Langkah-langkah:')
        print('1)Isi ember 1                       Isi ember 2(2')
        print('3)Kosongkan ember 1           Kosongkan ember 2(4')
        print('5)tuang isi ember 1-->2   tuang isi ember 2-->1(6')
        if cara == 16 or cara == 26  or cara >=31 : #jika pengguna masih belum menyelesaikan problem setelah beberapa langkah
            bantuan=input('\033[1;32mApakah Anda membutuhkan bantuan?\033[0m (y/n): ')
            if bantuan=='y':
                print('\033[1;31mHafalkan!\033[0m')
                print('3,4,2,6,3,6,2,6')
                print('Selamat Mencoba')
        langkah = int(input('Pilih langkah yang akan dilakukan: '))
        if langkah == 1:
            ember_1 = 3
        elif langkah == 2:
            ember_2 = 5
        elif langkah == 3:
            ember_1 = 0
        elif langkah == 4:
            ember_2 = 0
        elif langkah == 5:
            ember_tambahan = ember_1 + ember_2
            if ember_tambahan <= 5:
                ember_1 = 0
                ember_2 = ember_2 + ember_1
            else:  # ember_tambahan>5
                ember_2 = 5
                ember_1 = ember_tambahan - 5
        elif langkah == 6:
            ember_tambahan = ember_1 + ember_2
            if ember_tambahan <= 3:
                ember_2 = 0
                ember_1 = ember_tambahan
            else:  # ember_tambahan>3
                ember_1 = 3
                ember_2 = ember_tambahan - 3
        else:  # langkah!= 1/2/3/4/5/6
            print('\033[1;31mLangkah Tidak Dikenali!\033[0m')
    print('-------------------------------------------------')
    print('-------------------------------------------------')
    print('Kondisi Saat Ini:')
    print('Ember 1:\033[1;33m', ember_1, '\033[0mliter')
    print('Ember 2:\033[1;33m', ember_2, '\033[0mliter')
    print('\033[1;32mSelamat Anda Telah Berhasil Menyelesaikan Tantangan!\033[0m')
    if cara == 6:
        print('Anda menggunakan\033[1;32m', cara, '\033[0mlangkah')
        print('\033[1;32mAnda berhasil menggunakan cara yang paling efektif!\033[0m')
    else: #jika pengguna menggunakan >6 langkah maka akan ditanya apakah ingin mencoba lagi
        print('Anda menggunakan\033[1;31m', cara, '\033[0mlangkah')
        print('Rekor terbaik adalah\033[1;32m 6 \033[0mlangkah')
        coba_lagi = input('Apakah Anda ingin mencoba lagi? (y/n) :')
        if coba_lagi == 'y':
            start()
        else:
            exit('Terima Kasih telah mencoba tantangan kami')
#mulai sistem
start()





