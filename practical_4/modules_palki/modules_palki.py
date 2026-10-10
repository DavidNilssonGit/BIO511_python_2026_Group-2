#updated main.py

#!/usr/bin/env python3
# Import both functions from premade_script
from premade_script import codons, exercise_function
import argparse
import os


def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Split the sequences in a FASTA file into codons.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file')
    args = parser.parse_args()
    
    # We first call the function from the script, and use the input file path as an argument
    sequence_codons = codons(args.sequence)
    
    # --- CHECK THE OUTPUT OF THE CODONS FUNCTION ---
    print("\n--- [1] Output of codons() function ---")
    print(sequence_codons)
    
    print("\n--- [2] Output of exercise_function() (Translation) ---")
    # Loop through each sequence header and its list of codons
    for header, codon_list in sequence_codons.items():
        # Call exercise_function for each sequence's codon list
        amino_acids = exercise_function(codon_list)
        
        # --- CHECK THE OUTPUT OF THAT FUNCTION ---
        print(f"Header: {header}")
        print(f"Amino Acid Sequence: {amino_acids}\n")

if __name__ == "__main__":
    main()