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


def main():
    record1 = SeqIO.read("protein.fasta", format="fasta")
    record2 = SeqIO.read("co_seq.fasta", format="fasta")
    blastSearch1(record1.seq)
    fastaMake1()
    fastaFilter1()
    blastSearch2(record2.seq)
    fastaMake2()
    fastaFilter2()





def blastSearch1(protein_seq):
    results_all = NCBIWWW.qblast(

                                "blastp", "nr", protein_seq,
                                 matrix_name="PAM250",
                                 gapcosts="14 2",
                                 hitlist_size="10000",
                                 service="psi")
    with open("blast_results/blast_protein.xml", "w") as out_handle:
        out_handle.write(results_all.read())
    results_all.close()

def blastSearch2(protein_seq):
    results_all = NCBIWWW.qblast(

                                "blastp", "nr", protein_seq,
                                 matrix_name="PAM250",
                                 gapcosts="14 2",
                                 hitlist_size="10000",
                                 service="psi")
    with open("blast_results/blast_coseq.xml", "w") as out_handle:
        out_handle.write(results_all.read())
    results_all.close()


def fastaMake1():
    records = []
    blast_results = SearchIO.read("blast_results/blast_protein.xml", "blast-xml")
    for hit in blast_results:
        records.append(hit[0].hit)
    SeqIO.write(records, "blast_results/unfiltered_sequences_protein.fas", "fasta")

def fastaMake2():
    records = []
    blast_results = SearchIO.read("blast_results/blast_coseq.xml", "blast-xml")
    for hit in blast_results:
        records.append(hit[0].hit)
    SeqIO.write(records, "blast_results/unfiltered_sequences_coseq.fas", "fasta")


def fastaFilter1():
    sequences = {}
    for seq_record in SeqIO.parse("blast_results/unfiltered_sequences_protein.fas", "fasta"):
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
    with open("blast_results/filtered_sequences_protein.fas", "w+") as output_file:
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")

def fastaFilter2():
    sequences = {}
    for seq_record in SeqIO.parse("blast_results/unfiltered_sequences_coseq.fas", "fasta"):
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
    with open("blast_results/filtered_sequences_coseq.fas", "w+") as output_file:
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")




if __name__ == "__main__":
    main()


# In[ ]:
