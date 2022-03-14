def tiket():
    print('Kode Tiket   |   Tujuan      |   Harga Tiket ')
    print('001          |   Bali        |   1.000.000 ')
    print('002          |   Jakarta     |   900.000 ')
    print('003          |   Japan       |   1.500.000 ')
    print('004          |   Malaysia    |   1.250.000 ')
    print('005          |   Russia      |   2.000.000 ')
    print('006          |   Cina        |   1.500.000 ')
    print('007          |   US          |   2.000.000 ')
    print('008          |   Australia   |   1.700.000 ')
    print('009          |   Lebanon     |   1.600.000 ')
    print('010          |   Korea       |   1.400.000 ')
    garis()

def masukan ():
    nama = str(input('Nama Pembeli : '))
    nomor = int(input('Nomor Handphone : '))
    asal = str(input('Asal Kota : '))
    kode = input('Kode Tujuan Penerbangan : ')
    jumlah = int(input('Jumlah Beli / Jumlah Pemesanan :'))
    return nama,nomor,asal,kode,jumlah  

def pesan(kode):
    tujuan = []
    if kode == '001':
        tujuan.append ('BALI')
        harga = 1000000
    elif kode == '002':
        tujuan.append ('JAKARTA')
        harga = 900000
    elif kode == '003':
        tujuan.append ('JAPAN')
        harga = 1500000
    elif kode == '004':
        tujuan.append ('MALAYSIA')
        harga = 1250000
    elif kode == '005':
        tujuan.append ('RUSSIA')
        harga = 2000000
    elif kode == '006':
        tujuan.append ('CINA')
        harga = 1500000
    elif kode == '007':
        tujuan.append ('US')
        harga = 2000000
    elif kode == '008':
        tujuan.append ('AUSTRALIA')
        harga = 1700000
    elif kode == '009':
        tujuan.append ('LEBANON')
        harga = 1600000
    elif kode == '010':
        tujuan.append ('KOREA')
        harga = 1400000
    else:
        tujuan.append ('Kode Salah')
    return tujuan,harga

def get_hasil(jumlah,harga):
    hasil = jumlah * harga
    return hasil

def get_diskon(jumlah,hasil):
    if jumlah == 2:
        diskon = hasil * 0.1
    elif jumlah == 3:
        diskon = hasil * 0.15
    elif jumlah == 4:
        diskon = hasil * 0.3
    elif jumlah <= 5 :
        diskon = hasil * 0.5
    else:
        diskon = 0
    return diskon

def get_pajak (hasil):
    pajak = hasil * 0.03
    return pajak 

def get_total (hasil,pajak,diskon):
    total = hasil - pajak - diskon
    return total

def get_kembalian(uang,total):
    kembalian = uang - total
    return kembalian

def garis():
    print('------------------------------')

