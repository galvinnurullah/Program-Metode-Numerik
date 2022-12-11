#inputan
e = 2.718
z = str(input("Masukan Fungsi: ")) # masukan fungsi atau f(x)
batasBawah = float(input("Masukan Batas Bawah: "))
batasAtas = float(input("Masukan Batas Atas: "))
sub_interval = int(input("Masukan Banyak Partisi: "))

def f(n): #fungsi yang berfungsi untuk mengembalikan nilai dari f(x)
    temp = eval(z)
    
    return temp

# implementasi
def simpson13(x0,xn,n):
    #menghitung setiap step
    h = (xn - x0) / n # mencari jarak interval antar titik (delta x)
    
    for i in range(n+1): 
         
        k = x0 + i*h # menentukan titik selanjutnya 
         
        if i == 0:
            integration = f(x0)
            
        elif i == n:
            integration = integration + f(xn)
            
        elif i%2 == 0:
            integration = integration + 2 * f(k)
            
        elif i%2 == 1:
            integration = integration + 4 * f(k)
        print (integration)
        
    #  Cari nilai terakhir dari integrasi
    integration = integration * h/3
    
    return integration
    

# memanggil fungsi dan hasil
result = simpson13(batasBawah, batasAtas, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f"%(result))