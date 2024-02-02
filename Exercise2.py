#Program to produce faulty calculations
print("Enter a and b")
a=float(input())
b=float(input())
op=input("Choose an operation\t")
if a==45 and b==3 and op =="*":
    print(55)
elif a==56 and b==9 and op =="+":
    print(77)
elif a==56 and b==6 and op =="/":
    print(4)
else:
    if op == "*":
        print(a*b)
    elif op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "/":
        print(a/b)