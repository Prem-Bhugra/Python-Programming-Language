"""Program to prit only integers from a list"""
list1=["Prem","=",456,"Interstellar",98,"+","Excuse me",1,1234567890,"Aginomoto",6]
for items in list1:
    if type(items) == int and items > 6:
        print(items)