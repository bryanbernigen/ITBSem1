#PemasukkanKartu
print('Selamat datang di ATM BCA ')
print('Masukkan Kartu dan PIN Anda')
pin=int(input("PIN: "))
pin=str(pin)
while len(pin)!=6:
    print('\033[1;31mPIN harus 6 angka tanpa karakter lainnya\033[0m')
    pin = int(input("masukkan ulang PIN: "))
    pin=str(pin)


def menuF_pin_baru_tidak_6_digit():
        print('--------------------------------------')
        print('PIN harus 6 digit')
        print('Masukkan PIN: 0 untuk membatalkan penggantian PIN')
def menuF_pin_baru_sama_dengan_pin_lama():
    print('----------------------------------------')
    print('PIN baru tidak boleh sama dengan PIN lama')
    print('Masukkan PIN: 0 untuk membatalkan penggantian PIN')
def menuF():
    print('Masukkan PIN: 0 untuk membatalkan penggantian PIN')
    pin_lama = input('Masukkan PIN lama Anda: ')
    if pin_lama == '0':
        start()
    elif pin_lama == pin:
        print('-------------------------------------------------')
        print('Masukkan PIN: 0 untuk membatalkan penggantian PIN')
        pin_baru = int(input('Masukkan PIN baru Anda: '))
        pin_baru = str(pin_baru)
        if pin_baru == '0':
            start()
        while len(pin_baru) != 6:
            menuF_pin_baru_tidak_6_digit()
            pin_baru = int(input('Masukkan PIN baru Anda: '))
            pin_baru = str(pin_baru)
            if pin_baru == '0':
                exit('a')
        while pin_baru == pin_lama:
            menuF_pin_baru_sama_dengan_pin_lama()
            pin_baru = int(input('Masukkan PIN baru Anda: '))
            pin_baru = str(pin_baru)
            if pin_baru == '0':
                exit('a')
        konfirmasi_pin_baru = input('Konfirmasi PIN baru Anda: ')
        if konfirmasi_pin_baru == '0':
            start()
        elif pin_baru != konfirmasi_pin_baru:
            print('Konfirmasi PIN baru Anda gagal')
            menuF()
        else:
            print('---------------------------------')
            print('PIN Anda berhasil diubah')
            konfirmasi_pin_baru = str(konfirmasi_pin_baru)
            print('PIN baru Anda adalah ' + konfirmasi_pin_baru)
            print('Mohon jaga kerahasian PIN Anda')
            konfirmasi_pin_baru = int(konfirmasi_pin_baru)
            pin == konfirmasi_pin_baru
            print('-------------------------------------------------------')
            print('   Apakah ada yang hal lain yang ingin Anda lakukan?   ')
            print('A)Ya, kembali ke menu     Tidak, selesaikan transaksi(B')
            kembali_ke_menu = input()
            if kembali_ke_menu == 'A' or kembali_ke_menu == 'a':
                start()
            else:
                exit('Terima kasih telah menggunakan jasa kami')
    elif pin_lama != pin:
        print('---------------------------------------')
        print('Maaf PIN Anda salah')
        menuF()
