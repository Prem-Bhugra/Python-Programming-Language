num=["4","67","12"]
print(type(num[1]))
num=list(map(int,num))
print(type(num[1]))
numbers=[1,2,3,4,5]
sq=lambda n:n*n
squares=list(map(sq,numbers))
print(squares)
def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square,cube]
for i in range(5):
    print(list(map(lambda x:x(i),func)))