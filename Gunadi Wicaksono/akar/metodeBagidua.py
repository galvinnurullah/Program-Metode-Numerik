# Mendefinisikan fungsi
def f(x):
    return x**3-5*x-9

# Implementasi Metode Bagi Dua
def bagiDua(x0,x1,galat):
    i = 1
    print('\n\n#################### PROGRAM SPL METODE BAGI DUA ####################')
    kondisi = True
    while kondisi:
        x2 = (x0 + x1)/2
        print('Iterasi ke-%d, x2 = %0.6f dan f(x2) = %0.6f' % (i, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        i += 1
        kondisi = abs(f(x2)) > galat

    print('\nAkar yang ditemukan adalah : %0.8f' % x2)


x0 = input('Masukan Tebakan Pertama: ')
x1 = input('Masukan Tebakan Kedua: ')
galat = input('Tolerable Kesalahan: ')

# Konversi variabel input ke bentuk double
x0 = float(x0)
x1 = float(x1)
galat = float(galat)


# Proses pengecekan dari nilai tebakan yang telah dimasukan
if f(x0) * f(x1) > 0.0:
    print('Tebakan yang dimasukan tidak memiliki nilai akar atau memiliki akar kembar.')
    print('Coba lagi dengan nilai tebakan yang berbeda!')
else:
    bagiDua(x0,x1,galat)
