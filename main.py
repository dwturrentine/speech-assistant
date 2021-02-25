import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

# Recognizer - recognizes speech
r = sr.Recognizer()

# Function to remove from global scope
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            lyrad_speak(ask)
        audio = r.listen(source)

        voice_data = ''

        # Error handling for unintelligible speech and request error
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            lyrad_speak('Sorry, I did not get that')
        except sr.RequestError:
            lyrad_speak('Sorry my speech service is down.')
        return voice_data

# Function for Assistant to speak
def lyrad_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


# Function to take in voice data
def respond(voice_data):
    if 'what is your name' in voice_data:
        lyrad_speak('My name is Lyrad')
    if 'what time is it' in voice_data:
        lyrad_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        lyrad_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        lyrad_speak('Here is what the location of ' + location)
    if 'exit' in voice_data:
        exit()

# Continuous listening
time.sleep(1)
lyrad_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)

