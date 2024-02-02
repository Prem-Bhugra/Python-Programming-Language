list1= ["Prem","IIT",678,"Python padhle"]
list2= [34,67,21,5,98]
print(list1,list1[0])
list2.sort()
print(list2)
list2.reverse()
print(list2)
list3= ["a","b","c","d","e"]
print(list3[0:5],list3[0:3],list3[:],list3[::2],len(list3))
print(max(list3),min(list3),max(list2),min(list2))
list2.append(4)
list3.append(4)
print(list2,list3)
list3.insert(2,"f")
list3.remove("d")
list3.pop()
print(list3)
list2[1]= 1
print(list2)