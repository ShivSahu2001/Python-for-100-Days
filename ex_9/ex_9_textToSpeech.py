from gtts import gTTS

import os

li = ["Raj", "Shiv", "Bala"]
# myText = "Hey There Everyone!"

language = 'en'

for liname in li:
    readData = f"Shoutout to {liname}"
myObj = gTTS(
    text = readData,
    lang = language,
    slow = False
)

myObj.save("shoutout.mp3")

os.system("mpg321 shoutout.mp3")