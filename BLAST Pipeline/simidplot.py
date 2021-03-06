#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# for loop puts all the similarity and identity scores in lists

identity = []
similarity = []
for line in open("alignment.txt"):
    if line.startswith(" Identities"):
        identity.append(line.split(",")[0])
        similarity.append(line.split(",")[1])

for line in open("alignment.txt"):
    if 'sequences;' in line:
        y = int(line.split(' ')[11].replace(",", ""))
        t = str(y)
    


# In[33]:


simlist = []
for i in similarity:
    simlist.append(i.split("(")[1][:-2])
    
idlist = []
for i in identity:
    idlist.append(i.split("(")[1][:-2])





# In[36]:
# generating two plots one for identiy and one for similarity
# putting these plots together on one histogram and saving this histogram as a file

plt.figure(figsize=(20, 5))
idlist = [int(x) for x in idlist]
idlist.sort()
idlist = idlist[:-y]
arr = np.array(idlist)
a = np.hstack((arr,
              arr))

simlist = [int(x) for x in simlist]
simlist.sort()
simlist = simlist[:-y]
arr = np.array(simlist)
b = np.hstack((arr,
              arr))

plt.hist(a, bins='auto', label='identity')
plt.hist(b, bins='auto', label='similarity')
plt.title("Pairwise identity and similarity distribution in " + t + " homologs)
plt.legend()
plt.savefig("pairwise_dis.png")







