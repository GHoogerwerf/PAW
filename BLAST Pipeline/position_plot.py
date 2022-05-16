#!/usr/bin/env python
# coding: utf-8
from __future__ import division


from Bio import SeqIO
from Bio.Seq import Seq
from collections import Counter
import sys

# generates list of every amino acid on certain position and 
x = int(sys.argv[1])
mylist = []
align = SeqIO.parse(str(sys.argv[2]), "fasta")
count = 0
for i in align:
    mylist.append(i.seq[x - 1])
    count = count + 1

# generates disctionairy witb percentage of every amino acid of a certain position
dic = Counter(mylist)
c = dict(dic)
import matplotlib.pyplot as plt
plt.switch_backend('agg')

labels = []
sizes = []

for x, y in c.items():
    labels.append(x)
    sizes.append(y)

# Plot. creates plot with percentage of every amino acid on certain position in MSA
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend(loc="best")
plt.savefig(str(sys.argv[3]))

# prints out the percentages of all the amino acids on a certain position
values = c.values()
total = sum(values)
percent = []
for i in values:
    percent.append(round(i / total * 100, 2))
print(percent)






