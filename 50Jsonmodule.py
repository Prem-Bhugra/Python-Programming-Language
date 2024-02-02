import json
dict1 = '{"var1":"Prem","var2":"Yugal","var3":100,"var4":20}'
print(dict1)
dict2 = json.loads(dict1)
print(dict2)
print(dict2['var1'],dict2["var3"])
dict3 = {"var1":"Prem Bhugra","var2":["BMW","Audi","Mercedes"],"var3":("Mango","Apple"),"var4":False}
jscomp = json.dumps(dict3)
print(jscomp)