import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# name input system

name = input("What is your: ")

# speak def system

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish me system

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("hello " + name + "Sir I am Feed How Can i Help You")

    # take command system
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:  {query}")

    except Exception as e:
        # print(e)
        print("Say That Again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('name', 'password')
    server.sendmail('email', to, content)
    server.close()





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open YouTube" in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube")

        elif "open Google" in query:
            webbrowser.open("google.com")
            speak("Opening google")

        elif "facebook" in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook")
            
            # change the music folder location

        elif 'play music' in query:
            music_dir = 'C:\\Users\\your user\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(name + f"Sir, The Time is {strTime}")

        # change sent name and sent email

        elif 'email to sent name' in query:
            try:
                speak("What Should i Say?")
                content = takeCommand()
                to = "your sent email"
                sendEmail(to, content)
                speak("Email Has Been Sent!")
            except Exception as e:
                print(e)
                speak("Sorry"+ name +"Sir I am Not Able To Send This Email")


        elif "weather" in query:
            search = "temperature in city" 
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            date = BeautifulSoup(r.text,"html.parser")
            temp = date.find("div",class_="BNeawe").text
            print(f"current {search} is {temp}")
            speak(f"current {search} is {temp}")

        elif 'hello feed' in query:
            speak("Hi"+ name +"Sir!") 

        elif 'how are you' in query:
            speak("i am fine how are you")

        elif 'what is your name' in query:
            speak("Hello Sir My Name Is Feed How Can i Help You")

        elif 'happy birthday' in query:
            speak("happy birthday to you"+ name +"sir")

        elif 'you are so bad' in query:
            speak("sorry"+ name +"sir")
        
        elif 'thankyou feed' in query:
            speak("no problem")

        elif 'feed good night' in query:
            speak("good night"+ name +"sir have a sweet dream")
