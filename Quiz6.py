"""Program to create Comprehensions"""
list = []
n = int(input("Enter the number of elements you want to add\n"))
for i in range(n):
    Element = input(f"Enter Element number {i+1}\t")
    list.append(Element)
    print(list)
choice = int(input("What type of comprehension do you want? Enter 0 for List comprehension, 1 for Dictionary comprehension and 2 for Set comprehension\t"))
if choice == 0:
    print(list)
elif choice == 1:
    dict = {items for items in list}
    print(dict)
elif choice == 2:
    set = {items for items in list}
    print(set)