#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:59:39 2019

@author: k1899674
"""

import numpy as np
import matplotlib.pyplot as plt

energ  =  np.loadtxt('energies.csv', delimiter = ',')
npt_energy = np.loadtxt('npt-energy.csv', delimiter = ',')
npt_pressure = np.loadtxt('pressure.csv', delimiter = ',')
npt_temp = np.loadtxt('temp.csv', delimiter = ',')


plt.plot(energ[:,0], energ[:,1])

plt.xlabel('Time Step')
plt.ylabel('Potential Energy kJ mol$^{-1}$')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.tight_layout()

plt.savefig('HelixMin')

plt.show()


plt.plot(npt_energy[:,0], npt_energy[:,1])

plt.xlabel('Time Step')
plt.ylabel('Potential Energy kJ mol$^{-1}$')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.tight_layout()

plt.savefig('HelixNPTE')

plt.show()


plt.plot(npt_pressure[:,0], npt_pressure[:,1])

plt.plot(npt_pressure[:,0], np.ones(len(npt_pressure)), '--', color = 'black')

plt.xlabel('Time Step')
plt.ylabel('Pressure (bar)')

plt.tight_layout()

plt.savefig('HelixNPTP')

plt.show()

plt.plot(npt_temp[:,0], npt_temp[:,1])

plt.plot(npt_temp[:,0], 310 * np.ones(len(npt_temp)), '--', color = 'black')

plt.xlabel('Time Step')
plt.ylabel('Temperature (K)')

plt.tight_layout()

plt.savefig('HelixNPTT')

plt.show()
