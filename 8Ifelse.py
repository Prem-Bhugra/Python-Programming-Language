a=100
print("Enter b")
b=int(input())
if a>b:
    print("b is smaller")
elif a==b:
    print("b is equal")
else:
    print("b is greater")
list1=["a","b","c","d"]
if "c" in list1:
    print("c is present in list")
if "f" not in list1:
    print("f is not present in list")
l= [1,2,3]
s= ({1,2,3})
d= {1:10,2:20,3:30}
t= (1,2,3)
v= "Rekha"
u= 3
z= True
print(type(l),type(s),type(d),type(t),type(v),type(u),type(z))
a=int(input("Enter A\t"))
b=int(input("Enter B\t"))
if a>b: print("A is Greater than B")
print("B is greater than A") if b>a else print("A is greater than or equal to B")