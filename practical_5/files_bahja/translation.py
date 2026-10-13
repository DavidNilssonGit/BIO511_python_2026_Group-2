from Bio import SeqIO

records = SeqIO.parse("dna.fasta", "fasta")

for record in records:
    print(record.id)
    print("original", record.seq)
    t_protein = record.seq.translate()

    print (t_protein[:10])

controll = SeqIO.parse("dna_rc.fasta", "fasta")

for record in controll:
    print(record.id)
    print(record.description)
    
