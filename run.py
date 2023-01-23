from src.speech.main import getText
from src.utils.togglePrint import togglePrint
from src.speech.tools.calculator import isCalculus, sum
import pyttsx3
import sys

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while True:
    togglePrint(False)
    try:
        text = getText()
        if text:
            togglePrint(True)
            print(text)

            if isCalculus(text):
                result = sum(text)
                speakText(result)

    except KeyboardInterrupt:
        sys.exit()