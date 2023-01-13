# Metode Simpson 1/3

# Mendefinisikan fungsi untuk dilakukan integrasi
def f(x):
    return 1/(1 + x**2)

# Implementasi Simpson 1/3 
def simpson13(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Mencari Penjumlahan
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    
    # Menemukan nilai akhir integrasi
    integration = integration * h/3
    
    return integration
    
# Bagian input
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Memanggil fungsi
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )
