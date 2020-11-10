# This will be our main file to build the speech assistant

# In order to install pyaudio remember to install pipwin first
# You need that because pyaudio requires portaudio,
# which is a C library and not an official python package.

import speech_recognition as sr
from time import ctime
import time
import webbrowser

# First we will initialize a recognizer which is the main component of this library
# It is the think that actually recognizes speech
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("Sorry, I did not understand")
        except sr.RequestError:
            print("Sorry, my speech service is down")
        return voice_data


def respond(voice_data):
    if "What is your name" in voice_data:
        print("My name is Alex")
    if "What time is it" in voice_data:
        print(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        print("Here is what I found for" + search)
    if "find location" in voice_data:
        location = record_audio("What is the location?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        print("Here is the location of" + location)
    if "exit" in voice_data:
        exit()


time.sleep(1)
print("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)