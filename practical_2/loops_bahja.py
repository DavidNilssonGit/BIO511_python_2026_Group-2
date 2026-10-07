## LOOPS

my_list = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
type(my_list)  # This will return <class 'list'>

print(my_list)

print(my_list[0])

### Create another list with a for loop

my_2_list = ["Bio", "Informatics", "GU", 2026, "group2", "practical", "loops"]

print(my_2_list[0:7:2])

for index, item in enumerate(my_2_list):   #Enumerate == is function that gives you two things at the same time when looping over a list: The position number (index) The actual item
    print(index, item)

    if index == 5:   ## as soon as it reaches the index 5 alltså "practical" the loop stops
        break


# #### While loop
sequence = 'GATTACAGAACTGATAC'
count = 0
index = 0

# 1 question count while loop

while index < len(sequence):   ## this loops check index to the lenghth of the sequence
    if sequence[index] == "A":  ## this searches the index in the sequence if it matches "A"
        count += 1    ## And this basically counts "A" in the sequence
    index += 1    ## this moves forward to the next index number 
print (count)  ## this will have total result of how many "A" have been found in the sequence

# 1- question position while loop

a_count = 0
position = 0
count_a = 10

while a_count < 3:
    if sequence[position] == "A":
        a_count += 1
    position += 1
print( position - 1)

# 2 question for loop count

count = 0

for i in sequence:
    if i == "A":
        count += 1
    index += 1
    if index == 3:
        break

print(count)

# # 3 question for loop position 

position_2 = 0
a_count_2 = 0

for i in sequence:
    if i == "A":
        a_count_2 += 1
    position_2 += 1
    if a_count_2 == 3:
        break

print (position_2 - 1)

# # What is different about the two solutions? 
# # In the while loop, it checks whether you have found three A bases. 
# # In the for loop, you need to add the condition inside the loop yourself.
position_3 = 0
while a_count > count_a:
    for i in sequence[position_3]:
        if i == "A":
            count += 1
    position_3 += 1
print (position_3 - 1)


### Nestled loops
#example 
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']
start_stop = ["ATG", "TAG", "TAA", "TGA"]
for sequence in sequences:
  for codon in codons:
    if codon in sequence:
      print(codon + " is in " + sequence)

# question 2 nesled loops

for sequence in sequences:
    for start_stop_codons in start_stop :
        if start_stop_codons in sequence:
            print ("The sequences that has start or stop codons are: ", start_stop_codons, "in " + sequence)


for sequence in sequences:
    for start_stop_codons in sequence:
        start_position = sequence.find("ATG")
        
