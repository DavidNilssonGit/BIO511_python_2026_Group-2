"""

Input of the Function

• codon_list: This parameter expects a list of strings, where each string is a three-nucleotide sequence triplet representing a single codon (e.g., ['ATG', 'GCC', 'ATT']).

What This Function Does

The function translates a list of RNA/DNA codons into a continuous amino acid protein sequence string.
• It iterates through the provided codon_list one codon at a time.
• For each individual codon triplet, it converts it into a Biopython Seq object and calls the .translate() method to look up its corresponding single-letter amino acid symbol.
• It casts that amino acid into a standard Python string, appends it to a growing text sequence chain (aa_string), and returns the complete protein translation.

"""

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





#Here is how to update main.py script to include the Counter functionality from the collections module.
#This update handles counting the raw codons, extracting the single most frequent codon, and tracking the individual amino acid frequencies inside your finished protein strings.




#!/usr/bin/env python3
from premade_script import codons, exercise_function
# Import Counter from the standard collections library
from collections import Counter
import argparse
import os

def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path

def main():
    # Capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Analyze codons and amino acids in a FASTA file.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file')
    args = parser.parse_args()
    
    # Extract the dictionary of codon lists
    sequence_codons = codons(args.sequence)
    
    # Process each FASTA sequence sequentially
    for header, codon_list in sequence_codons.items():
        print(f"==================================================")
        print(f"ANALYSIS FOR SEQUENCE: {header}")
        print(f"==================================================")
        
        # --- Task 1: Count how many times each codon occurs ---
        codon_counts = Counter(codon_list)
        print("1. All Codon Occurrences:")
        print(dict(codon_counts)) # Cast to a standard dict for cleaner printing
        print("-" * 30)
        
        # --- Task 2: Print only the single most common codon and its count ---
        # .most_common(1) returns a list containing a single tuple: [('CODON', count)]
        if codon_list:
            most_common_codon, codon_freq = codon_counts.most_common(1)[0]
            print(f"2. Most Common Codon: {most_common_codon} (Occurs {codon_freq} times)")
        else:
            print("2. Most Common Codon: None (Sequence is empty)")
        print("-" * 30)
        
        # --- Task 3: Translate to protein and count amino acids ---
        amino_acid_string = exercise_function(codon_list)
        aa_counts = Counter(amino_acid_string)
        
        print(f"3. Full Translated Protein: {amino_acid_string}")
        print(f"   All Amino Acid Frequencies:")
        print(f"   {dict(aa_counts)}")
        
        if amino_acid_string:
            most_common_aa, aa_freq = aa_counts.most_common(1)[0]
            print(f"   🏆 Most Common Amino Acid: {most_common_aa} (Occurs {aa_freq} times)")
        else:
            print("   🏆 Most Common Amino Acid: None (Sequence is empty)")
        print("\n")

if __name__ == "__main__":
    main()
