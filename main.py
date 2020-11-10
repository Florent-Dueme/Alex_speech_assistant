# This will be our main file to build the speech assistant

# In order to install pyaudio remember to install pipwin first
# You need that because pyaudio requires portaudio,
# which is a C library and not an official python package.

import speech_recognition as sr
from time import ctime
import time
import webbrowser
import os
import random
import playsound
from gtts import gTTS


# First we will initialize a recognizer which is the main component of this library
# It is the think that actually recognizes speech
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alex_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            alex_speak("Sorry, I did not understand")
        except sr.RequestError:
            alex_speak("Sorry, my speech service is down")
        return voice_data


def alex_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 1000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if "What is your name" in voice_data:
        alex_speak("My name is Alex")
    if "What time is it" in voice_data:
        alex_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        alex_speak("Here is what I found for" + search)
    if "find location" in voice_data:
        location = record_audio("What is the location?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        alex_speak("Here is the location of" + location)
    if "exit" in voice_data:
        exit()


time.sleep(1)
print("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)