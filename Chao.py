#import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print "Hello, ready to listen."
    audio = r.listen(source)
    
try:
    print "Device thinks you said: " + r.recognize_google(audio)

except sr.UnknownValueError:
    print "I'm sorry, I didn't quite catch that"
    
except sr.RequestError as e:
    print "Device could not find results on Google; {0}".format(e)
    