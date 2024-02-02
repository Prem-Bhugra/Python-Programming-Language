class Students:
    books = 5
    def __init__(self,Name,Standard,Gender):
        self.name = Name
        self.standard = Standard
        self.gender = Gender
    def printstudents(self):
        return f"The name is {self.name},standard is {self.standard} and gender is {self.gender}"
class Kid(Students):
    reports = 9
    def __init__(self,Name,Standard,Gender,Languages):
        self.name = Name
        self.standard = Standard
        self.gender= Gender
        self.languages = Languages
    def printkid(self):
        return f"The name is {self.name}, standard is {self.standard}, gender is {self.gender} and the languages are {self.languages}"
Prem = Students("Prem Bhugra","12:B","Male")
Sagar = Kid("Sagar Nailwal","12:A","Male",["Python","Java","C++"])
print(Sagar.printstudents())
print(Sagar.printkid())