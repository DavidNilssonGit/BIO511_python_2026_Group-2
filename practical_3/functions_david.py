# Initial setup

# Provided inputs
from threading import local


nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"


# Exercise 1: Count numbers greater than a limit

# Define the function count_above with two parameters: seq(sequence) and lim(limit).
def count_above(seq: list, lim: int) -> int:
    """Count numbers in seq that are greater than lim."""
    # Initialize a counter variable to 0.
    count = 0
    # Loop through seq.
    # For each number greater than lim, increase count by 1.
    for num in seq:
        if num > lim:
            count += 1
    # Return the final count.
    return count

# Call the function we defined and store the result in the global variable count.
# Print the global count:
print(count)
# Call "count_above(nums, limit)" and print the returned value.
result = count_above(nums, limit)
print(result)  
# Print the global count again:
print(count)
# The count remains unchanged as 999 because the function uses a local
# variable count, which doesn't affect the global variable


# Exercise 2: Summarize a text:
