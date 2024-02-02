def func1(extra,*args,**kwargs):
    print(extra)
    print(type(args))
    print(args[1])
    print("The names of the students are:")
    for names in args:
        print(names)
    print(type(kwargs))
    for channels,series in kwargs.items():
        print(series,"is aired on",channels)
name=["Prem","Simran","Mayur","Khushi","Sagar"]
tv={"Cartoon Network":"BEN 10","Star Plus":"Kasauti Zindagi Ki","MTV":"Roadies","History TV 18":"Pawn Stars"}
extra1="This extra is not necessary but should be before the *args"
func1(extra1,*name,**tv)