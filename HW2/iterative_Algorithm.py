# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 06:05:29 2024

@author: teddy
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the iterated logarithm function
def log_star(n, base=2):
    if n <= 1:
        return 0
    else:
        return 1 + log_star(np.log(n)/np.log(base), base)

# Generate a range of values for n
n_values = np.linspace(2, 1000, 1000)
log_star_n_values = np.array([log_star(n) for n in n_values])
log_log_star_n_values = np.log(log_star_n_values)

# Calculate log*(log(n))
log_star_log_n_values = np.array([log_star(np.log(n)) for n in n_values])

# Plot the graph
plt.figure(figsize=(12, 7))
plt.plot(n_values, log_log_star_n_values, label='log(log*(n))', color='blue')
plt.plot(n_values, log_star_log_n_values, label='log*(log(n))', color='red')
plt.xlabel('n')
plt.ylabel('Value')
plt.title('Comparison of log(log*(n)) and log*(log(n))')
plt.legend()
plt.grid(True)
plt.show()
