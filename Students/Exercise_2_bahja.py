#Text Types:
greeting = str("Hello and welcome to the BIO511 Group 2 python repository")
print(greeting)

my_name = str("My names is: ")
print(my_name + "BIO511 Group 2")


#Numeric Types:
addition = int(8+12+30)
print(addition)


substraction = float(50.5 - 55)
print(substraction)

#Sequence Types:
seasons = list(["winter", "spring", "summer", "autumn"])


#Mapping Types:


#Set Types:
my_set_list = set([2, "PYHTON", "PRACTICAL 1", 2.5, "HEELO"])
print(my_set_list)


#Boolean Types:
print(5 > 3)


my_boolean_list = [1,2,2,3,4,5,6,7,8,9,10]

if 5 and 10 in my_boolean_list:
    print("Both 5 and 10 are in the list")

#Binary Types:

# Range
numbers = range(1, 6)
print(numbers)

#None Types:
final_result = None
print(final_result)

#If statement to check if a string is empty or not

our_string = "BionformaticsGroup2"

if len(our_string) == 0:
    print("The string is empty")
elif len(our_string) < 1:
    print("the string is non-empty")
else: 
    print (our_string)


## Interger check

our_integer = 7

if (our_integer) == 0:
    print("The integer is zero")

elif (our_integer) < 0:
    print ("The interger is negative")

else:
    print ("the is greater than 0 ")


## nested classification

my_list =[10, 20, 30, 40, 50]
my_range = range(2,40,4)
my_tuble = (1, 2, 3, 4, 5)

my_sequence = [2, 4, 6, 8, 10]

print(my_sequence)
print(type(my_sequence))
print(len(my_sequence))


if type(my_sequence) == list or type(my_sequence) == range or type(my_sequence) == tuple:
    if len(my_sequence) == 0:
        print("ITS EMPTY")

    elif len(my_sequence) == 1:
        print("The sequence is 1 item")

    else:
        print("The sequence is multiple items")

else:
    print("Wrong type for this task")
