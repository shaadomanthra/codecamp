import speech_recognition as sr
from gtts import gTTS
import webbrowser
import os

rec = sr.Recognizer()


with sr.Microphone() as m:
    print("Speak...")
    audio_input = rec.record(m,duration=3)
    text = rec.recognize_google(audio_input)
    print("You said: ",text)

    if text == 'French':
        print("Bonjour!!")
        t = gTTS("Bonjour")
        t.save('greeting_message.mp3')
        os.system("start greeting_message.mp3")
    elif text == 'Telugu':
        print("Namaskaram!!")
        t = gTTS("Namaskaram")
        t.save('greeting_message.mp3')
        os.system("start greeting_message.mp3")
    elif text == 'Facebook':
        print("Opening facebook website")
        webbrowser.open("https://facebook.com")
    elif text == 'Google':
        print("Opening google website")
        webbrowser.open("https://google.com")
    else:
        print("I dont know!!")
