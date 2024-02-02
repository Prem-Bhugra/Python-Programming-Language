f = open("File1.txt")
try:
    open("File.txt")
except Exception as e:
    print("Ye to error aa gaya:",e)
else:
    print("Else is executed only if Except is not executed,i.e., only if no error is thrown")
finally:
    print("Finally is compulsorily executed")
    print(f.read())
    f.close()