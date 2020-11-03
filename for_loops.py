# for loops are used to iterate through data

shopping_list = ["eggs", "milk", "bread"]

for items in shopping_list:
    if items == "milk":
        print(f"There's enough {items} at home")
    elif items == "eggs":
        print(f"No need to buy {items} this week")
    else:
        print(f"You need to buy {items}")
        break

user_details = {"first name": "John",
                "last name": "Doe",
                "Date of birth": "03/12/1997",
                "age": "22",
                "address": "12 Sesame st",
                "course": "DevOps",
                "grades": "A",
                "hobbies": ["football", "movies", "reading"]
}
for keys, values in user_details.items():
    print(keys)

for keys, values in user_details.items():
    print(values)



