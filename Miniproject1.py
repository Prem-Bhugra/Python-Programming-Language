class Library:
    def __init__(self,Name,Books):
        self.name = Name
        self.books = Books
        self.dict1 = {}
    def show(self):
        print(self.books)
    def lend(self):
        a = input("Enter the name of the book you want\t")
        if a not in self.books:
            print("Not available")
        else:
            self.books.remove(a)
            b = input("Enter your name\t")
            print(f"You have borrowed '{a}'.")
            self.dict1[f"{a}"] = f"{b}"
    def add(self):
        c = input("Enter the name of the book you want to add\t")
        self.books.append(c)
        print(f"You have returned '{c}'")
        del self.dict1[f"{c}"]
    def show_borrowed_books(self):
        return self.dict1
shelf = Library("Central",["Game Of Thrones","Harry Potter","Atomic Habits","Doglapan","Kayamat Ki Raat"])
while True:
    a = input("What do you want to do? Display, Borrow, Return or See borrowed books?\t")
    if a == "Display":
        shelf.show()
    elif a == "Borrow":
        shelf.lend()
    elif a == "Return":
        shelf.add()
    elif a == "See borrowed books":
        print(shelf.show_borrowed_books())
    else:
        print("This attribute is not available")