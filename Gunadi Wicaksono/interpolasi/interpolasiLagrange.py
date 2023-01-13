# Interpolasi Lagrange

# Melakukan import library numpy
import numpy as np

# Membaca jumlah data yang diinput
banyakData = int(input('Masukkan jumlah data / titik poin: '))

# Making array dari numpy sesuai banyaknya data yang diinput dan melakukan inisialisasi ke 0 untuk penyimpanan nilai x dan y dengan menggunakan tabel selisih terbagi
# to zero for storing x and y value along with differences of y
nilaiX = np.zeros((banyakData))
nilaiY = np.zeros((banyakData))


# Membaca data-data yang berada pada range tertentu
print('Masukan data X dan Y: ')
for i in range(banyakData):
    nilaiX[i] = float(input( 'nilaiX['+str(i)+']='))
    nilaiY[i] = float(input( 'nilaiY['+str(i)+']='))


# Membaca titik yang dilakukan interpolasi
nilaiXP = float(input('Masukkan titik interpolasi: '))

# Mengatur nilai fungsi dari titik interpolasi ke 0
nilaiYP = 0

# Melakukan implementasi interpolasi Lagrange
for i in range(banyakData):
    
    p = 1
    
    for j in range(banyakData):
        if i != j:
            p = p * (nilaiXP - nilaiX[j])/(nilaiX[i] - nilaiX[j])
    
    nilaiYP = nilaiYP + p * nilaiY[i]    

# Menampilkan hasil keluaran
print('Nilai interpolasi untuk titik %.3f adalah %.3f.' % (nilaiXP, nilaiYP))
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHu
