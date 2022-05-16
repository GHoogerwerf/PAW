#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
from Bio import Phylo
import numpy as np
import matplotlib.pyplot as plt

# In[4]:


import copy
from io import StringIO

from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PhyloXML import Phylogeny

get_ipython().run_line_magic('matplotlib', 'auto')

tree = Phylo.read("tree", "newick")


# In[22]:

tree_path1 = tree.get_path(str(sys.argv[1]))
nodes1 = []
for path1 in tree_path1:
    #print(path1)
    nodes1.append(str(path1))
    
#print(nodes1)

tree_path2 = tree.get_path(str(sys.argv[2]))
nodes2 = []
for path2 in tree_path2:
    #print(path2)
    nodes2.append(str(path2))
    
#print(nodes2)


# In[24]:


common_nodes = []
for i in nodes1:
    if i in nodes2:
        common_nodes.append(i.split("/")[0])
        print(i)
    else:
        next
        
print(common_nodes)


# In[25]:


from Bio import SeqIO

print("----------------------------------------------------------------------")
for record in SeqIO.parse("ASR.fasta", "fasta"):
    if record.name in common_nodes:
        print(">" + record.description + "\n" + record.seq)
    else:
        next


# In[11]:


import numpy as np
import pandas as pd

df = pd.read_csv("ASR_prediction.fas.state", sep="\t")
#df


# In[26]:

print("----------------------------------------------------------------------")
for index, row in df.iterrows():
    if row["Node"] in common_nodes:
        print(row)
    else:
        next




