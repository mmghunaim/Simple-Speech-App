def speak(txt):
    tts = gTTS(text= txt, lang='en')
    r = random.randint(1,10000000)
    audio = 'audio-'+ str(r)+'.mp3'
    tts.save(audio)
    playsound.playsound(audio)
    print(txt)
    os.remove(audio) 