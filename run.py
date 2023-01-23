from src.speech.main import getText
from src.utils.togglePrint import togglePrint
from src.speech.tools.calculator import isCalculus, sum
import sys

while True:
    togglePrint(False)
    try:
        text = getText()
        if text:
            togglePrint(True)
            print(text)

            if isCalculus(text):
                sum(text)

    except KeyboardInterrupt:
        sys.exit()