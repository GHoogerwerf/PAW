#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Show plots as part of the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Show images inline
from IPython.display import Image

# Standard library packages
import io
import os

# Import Biopython modules to interact with KEGG
from Bio import SeqIO
from Bio.KEGG import REST
from Bio.KEGG.KGML import KGML_parser
from Bio.Graphics.KGML_vis import KGMLCanvas

# Import Pandas, so we can use dataframes
import pandas as pd

# A bit of code that will help us display the PDF output
def PDF(filename):
    return HTML('<iframe src=%s width=700 height=350></iframe>' % filename)

# Some code to return a Pandas dataframe, given tabular text
def to_df(result):
    return pd.read_table(io.StringIO(result), header=None)


# In[35]:


from Bio import SeqIO


blast = []
coblast = []

for seq in SeqIO.parse("blast_kegg.fas", "fasta"):
    for coseq in SeqIO.parse("co_blast_kegg.fas", "fasta"):
        if seq.description.split(":")[0] in coseq.description.split(":")[0]:
            comb = seq.description + "*" + coseq.description
            blast.append(comb.split("*")[0].split("_")[0] + "_" + comb.split("-")[0].split("_")[1])
            coblast.append(comb.split("*")[1].split(" ")[0])
        else:
            next
            
position_blast = []
for seq in blast:
    try:
        
        query = seq
        result = REST.kegg_get(query).read()
        a = result.split("\n")
        for pos in a:
            if "POSITION" in pos:
                posS = pos.split("    ")[1]
                if "complement" in pos:
                    position_blast.append(posS.split("complement(")[1][:-1].split("..")[1])
                elif ":" in pos:
                    position_blast.append(posS.split(":")[1].split("..")[1])
                elif "Unknown" in pos:
                    position_blast.append(posS)
                else:
                    position_blast.append(posS.split("..")[1])
            else:
                next
    except:
        position_blast.append("UNKNOWN")
        


position_coblast = []
for seq in coblast:
    try:
        
        query = seq
        result = REST.kegg_get(query).read()
        a = result.split("\n")
        for pos in a:
            if "POSITION" in pos:
                posS = pos.split("    ")[1]
                if "complement" in pos:
                    position_coblast.append(posS.split("complement(")[1][:-1].split("..")[1])
                elif ":" in pos:
                    position_coblast.append(posS.split(":")[1].split("..")[1])
                elif "Unknown" in pos:
                    position_coblast.append(posS)
                else:
                    position_coblast.append(posS.split("..")[1])
            else:
                next
    except:
        position_coblast.append("UNKNOWN")
        
        

        

        
df = pd.DataFrame(
    {'BLAST': blast,
     'coBLAST': coblast,
     'BLAST end pos': position_blast,
     'coBLAST begin pos': position_coblast
    })

df.to_excel("co_blast_distance.xlsx")


# In[ ]:





# In[ ]:





# In[ ]:




