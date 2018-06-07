# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:38:07 2018

@author: mike
"""

import matplotlib.pyplot as plt
import numpy as np
import itertools

scores = np.loadtxt("allscores.txt")

scorelist = []
for i in scores:
    scorelist.append(list(i))

loser = []
winner = []

for n in scorelist:
    loser.append(n[0])
    winner.append(n[1])
    

plt.figure(figsize=(18,32))
plt.rc('font', size=18)
plt.title('NSFL Scorigami through S8W4 (Gradient)')
plt.ylabel('Winner Score')
plt.xlabel('Loser Score')
plt.xticks(range(0,35,1))
plt.yticks(range(0,70,1))
plt.grid()
plt.hist2d(loser,winner,bins=(35,70),cmap = "binary",range=[[0,35],[0,70]])
plt.tight_layout()
plt.savefig('scorigami_grad_s8w4.png')
plt.show()

loser_nodup = []
winner_nodup = []

scorelist.sort()
scores_nodup = list(scorelist for scorelist,_ in itertools.groupby(scorelist))
for n in scores_nodup:
    loser_nodup.append(n[0])
    winner_nodup.append(n[1])
    
plt.figure(figsize=(18,32))
plt.rc('font', size=18)
plt.title('NSFL Scorigami through S8W4')
plt.ylabel('Winner Score')
plt.xlabel('Loser Score')
plt.xticks(range(0,35,1))
plt.yticks(range(0,70,1))
plt.grid()
plt.hist2d(loser_nodup,winner_nodup,bins=(35,70),cmap='binary',range=[[0,35],[0,70]])
plt.tight_layout()
plt.savefig('scorigami_s8w4.png')
plt.show()