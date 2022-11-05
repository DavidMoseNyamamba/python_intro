#Input in python
# Python uses the function input () to capture and strore input in the application

print("User Profile Application")

first_name = input("First Name: ")
last_name = input("Last Name: ")
occupation = input("Your Job: ")

# print("Your first name is: " + first_name)
# print("Your last name is: " + last_name)
# print("Your job is: " + occupation)

# Another way of outputing information in python in is through formatted strings
print(f"Your fist name is {first_name} and your job is {occupation}")

# Handling non-string input
age = int(input("Please enter your age: "))

print(f"In two years, your ages will be {age+2} ")
