food=["Rajma","Maggie","Pasta","Daal"]
for items in food:
    print(items,"and",end=" ")
print("other food items")
a=" and ".join(food)
print(a,"and other food items")