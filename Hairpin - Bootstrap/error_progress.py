# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

b10 = np.loadtxt('bsResult10.csv',  skiprows = 12, delimiter = '\t')
b20 = np.loadtxt('bsResult20.csv',  skiprows = 12, delimiter = '\t')
b30 = np.loadtxt('bsResult30.csv',  skiprows = 12, delimiter = '\t')
b40 = np.loadtxt('bsResult40.csv',  skiprows = 12, delimiter = '\t')
b50 = np.loadtxt('bsResult50.csv',  skiprows = 12, delimiter = '\t')
b60 = np.loadtxt('bsResult60.csv',  skiprows = 12, delimiter = '\t')
b70 = np.loadtxt('bsResult70.csv',  skiprows = 12, delimiter = '\t')
b80 = np.loadtxt('bsResult80.csv',  skiprows = 12, delimiter = '\t')
b90 = np.loadtxt('bsResult90.csv',  skiprows = 12, delimiter = '\t')
b100 = np.loadtxt('bsResult100.csv',  skiprows = 12, delimiter = '\t')
b150 = np.loadtxt('bsResult150.csv',  skiprows = 12, delimiter = '\t')



av10 = np.average(b10[:, 2])
av20 = np.average(b20[:, 2])
av30 = np.average(b30[:, 2])
av40 = np.average(b40[:, 2])
av50 = np.average(b50[:, 2])
av60 = np.average(b60[:, 2])
av70 = np.average(b70[:, 2])
av80 = np.average(b80[:, 2])
av90 = np.average(b90[:, 2])
av100 = np.average(b100[:, 2])
av150 = np.average(b150[:, 2])


ns = np.array([10,20,30,40,50,60,70,80,90,100,150])

avs = np.array([av10, av20, av30, av40, av50, av60, av70, av80, av90, av100, av150])

plt.scatter(ns, avs)

plt.xlabel('Number of Bootstrap Iterations')
plt.ylabel('Average Standard Deviation (kcal mol$^-1$)')

plt.savefig('BootstrapSDev')
plt.show()
