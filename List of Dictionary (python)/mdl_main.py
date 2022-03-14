
import mdl_toko as mdt
import mdl_tiket as mdk

def garis():
    print('------------------------------')

def menu():
    print('Menu :')
    print('1. Toko ')
    print('2. Pembelian Tiket')
    print('3. Keluar')
    garis()
    pilihan = int(input('pilih menu : '))
    return pilihan

def sub_menu():
    print('menu :')
    print('1. beli :')
    print('2. kembali :')
    garis()
    pilihan = int(input('pilih menu : '))
    return pilihan

def sub_menu_tiket():
    print('menu :')
    print('1. beli :')
    print('2. kembali :')
    garis()
    pilih = int(input('pilih menu : '))
    return pilih


def pilihan():
    pilih = int(input('Pilih Menu : '))
    return pilih

def garis():
    print('------------------------------')

def get_cetak_toko(nama,kode,item,jumlah,merek,harga,diskon,pajak,sisa_stok,total,uang,kembalian):
    garis()
    print('TOKO SERBAGUNA ')
    garis()
    print('Nama Pembeli         :{:^8}'.format(nama))
    print('Kode Barang          :{:^8}'.format(kode))
    print('Jenis Barang         :{}'.format(item[0]))
    print('Jumlah Pembelian     :{:^8}'.format(jumlah))
    garis()
    print('Merk Barang          :{:^8}'.format(merek))
    print('Harga Barang         :{:,}'.format(harga))
    print('Diskon               :{:,}'.format(diskon))
    print('Pajak Pemesanan      :{:,}'.format(pajak))
    print('Sisa Stok            :{}'.format(sisa_stok))
    garis()
    print('Pelunasan Pembayaran')
    print('Jumlah Bayar         :{:,}'.format(total))
    print('Masukan Pembayaran   :{:,}'.format(uang))
    garis()
    print('Uang Kembalian       :{:,}'.format(kembalian))
    garis()

def cetak (nama,nomor,asal,kode,tujuan,jumlah,harga,diskon,pajak,total,uang,kembalian):
    garis()
    print('{}'.format('AIR ASIA'))
    garis()
    print('Nama Pembeli         :{}'.format(nama))
    print('Nomor HandPhone      :{}'.format(nomor))
    print('Asal Kota            :{}'.format(asal))
    print('Kode Barang          :{}'.format(kode))
    print('Tujuan Penerbangan   :{}'.format(tujuan))
    print('Jumlah Pembelian     :{}'.format(jumlah))
    garis()
    print('Harga Tiket          :{:,}'.format(harga))
    print('Diskon               :{:,}'.format(diskon))
    print('Pajak Pemesanan      :{:,}'.format(pajak))
    garis()
    print('Pelunasan Pembayaran Tiket')
    print('Jumlah Bayar         :{:,}'.format(total))
    print('Masukan Pembayaran   :{:,}'.format(uang))
    garis()
    print('Uang Kembalian       :{:,}'.format(kembalian))
    garis()

def main_toko(pilihan):
    while pilihan != 2:
        mdt.toko()
        garis()
        pilihan = sub_menu()
        garis()
        if pilihan == 1:
            nama = mdt.customer()
            garis()
            kode = mdt.inputan_toko()
            garis()
            mdt.sub_menu(kode)
            merek,jumlah = mdt.get_jumlah_pembelian()
            item,harga,stok = mdt.get_item(merek)
            sisa_stok = mdt.get_sisa_stok(stok,jumlah)
            hasil = mdt.get_rumus(jumlah,harga)
            diskon = mdt.diskon_toko(hasil)
            pajak = mdt.pajak_toko(hasil)
            total = mdt.sub_total(hasil,pajak,diskon)
            garis()
            print('Total Pembelian : Rp' ,total)
            garis()
            uang = int(input('Masukan Uang Pembayaran : Rp. '))
            kembalian = mdt.lebih(uang,total)
            print()
            print()
            get_cetak_toko(nama,kode,item,jumlah,merek,harga,diskon,pajak,sisa_stok,total,uang,kembalian)
            garis()
            print()
            print()
    else:
        pilihan = 2

def main_tiket():
    pilih = 0
    while pilih != 2:
        mdk.tiket()
        pilih = sub_menu_tiket()
        if pilih == 1:
            garis()
            nama,nomor,asal,kode,jumlah = mdk.masukan()
            garis()
            tujuan,harga = mdk.pesan(kode)
            hasil = mdk.get_hasil(jumlah,harga)
            diskon = mdk.get_diskon(jumlah,hasil)
            pajak = mdk.get_pajak(hasil)
            total = mdk.get_total(hasil,pajak,diskon)
            print('Jumlah Pembayaran : Rp. {:,} '.format(total))
            garis()
            uang = int(input('Masukan Uang Pembayaran : Rp. '))
            kembalian = mdk.get_kembalian(uang,total)
            print()
            print()
            cetak(nama,nomor,asal,kode,tujuan,jumlah,harga,diskon,pajak,total,uang,kembalian)
            print()
            print()
        else:
            pilih = 2