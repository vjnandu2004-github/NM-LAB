def func(x):
    return x**3 - x - 2

def bisection(a, b, tolerance):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b\n")
        return

    c = a
    while (b - a) / 2 >= tolerance:
        c = (a + b) / 2

        if func(c) == 0.0:
            break

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
            
    print(f"The value of root is: {c:.6f}")

# Driver code with user input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
tolerance = float(input("Enter the tolerance value: "))

bisection(a, b, tolerance)
