#Program to print a Star Pattern
def starpattern(n):
    for i in range(n):
        print("*"*(i+1))
def reversestarpattern(m):
    i=m
    while i>=1:
        print("*"*i)
        i-=1
b=int(input("Enter 0 if you want to print Star Pattern and 1 if you want to print Reverse Star Pattern\n"))
a=int(input("Enter the number of rows\n"))
if bool(b) == False:
    starpattern(a)
else:
    reversestarpattern(a)