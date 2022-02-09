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
    #get_ipython().run_line_magic('matplotlib', 'auto')
    record1 = SeqIO.read("protein.fasta", format="fasta")
    record2 = SeqIO.read("consensus_output/cleaned_consensus_msa_consensus.fasta",
                        format="fasta")
    mini = len(record1.seq) - 25
    maxi = 20
    blastSearch(record2.seq)
    fastaMake()
    fastaFilter()
    wholeSequences()
    truncateSequences(mini, maxi)




def blastSearch(protein_seq):
    #record = SeqIO.read(protein_seq, format="fasta")
    results_all = NCBIWWW.qblast(

                                "blastp", "nr", protein_seq,
                                 matrix_name="PAM250",
                                 gapcosts="14 2",
                                 hitlist_size="10000",
                                 service="psi")
    with open("truncate/blast.xml", "w") as out_handle:
        out_handle.write(results_all.read())
    results_all.close()




def fastaMake():
    records = []
    blast_results = SearchIO.read("truncate/blast.xml", "blast-xml")
    for hit in blast_results:
        records.append(hit[0].hit)
    SeqIO.write(records, "truncate/unfiltered_sequences.fas", "fasta")




def fastaFilter():
    sequences = {}
    for seq_record in SeqIO.parse("truncate/unfiltered_sequences.fas", "fasta"):
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
    with open("truncate/filtered_sequences.fas", "w+") as output_file:
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")




def wholeSequences():
    t = 0
    for record in SeqIO.parse("truncate/filtered_sequences.fas", "fasta"):
        try:
            t +=1
            sp = record.id.split('|')
            if len(sp[2]) < 2:
                s = sp[0] + "|" + sp[1] + "|" + sp[2]
            else:
                s = sp[0] + "|" + sp[1]
            Entrez.email = "Your.Name.Here@example.org"
            handle = Entrez.efetch(db="protein", id=s, retmode="xml")
            bs = Entrez.read(handle)
            seq = bs[0]['GBSeq_sequence']
            f = open("truncate/whole_sequence.fas", "a")
            f.write(">" + record.description + "\n" + seq.upper() + "\n")
            f.close()
            if t == 100:
                time.sleep(50)
                t = 0
            else:
                time.sleep(1)
        except:
            pass




def truncateSequences(minim, maxim_over):
    alignment = SeqIO.parse(open("truncate/whole_sequence.fas"), "fasta")
    align_hit = SeqIO.parse("truncate/filtered_sequences.fas", "fasta")
    mylist = []
    with open("truncate/truncated_sequences.fas", "w+") as output_file:
        for record, record_hit in zip(alignment, align_hit):
            search = str(record_hit.seq)
            search = search.replace("-", "")
            length = len(search)
            protein_seq = Seq(str(record.seq))
            s_sub = protein_seq.find(search)
            if len(record.seq) < minim:
                continue
            else:
                if s_sub < maxim_over:
                    output_file.write(">" + str(record.description) + "\n" + str(record.seq[s_sub - s_sub:s_sub + length + maxim_over]) + "\n")
                else:
                    output_file.write(">" + str(record.description) + "\n" + str(record.seq[s_sub - maxim_over:s_sub + length + maxim_over]) + "\n")



if __name__ == "__main__":
    main()


# In[ ]:
