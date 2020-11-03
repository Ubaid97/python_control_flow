name = "John Doe"
age = 22
birth_year = 2020 - age
print(f"OMG {name}, you're {age} years old and so were born in {birth_year}")

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
birth_date = int(input("Please enter the day of the month you were born in: "))
birth_month = input("What month were you born in: ").capitalize()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if (birth_month == "November" and birth_date > 3) or (birth_month == "December"):
    print("your birthday hasn't happened yet this year")
else:
    print("your birthday has already passed this year")
