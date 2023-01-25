import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
engine.setProperty('voice', 'es-es')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Buenos dias perro !")
  
    elif hour>= 12 and hour<18:
        speak("Buenas tarde perro !")  
  
    else:
        speak("Buenas noche bastardo !") 
  
    assname =("Jarvis 1 point o")
    speak("Soy tu asistente")
    speak(assname)
     
 
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='es-cl')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
  
