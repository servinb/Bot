import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup

chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' 
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path)) #Ensures Chrome opens instead of IE

#Converts speech to text
def initialize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print "Hello, ready to listen."
        audio = r.listen(source)
    text = ''
    try:
        text = r.recognize_google(audio)
        print "Device thinks you said, " + text
    except sr.UnknownValueError:
        print "Device could not understand what you said"
    except sr.RequestError as e:
        print "Device could not receive request from user {0}".format(e)

    return text

#Takes command and does certain operation
def perform(text):
    if "search" in text:
        webbrowser.get('chrome').open_new_tab('google.com')
    elif "play" in text:
        webbrowser.get('chrome').open_new_tab("youtube.com")
        
        
data = initialize()
perform(data)        

        
        
        
        
        
        
        
        
        
        
        
        