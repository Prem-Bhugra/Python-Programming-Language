class Students:
    books = 5
    def __init__(self,Name,Standard,Gender):
        self.name = Name
        self.standard = Standard
        self.gender= Gender
    @classmethod
    def changebooks(cls,newbooks):
        cls.books = newbooks
    @classmethod
    def fromstr(cls,string):
        list = string.split("-")
        print(list)
        return cls(list[0],list[1],list[2])
    @classmethod
    def fromstring(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This is the content:" + string)
Sagar = Students("Sagar Nailwal","12:B","Male")
print(Sagar.gender)
Sagar.changebooks(7)
print(Students.books,Sagar.books)
Prem = Students.fromstr("Prem Bhugra-12:B-Male")
Simran = Students.fromstring("Simran Singh-12:B-Female")
print(Simran.__dict__)
print(Prem.printgood("Hello"))