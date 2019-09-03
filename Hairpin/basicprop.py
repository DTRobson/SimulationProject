#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:53:26 2019

@author: k1899674
"""

import MDAnalysis as md

u = md.Universe('min.gro')

protein = u.select_atoms('protein')

res = protein.residues

for i in res:
    print(i)