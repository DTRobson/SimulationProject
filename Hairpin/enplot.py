#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:59:39 2019

@author: k1899674
"""

import numpy as np
import matplotlib.pyplot as plt

energy = np.loadtxt('energy.csv', delimiter = ',')
pressure = np.loadtxt('pressure.csv', delimiter = ',')
temp = np.loadtxt('temp.csv', delimiter = ',')



plt.plot(energy[:,0], energy[:,1])

plt.xlabel('Time Step')
plt.ylabel('Potential Energy kJ mol$^{-1}$')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.tight_layout()

plt.savefig('HairE')

plt.show()


plt.plot(pressure[:,0], pressure[:,1])

plt.plot(pressure[:,0], np.ones(len(pressure)), '--', color = 'black')

plt.xlabel('Time Step')
plt.ylabel('Pressure (bar)')

plt.tight_layout()

plt.savefig('HairNPTP')

plt.show()

plt.plot(temp[:,0], temp[:,1])

plt.plot(temp[:,0], 310 * np.ones(len(temp)), '--', color = 'black')

plt.xlabel('Time Step')
plt.ylabel('Temperature (K)')

plt.tight_layout()

plt.savefig('HairNPTT')

plt.show()
