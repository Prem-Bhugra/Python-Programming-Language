import sys
print(sys.path)
import Testfile1
print(Testfile1.a)
Testfile1.joke("This is me")
from Testfile1 import a
print(a)