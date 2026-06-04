import pyttsx3



def voice(text:str):
    engine = pyttsx3.init()

    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id) 

    engine.say(text)
    engine.runAndWait()



