# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 06:26:37 2024

@author: teddy
"""

import numpy as np
import matplotlib.pyplot as plt

# Define n range
n = np.arange(2, 51)

# Define T(n)
T_n = (1/2) * (n**2 - 3*n + 2)

# Plot T(n) vs n
plt.figure(figsize=(10, 6))
plt.plot(n, T_n, label='T(n) = 1/2*n^2 - 1/2*n', marker='o')
plt.title('Plot of T(n) vs. n for Selection Sort')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.grid(True)
plt.legend()
plt.show()