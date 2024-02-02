class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.classvar1 = "I am an instance variable in class A"
class B(A):
    classvar1 = "I am a class variable in class B"
    def __init__(self):
        self.classvar1 = "I am an instance variable in class B"
        self.special = "Special"
class C(B):
    classvar1 = "I am a class variable in class C"
    def __init__(self):
        super().__init__()
        self.classvar1 = "I am an instance variable in class C"
class D(B):
    classvar1 = "I am a class variable in class D"
    special = "SPECIAL"
    def __init__(self):
        self.classvar1 = "I am an instance variable in class D"
        super().__init__()
    
a = A()
b = B()
c = C()
d = D()
print(b.classvar1,c.classvar1,c.special,d.special,d.classvar1)
#Class variable is searched for after Instance variable