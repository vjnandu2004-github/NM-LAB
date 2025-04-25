import math

def forward_divided_difference():
    print("\nForward Divided Difference Method for Numerical Differentiation")
    print("-----------------------------------------------------------")
    
    # Step 1: User inputs the function
    while True:
        try:
            func_str = input("Enter the function f(x) (e.g., 'math.exp(x)' or 'x**2 + 3*x'): ")
            f = lambda x: eval(func_str)
            break
        except:
            print("Invalid function! Use Python syntax (e.g., 'math.sin(x)').")

    # Step 2: User inputs parameters
    x0 = float(input("Enter the point x where you want to compute the derivative: "))
    h = float(input("Enter step size h (e.g., 0.01): "))
    
    # Forward Divided Difference Formula
    derivative = (f(x0 + h) - f(x0)) / h
    
    # Output
    print(f"\nFirst derivative at x = {x0}: {derivative:.8f}")

if __name__ == "__main__":
    forward_divided_difference()