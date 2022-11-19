import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import googlesearch
import pyjokes
import time
import requests
from bs4 import BeautifulSoup
import googlescrap
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',205)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Heyy Good Morning! This is Alice....Your personal assistant...You can command me to perform various tasks such as calculating sums or opening applications." )

    elif hour>=12 and hour<18:
        speak(" heyy Good Afternoon!This is Alice....Your personal assistant...You can command me to perform various tasks such as calculating sums or opening applications.")   

    else:
        speak(" heyy Good Evening! This is Alice....Your personal assistant...You can command me to perform various tasks such as calculating sums or opening applications.")  


       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening that")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing!")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print(" Please say that again...")
  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       
        elif 'open browser' in query:
            webbrowser.open("google.com")

        elif 'open quora' in query:
            webbrowser.open("quora.com")   


        elif 'play music' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))
            os.startfile(os.path.join(music_dir, songs[2]))
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Chinmaya.")
            
    
        elif "calculate" in query:
             
            app_id = "TWY6XY-86VU5RA3LA"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)  
            
        elif "day" in query:
            day = datetime.datetime.today().weekday() + 1
     
            Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
            if  day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)
        
                
        elif 'date' in query:
         try:
            from datetime import date
            today = date.today()
            today = datetime.datetime.now().strftime("%d %B, %Y")
            print("Today's date:", today)
            speak("Today's date:" + today)
         except:
            speak("This operation is having some issue please try again!")      
             

        elif 'open code' in query:
             codePath ="C:\\Users\\91790\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)

        elif 'email to Chinmaya' in query:
             try:
                speak("What should I say?")
                content = takeCommand()
                to = "chinmayauniyal@gmail.com.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
             except Exception as e:
                print(e)
                speak("Sorry ! try again later")
        
        elif 'joke' in query:
             joke1=pyjokes.get_joke(language="en",category="all")
             print(joke1)
             speak(joke1)
        
        elif "exit" in query:
            speak("thank you...bye bye")
            break
        
        elif 'google' in query:
            import wikipedia as googlescrap 
            query=query.replace("alice","")
            query=query.replace("googlr search","")
            query= query.replace("google", "")
            speak("This is what i found on the web!")
            pywhatkit.search(query)
            
            try:
                result=googlescrap.summary(query,3)
                speak("result")
            except:
                speak("no data is available")
                
            
            
            
        
        time.sleep(5)
