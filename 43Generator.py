def gen(n):
    for i in range(n):
        yield i
g = gen(3)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
p = "Prem"
x = iter(p)
print(x.__next__())
print(x.__next__())
print(x.__next__())