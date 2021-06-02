def speech():
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening : ... ')
        audio = r.listen(source,timeout = 10,phrase_time_limit=5)
        
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print('sorry!! please try again')
            return -1
# print(speech())
def isYesNo():
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening : ... ')
        audio = r.listen(source,timeout = 10,phrase_time_limit=5)
        
        try:
            text = r.recognize_google(audio)
            return text
        except:
            #print('sorry!! please try again')
            return "No"