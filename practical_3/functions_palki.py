# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

def count_above(seq, lim):
    count = 0
    for num in seq:
        if num > lim:
            count += 1
    return count

print(count)
print(count_above(nums, limit))
print(count)

#RESULTS:
#999
#2
#999


##################################################
# Global variables
summary = "unset"

def summarize_text(s):

    # Local dictionary
    summary = {
        "digits": 0,
        "letters": 0,
        "other": 0
    }

    # Classify each character
    for char in s:
        if char.isdigit():
            summary["digits"] += 1
        elif char.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1

    return summary

text = "Room 101: bring 2 apples & 1 banana."

# Print global summary
print(summary)

# Call function and print returned value
print(summarize_text(text))

# Print global summary again
print(summary)

#RESULTS:
#unset
#{'digits': 4, 'letters': 22, 'other': 6}  
#unset

"""
Digits: 1 0 1 2 1 → 5 characters
Letters: Roombringapplesbanana → 26 characters
Other: everything that is neither a digit nor a letter
There are:
7 spaces
1 colon (:)
1 ampersand (&)
1 period (.)

"""

#######################################################

def aggregate(seq, mode, threshold):

    # Create local result
    if mode == "sum":
        result = 0

    elif mode == "count":
        result = 0

    else: # max
        result = None

    # Loop through numbers
    for n in seq:

        # Skip negative numbers
        if n < 0:
            continue

    # Process qualifying numbers
    if n >= threshold:

        if mode == "sum":
            result += n

        elif mode == "count":
            result += 1

        else: # max
            if result is None or n > result:
                result = n

    return result

# Outside the function
print(result)

print(aggregate(nums, "sum", limit))
print(aggregate(nums, "count", limit))
print(aggregate(nums, "max", limit))

print(result)

#####################################################

values = ['10', '5', 'hello', '8', 'three', '2']

for value in values:
    try:
        number = int(value)
        print(number)

    except ValueError:
        print(f"Skipping invalid value: {value}")

"""
results:
10
5
Skipping invalid value: hello
8
Skipping invalid value: three
2

"""