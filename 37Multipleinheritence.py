class Students:
    var=5
    def __init__(self,Name,Standard,Gender):
        self.name = Name
        self.standard = Standard
        self.gender = Gender
    def printstudents(self):
        return f"The name is {self.name}, standard is {self.standard} and gender is {self.gender}"
class Players:
    var=6
    def __init__(self,Name,Game):
        self.name = Name
        self.game = Game
    def printplayers(self):
        return f"The name is {self.name} and game is {self.game}"
class Both(Students,Players):
    pass
Prem = Students("Prem Bhugra","12:B","Male")
Sagar = Players("Sagar Nailwal","Basketball")
Kshitij = Both("Kshitij Manral","12:A","Male")
a = Kshitij.printstudents()
print(a,Kshitij.var)