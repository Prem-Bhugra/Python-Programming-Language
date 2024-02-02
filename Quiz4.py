"""Program to print any element of Fibonacci series"""
def fib(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fib(n-1)+fib(n-2)
a=int(input("Enter which term do you want\t"))
print(fib(a))