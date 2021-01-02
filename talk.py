import speech_recognition as sr
rec = sr.Recognizer()

with sr.Microphone() as m:
    print("Speak...")
    audio_input = rec.record(m,duration=3)
    text = rec.recognize_google(audio_input)
    print("You said: ",text)
