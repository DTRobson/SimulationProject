# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:17:48 2019

@author: Robbo
"""

import numpy as np
import matplotlib.pyplot as plt
import intsec as IS

DATA = np.loadtxt('histo.csv', delimiter = ',', skiprows = 12)

XVALS = DATA[:,0]

HISTS = DATA[:, 1:]

###################################################################################

num_hists = len(HISTS[0])

for i in range(num_hists):
    plt.plot(XVALS, HISTS[:,i])
    
plt.xlabel('$z$-coordinate (nm)')
plt.ylabel('Frequency')

plt.savefig('HelUMBs')

plt.show()

######################################################################################

sums = np.sum(HISTS, axis = 1)


plt.plot(XVALS, sums)

plt.xlabel('$z$-coordinate (nm)')
plt.ylabel('Total Frequency')

plt.savefig('HelUmbSums')

plt.show() 



##################################################################################

second_maxes = IS.second_maxima(HISTS)

plt.plot(XVALS, second_maxes)

plt.xlabel('$z$-coordinate (nm)')
plt.ylabel('Second Highest Frequency')

plt.savefig('HelUmbScnd')

plt.show()

##########################################################################

intersections = np.empty([len(HISTS[0]), len(HISTS[0])])
maxes = np.empty(len(HISTS[0]))


for i in range(len(HISTS[0])):
    for j in range(len(HISTS[0])):
        intersections[i, j] = IS.hist_inter(HISTS[:, i], HISTS[:, j])
    loc = np.where(HISTS[:, i] == max(HISTS[:,i]))[0]
    maxes[i] =  XVALS[loc]


fig, ax = plt.subplots()
im = ax.imshow(intersections, cmap = 'YlOrRd')

cbar = ax.figure.colorbar(im, ax=ax)

cbar.set_label('Overlap')

plt.xlabel('Histogram')
plt.ylabel('Histogram')

plt.savefig('HelUmbOver')

plt.show()

############################################################################

all_overlaps = np.empty(len(maxes))
for i in range(len(maxes)):
    all_overlaps[i] = np.sum(intersections[i, :])

inds = np.arange(len(maxes))
sort_laps =  [x for _, x in sorted(zip(maxes, all_overlaps))]
sort_inds =  [x for _, x in sorted(zip(maxes, inds))]
sort_maxes = sorted(maxes)



plt.plot(sort_maxes, sort_laps)


plt.xlabel('Maximum $z$-coordinate (nm)')
plt.ylabel('Overlap')


plt.savefig('HelUmbOVerTot')

plt.show()
######################################################################

sort_inter = np.empty(intersections.shape)

for i in range(len(sort_inter)):
    for j in range(len(sort_inter)):
        ind1 =  sort_inds[i]
        ind2 = sort_inds[j]
        sort_inter[i,j] = intersections[ind1, ind2]


fig, ax = plt.subplots()
im = ax.imshow(sort_inter, cmap = 'YlOrRd')

cbar = ax.figure.colorbar(im, ax=ax)

cbar.set_label('Overlap')

plt.xlabel('Histogram')
plt.ylabel('Histogram')

plt.savefig('HelUmbOverOrd')

plt.show()


        

    

