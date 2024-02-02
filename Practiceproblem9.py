"""Funny Names"""
import random
n = int(input("What number of names do you want to enter\n"))
lst1 = []
for i in range(n):
    name = input(f"Enter name {i+1}\t")
    lst1.append(name)
print(lst1)
first_names = [item.split(" ")[0] for item in lst1]
last_names = [item.split(" ")[1] for item in lst1]
print(first_names,last_names)
length = len(first_names)
funny_names = []
for i in range(length):
    f = random.choice(first_names)
    l = random.choice(last_names)
    funny_names.append(f +" "+ l)
    first_names.remove(f)
    last_names.remove(l)
for names in funny_names:
    print(names)