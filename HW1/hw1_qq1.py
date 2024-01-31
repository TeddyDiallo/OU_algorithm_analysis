# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:23:10 2024

@author: teddy
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar
from math import factorial, log

# Constants
operations_per_day = 86.4e12  # 86,400 seconds/day * 10^9 operations/second

# Functions for T(n)
def T1(n): return 15*n**2
def T2(n): return 8*n**3
def T3(n): return 2**n
def T4(n): return 3**n
def T5(n): return factorial(n)
def T6(n): return n*np.log(n)

# Function to find the maximum n for a given T(n)
def find_max_n(T, start=1, end=20):
    n = start
    while n <= end and T(n) <= operations_per_day:
        n += 1
    return n - 1 if n != start else n  # n-1 unless n is the start value

# For the factorial function, we'll use a different approach to avoid overflow and infinite loop
def find_max_n_factorial():
    n = 1
    while factorial(n) <= operations_per_day:
        n += 1
    return n - 1

# Find max n for each function
max_n_T1 = find_max_n(T1)
max_n_T2 = find_max_n(T2)
max_n_T3 = find_max_n(T3, end=50)  # Increased end for exponential growth
max_n_T4 = find_max_n(T4, end=50)  # Increased end for exponential growth
max_n_T5 = find_max_n_factorial()
max_n_T6 = find_max_n(T6)

# Results
print(f"Max n for T1 (15n^2): {max_n_T1}")
print(f"Max n for T2 (8n^3): {max_n_T2}")
print(f"Max n for T3 (2^n): {max_n_T3}")
print(f"Max n for T4 (3^n): {max_n_T4}")
print(f"Max n for T5 (n!): {max_n_T5}")
print(f"Max n for T6 (n*log(n)): {max_n_T6}")

# Plotting
n_values = range(2, 21)
plt.figure(figsize=(12, 8))
plt.plot(n_values, [T1(n) for n in n_values], label='15n^2')
plt.plot(n_values, [T2(n) for n in n_values], label='8n^3')
plt.plot(n_values, [T3(n) for n in n_values], label='2^n', linestyle='--')
plt.plot(n_values, [T4(n) for n in n_values], label='3^n', linestyle='-.')
plt.plot(n_values, [T5(n) for n in n_values], label='n!', linestyle=':')
plt.plot(n_values, [T6(n) for n in n_values], label='n*log(n)')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Operations (log scale)')
plt.title('T(n) for Different Functions')
plt.legend()
plt.grid(True)
plt.show()
