# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:12:25 2019

@author: Robbo
"""

import MDAnalysis as md
import MDAnalysis.analysis.hbonds as hb
import numpy as np
import matplotlib.pyplot as plt

u1 = md.Universe('./1-struct/struct.gro')
u2 = md.Universe('./2-struct/struct.gro')
u3 = md.Universe('./3-struct/struct.gro')
u4 = md.Universe('./4-struct/struct.gro')
u5 = md.Universe('./5-struct/struct.gro')
u6 = md.Universe('./6-struct/struct.gro')
u7 = md.Universe('./7-struct/struct.gro')
u8 = md.Universe('./8-struct/struct.gro')
u9 = md.Universe('./9-struct/struct.gro')
u10 = md.Universe('./10-struct/struct.gro')
u11 = md.Universe('./11-struct/struct.gro')
u12 = md.Universe('./12-struct/struct.gro')
u13 = md.Universe('./13-struct/struct.gro')
u14 = md.Universe('./14-struct/struct.gro')
u15 = md.Universe('./15-struct/struct.gro')
u16 = md.Universe('./16-struct/struct.gro')
u17 = md.Universe('./17-struct/struct.gro')
u18 = md.Universe('./18-struct/struct.gro')
u19 = md.Universe('./19-struct/struct.gro')
u20 = md.Universe('./20-struct/struct.gro')
u21 = md.Universe('./21-struct/struct.gro')


us = []
us.append(u1)
us.append(u2)
us.append(u3)
us.append(u4)
us.append(u5)
us.append(u6)
us.append(u7)
us.append(u8)
us.append(u9)
us.append(u10)
us.append(u11)
us.append(u12)
us.append(u13)
us.append(u14)
us.append(u15)
us.append(u16)
us.append(u17)
us.append(u18)
us.append(u19)
us.append(u20)
us.append(u21)

ns = []
dists = []
ave_dists = []
tabs = []

ind = 0

for i in us:
    print(ind)
    h = hb.HydrogenBondAnalysis(i, 'resid 1-6', 'resid 8-12', distance = 3)
    h.run()
    h.generate_table()
    tab = h.table
    tabs.append(tab)
    ns.append(len(tab))
    ds = np.empty(len(tab))
    for j in range(len(tab)):
        bonds = tab[j]
        ds[j] = bonds[-2]
    ave = np.sum(ds)/len(ds)
    dists.append(ds)
    ave_dists.append(ave)
    ind += 1


plt.plot(np.arange(21), ns)
plt.xticks(np.arange(21))
plt.show()

plt.plot(np.arange(21), ave_dists)
plt.show()
