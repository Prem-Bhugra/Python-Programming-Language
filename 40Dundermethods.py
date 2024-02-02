class Employees:
    Leaves = 8
    def __init__(self,Name,Salary,Role):
        self.name = Name
        self.salary = Salary
        self.role = Role
    @classmethod
    def changeleaves(cls,newleaves):
        cls.Leaves = newleaves
    def __add__(self,other):
        return self.salary + other.salary
    def __truediv__(self,other):
        return self.salary / other.salary
    def __repr__(self):
        return f"The name is {self.name}, salary is {self.salary} and role is {self.role}."
    def __str__(self):
        return f"{self.name} is the name,{self.salary} is the salary and {self.role} is the role."
emp1 = Employees("Prem Bhugra",50000,"Senior Manager")
emp2 = Employees("Simran Singh",40000,"Junior Manager")
print(emp1 + emp2,emp1 / emp2,emp1,repr(emp2))
print(emp1.__add__(emp2))