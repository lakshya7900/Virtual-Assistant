# Import stuff
from datetime import datetime
import webbrowser
import AppOpener
import os
from requests import get
import pyautogui
from tkinter.filedialog import *
from keyboard import press
from time import sleep
# import pywhatkit
from Functions.GetPartOfDay import getPartOfday
from Functions.TakeCommand import takeCommand
# from Functions.ChromeSpeak import say
from Functions.WindowsSpeak import say
from Functions.Chat import chat
from Functions.GetAIName import getname
from Functions.Whatsapp import WhatsappMsg
import Functions.SpotifyAutomation as spotify
from Functions.WeatherReport import GetWheatherReport
from Functions.GetBatteryStatus import batterystatus
from Functions.InternetSpeed import InternetSpeedTest
from Database.googleauthenticator import Verify
from Functions.UserDetails import GetUserDetails
import Functions.ClapDetection
# from Functions.PrivateRecordingMode import StartRecord, StopRecord
import json
from subprocess import CREATE_NEW_CONSOLE
import subprocess



ainame = getname()
command = []



# Do work using AI
def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n **************** \n\n"
    
    prompt = ''.join(prompt.split(f'ai')[1:]).strip()
    text = chat(prompt)

    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"D:\Virtual Assistant\OpenAI\{''.join(prompt.split('ai')[1:]).strip()}.txt", "w") as f:
        f.write(text)

    say("Sir file created and stored in OpenAI folder.")


