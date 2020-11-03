# Calculates birth year by taking age and subtracting it from the current year (2020)
name = "John Doe"
age = 22
birth_year = 2020 - age
print(f"OMG {name}, you're {age} years old and so were born in {birth_year}")

# User asked to input name, age, the day of the month, and the month in which they born
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
birth_date = int(input("Please enter the day of the month you were born in: "))
birth_month = input("What month were you born in: ").capitalize()
# input for birth month is capitalised to ensure the == function in the if statement below functions

# if statement checking whether the birth date (day/month) given by the user is after the 3rd of November or before. if after, user told that their birthday has yet to happen this year. if before, they're told that it's already passed
if (birth_month == "November" and birth_date > 3) or (birth_month == "December"):
    print("your birthday hasn't happened yet this year")
else:
    print("your birthday has already passed this year")
