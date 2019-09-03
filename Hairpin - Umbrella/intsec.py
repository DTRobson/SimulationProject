# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:02:37 2019

@author: Robbo
"""

import numpy as np

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
        return np.true_divide(inter, norm)
    
def second_maxima(all_hists):
    scnd_max = np.empty(len(all_hists))
    for i in range(len(all_hists)):
        if all(all_hists[i] == 0):
            scnd_max[i] = 0
        else:
            temp = np.copy(all_hists[i])
            frst_max = max(temp)
            loc = np.where(temp < frst_max)
            new = temp[loc]
            scnd_max[i] =  max(new)
    return scnd_max
        
def third_maxima(all_hists):
    third_max = np.empty(len(all_hists))
    for i in range(len(all_hists)):
        if all(all_hists[i] == 0):
            third_max[i] = 0
        else:
            temp = np.copy(all_hists[i])
            frst_max = max(temp)
            loc = np.where(temp < frst_max)
            new = temp[loc]
            if all(new == 0):
                third_max[i] = 0
            else:
                scnd_max =  max(new)
                loc2 = np.where(new < scnd_max)
                new2 =  new[loc2]         
                third_max[i] = max(new2)
    return third_max
    
    