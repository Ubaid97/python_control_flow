# Loop with range that says hello 10 times

# for i in range(10):
#     print("Hello")
#
list_names = []
for i in range(5):
    list_names.append(input("enter a name: "))

print(list_names)


list_names_lower = []
for items in list_names:
    list_names_lower.append(items.lower())

print(list_names_lower)