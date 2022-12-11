# untuk import library
import numpy as np
import matplotlib.pyplot as plt


banyakData = int(input('Masukan jumlah inputan data x dan y: '))
nilaiX = np.zeros((banyakData))
nilaiY = np.zeros((banyakData, banyakData))


print('Masukan data x dan y: ')
for i in range(banyakData):
    nilaiX[i] = float(input('nilaiX(' + str(i) + ') = '))
    nilaiY[i][0] = float(input('nilaiY(' + str(i) + ') = '))
    

xinput = input('Masukkan nilai x yang ingin diketahui: ')
xinput = float(xinput)

for i in range(1, banyakData):
    for j in range(0, banyakData-i):
        nilaiY[j][i] = (nilaiY[j + 1, i - 1] - nilaiY[j, i - 1])/(nilaiX[j+i] - x[j])

print('\n============================================TABEL SELISIH - TERBAGI==============================================');
for i in range(0, banyakData):
    print('%0.2f' % (x[i]), end='')
    for j in range(0, banyakData - i):
        print('\t\t%0.6f' % (nilaiY[i][j]), end='')
    print()
print('=================================================================================================================');

p = nilaiY[0,0]
for i in range (1, banyakData):
    a = nilaiY[0,i]
    for j in range(0, i):
        a = a * (xinput-x[j])
    p = p+a
print('Nilai hampiran dari data di atas adalah %0.6f' % p)
