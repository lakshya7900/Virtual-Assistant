from time import sleep
import os
import winsound

def startTimer(seconds):
    for time in range(seconds, 0, -1):
        os.system('cls')
        time = f"{(time//3600):02}:{((time%3600)//60):02}:{((time%3600)%60):02}"
        print(time)
        sleep(1)
    print("Time's UP!")
    while True:
        winsound.PlaySound('D:\Virtual Assistant\Database\AlarmSound.wav', winsound.SND_FILENAME)

with open("Database\\timer.txt", "r") as f:
    time = f.read()

startTimer(int(time))