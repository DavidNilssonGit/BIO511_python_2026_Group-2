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


## RESULT
# seq1
# original ATGCATGCATGCATGCATGCATGCATGC
# /home/bahja/miniconda3/lib/python3.14/site-packages/Bio/Seq.py:2874: BiopythonWarning: Partial codon, len(sequence) not a multiple of three. 
# Explicitly trim the sequence or add trailing N before translation. 
# This may become an error in future.
#   warnings.warn(
# MHACMHACM
# seq2
# original GATTACAGATTACAGATTACA
# DYRLQIT
# seq3
# original CGCGATATCGCGATATCGCGATATCGCGATATCGCGATATC
# RDIAISRYRD
# seq4
# original TTTAAACCCGGGTTTAAA
# FKPGFK
# seq5
# original GCCGCGGCGCGCCGCGGCGCGCCGCGGCGC
# AAARRGAPRR
# seq6
# original ATATATATATATATATATATAT
# IYIYIYI
# seq7
# original ACGTTGCAACGTTGCAACGTTGCAACGTTGCA
# TLQRCNVATL
# seq8
# original CATGACTGACTGATGCTAGCTAGCTGATCGTACGATC
# HD*LMLAS*S
# seq1_rc
# seq1_rc reverse complement of seq1
# seq2_rc
# seq2_rc reverse complement of seq2
# seq3_rc
# seq3_rc reverse complement of seq3
# seq4_rc
# seq4_rc reverse complement of seq4
# seq5_rc
# seq5_rc reverse complement of seq5
# seq6_rc
# seq6_rc reverse complement of seq6
# seq7_rc
# seq7_rc reverse complement of seq7
# seq8_rc
# seq8_rc reverse complement of seq8
