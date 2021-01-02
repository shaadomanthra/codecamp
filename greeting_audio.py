from gtts import gTTS
import os
x = int(input("Choose the language (1-Telugu,2-Hindi):"))

if x == 1:
    text = 'నమస్కరం!'
    t = gTTS(text)
    t.save("text.mp3")
    os.system("start text.mp3")
    print("The audio is generated in telugu")
elif x ==2:
    text = 'नमस्कार!'
    t = gTTS(text)
    t.save("text.mp3")
    os.system("start text.mp3")
    print("The audio is generated in hindi")
else:
    print("I dont know!")