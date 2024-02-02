dic1={"Prem":"Rajma","Rohan":"Sandwhich","Rahul":{"Breakfast":"Maggie","Lunch":"Chowmein","Dinner":"Momos"}}
print(dic1,dic1["Prem"],dic1["Rahul"],dic1["Rahul"]["Lunch"])
dic1["Ankit"]="Chole"
del dic1["Rohan"]
print(dic1)
dic2=dic1.copy()
del dic2["Prem"]
print(dic1,dic2)
dic2=dic1
del dic2["Prem"]
print(dic1,dic2)
dic3={34:43,45:54,67:76}
print(dic3.get(34))
dic3.update({89:98})
print(dic3,dic3.keys(),dic3.items())
