# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

UMB = np.loadtxt('bsResult.csv', skiprows = 12, delimiter = '\t')
BOOT = np.loadtxt('bsResult150.csv', skiprows = 12, delimiter = '\t')

num =  len(UMB)
zs = []
diffs = []
diff2s = []


for i in range(1, num):
    diffs.append(UMB[i, 1] - UMB[i-1, 1])
    if i > 1:
        diff2s.append(diffs[-1] - diffs[-2])

diffs = np.array(diffs)
diff2s = np.array(diff2s)

diffs = abs(diffs)
diff2s = abs(diff2s)


lin_diffs = diffs[:107]
quad_diff2s = diff2s[107:]

mean_diff = np.mean(lin_diffs)
var_diff = np.var(lin_diffs)
sd_diff = np.sqrt(var_diff)

cutoff = mean_diff + 1 * sd_diff

for i in range(len(lin_diffs)):
    if lin_diffs[i] > cutoff:
        zs.append(UMB[i, 0])


mean_q = np.mean(quad_diff2s)
var_q = np.var(quad_diff2s)
sd_q = np.sqrt(var_q)

cutoff2 = mean_diff + 1 * sd_diff

for i in range(len(quad_diff2s)):
    if quad_diff2s[i] > cutoff:
        zs.append(UMB[107 + i, 0])


hist, bins = np.histogram(zs, bins = 75)
mids = []
for j in range(1, len(bins)):
    mids.append((bins[j] + bins[j-1])/2)
    

plt.plot(UMB[:107, 0], lin_diffs, label = '1st Diff.')
plt.plot(UMB[109:, 0], quad_diff2s, label = '2nd Diff.')
plt.ylabel('Absolute Difference (kcal mol$^{-1}$)')
plt.xlabel('$z$-coordinate (nm)')
plt.legend()
plt.tight_layout()
plt.savefig('HairAbs')
plt.show()

plt.plot(mids, hist)
plt.yticks(np.arange(max(hist) + 1))
plt.xlabel('$z$-coordinate (nm)')
plt.ylabel('Number of Spikes')
plt.savefig('HairSpikes')
plt.show()

print(zs)



sds = BOOT[:, 2]

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

plt.savefig('hairPMF')

plt.show()
