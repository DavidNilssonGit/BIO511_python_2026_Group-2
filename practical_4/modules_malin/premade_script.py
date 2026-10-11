
    # Open the file
    with open(sequence_file) as fasta_file:
        # Read the file line by line
        for row in fasta_file:
            row = row.strip()
            # If the line starts with '>', it is a header and we start a new, empty sequence
            if row.startswith('>'):
                header = row[1:]
                sequences[header] = ""
            # If the line does not start with '>', it is part of the current sequence and we add it to that sequence
            else:
                sequences[header] += row

    # Now we split each sequence into codons
    sequence_codons = {}

    for header, sequence in sequences.items():
        codon_list = []
        # Loop over the sequence in steps of 3
        for i in range(0, len(sequence), 3):
            # Append the codon to the list if it is a full codon (3 nucleotides)
            if i + 3 <= len(sequence):
                codon_list.append(sequence[i:i + 3])
        # Save the list of codons under the header of the sequence
        sequence_codons[header] = codon_list

    # Return the dictionary of codons
    return sequence_codons


def exercise_function(codon_list):
    """Translates a list of codons into an amino acid sequence.

    Input: A list of codons.
    Output: A string containing the translated amino acid sequence.
    """

    # Start with an empty string to store the amino acid sequence
    aa_string = ""

    # Translate each codon into an amino acid using Biopython
    for codon in codon_list:
        amino_acid = Seq(codon).translate()

        # Add the amino acid to the sequence
        aa_string += str(amino_acid)

    # Return the translated amino acid sequence
    return aa_string