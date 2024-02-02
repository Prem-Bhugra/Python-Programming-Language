"""Rohan Das Is A Fraud"""
import random
def Search_index(n,lst):
    i = 0
    for items in lst:
        if items == n:
            break
        i += 1
    return i
a = int(input("Enter a number\t"))
def Wrong_table(n):
    lst = [n*(i+1) for i in range(10)]
    r = random.choice(lst)
    i = Search_index(r,lst)
    lst.remove(r)
    lst.insert(i,random.randint(n*(i+1),n*(i+2)))
    return lst
t = Wrong_table(a)
print(t)
def isCorrect(table,number):
    lst1 = [number*(i+1) for i in range(10)]
    i = 1
    for products in lst1:
        if products != table[i-1]:
            print(f"{i}th result is wrong")
            print("Hence proved, Rohan Das is a fraud")
            break
        else:
            None
        i += 1
    print(f"The correct multiplication table for {number} is:")
    for i in range(10):
        print(f"{number} x {i+1} = {number*(i+1)}")
isCorrect(t,a)