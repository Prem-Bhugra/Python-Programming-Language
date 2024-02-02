list1 = []
for i in range(20):
    if i%3 == 0:
        list1.append(i)
print(list1)
list2 = [i for i in range(20) if i%3==0]
print(list2)
dict1 = {i:f"item{i}" for i in range(20) if i%3 == 0}
print(dict1)
dict2 = {value:key for key,value in dict1.items()}
print(dict2)
Even = (i for i in range(100) if i%2 == 0)
print(Even.__next__())
print(Even.__next__())
print(Even.__next__())
set1 = {numbers for numbers in [2,34,45,65,6,78,890,2,65,78]}
print(set1)