list1 = ["Prem","Yugal","Yuvraj","Ninad"]
i=1
for items in list1:
    if i%2!=0:
        print(items)
    i+=1
for i,items in enumerate(list1):
    if i%2==0:
        print(items)