import speech_recognition as sr
# from googletrans import Translator
from datetime import datetime

def Input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=2)
            query = r.recognize_google(audio, language="en-IN")
            return str(query)
        except:
            return "no input"
        
# def Translate(text):
#     translate = Translator()
#     line = translate.translate(text)
#     data = line.text
#     return data

def takeCommand():
    query = Input()
    print("Recognizing...")
    # data = Translate(query)
    time = datetime.now().strftime("%H:%M")
    print(f"[{time}] User said: {query}")
    return query