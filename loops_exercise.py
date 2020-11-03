# Loop with range that says hello 10 times
for i in range(10):
    print("Hello")

# for loop that iterates over a range of 5 and adds a name (input by user) to a list in each iteration
list_names = []
for i in range(5):
    list_names.append(input("enter a name: "))

print(list_names)

# for loop that iterates over a list of names and converts all of them to lower case
list_names_lower = []
for items in list_names:
    list_names_lower.append(items.lower())

print(list_names_lower)

# for loop that iterates over a list of names, and displays whether the name has an even or odd number of characters using an if statement
for items in list_names:
    if len(items)%2 == 0:
        print(f"{items} has an even number of letters")
    else:
        print(f"{items} has an odd number of letters")