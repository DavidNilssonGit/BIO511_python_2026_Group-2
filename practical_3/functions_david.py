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

# Call the function we defined:
# Print the global count:
print(count)
# Call "count_above(nums, limit)" and print the returned value.
result = count_above(nums, limit)
print(result)  
# Print the global count again:
print(count)
# The count remains unchanged as 999 because the function uses a local
# variable count, which doesn't affect the global variable.


# Exercise 2: Summarize a text:

# Write a function that classifies each character in a string of text as a digit.
# Define the function summarize_text with one argument: s.
def summarize_text(s: str) -> str:
    """Summarize the text by counting digits, letters, and other characters."""
    # Create a local dictionary with keys 'digits', 'letters', and 'other'.
    # Each key should have an initial value of 0.
    summary = {"digits": 0, "letters": 0, "other": 0}
    # Classify each character in s and use an if/elif/else chain:
    for char in s:
        if char.isdigit():
            summary["digits"] += 1
        elif char.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    # Return the summary dictionary.
    return summary

# Call the function we defined:
print(summary)

summary = summarize_text(text)