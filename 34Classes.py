class Students:
    books = 5
    def printdetails(self):
        return f"The name is {self.name} and the standard is {self.standard} and the number of books is {self.books}"
Prem = Students()
Simran = Students()
Mayur = Students()
Prem.name = "Prem Bhugra"
Prem.standard = "12 -B"
Prem.subjects = ["English","Hindi","Science","Mathemtics"]
Simran.name = "Simran Singh"
Simran.subjects = ["English","Hindi","Science"]
Mayur.name = "Mayur Ranka"
print(Mayur.name,Simran.subjects,Prem.standard,Mayur.books,Prem.books,Simran.books,Students.books)
Simran.books = 6
print(Students.books,Simran.books)
print(Prem.__dict__,Students.__dict__)
print(Prem.printdetails())
print(type(Prem))