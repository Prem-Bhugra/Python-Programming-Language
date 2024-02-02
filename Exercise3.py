#Program to guess a number
i=0
while i<10:
    n=int(input("Guess the number\n"))
    i=i+1
    if n==18:
        print("Congratulations! You have guessed the correct number")
        break
    elif n>18:
        print("Wrong guess! guess a smaller value")
    elif n<18:
        print("Wrong guess! guess a bigger value")
    if i==9:
        print("Oops! you ran out of guesses")
        break
print(i,"guesses were made")