# Tasks
def tasks(query):
    # Change AI's name
    if "change" in query and "your" in query and "name" in  query:
        name = {}

        with open('D:\Virtual Assistant\Database\AIname.json', 'r') as f:
            name = json.load(f)

        say("Sir what do you want my name to be?")
        print("Listening...")
        name['name'] = "".join((takeCommand()).split())

        with open('D:\Virtual Assistant\Database\AIname.json', 'w') as f:
            json.dump(name, f)

        say(f"Ok sir. Name changed to {name['name']}")
        global ainame 
        ainame = name['name']
        
        # import Functions.ChromeSpeak as cs
        # cs.ainame = name['name']

        import Functions.Chat as ch
        ch.ainame = name['name']

        import Functions.WindowsSpeak as ws
        ws.ainame = name['name']
        
    # Open Stuff
    elif "open" in query:
        isWebsite = False
        with open("D:\Virtual Assistant\Database\Sites.json", "r") as f:
            sites = json.load(f)
        
        for site in sites['sites']:
            if f"open {site['name']}" in query:
                say(f"Opening {site['name']} Sir...")
                webbrowser.open(site['link'])
                isWebsite = True

        if isWebsite != True:
            appname_input = ''.join(query.split('open')[1:]).strip()
            try:
                appname = AppOpener.open(f"find {appname_input}", match_closest=True, output=False)
                AppOpener.open(appname_input.lower(), match_closest=True)
                say(f"Opening {appname} Sir.")
            except:
                say(f"Sir I was unable to find anything realted to {appname_input}.")
    
    # Close Application
    elif "close" in query:
        name = ''.join(query.split('close')[1:]).strip()

        try:
            appname = AppOpener.open(f"find {name}", match_closest=True, output=False)
            say(f"Ok sir, closing {appname}")
            AppOpener.close(appname, match_closest=True)
        except:
            say(f"Sir cannot find an open application with the name {name}")

    # Set a timer
    elif "set" in query and "timer" in query:
        hours, minutes, seconds = 0, 0, 0

        if "hour" in query or "minute" in query or "seconds" in query:
            say(f"Sure Sir\n"
                f"A timer set for {''.join(query.split('timer for')[1:]).strip()}")

            timearr = query.split()
            
            for x in range(len(timearr)):
                if 'hour' in str(timearr[x]).lower():
                    hours = int(timearr[x-1])
                elif 'minute' in str(timearr[x]).lower():
                    minutes = int(timearr[x-1])
                if 'second' in str(timearr[x]).lower():
                    seconds = int(timearr[x-1])


        else:
            say("Sir for how long would you like to the set the timer for")
            print("Listening...")
            uInput = takeCommand()
            say(f"Sir, a timer set for {uInput}")

            timearr = uInput.split()
            
            for x in range(len(timearr)):
                if 'hour' in str(timearr[x]).lower():
                    hours = int(timearr[x-1])
                elif 'minute' in str(timearr[x]).lower():
                    minutes = int(timearr[x-1])
                if 'second' in str(timearr[x]).lower():
                    seconds = int(timearr[x-1])

        finaltime = (hours * 3600) + (minutes * 60) + seconds

        with open("D:\Virtual Assistant\Database\\timer.txt", 'w') as f:
            f.write(str(finaltime))

        process = subprocess.Popen(["D:\Virtual Assistant\Functions\Timer.py"], shell=True)

    # Say current time
    elif "time" in query:
        time = datetime.now().strftime("%I:%M %p")
        say(f"The time right now is {time}.")

    # Say current date
    elif "date" in query:
        date = datetime.now().strftime("%B %d, %Y")
        say(f"Sir today is {date}.")

    # Say current day
    elif "day" in query:
        day = datetime.now().strftime("%A")
        say(f"Sir today is {day}.")

    # Get current temperature
    elif "temperature" in query:
        currenttemp = GetWheatherReport()[0]
        say(f"Sir the current temperature is {currenttemp} °Celsius")

    # Get weather report
    elif "weather" in query:
        temp, feelslike, temp_min, temp_max, weather_type = GetWheatherReport()
        say("Sir the current weather report is:\n"
            f"Weather type: {weather_type}\n"
            f"Temperatue: {temp} °C\n"
            f"Feels Like: {feelslike} °C\n"
            f"Minimum temperature: {temp_min} °C\n"
            f"Maximum temperature: {temp_max} °C")

    # Open cmd
    elif "open cmd" in query:
        say("Opening Command Prompt.")
        os.system("start cmd")

    # Get ip address
    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        say(f"Sir your IP Address is {ip}.")

    # Play songs on youtube
    # elif "play song on youtube" in query:
    #     say("Sir which song to play on youtube.")
    #     print("Listening...")
    #     uInput = takeCommand()

    #     say(f"Playing {uInput} on youtube.")
    #     pywhatkit.playonyt(uInput)

    # Play playlist on spotify
    elif "play" in query and "playlist" in query:
        name = ''.join(query.split('playlist')[1:]).strip()
        result = spotify.Playlist(name)

        if "ERROR" in result:
            say(f"Sorry I was unable to find any playlist of yours named: {name.capitalize()}")

    # Play songs on spotify
    elif "play" in query:
        name = ''.join(query.split('play')[1:]).strip()

        result = spotify.PlaySong(name)
        songlink = result['uri']
        songname = result['name']
        artistname = result['artists'][0]['name']

        if "Error" in result:
            say(f"Sir I was unable to find a song named {name} in spotify")
        else:
            say(f"Playing {songname} by {artistname} in spotify")
            webbrowser.open(songlink)
            AppOpener.open('spotify', match_closest=True, output=False)
            sleep(1)
            press('enter')
            
    # Pause/Play song
    elif "resume" in query and "song" in query or "pause" in query and "song" in query:
        spotify.PausePlaySong()
    
    # Next song
    elif "next" in query and "song" in query:
        spotify.NextSong()
        
    # Previous song
    elif "previous" in query and "song" in query:
        spotify.PreviousSong()

    # Starting song
    elif "start" in query and "song" in query:
        spotify.StartingSong()

    # Shuffle song
    elif "shuffle" in query and "song" in query:
        spotify.Shuffle()

    # Repeat song
    elif "repeat" in query and "song" in query:
        spotify.Repeat()

    # Skip 5 sec
    elif "skip" in query and "5 seconds" in query:
        spotify.SeekFrwd()

    # Rewind 5 sec
    elif "rewind" in query and "5 seconds" in query:
        spotify.SeekBkwrd()

    # Send whatsapp message
    elif "send" in query and "whatsapp" in query and "message" in query:
        say("Sir what message would you like to send?")
        print("Listening")
        message = takeCommand()
        while message == "":
            print("Listening...")
            say("Sorry sir I couldn't get what you said! Could you please repeat.")
            message = takeCommand()

        say("And to whom would you like to send this message?")
        print("Listening")
        name = takeCommand()
        while name == "":
            print("Listening...")
            say("Sorry sir I couldn't get what you said! Could you please repeat.")
            name = takeCommand()

        say("Sending message...")
        WhatsappMsg(name, message)
        say("Message sent.")

    # Get battery status
    elif "battery" in query:
        batteryperct = batterystatus()[0]
        if "percentage" in query:
            say(f"Sir your system currently has {batteryperct}% left")

        elif "status" in query:
            batterypluggedin = batterystatus()[1]
            if batterypluggedin:
                say("Sir your battery status report is: \n"
                    f"Battery Percentage = {batteryperct}%\n"
                    "Battery plugged in to power")
            else:
                say("Sir your battery status report is: \n"
                    f"Battery Percentage = {batteryperct}%   \n"
                    "Battery not plugged in to power")

    # Get internet speed
    elif "internet" in query and "speed" in query:
        say("Calculating your internet speed sir...")
        downloadspeed, uploadspeed, ping = InternetSpeedTest()
        say(f"Sir your internet speed results are as followed:\n"
            f"Download speed: {downloadspeed / 1048576:.2f} Mbps\n"
            f"Upload speed: {uploadspeed / 1048576:.2f} Mbps\n"
            f"Ping: {ping:.2f} ms")

    # Take screenshot
    elif "screenshot" in query and "take" in query:
        say("Taking Screenshot...")
        ss = pyautogui.screenshot()
        path = asksaveasfilename()
        ss.save(path+"_screenshot.png")
        say("Screenshot taken.")

    # Get passwords
    elif "password" in query:
        say("Sir first you will have to verify yourself!\n"
            "Please enter the two-factor authentication code!")
        code = input("CODE: ")

        if Verify(code):
            say("Sir which sites's credential do u need?")
            name = input("USER INPUT: ")

            result = GetUserDetails(name)

            if 'Sir I could not find any saved credentials' in result:
                say(result)
            else:
                say("Sir here are your credentials.")
                print(result)
        else:
            say("Sir the code was incorrect!")

    # Shutdown pc
    elif "shut" in query and 'down' in query:
        say("Shutting down system.")
        os.system("shutdown /s /t 5")

    # Restart pc
    elif "restart" in query:
        say("Restarting the system.")
        os.system("shutdown /r /t 5")

    # Put pc to sleep
    elif "sleep" in query:
        say("Putting the system to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    # Lock the screen
    elif "lock" in query:
        os.system("rundll32.exe user32.dll, LockWorkStation")

    # Use AI to create prompts
    elif "using ai" in query:
        say("Ok Sir, creating file.")
        ai(prompt=query)

    # Start Recording mode
    elif 'recording mode' in query and 'start' in query:
        stopRecordCalled = {"stopRecordCalled": "False"}

        with open('D:\Virtual Assistant\Database\ScreenRecord.json', 'w') as f:
            json.dump(stopRecordCalled, f)

        subprocess.Popen(["D:\Virtual Assistant\.venv\Scripts\python.exe", "D:\Virtual Assistant\Functions\PrivateRecordingMode.py"], shell=True)

    # Stop Recording mode
    elif 'recording mode' in query and 'stop' in query:
        stopRecordCalled = {"stopRecordCalled": "True"}

        with open('D:\Virtual Assistant\Database\ScreenRecord.json', 'w') as f:
            json.dump(stopRecordCalled, f)

    # Deactivate virtual assistant
    elif "deactivate" in query and ainame.lower() in query:
        say("Deactivated.")
        deactivated()

    # Quit virtual assistant
    elif "quit" in query and ainame.lower() in query:
        say("Ok Sir. Quitting....")
        exit()

    # Bye virtual assistant
    elif "bye" in query and ainame.lower() in query:
        say("Bye. Have a nice day sir!")
        exit()

    # Goodnight virtual assistant
    elif "good night" in query and ainame.lower() in query:
        say("Goodnight Sir.")
        exit()

    # Reset chat
    elif "reset chat" in query or "clear chat" in query:
        say("Chat reset!")
        chat('CLEAR CHAT 2202')

    # Blank input
    elif "no input" in query:
        say("Sorry Sir! I didn't quite get what you said, would you mind repeating!")

    # Chat with virtual assistant
    else:
        say(chat(query))



# Activated
def activated():
    hour = getPartOfday(datetime.now().hour)
    say(f"Good {hour} Sir. How may I help you?")

    while True:
        print("Listening...")
        query = takeCommand().lower()

        tasks(query)



# Deactivated
def deactivated():
    while True:
        print("Deactivated...")

        # Activate virtual assistant using clap
        # Functions.ClapDetection.ListenForClap() 
        # if Functions.ClapDetection.clap == True:
        #     activated()
        
        
        uInput = takeCommand().lower()
        # Activate virtual assistant using voice
        if "activate" in uInput and ainame.lower() in uInput:
            activated()

        # Wakeup virtual assistant
        elif "wake up" in uInput and ainame.lower() in uInput:
            activated()

        # Quit virtual assistant
        elif "quit" in uInput and ainame.lower() in uInput:
            say("Ok Sir. Quitting....")
            exit()

        # Bye virtual assistant
        elif "bye" in uInput and ainame.lower() in uInput:
            say("Bye. Have a nice day sir!")
            exit()

        # Goodnight virtual assistant
        elif "good night" in uInput and ainame.lower() in uInput:
            say("Goodnight Sir.")
            exit()

        elif f'hey {ainame.lower()}' in uInput or f'hello {ainame.lower()}' in uInput:
            query = ''.join(uInput.split(f'{ainame.lower()}')[1:]).strip()
            tasks(query)



# Call on start
if __name__ == '__main__':
    deactivated()