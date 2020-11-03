
age = int(input("What is your age: "))

if age >= 18:
    print("You're old enough to watch movies with any rating")
elif 15 <= age < 18:
    print("you can watch movies with an age rating uo to 15")
elif 12 <= age < 15:
    print("you can watch movies with an age rating uo to 12")
else:
    print("you can watch U rated movies")