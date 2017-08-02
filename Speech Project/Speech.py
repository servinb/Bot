import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print "Hello, ready to listen."
    audio = r.listen(source)
    

try:
    text = r.recognize_google(audio)
    print "Google thinks you said, " + text
except sr.UnknownValueError:
    print "Google could not understand what you said"

