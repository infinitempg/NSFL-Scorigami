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
    

plt.figure(figsize=(32,18))
plt.rc('font', size=18)
plt.title('NSFL Scorigami (S8W4)')
plt.xlabel('Winner Score')
plt.ylabel('Loser Score')
plt.yticks(range(0,35,1))
plt.xticks(range(0,70,1))
plt.grid()
plt.hist2d(winner,loser,bins=(70,35),cmap = "binary",range=[[0,70],[0,35]])
plt.tight_layout()
plt.savefig('scorigami_grad.png')
plt.show()

loser_nodup = []
winner_nodup = []

scorelist.sort()
scores_nodup = list(scorelist for scorelist,_ in itertools.groupby(scorelist))
for n in scores_nodup:
    loser_nodup.append(n[0])
    winner_nodup.append(n[1])
    
plt.figure(figsize=(32,18))
plt.rc('font', size=18)
plt.title('NSFL Scorigami (S8W4)')
plt.xlabel('Winner Score')
plt.ylabel('Loser Score')
plt.yticks(range(0,35,1))
plt.xticks(range(0,70,1))
plt.grid()
plt.hist2d(winner_nodup,loser_nodup,bins=(70,35),cmap='binary',range=[[0,70],[0,35]])
plt.tight_layout()
plt.savefig('scorigami.png')
plt.show()