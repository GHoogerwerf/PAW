# Protein Analysis Workflow
## About
PAW or Protein Analysis Workflow is a pipeline used to automate the analysis of protein families. The pipeline generates a list of homolog protein to the query protein, a high-quality multiple sequence alignment, a phylogenetic tree and a ancestral sequence reconstrunction of the phylogenetic tree.

This pipeline was tested using a Photoactive Yellow protein(PYP) found in Halorodospira Halophila. The test resulted in the discovery of new PYP's and the further aid in PYP research.
## Requirements
- Python 3.0 or higher
- biopython 1.78
- numpy 1.20.3
- pandas 1.3.4
- conda 4.11.0
## Installation
#### Snakemake
```
conda activate base
mamba create -c conda-forge -c bioconda -n snakemake snakemake
```
To activate and test Snakemake:
```
conda activate snakemake
snakemake --help
```
#### MAFFT
```
sudo apt install mafft
```
To install using conda:
```
conda install -c bioconda mafft
```
#### CIAlign
```
pip3 install cialign
```
To install using conda:
```
conda install -c bioconda cialign
```
#### IQ-TREE
```
sudo apt-get install iqtree
```
To install using conda:
```
conda install -c bioconda iqtree
```
#### BLAST
```
sudo apt-get install ncbi-blast+
```
## Usage

Download this github repository and navigate to the BLAST Pipeline/ folder. To test the pipeline simply skip the next step saying to change fasta files and follow all the other steps.

First to peform a protein analysis of your own query protein, alter the protein.fasta file to replace this with your own query protein. Also alter the original_out.fasta file and replace this with your outgroup for the phylogenetic tree and again your own query protein.

After doing this we can run the pipeline. First we have to activate Snakemake.
```
conda activate snakemake
```
After this we can run the pipeline 
```
snakemake -s Snakefile -cores "amount of cores you want to use"
```
This will generate multiple files and plots that can be used to analyse a protein family 

There are also some usefull scripts added that can help with the results. One of these is the position_plot.py script. this script will give the amino acid composition for a certain position in a MSA.
To run the script type the following command and change the argument to the right position and files.
```
ipython position_plot.py "the position you want to see in alignment" "the msa file" "name of the file you want to use for image.png"
```
One other usefull script is the asr_tree.py. This script will show you all the common nodes and thus ancestors between two leaves. Make sure the asr fasta file, asr prediction file and the tree file are in the same folder. to run the script enter the following command and change the arguments to the names of the leaves of interest.
```
ipython asr_tree.py "name of the first leaf" "name of the second leaf"
```