def start():
    # MenuAwal
    print('  Pilih Transkasi Yang Anda Ingin Lakukan  ')
    print('-------------------------------------------')
    print('A)Informasi                    Pembayaran(E')
    print('')
    print('B)Penarikan Tunai               Ganti Pin(F')
    print('')
    print('C)Transfer                          Flazz(G')
    print('')
    print('D)Voucher Isi Ulang                Keluar(H')
    print('-------------------------------------------')
    layanan = input('Pilih layanan yang Anda inginkan: ')
    # menuA
    if layanan == 'A' or layanan == 'a':
        cek_pin = input('Masukkan PIN Anda: ')
        if cek_pin == pin:
            print('Informasi Pengguna Kartu')
            print('Nama  : ********')
            print('PIN   : ' + pin)
            print('Saldo : Rp10000000')
            print('-------------------------------------------------')
            print('Apakah ada yang hal lain yang ingin Anda lakukan?')
            print('A)Ya, kembali ke menu    Tidak, selesaikan sesi(B')
            kembali_ke_menu= input()
            if kembali_ke_menu== 'A' or kembali_ke_menu == 'a':
                start()
            else:
                exit('Terima kasih telah menggunakan jasa kami')
        else:
            exit('Mohon maaf PIN Anda salah!')
    # menuB
    elif layanan == 'B' or layanan == 'b':
        print('-----------------------------------------')
        print('Penarikan Tunai')
        print('Jumlah \033[1;32mminumun\033[0m tarikan adalah \033[1;32mRp20000\033[0m')
        print('Masukkan Rp0 untuk membatalkan transaksi')
        print('Saldo Anda Rp10000000')
        jumlah_tarikan = int(input('Masukkan jumlah yang akan ditarik: Rp'))
        if jumlah_tarikan == 0:
            exit('Terima kasih telah menggunakan layanan kami')
        while jumlah_tarikan > 10000000:
            print('Mohon maaf jumlah tarikan Anda \033[1;31mmelebihi saldo\033[0m Anda')
            print('--------------------------------------------------')
            print('Jumlah \033[1;32mminumun\033[0m tarikan adalah \033[1;32mRp20000\033[0m')
            print('Masukkan Rp0 untuk membatalkan transaksi')
            print('Saldo Anda Rp10000000')
            jumlah_tarikan = int(input('Masukkan jumlah yang akan ditarik: Rp'))
            if jumlah_tarikan == 0:
                exit('Terima kasih telah menggunakan layanan kami')
        while jumlah_tarikan < 20000:
            print('Mohon maaf jumlah tarikan minimum adalah Rp20000')
            print('--------------------------------------------------')
            print('Jumlah \033[1;32mminumun\033[0m tarikan adalah \033[1;32mRp20000\033[0m')
            print('Masukkan Rp0 untuk membatalkan transaksi')
            print('Saldo Anda Rp10000000')
            jumlah_tarikan = int(input('Masukkan jumlah yang akan ditarik: Rp'))
            if jumlah_tarikan == 0:
                exit('Terima kasih telah menggunakan layanan kami')
        else:
            jumlah_tarikan = str(jumlah_tarikan)
            print('--------------------------------------------')
            print('Anda akan menarik tunai sebesar \033[1;34mRp' + jumlah_tarikan + '\033[0m')
            print('Apakah jumlah tersebut sudah benar?')
            print('A)Sudah                           Belum(B')
            print('C)Batalkan Transaksi                     ')
            verifikasi_jumlah_tarikan = str(input())
            if verifikasi_jumlah_tarikan == 'c' or verifikasi_jumlah_tarikan == 'C':
                exit('Terima kasih telah menggunakan jasa kami')
            else:
                while verifikasi_jumlah_tarikan != 'a' and verifikasi_jumlah_tarikan != 'A':
                    print('-------------------------------------')
                    print('Jumlah \033[1;32mminumun\033[0m tarikan adalah \033[1;32mRp20000\033[0m')
                    print('Masukkan Rp0 untuk membatalkan transaksi')
                    print('Saldo Anda Rp10000000')
                    jumlah_tarikan = int(input('Masukkan jumlah yang akan ditarik: Rp'))
                    if jumlah_tarikan == 0:
                        exit('Terima kasih telah menggunakan layanan kami')
                    while jumlah_tarikan > 10000000:
                        print('Mohon maaf jumlah tarikan Anda \033[1;32mmelebihi saldo\033[0m Anda')
                        print('--------------------------------------------------')
                        print('Jumlah \033[1;32mminumun\033[0m tarikan adalah \033[1;32mRp20000\033[0m')
                        print('Masukkan Rp0 untuk membatalkan transaksi')
                        print('Saldo Anda Rp10000000')
                        jumlah_tarikan = int(input('Masukkan jumlah yang akan ditarik: Rp'))
                        if jumlah_tarikan == 0:
                            exit('Terima kasih telah menggunakan layanan kami')
                    while jumlah_tarikan < 20000:
                        print('mohon maaf jumlah tarikan minimum adalah Rp20000')
                        print('--------------------------------------------------')
                        print('Jumlah \033[1;32mminumun\033[0m tarikan adalah \033[1;32mRp20000\033[0m')
                        print('Masukkan Rp0 untuk membatalkan transaksi')
                        print('Saldo Anda Rp10000000')
                        jumlah_tarikan = int(input('Masukkan jumlah yang akan ditarik: Rp'))
                        if jumlah_tarikan == 0:
                            exit('Terima kasih telah menggunakan layanan kami')
                    else:
                        jumlah_tarikan = str(jumlah_tarikan)
                        print('--------------------------------------------')
                        print('Anda akan menarik tunai sebesar \033[1;34mRp' + jumlah_tarikan + '\033[0m')
                        print('Apakah jumlah tersebut sudah benar?')
                        print('A)Sudah                           Belum(B')
                        print('C)Batalkan Transaksi                     ')
                        verifikasi_jumlah_tarikan = str(input())
                        if verifikasi_jumlah_tarikan == 'c' or verifikasi_jumlah_tarikan == 'C':
                            exit('Terima kasih telah menggunakan jasa kami')
                else:
                    cek_pin = input('Masukkan PIN Anda: ')
                    if cek_pin == pin:
                        jumlah_tarikan = str(jumlah_tarikan)
                        print('uang sebesar \033[1;32mRp' + jumlah_tarikan + '\033[0m berhasil ditarik')
                        jumlah_tarikan = int(jumlah_tarikan)
                        sisa = 10000000 - jumlah_tarikan
                        sisa = str(sisa)
                        print('sisa saldo anda adalah sebesar \033[1;32mRp' + sisa + '\033[0m')
                        print('Terima kasih telah menggunakan jasa kami')
                        print('-------------------------------------------------')
                        print('   Apakah ada yang hal lain yang ingin Anda lakukan?   ')
                        print('A)Ya, kembali ke menu     Tidak, selesaikan transaksi(B')
                        kembali_ke_menu = input()
                        if kembali_ke_menu == 'A' or kembali_ke_menu == 'a':
                            start()
                        else:
                            exit('Terima kasih telah menggunakan jasa kami')
                    else:
                        exit('Mohon maaf PIN Anda salah')
    # menuC
    elif layanan == 'C' or layanan == 'c':
        print('     Pilih Bank yang akan di transfer     ')
        print('------------------------------------------')
        print('A)BCA                            Mandiri(D')
        print('')
        print('B)BNI                            Permata(E')
        print('')
        print('C)BRI                            Kembali(F')
        print('------------------------------------------')
        bank_pilihan = input('Bank yang akan dituju: ')
        if bank_pilihan == 'f' or bank_pilihan == 'F':
            start()
        elif bank_pilihan == 'A' or bank_pilihan == 'a':
            nama_bank = 'BCA'
        elif bank_pilihan == 'B' or bank_pilihan == 'b':
            nama_bank = 'BNI'
        elif bank_pilihan == 'C' or bank_pilihan == 'c':
            nama_bank = 'BRI'
        elif bank_pilihan == 'D' or bank_pilihan == 'd':
            nama_bank = 'Mandiri'
        elif bank_pilihan == 'E' or bank_pilihan == 'e':
            nama_bank = 'Permata'
        else:
            exit('Error')
        no_rek = int(input('Masukkan nomor rekening yang akan dituju: '))
        no_rek = str(no_rek)
        print('Anda akan melakukan transfer ke ' + nama_bank + ' dengan nomor rekening ' + no_rek)
        print('Apakah bank tujuan dan nomor rekening sudah benar?')
        print('A)Sudah                           Belum(B')
        print('C)Batalkan Transaksi')
        konfirmasi_no_rek = input()
        if konfirmasi_no_rek == 'C' or konfirmasi_no_rek == 'c':
            exit('Terima kasih telah menggunkan jasa kami')
        while konfirmasi_no_rek != 'a' and konfirmasi_no_rek != 'A':
            print('     Pilih Bank yang akan di transfer     ')
            print('------------------------------------------')
            print('A)BCA                            Mandiri(D')
            print('')
            print('B)BNI                            Permata(E')
            print('')
            print('C)BRI                            Kembali(F')
            print('------------------------------------------')
            bank_pilihan = input('Bank yang akan dituju: ')
            if bank_pilihan == 'f' or bank_pilihan == 'F':
                start()
            elif bank_pilihan == 'A' or bank_pilihan == 'a':
                nama_bank = 'BCA'
            elif bank_pilihan == 'B' or bank_pilihan == 'b':
                nama_bank = 'BNI'
            elif bank_pilihan == 'C' or bank_pilihan == 'c':
                nama_bank = 'BRI'
            elif bank_pilihan == 'D' or bank_pilihan == 'd':
                nama_bank = 'Mandiri'
            elif bank_pilihan == 'E' or bank_pilihan == 'e':
                nama_bank = 'Permata'
            else:
                exit('Error')
            no_rek = int(input('Masukkan nomor rekening yang akan dituju: '))
            no_rek = str(no_rek)
            no_rek = str(no_rek)
            print('Anda akan melakukan transfer ke ' + nama_bank + ' dengan nomor rekening ' + no_rek)
            print('Apakah bank tujuan dan nomor rekening sudah benar?')
            print('A)Sudah                           Belum(B')
            print('C)Batalkan Transaksi')
            konfirmasi_no_rek = input()
            if konfirmasi_no_rek == 'C' or konfirmasi_no_rek == 'c':
                exit('Terima kasih telah menggunkan jasa kami')
        else:
            print('Minimum jumlah yang akan di transfer adalah Rp20000')
            print('Masukkan Rp0 untuk membatalkan transfer')
            jumlah_transfer = int(input('Masukkan jumlah yang akan ditransfer: Rp'))
            if jumlah_transfer == 0:
                exit('Terima kasih telah menggunakan jasa kami')
            while jumlah_transfer > 10000000:
                print('Mohon maaf jumlah transfer Anda melebihi salo Anda')
                print('--------------------------------------------------')
                print('Masukkan Rp0 untuk membatalkan transfer')
                print('Minimum jumlah yang akan di transfer adalah Rp20000')
                jumlah_transfer = int(input('Masukkan jumlah yang akan ditransfer: Rp'))
                if jumlah_transfer == 0:
                    exit('Terima kasih telah menggunakan jasa kami')
            while jumlah_transfer < 20000:
                print('Mohon maaf jumlah transfer minimum adalah Rp20000')
                print('-------------------------------------------------')
                print('Masukkan Rp0 untuk membatalkan transfer')
                print('Minimum jumlah yang akan di transfer adalah Rp20000')
                jumlah_transfer = int(input('Masukkan jumlah yang akan ditransfer: Rp'))
                if jumlah_transfer == 0:
                    exit('Terima kasih telah menggunakan jasa kami')
                jumlah_transfer = str(jumlah_transfer)
                print('Anda akan mentransfer uang sebesar Rp' + jumlah_transfer + ' ke rekening ' + no_rek)
                print('Apakah jumlah dan nomor rekeing yang akan ditransfer sudah benar?')
                print('A)Sudah                           Belum(B')
                print('C)Batalkan Transaksi')
                konfirmasi_transfer = input()
                if konfirmasi_transfer == 'C' or konfirmasi_transfer == 'c':
                    exit('Terima kasih telah menggunakan jasa kami')
                while konfirmasi_transfer != 'A' and konfirmasi_transfer != 'a':
                    print('-------------------------------------------------')
                    print('Minimum jumlah yang akan di transfer adalah Rp20000')
                    print('Masukkan Rp0 untuk membatalkan transfer')
                    jumlah_transfer = int(input('Masukkan jumlah yang akan ditransfer: Rp'))
                    if jumlah_transfer == 0:
                        exit('Terima kasih telah menggunakan jasa kami')
                    if jumlah_transfer > 10000000:
                        print('mohon maaf jumlah transfer Anda melebihi salo Anda')
                    elif jumlah_transfer < 20000:
                        print('mohon maaf jumlah transfer minimum adalah Rp20000')
                    else:
                        jumlah_transfer = str(jumlah_transfer)
                        print('Anda akan mentransfer uang sebesar Rp' + jumlah_transfer + ' ke rekening ' + no_rek)
                        print('Apakah jumlah dan nomor rekeing yang akan ditransfer sudah benar?')
                        print('A)Sudah                           Belum(B')
                        konfirmasi_transfer = input()
                        if konfirmasi_transfer == 'C' or konfirmasi_transfer == 'c':
                            exit('Terima kasih telah menggunakan jasa kami')
                if konfirmasi_transfer == 'a' or konfirmasi_transfer == 'A':
                    pin_verifikasi = input('masukkan PIN Anda :')
                    if pin_verifikasi == pin:
                        print('Transaksi Sukses!')
                        print('Uang sebesar ' + jumlah_transfer + ' telah terkirim ke rekening ' + no_rek)
                        print('Terima kasih telah menggunakan jasa kami')
                        print('-------------------------------------------------------')
                        print('   Apakah ada yang hal lain yang ingin Anda lakukan?   ')
                        print('A)Ya, kembali ke menu     Tidak, selesaikan transaksi(B')
                        kembali_ke_menu = input()
                        if kembali_ke_menu == 'A' or kembali_ke_menu == 'a':
                            start()
                        else:
                            exit('Terima kasih telah menggunakan jasa kami')
                    else:
                        exit('Mohon maaf PIN Anda salah')
    # menuD
    elif layanan == 'D' or layanan == 'd':
        print('Mohon maaf layanan masih dalam tahap pengembangan')
        exit('')
    # menuE
    elif layanan == 'E' or layanan == 'e':
        print('Mohon maaf layanan masih dalam tahap pengembangan')
        exit('Silahkan akses layanan melalui teller')
    # menuF
    elif layanan == 'F' or layanan == 'f':\
        menuF()
    # menuG
    elif layanan == 'G' or layanan == 'g':
        print('Mesin ATM ini belum dapat menerima Flazz')
        start()
    else:
        exit('Terima kasih telah menggunakan layanan kami')
start()