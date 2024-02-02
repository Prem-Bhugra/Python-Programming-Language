l=8
def func1(n):
    m=6
    print(l,m)
    print(n,"printed this")
func1("I have")
l=8
def func1(n):
    l=9
    m=6
    print(l,m)
    print(n,"printed this")
func1("I have")
print(l)
l=8
def func1(n):
    global l
    l=l+1
    m=6
    print(l,m)
    print(n,"printed this")
func1("I have")
func1("You have")
print(l)
x=1
def func2():
    x=7
    def func3():
        global x   #It globalizes x, so, x=3 is now a global variable, so, the local variable is x=7
        x=3
    print("Before calling func3",x)
    func3()
    print("After calling func3",x)
func2()
print(x)   #x=3, the global variable is printed