list1=[1,2,3,4,5,6,7,8,9]
greaterthan5 = lambda n:n>5  #Returns True or False
a=list(filter(greaterthan5,list1))
print(a)
from functools import reduce
list2=[1,2,3,4]
i=0
for item in list2:
    i=i+item
print(i)
sum=reduce(lambda m,n:m+n, list2)
print(sum)