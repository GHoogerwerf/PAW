# Protein Analysis Workflow
## Requirements
- Python 3.0 or higher
- biopython 1.78
- numpy 1.20.3
- pandas 1.3.4
- conda 4.11.0
## Installation
#### Snakemake
```
$ conda activate base
$ mamba create -c conda-forge -c bioconda -n snakemake snakemake
```
To activate and test Snakemake:
```
$ conda activate snakemake
$ snakemake --help
```
#### MAFFT
```
$ sudo apt install mafft
```
To install using conda:
```
conda install -c bioconda mafft
```
#### CIAlign
```
$ pip3 install cialign
```
To install using conda:
```
$ conda install -c bioconda cialign
```
#### IQ-TREE
```
$ sudo apt-get install iqtree
```
To install using conda:
```
$ conda install -c bioconda iqtree
```
#### BLAST
```
$ sudo apt-get install ncbi-blast+
```
## Usage

Download this github repository and navigate to the BLAST Pipeline/ folder. To test the pipeline simply skip the next step saying to change fasta files and follow all the other steps.

First to peform a protein analysis of your own query protein, alter the protein.fasta file to replace this with your own query protein. Also alter the original_out.fasta file and replace this with your outgroup for the phylogenetic tree and again your own query protein.

After doing this we can run the pipeline. First we have to activate Snakemake.
```
$ conda activate snakemake
```
After this we can run the pipeline 
```
$ snakemake -s Snakefile -cores ["amount of cores you wan to use]
```
This will generate multiple files and plots that can be used to analyse a protein family 

There are also some usefull scripts added that can help with the results. One of these is the position_plot.py script. this script will give the amino acid composition for a certain position in a MSA.
To run the script type the following command and change the argument to the right position and files.
```
ipython position_plot.py [the position you want to see in alignment] [the msa file] ["name of the file you want to use for image".png] 
```
