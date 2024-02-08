# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:20:53 2024

@author: teddy
"""

import numpy as np

# Define the inequality function
def inequality(n):
    return 6 * n * np.log(n)/np.log(2) + 6 * n - 0.5 * n**2

# Start with the smallest n that makes sense for the problem, which is n=2, since log(1) is 0 and would not be meaningful for this inequality
n = 2

# Iterate through values of n to find when the inequality becomes true
while True:
    if inequality(n) < 0:
        break
    n += 1

# n now holds the smallest integer value for which the inequality is true
print(f"The inequality 6nlog(n) + 6n < 0.5n^2 holds for n >= {n}")
