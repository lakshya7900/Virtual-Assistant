import pyttsx3
import pyaudio
from Functions.GetAIName import getname

engine = pyttsx3.init()
ainame = getname()

def say(text):
    print(f"{ainame}: {text}")
    engine.say(text)
    engine.runAndWait()