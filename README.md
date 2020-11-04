# Control flow
## if statements
## for loops
## while loops
- used for monitoring
- ````break```` and ````continue```` are the key words used to control flow
- while loop that will continue to loop, adding 1 to number in each loop, until number is no longer < 10:
````
number = 0

while number < 10:
    print(f"It's working --> {number}")
    number += 1
````

- while loop that takes in user input, with a nested if statement:
````
user_prompt = True


while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide your age in digits"

print(f"Your age is {age}")
````