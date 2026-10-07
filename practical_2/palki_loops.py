# Example code

# Make a list
mylist = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
# You can double check if it's a list
type(mylist)

# print your list
print(mylist)

# print the first item in your list
print(mylist[0])



countries = ["India", "Sweden", "Italy", "China", "Japan", "Nepal", "Iran"]
for index, country in enumerate(countries, start=1):
    print("Loop number:", index)
    print("Country:", country)
    if index==5:
        break