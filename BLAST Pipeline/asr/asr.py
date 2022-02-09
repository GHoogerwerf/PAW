#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

df = pd.read_table("final_msa/final_msa.fasta.state")

with open("asr/asr.fas", "w") as out:
    node_n = ""
    state_n = ""
    for index, row in df.interrows():
        if row["Node"] != node_n:
            out.write("\n" + ">" + row["Node"] + "\n")
            if row["State"] != "-":
                out.write(row["State"])
            else:
                next
            node = row["Node"]
        elif row["Node"] != node:
            if row["State"] != "-":
                out.write(row["State"] + "\n")
            else:
                next
        elif row["Node"] == node:
            if row["State"] != "-":
                out.write(row["State"])
            else:
                next
        node_n = row["Node"]
