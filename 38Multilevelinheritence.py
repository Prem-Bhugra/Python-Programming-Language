class Electronicdevices:
    var = 1 
    x = 50
    public = 123
    _protected = 456
    __private = 789
class Pocketgadgets(Electronicdevices):
    var = 2
    y = 75
class Phones(Pocketgadgets):
    var = 3
    z = 100
Toaster = Electronicdevices()
Taser = Pocketgadgets()
Samsung = Phones()
print(Samsung.var,Taser.var,Toaster.var,Samsung.z,Samsung.y,Samsung.x,Taser.y,Taser.x,Toaster.x)
print(Toaster.public,Toaster._protected,Toaster._Electronicdevices__private,Taser.public,Taser._protected,Taser._Electronicdevices__private)