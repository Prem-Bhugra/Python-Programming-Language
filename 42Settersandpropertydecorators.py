class Employee:
    def __init__(self,FirstName,LastName):
        self.fname = FirstName
        self.lname = LastName
        self.email = f"{self.fname.lower()}.{self.lname.lower()}@gmail.com"
    def Email(self):
        return f"{self.fname.lower()}.{self.lname.lower()}@gmail.com"
    @property
    def Email2(self):
        if self.fname == "None" and self.lname == "None":
            print("Email is not set")
        return f"{self.fname.lower()}.{self.lname.lower()}@gmail.com"
    @Email2.setter
    def Email2(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @Email2.deleter
    def Email2(self):
        self.fname = "None"
        self.lname = "None"
prem = Employee("Prem","Bhugra")
simran = Employee("Simran","Singh")
print(prem.email)
prem.fname = "Salman"
print(prem.email)
print(simran.Email())
simran.fname = "Radha"
print(simran.Email())
print(simran.Email2)
prem.Email2 = "This.That@gmail.com"
print(prem.fname,prem.lname)
del prem.Email2
print(prem.Email2)
print(dir(prem))
import inspect
print(inspect.getmembers(prem))