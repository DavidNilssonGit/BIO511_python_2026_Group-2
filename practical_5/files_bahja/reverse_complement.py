from Bio import SeqIO
from Bio.SeqRecord import SeqRecord   ## Stores the sequence plus the information about it
from Bio.Seq import Seq

records = SeqIO.parse("dna.fasta", "fasta")

reverse_complement = []

for record in records:
    print("Original", record.seq)
    rc = record.seq.reverse_complement()  #skapar reverse transkript av sekvensen
    new_rc_seq = SeqRecord(rc, id=record.id +"_rc",
    des = "reverse complement of " + record.id)  # skapar ett seqrec och dess deskription
    print ("reverse complement:", rc)

    reverse_complement.append(new_rc_seq)

SeqIO.write(reverse_complement, "dna_rc.fasta", "fasta")