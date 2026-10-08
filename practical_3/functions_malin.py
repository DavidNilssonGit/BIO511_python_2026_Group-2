# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]  # List of numbers
limit = 4  # Limit to compare numbers with
text = "Room 101: bring 2 apples & 1 banana."  # Text to analyse

# Global variables
count = 999  # Global count variable
summary = "unset"  # Global summary variable
result = "unset"  # Global result variable

# Count numbers
def count_above(seq, lim):  # Define function named count_above, two arguments: seq and lim
    count = 0  # Local counter
    for number in seq:  # Loop through each number in seq
        if number > lim:  # If number is greater than lim
            count = count + 1  # Increase count by one
    return count  # Return the final count

print(count)  # Print the global count
print(count_above(nums, limit))  # Call the function and print the returned number
print(count)  

# Summarize a text
def summarize_text(s):  # Define function named summarize_text with one argument: s
    summary = {"digits": 0, "letters": 0, "other": 0}  # Create dictionary with three counters
    for character in s:  # Loop through each character in s
        if character.isdigit():  # If the character is a digit
            summary["digits"] = summary["digits"] + 1  # Increase digit count by one
        elif character.isalpha():  # Otherwise, if the character is a letter
            summary["letters"] = summary["letters"] + 1  # Increase letter count by one
        else:  # Otherwise
            summary["other"] = summary["other"] + 1  # Increase other count by one
    return summary  # Return the dictionary

print(summary)  # Print the global summary
print(summarize_text(text))  # Call the function and print the returned dictionary
print(summary)  
print(len(text))  # Print the number of characters in text

# Aggregate with a mode
def aggregate(seq, mode, threshold):  # Define function with three arguments
    if mode == "sum":  # If mode is sum
        result = 0  # Start result at 0
    elif mode == "count":  # Otherwise, if mode is count
        result = 0  # Start result at 0
    else:  
        result = None  # Start result as None

    for n in seq:  # Loop through each number in seq
        if n < 0:  # If the number is negative
            continue  # Skip this number and continue the loop
        if n >= threshold:  # If number is greater than or equal to threshold
            if mode == "sum":  # If mode is sum
                result = result + n  # Add number to result
            elif mode == "count":  # Otherwise, if mode is count
                result = result + 1  # Increase result by one
            else:  
                if result == None or n > result:  # If result is None or n is greater than result
                    result = n  # Set result to n

    return result  # Return the final result

print(result)  # Print the global result
print(aggregate(nums, "sum", limit))  # Call aggregate in sum mode
print(aggregate(nums, "count", limit))  # Call aggregate in count mode
print(aggregate(nums, "max", limit))  # Call aggregate in max mode
print(result)  