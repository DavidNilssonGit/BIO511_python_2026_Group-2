# Make a list
mylist = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
# You can double check if it's a list
type(mylist)

# print your list
print(mylist)

# print the first item in your list
print(mylist[0])

#########################################################################


#Simple loops:
countries = ["India", "Sweden", "Italy", "China", "Japan", "Nepal", "Iran"]
for index, country in enumerate(countries, start=1):
    print("Loop number:", index)
    print("Country:", country)
    if index==5:
        break

#results:
#Loop number: 1
#Country: India
#Loop number: 2
#Country: Sweden
#Loop number: 3
#Country: Italy
#Loop number: 4
#Country: China
#Loop number: 5
#Country: Japan


#########################################################################

#Nested loops:

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']
for sequence in sequences:
  for codon in codons:
    if codon in sequence:
      print(codon + " is in " + sequence)

#results:
#CCA is in ATCTGAGTCCACACATG
#TGT is in GCGTCGTGCGATGTTCACGTTGAT
#GTA is in CAGTAGTACTCAGT
#TAG is in CAGTAGTACTCAGT
#GTA is in GGTATGCTAGACGAGATCTAATA
#TAG is in GGTATGCTAGACGAGATCTAATA

#########################################################################

#check each sequence for the presence of both a start codon and any of the valid stop codons

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']

start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

# Loop through each sequence
for seq in sequences:
    has_start = False
    has_stop = False
    
    # Check for the start codon
    if start_codon in seq:
        has_start = True
        
    # Nested loop to check for any of the stop codons
    for stop in stop_codons:
        if stop in seq:
            has_stop = True
            
    # Check if both flags are True
    if has_start and has_stop:
        print(f"Has both: {seq}")
#result:
#Has both: ATCTGAGTCCACACATG
#Has both: GCGTCGTGCGATGTTCACGTTGAT
#Has both: GGTATGCTAGACGAGATCTAATA


#########################################################################

#Which sequence(s) have a start codon before a stop codon?

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']

start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

for seq in sequences:
    # Get the position of the start codon
    start_pos = seq.find(start_codon)
    
    # If the start codon exists, look for a stop codon after it
    if start_pos != -1:
        for stop in stop_codons:
            stop_pos = seq.find(stop)
            
            # Check if the stop codon exists AND comes after the start codon
            if stop_pos != -1 and start_pos < stop_pos:
                print(f"Valid sequence found: {seq}")
                print(f"  -> '{start_codon}' at index {start_pos}")
                print(f"  -> '{stop}' at index {stop_pos}\n")
                break  # Stop checking other stop codons for this sequence

#results:
#Valid sequence found: GCGTCGTGCGATGTTCACGTTGAT
#  -> 'ATG' at index 11
#  -> 'TGA' at index 20

#Valid sequence found: GGTATGCTAGACGAGATCTAATA
#  -> 'ATG' at index 3
#  -> 'TAG' at index 8




#########################################################################

#while loop example:
sequence = "GATTACAGAACTGATAC"
 
position = 0
a_count = 0
 
while a_count < 3:
    if sequence[position] == "A":
        a_count += 1
    
    # We only want to move to the next position if we haven't hit our 3rd 'A' yet!
    if a_count < 3:
        position += 1
 
print(position)
#6 (result)


#########################################################################

#for loop example:
sequence = 'GATTACAGAACTGATAC'

# 1. Use a counter to keep track of the number of A bases found
a_count = 0

# 2. Loop through the sequence with its index position
for index, base in enumerate(sequence):
    
    # Check if the current base is 'A'
    if base == 'A':
        a_count += 1
        
        # Hint: When the counter reaches 3, use break to stop the loop
        if a_count == 3:
            print(f"The third 'A' is found at index: {index}")
            break

#The third 'A' is found at index: 6 (result)


###########################################################################

#with both for and while loop solution:
sequence = 'GATTACAGAACTGATAC'

# ==========================================
# SOLUTION 1: The 'while' loop approach
# ==========================================
position = 0
while_a_count = 0

while while_a_count < 3:
    if sequence[position] == "A":
        while_a_count += 1
    
    # Only advance the index if we haven't reached the 3rd 'A' yet
    if while_a_count < 3:
        position += 1

print(f"While Loop Solution Position: {position}")


