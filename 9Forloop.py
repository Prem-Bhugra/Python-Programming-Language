list1 = [["Prem",3],["Yuvraj",6],["Ninad",2]]
for name,number in list1:
    print(name,"eats",number,"lollypops")
dic1 = dict(list1)
print(dic1)
for name,number in dic1.items():
    print(name,"eats",number,"lollypops")
for number in dic1:
    print(number)