"""Program to build Pascal's Triangle"""
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
def comb(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))
def printcombs(n):
    for i in range (n+1):
        print(comb(n,i),end = "")
        print(" ",end = "")
def triangle(n):
    for i in range(n):
        print((n-(i+1))*" ",end = "")
        printcombs(i)
        print((n-(i+1))*" ")
triangle(5)