def toko ():
    print('Kode Barang  |   Nama    ')
    garis()
    print('bk           |   Buku    ')
    print('kp           |   Kopi    ')
    print('sb           |   Sabun   ')
    print('sp           |   Sampoo  ')
    print('br           |   Beras   ')
    print('ec           |   Es Cream')
    print('bj           |   Baju    ')

def customer():
    nama = str(input('Nama Pembeli      : '))
    return nama

def inputan_toko():
    kode = input('Pilih Kode Barang : ')
    return kode

def get_jumlah_pembelian():
    merek = input('pilih merek barang :')
    jumlah = int(input('jumlah Barang yang dibeli  : '))
    return merek,jumlah

def sub_menu(kode):
    if kode == 'bk':
        print('  Merek  |   Harga   |   Stok')
        garis()
        print('SIDU     |   5.000   |     15')
        print('BOOK     |   3.500   |     20')
        print('SINAR MAS|   4.000   |     25')
        print('GLOBE    |   4.500   |     30')
        garis()
    elif kode == 'kp':
        print('     Merek       |   Harga    |   Stok')
        garis()
        print('ABC              |   5.000    |    100')
        print('KAPAL API        |   10.000   |     85')
        print('LUWAK WHITE COFFE|   15.000   |     90')
        print('CAPPUCINO        |   20.000   |     66')
        garis()
    elif kode == 'sb':
        print('  Merek  |   Harga   |   Stok')
        garis()
        print('DETTOL   |  10.000   |    200')
        print('NUVO     |   9.000   |    155')
        print('GIV      |   8.500   |    114')
        print('CITRA    |   6.000   |    102')
        garis()
    elif kode == 'sp':
        print('  Merek          |   Harga   |   Stok')
        garis()
        print('PANTENE          |   5.000   |     66')
        print('CLEAR            |   3.500   |    100')
        print('DOVE             |   4.000   |    108')
        print('HEAD & SHOULDERS |   4.500   |    150')
        garis()
    elif kode == 'br':
        print('  Merek     |   Harga    |   Stok')
        garis()
        print('MAKNYUS     |   75.000   |     20')
        print('PANDA WANGI |   60.000   |     30')
        print('PUTRI MAS   |   55.000   |     25')
        print('PULLEN      |   90.000   |     10')
        garis()
    elif kode == 'ec':
        print('  Merek  |   Harga   |   Stok')
        garis()
        print('CAMPINA  |   15.000  |     33')
        print('DIAMOND  |   20.500  |     15')
        print('MAGNUM   |   30.000  |     14')
        print('AICE     |   7.500   |      9')
        garis()
    elif kode == 'bj':
        print('  Merek  |   Harga     |   Stok')
        garis()
        print('KEMEJA   |   200.000   |     15')
        print('JACKET   |   300.000   |      9')
        print('SWEETER  |   250.000   |     22')
        print('KAOS     |   155.000   |     23') 
        garis()


def get_item(merek):
    item   = []
    if merek == 'SIDU':
        item.append('SIDU')
        harga = 5000
        stok = 15
    elif merek == 'BOOK':
        item.append('BOOK')
        harga = 5000
        stok = 15
    elif merek == 'SINAR MAS':
        item.append('SINAR MAS')
        harga = 5000
        stok = 15
    elif merek == 'GLOBE':
        item.append('GLOBE')
        harga = 5000
        stok = 15  

    elif merek == 'ABC':
        item.append('ABC')
        harga = 5000
        stok = 100
    elif merek == 'KAPAL API':
        item.append('KAPAL API')
        harga = 10000
        stok = 85
    elif merek == 'LUWAK WHITE COFFE':
        item.append('LUWAK WHITE COFFE')
        harga = 15000
        stok = 90
    elif merek == 'CAPPUCINO':
        item.append('CAPPUCINO')
        harga = 20000
        stok = 66 

    elif merek == 'DETTOL':
        item.append('DETTOL')
        harga = 10000
        stok = 200
    elif merek == 'NUVO':
        item.append('NUVO')
        harga = 9000
        stok = 155
    elif merek == 'GIV':
        item.append('GIV')
        harga = 8500
        stok = 114
    elif merek == 'CITRA':
        item.append('CITRA')
        harga = 6000
        stok = 102        
    
    elif merek == 'PANTENE':
        item.append('PANTENE')
        harga = 5000
        stok = 66
    elif merek == 'CLEAR':
        item.append('CLEAR')
        harga = 5000
        stok = 100
    elif merek == 'DOVE':
        item.append('DOVE')
        harga = 4000
        stok = 108
    elif merek == 'HEAD & SHOULDERS':
        item.append('HEAD & SHOULDERS')
        harga = 4500
        stok = 150       

    elif merek == 'MAKNYUS':
        item.append('MAKNYUS')
        harga = 75000
        stok = 20
    elif merek == 'PANDA WANGI':
        item.append('PANDA WANGI')
        harga = 60000
        stok = 30
    elif merek == 'PUTRI MAS':
        item.append('PUTRI MAS')
        harga = 55000
        stok = 25
    elif merek == 'PULLEN':
        item.append('PULLEN')
        harga = 90000
        stok = 10        

    elif merek == 'CAMPINA':
        item.append('CAMPINA')
        harga = 15000
        stok = 33
    elif merek == 'DIAMOND':
        item.append('DIAMOND')
        harga = 20500
        stok = 15
    elif merek == 'MAGNUM':
        item.append('MAGNUM')
        harga = 30000
        stok = 14
    elif merek == 'AICE':
        item.append('AICE')
        harga = 7500
        stok = 9        

    elif merek == 'KEMEJA':
        item.append('KEMEJA')
        harga = 200000
        stok = 15
    elif merek == 'JACKET':
        item.append('JACKET')
        harga = 300000
        stok = 9
    elif merek == 'SWEETER':
        item.append('SWEETER')
        harga = 250000
        stok = 22
    elif merek == 'KAOS':
        item.append('KAOS')
        harga = 155000
        stok = 23
    else:
        item.append('Item tidak terdaftar')        
        
    return item,harga,stok
    
def get_sisa_stok(stok,jumlah):
    sisa = int(stok - jumlah)
    if jumlah > stok:
        sisa = 'Melebihi Stok Barang'
    return sisa

def get_rumus(jumlah,harga):
    hasil = int (jumlah * harga)
    return hasil

def diskon_toko(hasil):
    if hasil >= 500000:
        diskon = hasil * 0.5
    elif hasil >= 1000000:
        diskon = hasil * 0.10
    else:
        diskon = 0
    return diskon

def pajak_toko(hasil):
    pajak = hasil * 0.02
    return pajak

def sub_total(hasil,pajak,diskon):
    total = hasil - pajak - diskon
    return total

def lebih(uang,total):
    hasil = uang - total
    return hasil

def garis():
    print('------------------------------')