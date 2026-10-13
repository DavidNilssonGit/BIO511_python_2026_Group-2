from Bio import SeqIO
from Bio.SeqRecord import SeqRecord   ## Stores the sequence plus the information about it

records = SeqIO.parse("dna.fasta", "fasta")

reverse_complement = []

for record in records:
    print("ID", record.id)
    print("Original", record.seq)
    rc = record.seq.reverse_complement()  #skapar reverse transkript av sekvensen
    new_rc_seq = SeqRecord(rc, id=record.id +"_rc",
    description = "reverse complement of " + record.id)  # skapar ett seqrec och dess deskription
    print("New ID", new_rc_seq.id)
    print ("reverse complement:", rc)
   

    reverse_complement.append(new_rc_seq)

SeqIO.write(reverse_complement, "dna_rc.fasta", "fasta")


###Result
# seq1_rc reverse complement of seq1
# GCATGCATGCATGCATGCATGCATGCAT
# >seq2_rc reverse complement of seq2
# TGTAATCTGTAATCTGTAATC
# >seq3_rc reverse complement of seq3
# GATATCGCGATATCGCGATATCGCGATATCGCGATATCGCG
# >seq4_rc reverse complement of seq4
# TTTAAACCCGGGTTTAAA
# >seq5_rc reverse complement of seq5
# GCGCCGCGGCGCGCCGCGGCGCGCCGCGGC
# >seq6_rc reverse complement of seq6
# ATATATATATATATATATATAT
# >seq7_rc reverse complement of seq7
# TGCAACGTTGCAACGTTGCAACGTTGCAACGT
# >seq8_rc reverse complement of seq8
# GATCGTACGATCAGCTAGCTAGCATCAGTCAGTCATG