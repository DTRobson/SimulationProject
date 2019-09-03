# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:02:37 2019

@author: Robbo
"""

import numpy as np
import matplotlib.pyplot as plt


def hist_inter(hist1, hist2):
    n = len(hist1)
    n2 = len(hist2)
    if abs(n - n2) > 0.001:
        print('Error, Histograms must have the same number of bins')
        return 0
    else:
        norm = np.sum(hist1)
        minima = np.minimum(hist1, hist2)
        inter = np.sum(minima)
        return np.true_divide(inter, norm), minima
    
def second_maxima(all_hists):
    scnd_max = np.empty(len(all_hists))
    for i in range(len(all_hists)):
        if all(all_hists[i] == 0):
            print(all_hists[i])
            scnd_max[i] = 0
        else:
            temp = np.copy(all_hists[i])
            frst_max = max(temp)
            loc = np.where(temp < frst_max)
            new = temp[loc]
            scnd_max[i] =  max(new)
    return scnd_max
        

def mids(bins):
    mids = np.empty(len(bins)-1)
    for i in range(len(mids)):
        mids[i] = 1/2 * (bins[i] + bins[i + 1])
    return mids

'''
g1 = np.random.normal(loc =  5, size = 10000)
g2 = np.random.normal(loc = 25, size = 10000)

hist1, bins1 = np.histogram(g1, bins = 100, range = [-30, 30])
hist2, bins2 = np.histogram(g2, bins = 100, range = [-30, 30])

inter, minima = hist_inter(hist1, hist2)


plt.hist(g1, bins1, label = '1', alpha = 0.6, lw = 2, ls = 'dashed', color = 'red')
plt.hist(g2, bins2, label = '2', alpha = 0.6, lw = 2, ls = 'dashed', color = 'blue')

plt.legend()
plt.show()


xs = mids(bins1)

plt.plot(xs, hist1, label = '1')
plt.plot(xs, hist2, label = '2')
plt.plot(xs, minima, label = 'min')

plt.legend()

plt.show()


        
print('Intersection = ', inter)
     
all_hists = np.empty([len(hist1), 2])


all_hists[:,0] = hist1
all_hists[:,1] = hist2

minima2 = second_maxima(all_hists)

plt.plot(xs, minima)
plt.plot(xs, minima2)
plt.show()    
    
'''    
    