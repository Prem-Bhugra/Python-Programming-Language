#Program for pickling lists from a text file
import requests
import pickle
r =  requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
#Link content stored in File6.txt
list1 = r.split("\n")
list2 = [item.split(",") for item in list1 if len(item) != 0]
with open("Iris.pkl","wb") as fileobject:
    pickle.dump(list2,fileobject)
with open("Iris.pkl","rb") as fileobject:
    print(pickle.load(fileobject))