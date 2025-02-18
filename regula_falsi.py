MAX_ITER = 1000000

def func(x):
    return x**3 - x**2 + 2

def regulaFalsi(a, b, tolerance=0.0001):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return None
    
    c = a
    for _ in range(MAX_ITER):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        
        if abs(func(c)) < tolerance:
            print("The value of root is: {:.4f}".format(c))
            return c
        
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    print("Method did not converge within the maximum number of iterations.")
    return None

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
tolerance = float(input("Enter the tolerance value: "))
regulaFalsi(a, b, tolerance)