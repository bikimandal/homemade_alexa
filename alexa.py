import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import pyjokes
# import wikipedia
import winsound
from playsound import playsound
import requests
import winsound
from AppOpener import run
import sys

import requests 
 
frequency = 1000
duration = 500


user_name = "Beekey"
# global city
user_city = "siliguri"

def check_connection() -> None:
     try:
        requests.get("https://google.com")
        return True
     except requests.RequestException:
        return False
    
    
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("rate", 110)
engine.setProperty("voice", voices[1].id)
command = ("")
def talk(text):

    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            winsound.Beep(frequency, duration)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            global exit
            exit = False
            if "turn off" in command and "system" in command:
                # raise SystemExit
                print("")
            elif "turn off" in command:
                exit = True
            elif "alexa" in command:
                # playsound('sound1.mp3')
                print("working...")
                command = command.replace("alexa", "")
                return command
            else:
                talk("not recognised")
                command = ""  
                take_command()   
    except:
        command = ""
        take_command()
        pass

    return command

def run_alexa():
    command = take_command()
    if "hi" in command or "hai" in command:
        talk("Hii" + user_name + "what can i do for you")
                                                                         #weather
    if "weather" in command :
        print(weather(user_city))
        talk(weather(user_city))
                                                                         #open
    elif "open" in command:
        app_name = command.replace("open", "")
        talk("opening" + app_name)
        run(app_name)
        sys.exit("Closing Alexa")
                                                                         # playing youtube songs
    elif "play" in command:
        song = command.replace("play", "")
        talk("playing" + song + "on youtube")
        pywhatkit.playonyt(song)
        sys.exit("Closing Alexa")
                                                                         # date and time
    elif "time" in command:
        time = datetime.now().strftime("%I:%M %p")
        talk("current time is " + time)
                                                                         # search
    # elif "who is" in command:
    #     person = command.replace("who is", "")
    #     info = search("Google", num_results=1)
    #     print(info)
    #     talk(info)
    # single
    elif "are you single" in command:
        talk("i am in a relationship with wifi")
    # joke
    elif "joke" in command:
        talk(pyjokes.get_joke())
    # else
    elif "turn off" in command:
        exit = True
    elif "thank you" in command:
        talk("Mention not. It is my plesure.")
    elif "who is my girlfriend" in command:
        talk("as far as i know u are in love with shubhaankeeta")

    else:
        talk("please say it again")
        take_command()

def close_alexa():
    talk("Bye Bye" + user_name + "seee you later")


def get_time_of_day(time):
    if time < 12:
        return "Morning"
    elif time < 16:
        return "Afternoon"
    elif time < 19:
        return "Evening"
    else:
        return "Night"
global now
now = datetime.now()
def greetings():
    if 'Night' in get_time_of_day(now.hour):
        print("Hey " + user_name +" Good Evening")
        talk("hey " + user_name +"good Evening")
    elif "Morning" in get_time_of_day(now.hour):
        print("Hey " + user_name +" Good Morning")
        talk("hey" + user_name +"Good Morning")
    else:
        print("Hey " + user_name +" Good Evening")
        talk("hey" + user_name +"Good Evening")

def weather(city):
    # city = input("input city: ")
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
        
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)

    output=(f"The weather in {city} is {condition} and the current Temperature there is {temp} degree celcious") 
    return output



                                                #main_program
if check_connection() == True:
    greetings()
    while True:
        run_alexa()
        if exit == True:
            print("Turning off")
            close_alexa()
            break
else:
    talk("Check Your Internet Connection and try again")




    
