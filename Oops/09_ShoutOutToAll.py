# Write a program to shoutout the names given int the list using WIN32 API 


l = ["Santosh", "Bilok", "Bauaa"]

import pyttsx3
engine = pyttsx3.init()
for name in l:
    engine.say(f"Hello, how are you? {name}")

engine.runAndWait()
