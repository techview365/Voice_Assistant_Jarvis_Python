import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


# speech recognition function 
def sptext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("recognizing...")
            data = r.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print(" Not Understand ")
            
sptext()