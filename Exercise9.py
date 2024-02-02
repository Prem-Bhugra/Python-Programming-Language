#Program to read a news report
import requests
import json
def speak(str):
      from win32com.client import Dispatch
      speak = Dispatch("Sapi.SpVoice")
      speak.Speak(str)
if __name__ == "__main__":
    r = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3fbc8ab38b4140509d7679a1290db441").text
    dict = json.loads(r)
    speak("News for today.... Lets begin!")
    i = 1
    while i<=10:
        a =  input("Press space and then enter to listen to the news\n")
        if a == " ":
            print(((dict['articles'])[i-1])['title'])
            speak(((dict['articles'])[i-1])['title'])
            i += 1
        else:
            print("Wrong key")
            break
    speak("Thanks for listening")
    print("No more news reports present")