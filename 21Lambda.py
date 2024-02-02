add = lambda a,b:a+b
print(add(7,3))
def listsort(list):
    return list[1]
list1 = [[1,98],[34,6],[45,54],[23,0]]
list1.sort(key=listsort)
print(list1)
listsortlambda = lambda list:list[1]
list1.sort(key=listsortlambda)
print(list1)