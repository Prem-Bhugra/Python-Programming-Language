#Program to format a directory
import os
def soldier(path,file,format):
    list1 = os.listdir(f"{path}")
    list2 = [f"{items}" for items in list1 if items.split(".")[1] == "txt"]                                          
    with open(f"{file}") as f:
        s = f.read()
        list3 = []
        for items in list2:
            if items.capitalize().split(".")[0] not in s:
                list3.append(f"{items.capitalize()}")
            else:
                list3.append(f"{items}")
        os.chdir(f"{path}")
        i = 0
        while i < len(list3):
            os.rename(f"{list2[i]}",f"{list3[i]}")
            i += 1
    list4 = [f"{items}" for items in list1 if items.split(".")[1] == f"{format}"]
    os.chdir(f"{path}")
    for i in range(len(list4)):
        os.rename(f"{list4[i]}",f"{i+1}.{format}")
soldier("C://Users/Prem/OneDrive/Desktop/Python Programming Language/Test Folder 1","File5.txt", "pdf")