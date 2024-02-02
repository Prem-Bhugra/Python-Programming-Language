import time
a=time.time()
print(a)
i=0
while i<5:
    print(i,end="")
    time.sleep(2)
    i+=1
print("\n",time.time()-a)
b=time.time()
print(b)
for j in range(5):
    print(j,end="")
print("\n",time.time()-b)
x=time.asctime(time.localtime(time.time()))
print(x)