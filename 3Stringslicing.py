name1="Prem is in IIT "
name2="premisinIIT"
number="67"
print(name1[3],name1[0:4],len(name1),name1[0:4:2],name1[:4],name1[0:],name1[0:4:],name1[::],name1[::3])
print(name1[::4000],name1[-4:-1],name1[::-1],name1[::-2])
print(name1.isalpha(),number.isalpha(),name2.isalpha(),name1.isalnum(),number.isalnum(),name2.isalnum())
print(name1.endswith("IIT "), name1.endswith("IIT"))
print(name1.count("I"),name1.count("P"),name2.capitalize())
print(name1.find("is"),name1.lower(),name2.upper())
print(name1.replace("is","are"))