from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

records = SeqIO.parse("dna.fasta", "fasta")

gc_records = []

for record in records:
    g_count = record.seq.count("G")
    c_count = record.seq.count("C")
    gc_percent = 100 * (g_count + c_count) / len(record.seq)
    gc_percent = round(gc_percent, 1)
    new_record = record[:]
    new_record.description = record.description + " GC=" + str(gc_percent) + "%"
    gc_records.append(new_record)

SeqIO.write(gc_records, "dna_with_gc.fasta", "fasta")
