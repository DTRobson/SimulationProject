#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:50:30 2019

@author: k1899674
"""

import numpy as np
import matplotlib.pyplot as plt

p1 = np.loadtxt('pull-v-0-1_z.csv', delimiter = '\t', skiprows = 19)
print('da')
p2 = np.loadtxt('pull-v-0-01_z.csv', delimiter = '\t', skiprows = 19)
p3 = np.loadtxt('pull-v-0-001_z.csv', delimiter = '\t', skiprows = 19)
p4 = np.loadtxt('pull-v-0-0001_z.csv', delimiter = '\t', skiprows = 19)

plt.scatter(p1[:,0], p1[:,2])
plt.scatter(p2[:,0], p2[:,2])
plt.scatter(p3[:,0], p3[:,2])
plt.scatter(p4[:,0], p4[:,2])

plt.show()