#Program to build the game SNAKE,WATER,GUN
import random
list1=["Snake","Water","Gun"]
dict1={1:"Snake",2:"Water",3:"Gun"}
i=1
while i<=10:
    a=random.choice(list1)
    b=int(input("Enter 1 for Snake, 2 for Water and 3 for Gun\t"))
    if (a == "Snake" and  b == 1) or (a == "Water" and b == 2) or (a == "Gun" and b == 3):
        x = f"The computer chose {a} and you chose {dict1[b]}"
        print(x)
        print("Nobody wins")
    elif (a == "Snake" and b == 2) or (a == "Water" and b == 3) or (a == "Gun" and b == 1):
        x = f"The computer chose {a} and you chose {dict1[b]}"
        print(x)
        print("The computer wins")
    else:
        x = f"The computer chose {a} and you chose {dict1[b]}"
        print(x)
        print("You win")
    i+=1
print("The game ended")