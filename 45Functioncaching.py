import time
from functools import lru_cache
@lru_cache(maxsize = 3)
def somework(n):
    time.sleep(n)
    return n
if __name__=='__main__':
    print("Now running somework")
    somework(2)
    print("Done...Calling Again")
    somework(2)
    print("Called again")