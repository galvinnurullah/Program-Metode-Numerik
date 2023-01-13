# Definisikan suatu matriks A berordo 2x3 dengan entri-entri yang ditentukan sendiri
#tulis code disini
matriksA = [[1,2,0],
            [2,2,1],]

print("Matriks A : ");
for a in matriksA :
    print(a);

# Definisikan suatu matriks B berordo 3x3 dengan entri-entri yang ditentukan sendiri
#tulis code disini
matriksB = [[-1,5,6],
            [3,1,2],
            [0,1,4]]

print("Matriks B : ");
for b in matriksB :
    print(b);

# Definisikan suatu matriks C berordo 3x2 dengan entri-entri yang ditentukan sendiri
#tulis code disini
matriksC = [[0,3],
            [9,1],
            [3,3]]

print("Matriks C : ");
for c in matriksC :
    print(c);
# Carilah perkalian matriks A dan B kemudian print hasilnya
#tulis code disini
hasil1 = [[0,0,0],
         [0,0,0]]

for i in range(len(matriksA)):
   for j in range(len(matriksB[0])):
       for k in range(len(matriksB)):
           hasil1[i][j] += matriksA[i][k] * matriksB[k][j]


print("\nHasil Perkalian Matriks A dan B : ");
for r in hasil1:
   print(r)
           
# Carilah perkalian matriks B dan C kemudian print hasilnya
#tulis code disini
hasil2 = [[0,0],
         [0,0],
         [0,0]]

for i in range(len(matriksB)):
   for j in range(len(matriksC[0])):
       for k in range(len(matriksC)):
           hasil2[i][j] += matriksB[i][k] * matriksC[k][j]


print("\nHasil Perkalian Matriks B dan C : ");
for r in hasil2:
   print(r)
           
# Carilah perkalian matriks C dan A kemudian print hasilnya
#tulis code disini
hasil3 = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(matriksC)):
   for j in range(len(matriksA[0])):
       for k in range(len(matriksA)):
           hasil3[i][j] += matriksC[i][k] * matriksA[k][j]


print("\nHasil Perkalian Matriks C dan A : ");
for r in hasil3:
   print(r)
