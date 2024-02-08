# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 06:36:19 2024

@author: teddy
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the range of n
n = np.arange(2, 51)

# Define the functions
T_n = (1/2) * (n**2 - 3*n + 2) # Time complexity of selection sort
f1_n = (3/4) * n**2             # Function f1(n)
f2_n = (1/8) * n**2             # Function f2(n)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n, f1_n, label='f1(n) = 3/4*n^2', marker='o')
plt.plot(n, T_n, label='T(n) = 1/2*n^2 - 1/2*n', linestyle='--', marker='x')
plt.plot(n, f2_n, label='f2(n) = 1/8*n^2', marker='^')
plt.title('Comparison of f1(n), T(n), and f2(n)')
plt.xlabel('n')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()
