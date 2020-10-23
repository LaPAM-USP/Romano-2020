Author information: Naila Cristina Soler Camargo (nailasoler@usp.br)

INPUT files:

1 - The "snp_db.txt" output from creating_snp_db.py algorithm.
2 - The VCF file of each genome that must contain the following information:

column 1: ID or name of the genome.
column 2: positional coordinate of the snp.
column 3: a dot "." or or leave it blank.
column 4: nucleotide at given positional coordinate of the snp on reference genome.
column 5: nucleotide at given positional coordinate of the snp on current genome.


Put the files in a directory with snp_clustering.py algorithm and run the following comand:

python3 snp_clustering.py


OUTPUT files:

1 - The "snps95.xlsx" file, that contains a list of snps and positional coordinates from core 95%.

NOTES:

- You may run this algorithm for all analyzed genomes at once.



