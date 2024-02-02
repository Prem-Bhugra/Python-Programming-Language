num1=input("Enter A\n")
num2=input("Enter B\n")
try:
    print("The sum is",int(num1)+int(num2))
except Exception as e:
    print(e)
    print("Error arived")
print("It was all done to execute this line even if the previous code doesn't work")