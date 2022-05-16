#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Bio import AlignIO
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SearchIO
from Bio import Entrez
from collections import Counter
import time
import sys

# Main function creates input variables for other functions.
# These variables include simgle protein sequence files in fasta format 
# and the maximum and minimum amount of characters a sequence can have.
def main():
    record = SeqIO.read("protein.fasta", format="fasta")
    blastSearch(record.seq)
    fastaMake()
    fastaFilter()
 



# blastSearch functions performs a BLAST search in the NCBI database with specific paramaters
# and writes the results in a XML file.
def blastSearch(protein_seq):
    results_all = NCBIWWW.qblast(

                                "blastp", "nr", protein_seq,
                                 matrix_name="PAM250",
                                 gapcosts="14 2",
                                 hitlist_size="10000",
                                 service="psi")
    with open("consensus_blast/blast.xml", "w") as out_handle:
        out_handle.write(results_all.read())
    results_all.close()



# fastaMake function parses through BLAST xml file
# and writes the sequences obtained to a new file in Fasta format.
def fastaMake():
    records = []
    blast_results = SearchIO.read("consensus_blast/blast.xml", "blast-xml")
    for hit in blast_results:
        records.append(hit[0].hit)
    SeqIO.write(records, "consensus_blast/unfiltered_sequences.fas", "fasta")



# fastaFilter function filters the file from mutant and duplicates
# and puts the other sequences in a new file in Fasta format.
def fastaFilter():
    sequences = {}
    for seq_record in SeqIO.parse("consensus_blast/unfiltered_sequences.fas", "fasta"):
        sequence = str(seq_record.seq).upper()
        descript = str(seq_record.description).lower()
        if (
            (float(sequence.count("N")) / float(len(sequence))) * 100 <= 1000
            and descript.find("mutant") <= 0
        ):
            if sequence not in sequences:
                sequences[sequence] = seq_record.description
            else:
                sequences[sequence] = seq_record.description
    with open("consensus_blast/filtered_sequences.fas", "w+") as output_file:
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")





if __name__ == "__main__":
    main()
