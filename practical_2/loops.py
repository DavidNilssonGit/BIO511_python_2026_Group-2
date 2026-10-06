#calculate GC content as a percentage of the total sequence length
sequence = "ATGCGTACTTAGCAAT"
gc_count = 0
for base in sequence:
    if base == "G" or base == "C":
        gc_count += 1
gc_content = (gc_count / len(sequence)) * 100
print(gc_content)
#prints 37.5(result)


sequence = "TTAGGCATGCCGATATCGGCTTA"
gc_count = 0
for base in sequence:
    if base == "G" or base == "C":
        gc_count += 1
gc_content = (gc_count / len(sequence)) * 100
print(gc_content)
#prints 47.82608695652174(result)
