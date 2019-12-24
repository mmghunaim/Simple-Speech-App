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