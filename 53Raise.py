a = input("Enter a word\n")
if a.isnumeric():
    raise Exception("Digits are not allowed")
b = input("Enter a word\t")
try:
    print(a) #Change a to c while running
except Exception as e:
    if b == "hello":
        raise ValueError("This word is not allowed")
    print("Exception handled")