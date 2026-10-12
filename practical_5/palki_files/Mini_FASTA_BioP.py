import gc
import sys
import os
from pathlib import Path
from Bio import SeqIO

## Change path to the working directory ##
os.chdir("/Users/palkidas/My_Python_Course/BIO511_python_2026_Group-2/practical_5/palki_files/")

records = list( SeqIO.parse("dna.fasta", "fasta") )
# print(records)

for record in records:
    print(record.id)
    # print(record.description)
    # print(record.name)
    # print(record.annotations)
    # print(record.features)
    print(record.seq)
    print(f'Length: {len(record.seq)}')
    print(f'first 10 bases: {record.seq[:10]}')
    # print("\n")  # Add a newline for better readability§

## Reverse + complement ##

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

input_fasta = "dna.fasta"
output_fasta = "dna_rc.fasta"

reverse_records = []

for record in SeqIO.parse(input_fasta, "fasta"):
    rc_seq = record.seq.reverse_complement()

    rc_record = SeqRecord(
        rc_seq,
        id=record.id + "_rc",
        description=f"reverse complement of {record.id}"
    )

    reverse_records.append(rc_record)

SeqIO.write(reverse_records, output_fasta, "fasta")


## GC percentage calculation ##

input_fasta = "dna.fasta"
output_fasta = "dna_with_gc.fasta"

gc_pct = []

for record in SeqIO.parse(input_fasta, "fasta"):
    gc = (record.seq.count("G") + record.seq.count("C")) / len(record.seq) * 100

    gc_record = SeqRecord(
        Seq(str(round(gc, 2))),
        id=record.id,
        description=f"GC percentage of {record.id}"
    )

    gc_pct.append(gc_record)

SeqIO.write(gc_pct, output_fasta, "fasta")


## Translation ##

# 1. Translate each DNA sequence and print first 10 amino acids
for record in SeqIO.parse("dna.fasta", "fasta"):
    protein = record.seq.translate()
    print(record.id, protein[:10])

# 2. Read dna_rc.fasta and check IDs/descriptions
for record in SeqIO.parse("dna_rc.fasta", "fasta"):
    print(record.id)
    print(record.description)