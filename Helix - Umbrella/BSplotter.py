# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

UMB = np.loadtxt('bsResult.csv', skiprows = 12, delimiter = '\t')
BOOT = np.loadtxt('bsResult100.csv', skiprows = 12, delimiter = '\t')

num =  len(UMB)
inds = []
zs = []
changes = []
diffs = []


for i in range(1, num):
    diffs.append(abs(UMB[i, 1] - UMB[i-1, 1]))

mean_diff = np.mean(diffs)
var_diff = np.var(diffs)
sd_diff = np.sqrt(var_diff)

cutoff = mean_diff

for i in range(1, num):
    if abs(UMB[i, 1] - UMB[i-1, 1]) > cutoff:
        inds.append(i)
        zs.append(UMB[i, 0])
        changes.append(abs(UMB[i, 1] - UMB[i-1, 1]))

hist, bins = np.histogram(zs, bins = 75)
mids = []
for j in range(1, len(bins)):
    mids.append((bins[j] + bins[j-1])/2)




plt.plot(UMB[1:,0], diffs)
plt.xlabel('$z$-coordinate (nm)')
plt.ylabel('Absolute Difference in PMF (kcal mol$^{-1}$)')
plt.show()

plt.plot(mids, hist)
plt.yticks(np.arange(max(hist) + 1))
plt.xlabel('$z$-coordinate (nm)')
plt.ylabel('Number of Spikes')
plt.show()

print(zs)
print(changes)

'''sds = BOOT[:, 2]

plus_1 = UMB[:, 1] + sds
minus_1 = UMB[:, 1] - sds

plus_3 = UMB[:, 1] + 3 * sds
minus_3 = UMB[:, 1] - 3 * sds

plus_5 = UMB[:, 1] + 5 * sds
minus_5 = UMB[:, 1] - 5 * sds



plt.plot(UMB[:,0], UMB[:, 1], label = 'Calculated', color = 'blue')

plt.plot(UMB[:, 0], plus_3, label = '$ \pm 3\sigma$', color = 'orange')
plt.plot(UMB[:, 0], minus_3, color = 'orange')

plt.plot(UMB[:, 0], plus_5, label = '$\pm 5\sigma$', color = 'red')
plt.plot(UMB[:, 0], minus_5, color = 'red')

plt.legend()

plt.ylabel('PMF (kcal mol$^{-1}$)')
plt.xlabel('$z$-coordinate (nm)')

plt.tight_layout()

plt.savefig('helPMF')

plt.show()'''
