"""Guess The Number"""
import random
def Select_the_number(a,b):
    lst = []
    for j in range(2):
        print(f"Player {j+1}'s turn")
        randomnumber = random.randint(a,b)
        i = 1
        while True:
            n = int(input("Guess the number\t"))
            if n < randomnumber:
                print("Wrong guess! Guess a greater number")
                i += 1
            elif n > randomnumber:
                print("Wrong guess! Guess a smaller number")
                i += 1
            else:
                print("You guessed the correct number")
                print(f"Number of guesses taken: {i}")
                lst.append(i)
                break
    if lst[0] < lst[1]:
        print("Player 1 wWins!")
    elif lst[1] < lst[0]:
        print("Player 2 Wins")
    else:
        print("Its a Draw! Nobody Wins")
p = int(input("Enter the value of lower bound\n"))
q = int(input("Enter the value of upper bound\n"))
Select_the_number(p,q)