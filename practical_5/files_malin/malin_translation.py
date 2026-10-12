from Bio import SeqIO

records = SeqIO.parse("dna.fasta", "fasta")

for record in records:
    protein = record.seq.translate()
    print(protein[:10])