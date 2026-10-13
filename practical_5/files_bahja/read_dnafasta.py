from Bio import SeqIO

records = SeqIO.parse("dna.fasta", "fasta")

for record in records:
    print(record.id)  ## sequence id
    print(record.seq)  ## Sequence itself
    print(len(record.seq))  ## Sequence length
    print(record.seq[:10]) ## first ten bases