"""Program to ovveride some operators in a class"""
class Alphabet:
    var = 5
    def __init__(self,Alpha,Position,List):
        self.alpha = Alpha
        self.position = Position
        self.list = List
    @classmethod
    def changevariable(cls,newvar):
        cls.var = newvar
    def __floordiv__(self,other):
        return self.position // other.position
    def __pow__(self,other):
        return self.position ** other.position
    def __mod__(self,other):
        return self.position % other.position
a = Alphabet("A",1,["Z","Y","X"])
e = Alphabet("E",5,["W","U","V"])
a.changevariable(9)
print(a.alpha,a.var,a//e,a**e,a%e)