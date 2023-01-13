# Mendefinisikan fungsi
def f(x):
    return x**3 - 2*x + 7

# Defining derivative of function
def g(x):
    return 3*x**2 - 2

# Implementing Newton Raphson Method

def newtonRaphson(x0,galat,jumlahIterasi):
    print('\n\n#################### PROGRAM SPL METODE NEWTON-RAPHSON ####################')
    langkah = 1
    tanda = 1
    kondisi = True
    while kondisi:
        if g(x0) == 0.0:
            print('Tidak bisa dibagi dengan 0!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iterasi ke-%d, x1 = %0.6f and f(x1) = %0.6f' % (langkah, x1, f(x1)))
        x0 = x1
        langkah += 1
        
        if langkah > jumlahIterasi:
            tanda = 0
            break
        
        kondisi = abs(f(x1)) > galat
    
    if tanda==1:
        print('\nAkar yang ditemukan adalah: %0.8f' % x1)
    else:
        print('\nTidak konvergen atau memiliki akar kembar.')


# Bagian input nilai
x0 = input('Masukan tebakan awal: ')
galat = input('Toleransi kesalahan: ')
jumlahIterasi = input('Maksimal iterasi: ')

# Konversi x0 dan galat ke double
x0 = float(x0)
galat = float(galat)

# Konversi Jumlah Iterasi ke bilangan bulat
jumlahIterasi = int(jumlahIterasi)


# Pemanggilan fungsi Newton-Raphson
newtonRaphson(x0,galat,jumlahIterasi)
