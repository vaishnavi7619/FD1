import numpy as np
import matplotlib.pyplot as plt

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

G_LP = 0.4166
num = G_LP

Omega_p1 = 0.2735
Omega_p2 = 0.3600

Omega_s1 = 0.2467
Omega_s2 = 0.3778

# Define parameters for transformation
B = 0.0865
Omega0 = 0.314

# Perform transformation to get s_L
s_L = (1j * w)**2 + Omega0**2
s_L = s_L / (B * (1j * w))

# Band pass gain
G_bp = 1.0370

# Substitute s = jw into H(s)
H = G_bp * (num / np.polyval(den, s_L))

# Plot magnitude response for H(s)
plt.figure()
plt.plot(w, abs(H), linewidth=1)
plt.title('Band Pass Filter')
plt.xlabel('Analog Frequency ($\Omega$)')
plt.ylabel('|H_{a,BP}($\Omega$)|')
plt.grid(True)
plt.xlim(-1.5,1.5)
plt.ylim(0, 2)
plt.savefig("Band_Pass_Filter.png")
