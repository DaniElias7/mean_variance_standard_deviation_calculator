import mean_var_std

# Test script for the calculate function in mean_var_std module

# List of test matrices
matrices = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],         
    [5, 9, 1, 3, 6, 8, 4, 7, 2],           
    [9, 8, 7, 6, 5, 4, 3, 2, 1],           
    [3, 7, 2, 8, 1, 4, 6, 9, 5],           
    [-1, 2, -3, 4, 0, -2, 3, -4, 1]        
]

# Test each matrix
for i, matriz in enumerate(matrices, 1):
    try:
        resultado = mean_var_std.calculate(matriz)
        print(f"Result for matrix {i} {matriz}:")
        print(resultado)
        print()  # Blank line to separate results
    except ValueError as e:
        print(f"Error in matrix {i}: {e}")