import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time


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
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    if "hey peter" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if"your name" in data1:
                name = "my name is peter"
                print(name)
                speechtx(name)
            elif "old are you" in data1:
                age = "i am two years old"
                print(age)
                speechtx(age)
            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'web' in data1:
                webbrowser.open("https://www.techview365.com/")
            elif 'joke' in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)
            elif 'play song' in data1:
                add = "C:/Users/Manis/OneDrive/Desktop/projects/tv365/Python Project/Voice_Assistant_Jarvis_Python/song"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))
            elif "exit" in data1:
                speechtx("thank you")
                break
            time.sleep(5)
    else:
        print("thanks")