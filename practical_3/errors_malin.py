values = ['10', '5', 'hello', '8', 'three', '2','bark']

for value in values:
    try:
        value = int(value)
        print(value)
    except ValueError:
        print("Skipping invalid value:", value)