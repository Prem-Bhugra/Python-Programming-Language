def func1():
    print("Prem Bhugra")
func2 = func1
del func1
func2()
def func3(num):
    if num == 0:
        return print
    elif num == 1:
        return int
a = func3(0)
b = func3(1)
print(a,b)
def func4(func5):
    func5("This")
func4(print)
def dec1(func6):
    def executor():
        print("Now executing")
        func6()
        print("Executed")
    return executor
def whoisprem():
    print("Prem is a good boy")
whoisprem = dec1(whoisprem)
whoisprem()
@dec1 #@dec1 is equivalent to whoisharry = dec1(whoisharry)
def whoisharry():
    print("Harry is my teacher")
whoisharry()