#!/usr/bin/env python3

#Author information: Naila Cristina Soler Camargo (nailasoler@usp.br)

import glob

#output
out = open('snp_db.txt', 'w')


#nr database with snps and coordenates
snp_db = []
s = 0

for file in glob.glob('*.vcf'):

	strain = open(file, 'r')
	strain = strain.read()
	strain = strain.split('\n')

	del strain[-1]


	for line in strain:

		item = line.split('\t')

		coord_snp = item[1] + '\t' + item[2] + '\t' + item[3] + '\t' + item[4]

		if coord_snp not in snp_db:

			snp_db.append('')
			snp_db[s] = coord_snp
			s+=1

for item in snp_db:

	out.writelines(item)
	out.writelines('\n')
	
