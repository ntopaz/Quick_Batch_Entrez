from Bio import SeqIO, Entrez

Entrez.email = raw_input('Enter NCBI email: ')
my_seqs = raw_input('Input File: ')
#accepts fasta or clustal input

seqs_format = raw_input('Output format: fasta (f) or TinySeq XML (t): ')
#input f for fasta or t for tinyseq_XML

output_file = open("output","w")
count = 0

#retrieves information using GI number based on selected format type and writes to file
if seqs_format == ('f'):
	for record in SeqIO.parse(my_seqs, 'fasta'):
		split_id = str.split(record.id)
		my_gi = str.split(split_id[0], '|')
		handle = Entrez.efetch(db="protein", id=my_gi[1],rettype = "fasta",retmode= "text")
		output_file.write(handle.read().strip() +"\n")
		count = count + 1
if seqs_format == ('t'):
	for record in SeqIO.parse(my_seqs, 'fasta'):
		split_id = str.split(record.id)
		my_gi = str.split(split_id[0], '|')
		handle = Entrez.efetch(db="protein", id=my_gi[1],rettype = "fasta",retmode= "xml")
		output_file.write(handle.read().strip() +"\n")
		count = count + 1

print (str(count) + " sequences saved to output")
output_file.close()
raw_input()
	
	

	
