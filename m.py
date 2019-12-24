import speech_recognition as sr
from time import ctime
import webbrowser
import time
from gtts import gTTS
import playsound
import os
import random

r = sr.Recognizer()


def save_aduio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Say something known')
        except sr.RequestError:
            speak('The service is down because you start to use it')
    return voice_data


def speak(txt):
    tts = gTTS(text= txt, lang='en')
    r = random.randint(1,10000000)
    audio = 'audio-'+ str(r)+'.mp3'
    tts.save(audio)
    playsound.playsound(audio)
    print(txt)
    os.remove(audio)


def reply(data):
    if 'hi' in data:
        speak('Hi mr.mohammed')    
    if 'Tell me the time' in data:
        speak('nth')
        print(ctime())
    if 'find' in data:
        search = save_aduio('What do you want to search for?')  
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak('Here is what I found for '+search)
    if 'what is my location' in data:
        # location = save_aduio('What location is it?')
        # url = 'https://google.nl/maps/place/'+location+'/&amp;'
        url = 'https://google.nl/maps/place/gaza/&amp;'
        webbrowser.get().open(url)
    if 'exit' in data:
        exit()    


time.sleep(1)
speak('This app programmed by Mr. Mohammed Ghunaim')
speak('How can I help you')
while 1:
    voice_data = save_aduio()
    reply(voice_data)

