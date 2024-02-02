"""Foods And Calories"""
lst1 = ["Rajma","Chole","Maggie","Fried Rice","Campa","Aginomoto"]
def Normal_reverse(lst):
    lst.reverse()
    return lst
print(Normal_reverse(lst1))
lst2 = ["Rajma","Chole","Maggie","Fried Rice","Campa","Aginomoto","Apple"]
def Slicing_reverse(lst):
    return lst[::-1]
print(Slicing_reverse(lst2))
lst3 = ["Rajma","Chole","Maggie","Fried Rice","Campa","Aginomoto","Apple","Raddish"]
def Swapping_reverse(lst):
    i = 0
    j = len(lst)-1
    while i <= j:
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        i += 1
        j -= 1
    return lst
print(Swapping_reverse(lst3))
print(lst1,lst2,lst3)