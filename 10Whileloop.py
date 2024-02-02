i=0
while i<10:
    if i<5:
        i=i+1
        continue
    print(i)
    i=i+1
    if i==9:
        break
while True:
    a=int(input("Enter a number\n"))
    if a>100:
        print("You have entered a number greater than 100")
        break
    else:
        print("Enter a number again")
        continue