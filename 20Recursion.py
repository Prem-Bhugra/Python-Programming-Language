a=int(input("Enter the number\n"))
b=int(input("Press 0 to use iterative approach and 1 to use recursive approach\n"))
def iterativefact(n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
    return fact
def recursivefact(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m*recursivefact(m-1)
if b == 0:
    print("You chose iterative approach")
    print(iterativefact(a))
elif b == 1:
    print("You chose recursive approach")
    print(recursivefact(a))