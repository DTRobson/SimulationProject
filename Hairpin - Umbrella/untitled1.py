#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:23:08 2019

@author: k1899674
"""

import numpy as np
import matplotlib.pyplot as plt

UMB = np.loadtxt('bsResult.csv', skiprows = 12, delimiter = '\t')



x1s = UMB[:107, 0]
y1s = UMB[:107, 1]

x2s = UMB[107:, 0]
y2s = UMB[107:, 1]



a1, b1 = np.polyfit(x1s, y1s, 1)
a2, b2, c2 = np.polyfit(x2s, y2s, 2)



lin = a1 * x1s + b1
quad = a2 * (x2s ** 2) + b2 * x2s + c2


plt.plot(UMB[:, 0], UMB[:, 1], label = 'real')


plt.plot(x1s, lin, label = 'l')

plt.plot(x2s, quad, label = 'q')

plt.legend()

plt.show()