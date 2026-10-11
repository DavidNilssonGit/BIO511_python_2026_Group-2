## practical 3 functions

# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"
#count numbers above 4

def count_above (seq, lim):
    count = 0    #local
    for num in seq:
        if num > lim:
            count += 1
    return count

print (count)    
print (count_above(nums, limit))
print(count)

## Result
# 999
# 2
# 999

#summarise a text

def summarixe_text (s):
    summary = {"digits": 0, "letters": 0, "other": 0}

#classify each chracter
    for char in s:
        if char.isdigit():
            summary ["digits"] += 1
        elif char.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary

print(f"print the global summary: {summary}")
print(summarixe_text(text)) ## call upon the defines function and print the returned dictionary
print(f"print the global summary again: {summary}")
print(f"prinyt and check that the numbers addupp to the length of the string: {len(text)}")

## Result
# print the global summary: unset
# {'digits': 5, 'letters': 21, 'other': 10}
# print the global summary again: unset
# prinyt and check that the numbers addupp to the length of the string: 36

## Aggregate with a mode

def aggregate (seq, mode, threshold):
    result = 0 

    if mode == "sum":
        result = 0
    elif mode == "count":
        result = 0
    else:
        result = None

    for n in seq:
        if n < 0:
            continue
        if n >= threshold:
            if mode == "sum":
                result = result + n
            elif mode == "count":
                result += 1
            else:
                if result is None or n > result:
                    result = n
    return result

print(f"print the global result: {result}")
print(f"call the the function three times: {aggregate(nums, "sum", limit)}, {aggregate(nums, "count", limit)}, {aggregate(nums, "max", limit)}")
print(f"print the global result again: {result}")
print(aggregate(nums, "max", 100))

## REsult
# print the global result: unset
# call the the function three times: 20, 3, 9
# print the global result again: unset
# None

## Errors and try/except

number = int('five')
print(number)

try:
    number = int('five')
    print(number)
except ValueError:
    print('That is not a valid number.')

values = ["bahja", '10', '5', 'hello', '8', 'three', '2']

for i in values:
    try:
        number = int(i)
        print (number)
    except ValueError:
        print (f"Skipping invalid value: {i}")

## Result 
# Skipping invalid value: bahja
# 10
# 5
# Skipping invalid value: hello
# 8
# Skipping invalid value: three
# 2