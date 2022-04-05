#!/usr/bin/env python
# coding: utf-8

# In[7]:


identity = []
similarity = []
for line in open("pairwise/alignment.txt"):
    if line.startswith(" Identities"):
        identity.append(line.split(",")[0])
        similarity.append(line.split(",")[1])



# In[21]:




idpercent100_90 = []
idpercent90_80 = []
idpercent80_70 = []
idpercent70_60 = []
idpercent60_50 = []
idpercent50_40 = []
idpercent40_30 = []
idpercent30_20 = []
idpercent20_10 = []
idpercent10_0 = []
idpercent100 = []

for i in identity:
    i = i.split("(")[1][:-2]
    i = int(i)
    if i < 100 and i >= 90:
        idpercent100_90.append(i)
    elif i < 90 and i >= 80:
        idpercent90_80.append(i)
    elif i < 80 and i >= 70:
        idpercent80_70.append(i)
    elif i < 70 and i >= 60:
        idpercent70_60.append(i)
    elif i < 60 and i >= 50:
        idpercent60_50.append(i)
    elif i < 50 and i >= 40:
        idpercent50_40.append(i)
    elif i < 40 and i >= 30:
        idpercent40_30.append(i)
    elif i < 30 and i >= 20:
        idpercent30_20.append(i)
    elif i < 20 and i >= 10:
        idpercent20_10.append(i)
    elif i < 10 and i >= 0:
        idpercent10_0.append(i)
    elif i == 100:
        idpercent100.append(i)





# In[28]:


sipercent100_90 = []
sipercent90_80 = []
sipercent80_70 = []
sipercent70_60 = []
sipercent60_50 = []
sipercent50_40 = []
sipercent40_30 = []
sipercent30_20 = []
sipercent20_10 = []
sipercent10_0 = []
sipercent100 = []

for i in similarity:
    i = i.split("(")[1][:-2]
    i = int(i)
    if i < 100 and i >= 90:
        sipercent100_90.append(i)
    elif i < 90 and i >= 80:
        sipercent90_80.append(i)
    elif i < 80 and i >= 70:
        sipercent80_70.append(i)
    elif i < 70 and i >= 60:
        sipercent70_60.append(i)
    elif i < 60 and i >= 50:
        sipercent60_50.append(i)
    elif i < 50 and i >= 40:
        sipercent50_40.append(i)
    elif i < 40 and i >= 30:
        sipercent40_30.append(i)
    elif i < 30 and i >= 20:
        sipercent30_20.append(i)
    elif i < 20 and i >= 10:
        sipercent20_10.append(i)
    elif i < 10 and i >= 0:
        sipercent10_0.append(i)
    elif i == 100:
        sipercent100.append(i)





# In[59]:


import matplotlib.pyplot as plt
import numpy as np

names = ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]

values1 = [ len(idpercent10_0), len(idpercent20_10), len(idpercent30_20), len(idpercent40_30), len(idpercent50_40),
          len(idpercent60_50), len(idpercent70_60), len(idpercent80_70),
           len(idpercent90_80), len(idpercent100_90), len(idpercent100)-1234]

values2 = [ len(sipercent10_0), len(sipercent20_10), len(sipercent30_20), len(sipercent40_30), len(sipercent50_40),
          len(sipercent60_50), len(sipercent70_60), len(sipercent80_70),
           len(sipercent90_80), len(sipercent100_90), len(sipercent100)-1234]


plt.figure(figsize=(20, 3))
n = 11
X_axis = np.arange(n)
plt.subplot(132)
plt.bar(X_axis - 0.2, values1, 0.5, label = "Identity")
plt.bar(X_axis + 0.2, values2, 0.4, label = "Similarity")
plt.xticks(X_axis,["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
plt.legend()


plt.subplot(133)
plt.plot(names, values1, label="Identity")
plt.plot(names, values2, label="Similarity")
plt.legend()
plt.suptitle("Pairwise identity and similarity distribution")
plt.savefig("pairwise_dis.png")


# In[ ]:
