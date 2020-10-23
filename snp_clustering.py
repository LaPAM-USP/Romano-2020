#!/usr/bin/env python3

#Author information: Naila Cristina Soler Camargo (nailasoler@usp.br)

import glob

#output
out95 = open('snps95.xlsx', 'w')


#preparing snp_db
snp_db = open('snp_db.txt', 'r')
snp_db = snp_db.read()
snp_db = snp_db.split('\n')

del snp_db[-1]


#snp search

n = 1
for snp in snp_db:

	count = 0
	for file in glob.glob('*.vcf'):

		strain = open(file, 'r')
		strain = strain.read()
		strain = strain.split('\n')

		del strain[-1]

		for line in strain:

			if snp in line:

				count+=1
				this_line = line


	if count >= 69:
		snp_line = this_line + '\n'
		out95.writelines(snp_line)


	print('Searching SNP ' + str(n) + '...')
	n+=1


out95.close()


	
