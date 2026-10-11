#!/usr/bin/env python3
from premade_script import codons, exercise_function
from collections import Counter
import argparse
import os


def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(
        description="Split the sequences in a FASTA file into codons."
    )
    parser.add_argument(
        '-s', '--sequence',
        type=existing_file,
        required=True,
        help='Path to the input FASTA file'
    )
    args = parser.parse_args()

    # EXPLORE THE CODONS FUNCTION
    # The input to codons() is the path to a FASTA file.
    # The function reads the sequences and splits them into codons of three nucleotides each.
    # It returns a dictionary with sequence headers as keys and lists of codons as values.
    sequence_codons = codons(args.sequence)

    # Print the output of the codons() function.
    print(sequence_codons)

    # EXPLORE AND TEST THE EXERCISE_FUNCTION
    # The input to exercise_function() is a list of codons.
    # The function translates each codon into an amino acid and joins the amino acids into a protein sequence.
    # Biopython is required for this function to work.

    for header, codon_list in sequence_codons.items():
        protein = exercise_function(codon_list)
        print(header, protein)

        # EXTRA TASK: CODON USAGE

        # Count how many times each codon occurs.
        codon_counts = Counter(codon_list)
        print("Codon counts:", codon_counts)

        # Print the most common codon and its occurrence count.
        print("Most common codon:", codon_counts.most_common(1))

        # Count how many times each amino acid occurs.
        amino_acid_counts = Counter(protein)
        print("Amino acid counts:", amino_acid_counts)

        # Print the most common amino acid and its occurrence count.
        print("Most common amino acid:", amino_acid_counts.most_common(1))


if __name__ == "__main__":
    main()