# ==========================================
# SOLUTION 2: The 'for' loop approach
# ==========================================
for_a_count = 0

for index, base in enumerate(sequence):
    if base == 'A':
        for_a_count += 1
        
        if for_a_count == 3:
            print(f"For Loop Solution Position  : {index}")
            break


#results:
#While Loop Solution Position: 6
#For Loop Solution Position  : 6



#####################################################################

sequence = 'GATTACAGAACTGATAC'

# Change this value to search for a different occurrence
count_a = 3

# ==========================================
# SOLUTION 1: The 'while' loop approach
# ==========================================
position = 0
while_a_count = 0

while while_a_count < count_a:
    if sequence[position] == "A":
        while_a_count += 1
    
    if while_a_count < count_a:
        position += 1

print(f"While Loop Solution Position: {position}")


# ==========================================
# SOLUTION 2: The 'for' loop approach
# ==========================================
for_a_count = 0

for index, base in enumerate(sequence):
    if base == 'A':
        for_a_count += 1
        
        if for_a_count == count_a:
            print(f"For Loop Solution Position  : {index}")
            break

#results:
#While Loop Solution Position: 6
#For Loop Solution Position  : 6


#######################################################################


#Loop through a dictionary
data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# Loop through the dict printing each key and each value as a list.
for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)
  print('bac889Ytd' in value_bact_list)

#results:
#pat_001
#['bacZZt98', 'bac889Ytd']
#True
#pat_002
#['bac0GFrr']
#False
#pat_003
#['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
#True
#pat_001
#['bacZZt98', 'bac889Ytd']
#True
#pat_002
#['bac0GFrr']
#False
#pat_003
#['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
#True   


#########################################################################

#Reverse the dictionary: Loop through data and then through each patient’s list of bacteria. Add a bacterium to unique_bacteria only if it is not already in the list.

data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
 }
 
# 1. Create an empty list called unique_bacteria
unique_bacteria = []
# 2. Loop through the data dictionary
for patient, bacteria_list in data.items():
     
     # 3. Loop through each patient's list of bacteria
     for bacterium in bacteria_list:
         
         # 4. Add to unique_bacteria only if it is not already in the list
         if bacterium not in unique_bacteria:
             unique_bacteria.append(bacterium)
 
# 5. Print the list
print(unique_bacteria)
 
#['bacZZt98', 'bac889Ytd', 'bac0GFrr', 'bacFq55Hj'] (result)


#########################################################################

#Create an empty dictionary called bacteria_to_patients. Use the list from step 1 to add each unique bacterium as a key. Give every key an empty list as its value.
data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# --- STEP 1: Find unique bacteria (from previous step) ---
unique_bacteria = []
for patient, bacteria_list in data.items():
    for bacterium in bacteria_list:
        if bacterium not in unique_bacteria:
            unique_bacteria.append(bacterium)

# --- STEP 2: Create the initial reverse dictionary framework ---
# Create an empty dictionary called bacteria_to_patients
bacteria_to_patients = {}

# Use the list from step 1 to add each unique bacterium as a key with an empty list value
for bacterium in unique_bacteria:
    if bacterium not in bacteria_to_patients:
        bacteria_to_patients[bacterium] = []

# Print the empty dictionary setup
print(bacteria_to_patients)

#results:
#{'bacZZt98': [], 'bac889Ytd': [], 'bac0GFrr': [], 'bacFq55Hj': []}


#########################################################################

#Add the patients to the reverse dictionary.
data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# 1. Initialize an empty dictionary for the reversed mapping
reverse_data = {}

# 2. Loop through the original data (patient and their bacteria list)
for patient, bacteria_list in data.items():
    
    # 3. Loop through each individual bacterium in that list
    for bacterium in bacteria_list:
        
        # 4. If the bacterium is not yet a key in reverse_data, create it with an empty list
        if bacterium not in reverse_data:
            reverse_data[bacterium] = []
            
        # 5. Append the patient ID to that bacterium's list
        reverse_data[bacterium].append(patient)

# 6. Print the completed dictionary
print(reverse_data)

#result:
#{
#    'bacZZt98': ['pat_001', 'pat_003'], 
#   'bac889Ytd': ['pat_001', 'pat_003'], 
#    'bac0GFrr': ['pat_002'], 
#   'bacFq55Hj': ['pat_003']
#}