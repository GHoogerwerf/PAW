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
## Usage
