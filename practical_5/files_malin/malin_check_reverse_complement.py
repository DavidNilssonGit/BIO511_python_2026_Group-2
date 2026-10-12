from Bio import SeqIO

records = SeqIO.parse("dna_rc.fasta", "fasta")
for record in records:
    print(record.id)
    print(record.description)