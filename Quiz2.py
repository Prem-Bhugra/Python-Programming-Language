"""Program to check whether a person can drive or not"""
print("Enter your age")
age = int(input())
if age>18:
    print("You are allowed to drive")
elif age==18:
    print("You shall come to the office to get you license")
else:
    print("You are not allowed to drive")