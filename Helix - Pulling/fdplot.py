#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:51:07 2019

@author: k1899674
"""

import numpy as np
import matplotlib.pyplot as plt

fd_0_1 = np.loadtxt('force-vs-distance-v-0-1.dat')
x_0_1 = abs(fd_0_1[:,0] )
f_0_1 = fd_0_1[:,1]


fd_0_01 = np.loadtxt('force-vs-distance-v-0-01.dat')
x_0_01 = abs(fd_0_01[:,0] )
f_0_01 = fd_0_01[:,1]

fd_0_001 = np.loadtxt('force-vs-distance-v-0-001.dat')
x_0_001 = abs(fd_0_001[:,0] )
f_0_001 = fd_0_001[:,1]

fd_0_0001 = np.loadtxt('force-vs-distance-v-0-0001.dat')
x_0_0001 = abs(fd_0_0001[:,0] )
f_0_0001 = fd_0_0001[:,1]

plt.scatter(x_0_1, f_0_1, label = '0.1nm/ps')
plt.xlabel('End to end distance (nm)')
plt.ylabel('Force kJ mol$^{-1}$ nm$^{-1}$')
plt.show()

plt.scatter(x_0_01, f_0_01, label = '0.01nm/ps')
plt.xlabel('End to end distance (nm)')
plt.ylabel('Force kJ mol$^{-1}$ nm$^{-1}$')
plt.show()


plt.scatter(x_0_001, f_0_001, label = '0.001nm/ps')
plt.xlabel('End to end distance (nm)')
plt.ylabel('Force kJ mol$^{-1}$ nm$^{-1}$')
plt.show()

plt.scatter(x_0_0001, f_0_0001, label = '0.0001nm/ps')
plt.xlabel('End to end distance (nm)')
plt.ylabel('Force kJ mol$^{-1}$ nm$^{-1}$')
plt.show()


copy = np.copy(fd_0_0001)
copy[:,0] *= -1

m = np.mean(copy, axis = 0)

print(m.shape)

t = np.transpose(copy)
cov = np.cov(t)

print(cov.shape)

rands = np.random.multivariate_normal(m, cov, size = 501)

xs = rands[:, 0]
ys = rands[:, 1]

hist, xedges, yedges = np.histogram2d(xs, ys, bins = 100, density = True)

plt.imshow(hist)
plt.show()


plt.scatter(xs, ys, label = 'Gaussian')
plt.scatter(x_0_0001, f_0_0001, label = 'Observed')
plt.xlabel('End to end distance (nm)')
plt.ylabel('Force kJ mol$^{-1}$ nm$^{-1}$')
plt.legend()
plt.tight_layout()
plt.savefig('FDG2')
plt.show()


copy2 = np.copy(fd_0_001)
copy2[:,0] *= -1

m2 = np.mean(copy2, axis = 0)

t2 = np.transpose(copy2)
cov2 = np.cov(t2)

rands2 = np.random.multivariate_normal(m2, cov2, size = 501)

xs2 = rands2[:, 0]
ys2 = rands2[:, 1]

hist2, xedges2, yedges2 = np.histogram2d(xs2, ys2, bins = 100, density = True)

plt.imshow(hist2)
plt.show()


plt.scatter(xs2, ys2, label =  'Gaussian')
plt.scatter(x_0_001, f_0_001, label = 'Observed')
plt.xlabel('End to end distance (nm)')
plt.ylabel('Force kJ mol$^{-1}$ nm$^{-1}$')
plt.legend()
plt.tight_layout()
plt.savefig('FDG1')
plt.show()

corr_coeff = cov[0,1]/(np.sqrt(cov[0,0] * cov[1,1]))
corr_coeff2 = cov2[0,1]/(np.sqrt(cov2[0,0] * cov2[1,1]))

print(corr_coeff)
print(corr_coeff2)