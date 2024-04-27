#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:35:56 2024

@author: brettnakao
"""
# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# 
# t = np.linspace(0, 2, 20)
# 
# #W1
# A = 1
# tau = 1
# 
# W = np.empty(len(t))
# 
# for i in range(len(t)):
#     W[i] = A*(np.exp(-t[i]/tau)-1+t[i]/tau)
# 
# #W2
# A2 = 3
# tau2 = .8
# 
# W2 = np.empty(len(t))
# 
# for i in range(len(t)):
#     W2[i] = A2*(np.exp(-t[i]/tau2)-1+t[i]/tau2)
# 
# #W3
# A3 = 7
# tau3 = 5
# 
# W3 = np.empty(len(t))
# 
# for i in range(len(t)):
#     W3[i] = A3*(np.exp(-t[i]/tau3)-1+t[i]/tau3)
# 
# # Plotting
# plt.figure()
# 
# plt.plot(t, W, linestyle='solid', color='black', label='W1')
# plt.plot(t, W2, linestyle='dashed', color='blue', label='W2')
# plt.plot(t, W3, linestyle='dotted', color='green', label='W3')
# 
# plt.xlabel('Time')
# plt.ylabel('W(t)')
# plt.title('W(t)')
# plt.legend()
# 
# plt.show
# =============================================================================

""" A) """
import numpy as np
import matplotlib.pyplot as plt

# Define time array
t = np.linspace(0, 7, 20)

tau = 3.3

# Define V(t) array
V = np.empty(len(t))
for i in range(len(t)):
    V[i] = 1-np.exp(-t[i]/tau)

# Import data
novickA_data = np.genfromtxt('g149novickA.csv', delimiter=",")
x = novickA_data[:, 0]
y = novickA_data[:, 1]

# Plot
plt.figure()
plt.plot(t, V, linestyle='solid', color='black', label='Curve-fit')
plt.scatter(x, y, marker='+', label='Experimental Data')
plt.xlabel('Time')
plt.ylabel('V(t)')
plt.title('V(t)')
plt.legend()
plt.show

""" B) """
import numpy as np
import matplotlib.pyplot as plt

# Define time array
time = np.linspace(0, 10, 20)

# Constants
A = .36
tau = 10

# Define W array
W = np.empty(len(time))
for i in range(len(time)):
    W[i] = A*(np.exp(-time[i]/tau)-1+time[i]/tau)

# Import data
novickB_data = np.genfromtxt('g149novickB.csv', delimiter=",")
x1 = novickB_data[0:11, 0]
y2 = novickB_data[0:11, 1]
print(novickB_data)
print(x1)

# Plot
plt.figure()
plt.plot(time, W, linestyle='solid', color='black', label='Curve-fit')
plt.scatter(x1, y2, marker='+', label='Experimental Data')
plt.xlabel('Time')
plt.ylabel('W(t)')
plt.title('W(t)')
plt.legend()
plt.show