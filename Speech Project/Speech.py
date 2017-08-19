import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
import wolframalpha
import winshell
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

#Wolframalpha API I.D.
app_id='PA237Q-XA42375UEE'
client = wolframalpha.Client(app_id)

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
        text = text.split()
        text = ' '.join(text[1:])
        speak.Speak("searching")
        webbrowser.get('chrome').open_new_tab('google.com/search?q=' + text)
    elif "video" in text:
        text = text.split()
        text = '+'.join(text[1:])
        speak.Speak("pulling up video")
        webbrowser.get('chrome').open_new_tab("youtube.com/results?search_query=" + text)
    elif "mail" in text:
        speak.Speak("opening mail")
        webbrowser.get('chrome').open_new_tab('portal.office.com')
    elif "math" in text:
        r2 = sr.Recognizer()
        with sr.Microphone() as source:
            speak.Speak("Ask your math question")
            audio2 = r2.listen(source)
        question = ''
        try:
            question = r2.recognize_google(audio2)
            print "Device thinks you said, " + question
            try: 
                res = client.query(question)
                ans = (next(res.results).text)
                speak.Speak(ans)
            except:
                speak.Speak('I don\'t understand your question')
            #print ans
        except sr.UnknownValueError:
            print "Device could not understand what you said"
        except sr.RequestError as e:
            print "Device could not receive request from user {0}".format(e)
        
    elif "empty" in text:
        recycle_bin = winshell.recycle_bin()
        speak.Speak("emptying recycle bin")
        recycle_bin.empty(confirm=False, show_progress=False, sound=True)
    elif "desktop" in text:
        speak.Speak("opening desktop")
        winshell.desktop(common=True)
        
        
data = initialize()
perform(data)        

        
        
        
        
        
            
        
        
        
        
        
        