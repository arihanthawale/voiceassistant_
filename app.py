import pyttsx3 as p
import speech_recognition as sr
from yt_audio import Music
from selenium_web import infow

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello, I am your Voice Assistant. How are You")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=2)
    print("Listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Recognized:", text)

    if "what" in text and "about" in text and "you" in text:
        speak("I am having a good day")

    speak("What can I do for you?")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)

    if "information" in text2:
        speak("You need information related to which topic?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=2)
            print("Listening...")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
        speak("Searching {} in Wikipedia".format(infor))
        assist = infow()
        assist.get_info(infor)

    elif "play" in text2 and "video" in text2:
        print("Recognized play command")
        speak("You want me to play which video?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=2)
            print("Listening...")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
        speak("Playing {} on YouTube".format(vid))
        assist = Music()
        assist.play(vid)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except Exception as ex:
    print("An error occurred:", ex)
