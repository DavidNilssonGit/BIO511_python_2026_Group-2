from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

records = SeqIO.parse("dna.fasta", "fasta")
gc_record = []

for record in records:
    g_record = record.seq.count("G")
    c_record = record.seq.count("C")
    g_c_records = 100 * ((g_record + c_record) / len(record.seq))
    gc_round_record = (round(g_c_records, 1))
    copy_record = SeqRecord(record.seq, id=record.id, description = f"gc={gc_round_record}%")

    gc_record.append(copy_record)

    print(record.id)
SeqIO.write(gc_record, "dna_with_gc.fasta", "fasta")




