from sympy import symbols, simplify

# Define symbolic variable s
z = symbols('z')

# Constants
omega0_val = 0.314
B_val = 0.0865
s = (z-1)/(z+1)
# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s1 = -0.3385 - 0.4076j
s2 = -0.3385 + 0.4076j
s3 = -0.1402 + 0.9840j
s4 = -0.1402 - 0.9840j

# Define the given polynomial expression
x = s**8 + 0.0828*s**7 + 0.4052*s**6 + 0.025*s**5 + 0.0605*s**4 + 0.0024*s**3 + 0.0039*s**2 + 0.000079*s + 0.000094
polynomial_expr = 1 / x

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
