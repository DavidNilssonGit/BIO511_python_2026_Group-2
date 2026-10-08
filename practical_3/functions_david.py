# Initial setup

# Provided inputs
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
result_1 = count_above(nums, limit)
print(result_1)  
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
# Call "summarize_text(text)" and print the returned value.
result_2 = summarize_text(text)
print(result_2)
# Print the global summary again:
print(summary)


# Exercise 3: Aggregate with a mode.

# Write one function that can calculate three different things,
# depending on a mode argument.
# Define the function aggregate that takes three arguments: seq, mode, and threshold.
def aggregate(seq, mode, threshold):
    """ """
    # Create a local variable named result with the starting value depending on mode.
    if mode == "sum":
        result = 0
    elif mode == "count":
        result = 0
    elif mode == "max":
        result = None
    else:
        raise ValueError("Invalid mode. Choose 'sum', 'count', or 'max'.")
    # Loop through each number n in seq.
    for n in seq:
        # If n is negative, skip to the next step in the loop.
        if n < 0:
            continue
        # If n is greater than threshold, update result based on mode.
        # If mode isn't "sum" or "count", treat the mode as "max".
        # If result is none, or n is greater than result, set result to n.
        if n > threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:  # mode is "max"
                if result is None or n > result:
                    result = n
    # Return the final result from the function.
    return result

# Call the function we defined:
# Print the global result:
print(result)
# Call "aggregate(nums, "mode", limit)" three times and print each returned value.
result_sum = aggregate(nums, "sum", limit)
print(result_sum)
result_count = aggregate(nums, "count", limit)
print(result_count)
result_max = aggregate(nums, "max", limit)
print(result_max)
# Print the global result again:
print(result)

# aggregate(nums, "max", 100) returns None because all numbers in nums are less than 100.