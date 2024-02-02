"""Divide The Apples"""
def Apples_and_range(n,mn,mx):
    if mn == mx:
        print("This is not a range")
        if n%mn == 0:
            print(mn,"is a divisor of",n)
        else:
            print(mn,"is not a divisor of",n)
    elif mn < mx:
        for i in range(mn,mx+1):
            if n%i == 0:
                print(i,"is a divisor of",n)
            else:
                print(i,"is not a divisor of",n)
    else:
        print("Wrong input")
Apples_and_range(20,2,5)
Apples_and_range(20,2,2)
Apples_and_range(20,3,3)
Apples_and_range(20,5,2)
Apples_and_range(45,2,9)