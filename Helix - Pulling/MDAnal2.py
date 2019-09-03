# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:12:25 2019

@author: Robbo
"""

################ Import Relevant Modules for Anaylsis and Plotting #####################


import MDAnalysis as md
import MDAnalysis.analysis.distances as ds
import numpy as np
import matplotlib.pyplot as plt


##################################################################################

def draw_gauss(mu, var, xs):
    diffs = xs - mu
    d2s = diffs ** 2
    exponents = - 1 / (2 * var) * d2s
    curve = np.exp(exponents)
    coeff = 1 / np.sqrt(2 * np.pi * var)
    gauss = coeff * curve
    return gauss
    

def find_mids(xs):
    mids = np.empty(len(xs) - 1)
    diffs = np.empty(len(xs) - 1)
    for i in range(len(xs)-1):
        mids[i] = (xs[i] + xs[i+1])/2
        diffs[i] = xs[i+1] - xs[i]
    return mids, diffs


############################# Load the Trajectories ##########################################

u1 = md.Universe('pull-v-0-1.gro', 'pull-v-0-1-c.xtc')
at1 = u1.select_atoms("protein")
res1_1 = at1.select_atoms("resid 8439 and name CA")
res2_1 = at1.select_atoms("resid 8451 and name CA")

u2 = md.Universe('pull-v-0-1.gro','pull-v-0-01-c.xtc')
at2 = u2.select_atoms("protein")
res1_2 = at2.select_atoms("resid 8439 and name CA")
res2_2 = at2.select_atoms("resid 8451 and name CA")

u3 = md.Universe('pull-v-0-001.gro','pull-v-0-001-c.xtc')
at3 = u3.select_atoms("protein")
res1_3 = at3.select_atoms("resid 8439 and name CA")
res2_3 = at3.select_atoms("resid 8451 and name CA")

u4 = md.Universe('pull-v-0-0001.gro','pull-v-0-0001-c.xtc')
at4 = u4.select_atoms("protein")
res1_4 = at4.select_atoms("resid 8439 and name CA")
res2_4 = at4.select_atoms("resid 8451 and name CA")

################################################################################################

Rgyr1 = []
Rgyr2 = []
Rgyr3 =[]
Rgyr4 = []

end_to_end_1_norm = []
end_to_end_2_norm = []
end_to_end_3_norm = []
end_to_end_4_norm = []


for ts in u1.trajectory:
    Rgyr1.append((u1.trajectory.time, at1.radius_of_gyration()))
    xyz = ds.dist(res1_1, res2_1)
    end_to_end_1_norm.append((u1.trajectory.time, xyz[2,0]))

for ts in u2.trajectory:
    Rgyr2.append((u2.trajectory.time, at2.radius_of_gyration()))
    xyz = ds.dist(res1_2, res2_2)
    end_to_end_2_norm.append((u2.trajectory.time, xyz[2,0]))

for ts in u3.trajectory:
    Rgyr3.append((u3.trajectory.time, at3.radius_of_gyration()))
    xyz = ds.dist(res1_3, res2_3)
    end_to_end_3_norm.append((u3.trajectory.time, xyz[2,0]))


for ts in u4.trajectory:
    Rgyr4.append((u4.trajectory.time, at4.radius_of_gyration()))
    xyz = ds.dist(res1_4, res2_4)
    end_to_end_4_norm.append((u4.trajectory.time, xyz[2,0]))

Rgyr1 = np.array(Rgyr1)
Rgyr2 = np.array(Rgyr2)
Rgyr3 = np.array(Rgyr3)
Rgyr4 = np.array(Rgyr4)

Rgyr1 /= 10
Rgyr2 /= 10
Rgyr3 /= 10
Rgyr4 /= 10

end_to_end_1_norm = np.array(end_to_end_1_norm)/10
end_to_end_2_norm = np.array(end_to_end_2_norm)/10
end_to_end_3_norm = np.array(end_to_end_3_norm)/10
end_to_end_4_norm = np.array(end_to_end_4_norm)/10

#####################################################################################################
plt.plot(Rgyr1[:,0], Rgyr1[:,1], label ='0.1 nm/ps')

plt.xlabel('Time (ps)')
plt.ylabel('Radius of Gyration (nm)')

plt.tight_layout()

plt.savefig('RG1')

plt.show()

#####################################################

plt.plot(Rgyr2[:,0], Rgyr2[:,1], label ='0.01 nm/ps')

plt.xlabel('Time (ps)')
plt.ylabel('Radius of Gyration (nm)')

plt.tight_layout()

plt.savefig('RG2')

plt.show()

###########################################################

plt.plot(Rgyr3[:,0], Rgyr3[:,1], label ='0.001 nm/ps')

plt.xlabel('Time (ps)')
plt.ylabel('Radius of Gyration (nm)')

plt.tight_layout()

plt.savefig('RG3')

plt.show()

##############################################################

plt.plot(Rgyr4[:,0], Rgyr4[:,1], label ='0.0001 nm/ps')

plt.xlabel('Time (ps)')
plt.ylabel('Radius of Gyration (nm)')

plt.tight_layout()

plt.show()

#################################################################

plt.plot(end_to_end_1_norm[:,0], end_to_end_1_norm[:,1], label = '1')


plt.xlabel('Time (ps)')
plt.ylabel('End-To-End CA Distance (nm)')

plt.tight_layout()

plt.show()

####################################################################

plt.plot(end_to_end_2_norm[:,0], end_to_end_2_norm[:,1], label = '2')


plt.xlabel('Time (ps)')
plt.ylabel('End-To-End CA Distance (nm)')

plt.tight_layout()

plt.show()

#####################################################################

plt.plot(end_to_end_3_norm[:,0], end_to_end_3_norm[:,1], label = '3')


plt.xlabel('Time (ps)')
plt.ylabel('End-To-End CA Distance (nm)')

plt.tight_layout()

plt.show()

#####################################################################

plt.plot(end_to_end_4_norm[:,0], end_to_end_4_norm[:,1], label = '4')


plt.xlabel('Time (ps)')
plt.ylabel('End-To-End CA Distance (nm)')

plt.tight_layout()

plt.show()

#####################################################################

len1 = len(end_to_end_1_norm)
len2 = len(end_to_end_2_norm)
len3 = len(end_to_end_3_norm)
len4 = len(end_to_end_4_norm)

mu1 = np.mean(end_to_end_1_norm[:,1])
var1 = np.var(end_to_end_1_norm[:,1])
sd1 = np.sqrt(var1)

mu2 = np.mean(end_to_end_2_norm[:,1])
var2 = np.var(end_to_end_2_norm[:,1])
sd2 = np.sqrt(var2) 

mu3 = np.mean(end_to_end_3_norm[:,1])
var3 = np.var(end_to_end_3_norm[:,1])
sd3 = np.sqrt(var3)

mu4 = np.mean(end_to_end_4_norm[:,1])
var4 = np.var(end_to_end_4_norm[:,1])
sd4 = np.sqrt(var4)

vals1 = np.random.normal(mu1, sd1, size = 5000000)
vals2 = np.random.normal(mu2, sd2, size = 5000000)
vals3 = np.random.normal(mu3, sd3, size = 5000000)
vals4 = np.random.normal(mu4, sd4, size = 5000000)



###################################################################################################

'''h1, bins1 = np.histogram(end_to_end_1_norm[:,1], bins = int(len1/2))

h2, bins2 = np.histogram(end_to_end_2_norm[:,1], bins = int(len2/2))

h3, bins3 = np.histogram(end_to_end_3_norm[:,1], bins = int(len3/2))

h4, bins4 = np.histogram(end_to_end_4_norm[:,1], bins = int(len4/2))

mids1, diffs1 = find_mids(bins1)
mids2, diffs2 = find_mids(bins2)
mids3, diffs3 = find_mids(bins3)
mids4, diffs4 = find_mids(bins4)

x1 = np.linspace(mids1[0] -2, mids1[-1] + 2, num = 500)
x2 = np.linspace(mids2[0] - 2, mids2[-1] + 2, num = 500)
x3 = np.linspace(mids3[0] - 2, mids3[-1] + 2, num = 500)
x4 = np.linspace(mids4[0] - 2, mids4[-1] + 2, num = 500)

d1 = (max(x1)- min(x1))/len(x1)
d2 = (max(x2)- min(x2))/len(x2)
d3 = (max(x3)- min(x3))/len(x3)
d4 = (max(x4)- min(x4))/len(x4)

g1 = draw_gauss(mu1, var1, x1)
g2 = draw_gauss(mu2, var2, x2)
g3 = draw_gauss(mu3, var3, x3)
g4 = draw_gauss(mu4, var4, x4)

g1 *= d1
g2 *= d2 
g3 *=  d3 
g4 *=  d4 

g1 *= len1
g2 *= len2
g3 *= len3
g4 *= len4

plt.hist(end_to_end_1_norm[:,1], bins = int(len1/2), label = 'data')
plt.plot(x1, g1, '--', label = 'Gaussian')
plt.xlabel('End-To-End CA Distance (nm)')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()

plt.hist(end_to_end_2_norm[:,1], bins = int(len2/2), label = 'data')
plt.plot(x2, g2, '--', label = 'Gaussian')
plt.xlabel('End-To-End CA Distance (nm)')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()

plt.hist(end_to_end_3_norm[:,1], bins = int(len3/2), label = 'data')
plt.plot(x3, g3, '--', label = 'Gaussian')
plt.xlabel('End-To-End CA Distance (nm)')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()


plt.hist(end_to_end_4_norm[:,1], bins = int(len4/2), label = 'data')
plt.plot(x4, g4, '--', label = 'Gaussian')
plt.xlabel('End-To-End CA Distance (nm)')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()'''


xs = np.linspace(min(Rgyr4[:,1]**2), max(Rgyr4[:,1]**2))

plt.plot(Rgyr4[:,1]**2, end_to_end_4_norm[:,1]**2, '.')
plt.plot(xs, 6 * xs, ':')

plt.show()
