import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit as pw
import pyjokes
import tkinter as tk
from tkinter import filedialog

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<20:
        speak("Good Evening!")
    else:
        speak("Good Day!")
  
    speak("What you got for Jarvis to do? ")

def takeCommand():
    #Takes microphone input and give string output

    listener = sr.Recognizer()
    with sr.Microphone() as source :
        speak("Listening.....")
        print("Listening.....")
        listener.pause_threshold = 1
        listener.phrase_threshold = 0.5
        audio = listener.listen(source)

    try:
        print("In process....")
        query = listener.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        query = query.lower()
        
        if "jarvis" in query: 
            query = query.replace("jarvis","")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand()

        if "wikipedia" in query:
            try:
                speak("Searching Wiki....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                pass
        
        elif "turn off" in query:
            break

        elif "open folder" in query:
            root = tk.Tk()
            root.withdraw()
            filePath = filedialog. askopenfilename()
            os.startfile(filePath)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            webbrowser.open("https://www.google.com/")

        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com/")

        elif "play music" in query:
            # path folder with every \ as \\
            codePath = "D:\\Shreyansh\\Music"
            os.startfile(codePath)

        elif "play" in query:
            song = query.replace("play","")
            speak("playing" + song)
            print(song)
            pw.playonyt(song)
                
        elif "time" in query:
            Time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the current time is {Time}")
            print(f"Jarvis said: {Time}\n")
        
        elif "open code" in query:
            #path folder with every \ as \\
            codePath = "C:\\Users\\shrey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif "open edge" in query:
            #path folder with every \ as \\
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)

        elif "search" in query:
            command = query.replace("search","")
            speak("Searching" + command)
            print(command)
            pw.search(command)

        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)