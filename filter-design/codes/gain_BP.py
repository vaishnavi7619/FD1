import numpy as np

# Given parameters
s1 = -0.3385 - 0.4076j
s2 = -0.3385 + 0.4076j
s3 = -0.1402 + 0.9840j
s4 = -0.1402 - 0.9840j
epsilon = 0.505
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.2474

# Define parameters for transformation
B = 0.0865
Omega0 = 0.314

# Perform transformation to get s_L
s_L = (1j * 0.2735)**2 + Omega0**2
s_L /= B * (1j * 0.2735)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
