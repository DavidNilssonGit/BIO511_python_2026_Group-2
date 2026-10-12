import sys
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import os
from pathlib import Path
import csv

## Change path to the working directory ##
os.chdir("/Users/palkidas/My_Python_Course/BIO511_python_2026_Group-2/practical_5/palki_files/")

import argparse

# Create parser
parser = argparse.ArgumentParser(description="Read a CSV file")

# Add command-line argument
parser.add_argument("filename", help="Name of the CSV file")

# Parse arguments
args = parser.parse_args()

# Open and display the file
with open(args.filename, "r") as file:
    for line in file:
        print(line.strip())
        print("\n")  # Add a newline for better readability 


# Read CSV into DataFrame (df)
df = pd.read_csv(args.filename, header=0)

# Display DataFrame
print("DataFrame:")
print(df)

# Display summary statistics Pandas ##
print("\nSummary:")
desc = df.describe()
print()

## Write descriptive statistics to a new CSV file using Pandas ##
desc.to_csv("palki_desc_out.csv", index=False)

## Execute from command line not from editor with the play button: 
## python arguments_pandas.py palki.csv ##
