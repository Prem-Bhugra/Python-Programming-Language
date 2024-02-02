#Program to set reminders for various activities
from time import time
from pygame import mixer
from datetime import datetime
def play(soundtrack,Stopper):
    mixer.init()
    mixer.music.load(soundtrack)
    mixer.music.play()
    while True:
        a = input()
        if a == Stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("Logs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
water = time()
eyes = time()
exercise = time()
watertime = 10
eyestime = 20
exercisetime = 30
while True:
    if time() - water > watertime:
        print("Time to drink water! Enter 'Drank' to stop the alarm.")
        play("Water.mp3","Drank")
        water = time()
        log("Drank water at")
    if time() - eyes > eyestime:
        print("Time to exercise your eyes! Enter 'Edone' to stop the alarm.")
        play("Eyes.mp3","Edone")
        eyes = time()
        log("Eyes exercised at")
    if time() - exercise > exercisetime:
        print("Time to exercise! Enter 'Exdone' to stop the alarm.")
        play("Exercise.mp3","Exdone")
        exercise = time()
        log("Exercised at")