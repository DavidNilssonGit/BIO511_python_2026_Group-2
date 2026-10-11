from Bio.Seq import Seq

def codons(sequence_file):
    """Read a FASTA file and return a dictionary of codons for each sequence."""

    # First we read each sequence and store it in a dictionary
    sequences = {}

    # Open the file
    with open(sequence_file) as fasta_file:
        # Read the file line by line
        for row in fasta_file:
            row = row.strip()

            # If the line starts with '>', it is a header
            if row.startswith('>'):
                header = row[1:]
                sequences[header] = ""

            # Otherwise, add the row to the current sequence
            else:
                sequences[header] += row

    # Split each sequence into codons
    sequence_codons = {}

    for header, sequence in sequences.items():
        codon_list = []

        # Loop over the sequence in steps of 3
        for i in range(0, len(sequence), 3):

            # Only include complete codons
            if i + 3 <= len(sequence):
                codon_list.append(sequence[i:i + 3])

        # Store the codon list under its sequence header
        sequence_codons[header] = codon_list

    return sequence_codons


def exercise_function(codon_list):
    """Translate a list of codons into a protein sequence."""

    aa_string = ""

    for codon in codon_list:
        amino_acid = Seq(codon).translate()
        aa_string += str(amino_acid)

    return aa_string
