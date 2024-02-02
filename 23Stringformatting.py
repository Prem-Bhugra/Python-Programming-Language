name ="Prem"
surname="Bhugra"
print("This is %s\n"%name,end="This is %s %s\n"%(name,surname))
a="This is {} {}\n"
b=a.format(name,surname)
c="This is {1} {0}\n"
d=c.format(name,surname)
print(b,end=d)