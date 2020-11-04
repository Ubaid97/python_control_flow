
number = 0

# while loop that will continue to loop, adding 1 to number in each loop, until number is no longer < 10
while number < 10:
    print(f"It's working --> {number}")
    number += 1


# user_prompt variable is declared as true
user_prompt = True

# while loop which continues to loop over the code within it as long as user_prompt is true
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit() and int(age) < 117:
    # .isdigit() checks whether the value of the variable is made up of only digits
        user_prompt = False
        # if the condition specified in the if statement is satisfied, user_prompt becomes false, ending the            while loop
    else:
        print("Please provide your age in digits")
        # if the condition isn't satisfied, the user is asked to enter their age in digits

print(f"Your age is {age}")