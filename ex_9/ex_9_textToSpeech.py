# from gtts import gTTS

# import os

# li = ["Raj", "Shiv", "Bala"]
# # myText = "Hey There Everyone!"

# language = 'en'

# for liname in li:
#     readData = f"Shoutout to {liname}"
# myObj = gTTS(
#     text = readData,
#     lang = language,
#     slow = False
# )

# myObj.save("shoutout.mp3")

# os.system("mpg321 shoutout.mp3")


import pyttsx3 
engine = pyttsx3.init()
names = ["Raj", "Bala", "Shiv", "Sakshi", "Riya", "Neha"]
for name in names:
    engine.say(f" Shoutout to {name}")

engine.runAndWait()