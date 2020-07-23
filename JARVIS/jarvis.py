
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import datetime
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("Good morning Dhara")

    elif hour>=12 and hour<18:
        speak("Good afternoon Dhara")    
    
    elif hour>=18 and hour<21:
        speak("good evening dhara")
    
    else:
        speak("good night dhara")
        
    speak("Your virtual assistant Jarvis is here. Please tell me how I can help you!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 553)
    server.ehlo()
    server.starttls()
    server.login('pd553025@gmail.com', 'password')
    server.sendmail('pritamdhara914@gmail.com', 'to', 'content')
    server.close()


if __name__ == "__main__":
    wishMe()
    if 1:
     query = takeCommand().lower()

     if 'wikipedia' in query:
         speak("Searching Wikipedia...")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("Acoording to Wikipedia")
         speak(results)
    
    
     elif 'open youtube' in query:  
         webbrowser.open("youtube.com")
         speak("opening youtube")
     
     elif 'open google' in query:  
         webbrowser.open("google.com")
         speak("opening google")
     
     elif 'open github' in query:  
         webbrowser.open("github.com")
         speak("opening github")

     elif 'play music' in query:
         webbrowser.open('https://www.youtube.com/watch?v=8CdcCD5V-d8&list=PLZMUPoLveOyiXf00FAWYYzr1xIA9ApV5f')    
         speak("sure")
     
     elif 'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"The time is {strTime}")

     elif 'code' in query:
         codePath = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"    
         os.startfile(codePath)
         speak("opening visual studio code")

     elif 'email to pd' in query:
         try:
             speak("What should I say?")    
             content = takeCommand()
             to = "pritamdhara914@gmail.com"
             sendEmail(to, content)
             speak("Your email has been sent!")
         except Exception as e:
             print(e)    
             speak("Pardon me sir! I failed to do so")

