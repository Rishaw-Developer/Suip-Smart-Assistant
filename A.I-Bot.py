import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import pywhatkit

engine = pyttsx3.init('sapi5') 
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[11].id)
engine.setProperty('volume', 1.2) 

def speak(tell):
    engine.say(tell)
    engine.runAndWait()

def wishes():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hy boss, I am suip. Please tell me how can I help you.") 

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening you sir!")
        r.pause_threshold = 1
        command = r.listen(source)

    try:
        print("Hearing...")
        take = r.recognize_google(command, language='en-in')
        print(f"You said: {take}\n")

    except Exception as e:
        speak("Sorry sir I can't hear you. Can you please speak again.")
        return ""

    return take

def whatsapp():
    contact = {
        """Enter your all contacts here"""
        """Write like this
        "enter the name here such as (Iron Man)": "enter the number here such as (+91 222222555....)", !important add a comma after adding a contact
        """
    }
    print("Where to be sent...")
    where = hear().lower()
    print("What to be sent...")
    text = hear()
    time_hour = int(datetime.datetime.now().hour)
    time_minutes = int(datetime.datetime.now().minute + 2)
    pywhatkit.sendwhatmsg(contact[where], text, time_hour, time_minutes)


def starting_the_command(info):

    if "wikipedia" in info:
        speak("Searching Wikipedia...")
        info = info.replace("wikipedia", "")
        answer = wikipedia.summary(info, sentences=2)
        print('According to Wikipedia')
        print(answer)
        speak(answer)

    elif "youtube" in info:
        speak('Opening Youtube')
        webbrowser.open('http://www.youtube.com')

    elif "open google" in info:
        speak('Opening Google')
        webbrowser.open('http://www.google.com')

    elif "open stackoverflow" in info:
        speak('Opening Stackoverflow')
        webbrowser.open('http://www.stackoverflow.com')

    elif "open w3schools" in info:
        speak('Opening w3schools')
        webbrowser.open('http://www.w3schools.com')

    elif "the time" in info:
        speak('Getting the time')
        get_time = datetime.datetime.now().strftime("%I:%M")
        speak(f"Sir, the time is {get_time}")

    elif "open code" in info:
        path = r'C:\Users\Rishaw\AppData\Local\Programs\Microsoft VS Code\Code.exe'
        speak('Opening your code')
        os.startfile(path)

    elif "open pycharm" in info:
        path_pycharm = r'C:\Program Files\JetBrains\PyCharm Community Edition 2020.3.2\bin\pycharm64.exe'
        speak("Opening pycharm")
        os.startfile(path_pycharm)

    elif "message" in info:
        speak("Ya sending the message...")
        whatsapp()

    elif "plus" or "add" or "+" in info:
        if "plus" in info:
            get = info.split("plus")
        
        elif "add" in info:
            get = info.split("add")

        elif "+" in info:
            get = info.split("+")

        sum = 0
        for x in range(len(get)):
            sum += int(get[x])

        print(f"The sum is {sum}")
        speak(f"The sum is {sum}")

    elif "minus" or "subtract" or "-" in info:
        if "minus" in info:
            get = info.split("minus")
        
        elif "suntract" in info:
            get = info.split("subtract")

        elif "-" in info:
            get = info.split("-")

        subtraction = int(info[0]) - int(info[1])

        print(f"The subtraction is {subtraction}")
        speak(f"The subtraction is {subtraction}")

    elif "quit" in info:
        speak('By sir. Thanks for using me')
        sys.exit('BY')

    elif "google" or "Google" or info in info:
        if info == "":
            pass

        else:
            speak('Searching on google...')
            info = info.replace("google", "")
            webbrowser.open(f"https://www.google.com/search?q={info}&oq=w3&aqs=chrome.1.69i57j35i39j0i395i433l4j0i395j69i59.2196j1j15&sourceid=chrome&ie=UTF-8")

    else:
        speak("I am quiting. BY BY...")
        sys.exit('BY BY')    
    
if __name__ == '__main__':
    wishes()
    info = hear().lower()
    starting_the_command(info)
