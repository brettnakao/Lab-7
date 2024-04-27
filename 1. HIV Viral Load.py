#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:18:48 2024

@author: brettnakao
"""

import numpy as np
import matplotlib.pyplot as plt

# Create time array
time = np.linspace(0, 10, 100)

B = 175000
A = 0
alpha = 0
beta = .5

viral_load = np.empty(len(time))

for i in range(len(time)):
    viral_load[i] = A*np.exp(alpha*time[i]) + B*np.exp(-beta*time[i])

# Import data
hiv_data = np.genfromtxt('HIVseries.csv', delimiter=",")
x = hiv_data[:, 0]
y = hiv_data[:, 1]

# Plot
plt.figure()
plt.plot(time, viral_load, label='Function')
plt.scatter(x, y, marker='+', label='Experimental Data')
plt.xlabel('Time')
plt.ylabel('Viral Load')
plt.title('Viral Load vs. Time for an HIV-positive patient')
plt.legend()

plt.show