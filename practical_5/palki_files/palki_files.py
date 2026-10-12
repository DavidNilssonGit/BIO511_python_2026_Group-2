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

''' with open('palki.csv', 'w') as file:
    file.write('Name,Age,Gender,Salary,Country\n')
    file.write('John,28,Male,50000,USA\n')
    file.write('Jane,32,Female,60000,Canada\n')
    file.write('Mike,45,Male,80000,Australia\n')
    file.write('Emily,29,Female,55000,UK\n')

print("CSV file 'palki.csv' created successfully.") '''

with open('palki.csv', 'a') as file:
    file.write(",".join(sys.argv[1:]) + "\n")

## sys.argv runs on command line and takes input as such ##
## python palki_files.py 'Peter,28,Male,70000,Canada'