# Melakukan impor library numpy
import numpy as np
import sys

# Membaca nilai dimensi matriks yang diinginkan
number = int(input('Masukan angka untuk ukuran matriks: '))

# Membuat array dengan numpy dari angka x angka increament dan melakukan inisilaisasi ke matriks yang elemennya berisi 0
matriksA = np.zeros((number,number+1))

# Membuat arrau dengan numpy dari besarnya angka dan melakukan inisialisasi ke angka 0 untuk tempat solusi dalam bentuk vektor
matriksHasil = np.zeros(number)

# Membaca koefisien penjumlahan matriks
print('Masukan Nilai Koefisien Penjumlahan Matriks:')
for i in range(number):
    for j in range(number+1):
        matriksA[i][j] = float(input( 'matriksA['+str(i)+']['+ str(j)+']='))

# Melakukan Implementasi elminasi Gauss-Jordan
for i in range(number):
    if matriksA[i][i] == 0.0:
        sys.exit('Mendeteksi Pembagian dengan 0!')
        
    for j in range(number):
        if i != j:
            ratio = matriksA[j][i]/matriksA[i][i]

            for k in range(number+1):
                matriksA[j][k] = matriksA[j][k] - ratio * matriksA[i][k]

# Memperoleh Solusi

for i in range(number):
    matriksHasil[i] = matriksA[i][number]/matriksA[i][i]

# Menampilkan solusi
print('\nSolusi yang ditemukan adalah : ')
for i in range(number):
    print('X%d = %0.2f' %(i,matriksHasil[i]), end = '\t')
