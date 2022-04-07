#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

identity = []
similarity = []
for line in open("alignment.txt"):
    if line.startswith(" Identities"):
        identity.append(line.split(",")[0])
        similarity.append(line.split(",")[1])
    


# In[33]:


simlist = []
for i in similarity:
    simlist.append(i.split("(")[1][:-2])
    
idlist = []
for i in identity:
    idlist.append(i.split("(")[1][:-2])





# In[36]:


plt.figure(figsize=(20, 5))
idlist = [int(x) for x in idlist]
idlist.sort()
arr = np.array(idlist)
a = np.hstack((arr,
              arr))

simlist = [int(x) for x in simlist]
simlist.sort()
arr = np.array(simlist)
b = np.hstack((arr,
              arr))

plt.hist(a, bins='auto', label='identity')
plt.hist(b, bins='auto', label='similarity')
plt.title("Pairwise identity and similarity distribution")
plt.legend()
plt.savefig("pairwise_dis.png")







