import numpy as np

def gauss_elimination_pivoting():
    print("\nGaussian Elimination with Partial Pivoting")
    print("----------------------------------------")
    
    # User inputs the number of equations
    n = int(input("Enter the number of equations/variables: "))
    
    # Initialize augmented matrix [A|B]
    A = np.zeros((n, n))
    B = np.zeros(n)
    
    # Input coefficients
    print("\nEnter the coefficients of the matrix A:")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))
    
    print("\nEnter the constants of the matrix B:")
    for i in range(n):
        B[i] = float(input(f"B[{i+1}]: "))
    
    # Combine A and B into augmented matrix
    AB = np.column_stack((A, B))
    
    # Gaussian Elimination with Partial Pivoting
    for k in range(n):
        # Partial Pivoting: Find the row with the largest absolute value in column k
        max_row = np.argmax(np.abs(AB[k:, k])) + k
        AB[[k, max_row]] = AB[[max_row, k]]  # Swap rows
        
        # Elimination
        for i in range(k + 1, n):
            factor = AB[i][k] / AB[k][k]
            AB[i] -= factor * AB[k]
    
    # Back Substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (AB[i][n] - np.dot(AB[i][i+1:n], x[i+1:n])) / AB[i][i]
    
    # Display results
    print("\nSolution:")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.6f}")

if __name__ == "__main__":
    gauss_elimination_pivoting()