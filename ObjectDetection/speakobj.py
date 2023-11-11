from plyer import tts
import pyttsx3
from googletrans import Translator

def CountFreq(li):
    freq = {}
    for items in li:
        freq[items] = li.count(items)
    return str(freq)

def speak(a):
    translator = Translator()
    translated = translator.translate(a, src="en", dest="pt").text
    engine = pyttsx3.init()
    engine.say(translated)
    engine.runAndWait()