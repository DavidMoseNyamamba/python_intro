# # Python uses 'if' statements to evaluate conditions
# driver_age = int(input("Please enter your age: "))
# if (driver_age >= 18):
#     print("Eligible to have a driver's license")
# else:
#     print("Not elegible to have a driver's license")
#     print(f"Please check back with us in {18 - driver_age} years")
student_mark = int(input("Enter Final Mark: "))

if (student_mark >= 70):
    print("Pass: Grade A")
elif (student_mark >= 60):
    print("Pass: Grade B")
elif (student_mark >= 50):
    print("Pass: Grade C")
elif (student_mark >= 40):
    print("Pass: Grade D")
else:
    print("Fail")
