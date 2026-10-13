from Bio import SeqIO

records = SeqIO.parse("dna.fasta", "fasta")

for record in records:
    print(record.id)  ## sequence id
    print(record.seq)  ## Sequence itself
    print(len(record.seq))  ## Sequence length
    print(record.seq[:10]) ## first ten bases

##RESULTS
# seq1
# ATGCATGCATGCATGCATGCATGCATGC
# 28
# ATGCATGCAT
# seq2
# GATTACAGATTACAGATTACA
# 21
# GATTACAGAT
# seq3
# CGCGATATCGCGATATCGCGATATCGCGATATCGCGATATC
# 41
# CGCGATATCG
# seq4
# TTTAAACCCGGGTTTAAA
# 18
# TTTAAACCCG
# seq5
# GCCGCGGCGCGCCGCGGCGCGCCGCGGCGC
# 30
# GCCGCGGCGC
# seq6
# ATATATATATATATATATATAT
# 22
# ATATATATAT
# seq7
# ACGTTGCAACGTTGCAACGTTGCAACGTTGCA
# 32
# ACGTTGCAAC
# seq8
# CATGACTGACTGATGCTAGCTAGCTGATCGTACGATC
# 37
# CATGACTGAC