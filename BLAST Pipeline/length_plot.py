import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO

# get all lengths for every whole sequence
seqlen = []
for seq in SeqIO.parse("seq.fas", "fasta"):
    seqlen.append(len(seq.seq))
    
    
# create the x and y axis for the plot
plt.figure(figsize=(15, 5))
seqlen = [int(x) for x in seqlen]
seqlen.sort()
seqlen = seqlen[:-1]
arr = np.array(seqlen)
a = np.hstack((arr,
              arr))

# generate plot for full length distribution
plt.hist(a, bins="auto")
plt.xlabel("Length of sequence")
plt.ylabel("Number of sequences")
plt.title("Distribution of length in 1234 homologs of Halorhodospira halophila PYP")
plt.savefig("lengths_distribution.png")


# get lengths for every truncated sequences
seqlenB = []
for seq in SeqIO.parse("truncated_sequences.fas", "fasta"):
    seqlenB.append(len(seq.seq))
    
# create the x and y axis for the plot     
plt.figure(figsize=(15, 5))
seqlenB = [int(x) for x in seqlenB]
seqlenB.sort()
#seqlenB = seqlenB[:-1]
arr = np.array(seqlenB)
b = np.hstack((arr,
              arr))

# generate plot for truncated length distribution
plt.hist(b, bins="auto")
plt.xlabel("Length of sequence")
plt.ylabel("Number of sequences")
plt.title("Distribution of length in 1234 truncated homologs of Halorhodospira halophila PYP")
plt.savefig("lengths_distribution_truncated.png")
