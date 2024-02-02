#Program to find the meaning of a word
dic1={"Mutable":"One which can be changed","Immutable":"On which cannot be changed","Wager":"Bet"
,"Procrastination":"Delaying or postponing work","Aesthetic":"Concerned eith beauty"}
word1=input("Enter a word\t")
word2=word1.capitalize()
print(word2,"means",dic1[word2])