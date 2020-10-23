Author information: Naila Cristina Soler Camargo (nailasoler@usp.br)

INPUT files:

1 - The VCF file of each genome that must contain the following information:

column 1: ID or name of the genome.
column 2: positional coordinate of the snp.
column 3: a dot "." or or leave it blank.
column 4: nucleotide at given positional coordinate of the snp on reference genome.
column 5: nucleotide at given positional coordinate of the snp on current genome.


Put all the files (.vcf) in a directory with the creating_snp_db.py algorithm and run the following comand:

python3 creating_snp_db.py


OUTPUT file:

1 - The "snp_db.txt" file, that contains a list of non-redundant snps and its positional coordinates.

NOTES:

- You may run this algorithm for all analyzed genomes at once.




