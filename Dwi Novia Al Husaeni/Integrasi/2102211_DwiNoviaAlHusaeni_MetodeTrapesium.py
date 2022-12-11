# Mendefinisikan fungsi untuk dilakukan integrasi
def f(x):
    return 1/(1 + x**2)

# Implementasi metode trapesium
def trapesium(x0,xn,n):
    # perhitungan ukuran langkah
    h = (xn - x0) / n
    
    # Menemukan penjumlahan
    integrasi = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integrasi = integrasi + 2 * f(k)
    
    # Menemukan nilai akhir dari integrasi
    integrasi = integrasi * h/2
    
    return integrasi
    
# Input
batasBawah = float(input("Masukan batas bawah dari integrasi: "))
batasAtas = float(input("Masukan batas atas dari integrasi: "))
subInterval = int(input("Masukan angka untuk sub intervals: "))

# Memanggil fungsi metode trapesium dan menampilkan hasil
hasil = trapesium(batasBawah, batasAtas, subInterval)
print("Hasil integrasi adalah : %0.6f" % (hasil) )