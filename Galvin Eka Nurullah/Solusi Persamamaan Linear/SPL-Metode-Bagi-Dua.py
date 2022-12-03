# Mendefinisikan fungsi
def f(x):
    return x**3-5*x-9

# Implementasi Metode Bagi Dua
def bisection(x0,x1,e):
    i = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (i, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        i += 1
        condition = abs(f(x2)) > e

    print('\nAkar yang ditemukan adalah : %0.8f' % x2)


x0 = input('Masukan Tebakan Pertama: ')
x1 = input('Masukan Tebakan Kedua: ')
e = input('Tolerable Kesalahan / Galat: ')

# Konversi variabel input ke bentuk double
x0 = float(x0)
x1 = float(x1)
e = float(e)


# Proses pengecekan dari nilai tebakan yang telah dimasukan
if f(x0) * f(x1) > 0.0:
    print('Tebakan yang dimasukan tidak memiliki nilai akar.')
    print('Coba lagi dengan nilai tebakan yang berbeda!')
else:
    bisection(x0,x1,e)

