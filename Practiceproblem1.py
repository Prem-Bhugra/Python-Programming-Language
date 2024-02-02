"""You Age In 2090"""
a = int(input("Enter age or year of birth\n"))
if a <= 99 and a >= 0:
    print("Age was entered by you")
elif a >= 1924 and a <= 2023:
    print("Year of birth was entered by you")
elif a > 2023:
    print("You are not born yet")
elif a == 100 or a == 1923:
    print("You seem to be the oldest person alive as you are already 100 years old")
else:
    print("Wrong input")
def year_to_hit_100(n):
    if n <= 99 and n >= 0:
        print("You will turn a 100 years old in the year",2023 + (100 - n))
    elif n >= 1924 and n <= 2023:
        print("You will turn a 100 years old in the year",2023 + (100 - (2023 - n)))
    else:
        pass
year_to_hit_100(a)