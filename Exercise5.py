#Program to build a Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()
a=getdate()
name=input("Enter your name\n")
plan=int(input("Enter 1 for accessing diet plan and 2 for exercise plan\n"))
choice=int(input("Enter 1 for logging data and 2 for retrieving it\n"))
if name.capitalize() == "Harry":
    if plan == 1:
        if choice == 1:
            food=input("What did you eat?\n")
            with open("Harry'sDietPlan.txt","a") as f:
                f.write(str(a))
                f.write("\t")
                f.write(food.capitalize())
                f.write("\n")
        elif choice == 2:
            with open("Harry'sDietPlan.txt") as f:
                print(f.read())
    elif plan == 2:
        if choice == 1:
            exercise=input("What exercise did you do?\n")
            with open("Harry'sExercisePlan.txt","a") as f:
                f.write(str(a))
                f.write("\t")
                f.write(exercise.capitalize())
                f.write("\n")
        elif choice == 2:
            with open("Harry'sExercisePlan.txt") as f:
                print(f.read())
elif name.capitalize() == "Prem":
    if plan == 1:
        if choice == 1:
            food=input("What did you eat?\n")
            with open("Prem'sDietPlan.txt","a") as f:
                f.write(str(a))
                f.write("\t")
                f.write(food.capitalize())
                f.write("\n")
        elif choice == 2:
            with open("Prem'sDietPlan.txt") as f:
                print(f.read())
    elif plan == 2:
        if choice == 1:
            exercise=input("What exercise did you do?\n")
            with open("Prem'sExercisePlan.txt","a") as f:
                f.write(str(a))
                f.write("\t")
                f.write(exercise.capitalize())
                f.write("\n")
        elif choice == 2:
            with open("Prem'sExercisePlan.txt") as f:
                print(f.read())
elif name.capitalize() == "Piyush":
    if plan == 1:
        if choice == 1:
            food=input("What did you eat?\n")
            with open("Piyush'sDietPlan.txt","a") as f:
                f.write(str(a))
                f.write("\t")
                f.write(food.capitalize())
                f.write("\n")
        elif choice == 2:
            with open("Piyush'sDietPlan.txt") as f:
                print(f.read())
    elif plan == 2:
        if choice == 1:
            exercise=input("What exercise did you do?\n")
            with open("Piyush'sExercisePlan.txt","a") as f:
                f.write(str(a))
                f.write("\t")
                f.write(exercise.capitalize())
                f.write("\n")
        elif choice == 2:
            with open("Piyush'sExercisePlan.txt") as f:
                print(f.read())
else:
    print("No client found")