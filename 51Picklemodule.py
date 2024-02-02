import pickle
cars = ["BMW","Maruti Suzuki","Hero Honda","Mercedes"]
with open("Mycar.pkl","wb") as fileobject:
     pickle.dump(cars,fileobject)
with open("Mycar.pkl","rb") as fileobject:
    Mycar = pickle.load(fileobject)
    print(Mycar)