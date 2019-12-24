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