from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

records = SeqIO.parse("dna.fasta", "fasta")

rc_records = []
for record in records:
    rc_seq = record.seq.reverse_complement()
    new_record = SeqRecord(rc_seq, id=record.id + "_rc")
    new_record.description = "reverse complement of " + record.id
    rc_records.append(new_record)

SeqIO.write(rc_records, "dna_rc.fasta", "fasta")