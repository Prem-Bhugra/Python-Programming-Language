import time
def searcher():
    Names = "Prem Simran Abhiram Sagar Mayur Rahul Yuvraj Ninad Sabhya Pawan Taru Shinchan Doraemon Nobita Yash"
    time.sleep(2)
    while True:
        Name = (yield)
        if Name in Names:
            print("Your name is present")
        else:
            print("Your name is not present")
search = searcher()
print("Start searching")
next(search)
name = input("Enter your name\n")
search.send(name)
search.close
search.send("Simran")