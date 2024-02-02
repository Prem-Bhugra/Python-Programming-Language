with open("File4.txt") as f:
    print(f.tell())
    print(f.readline())
    print(f.tell())
    print(f.readline())
    print(f.tell())
    f.seek(10)
    print(f.tell())
    print(f.readline())