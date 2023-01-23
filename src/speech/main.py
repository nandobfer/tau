import speech_recognition as sr

recognizer = sr.Recognizer()

def getText():
    with sr.Microphone() as source2:
        recognizer.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = recognizer.listen(source2)
        try:
            MyText = recognizer.recognize_google(audio2, language = 'pt-BR').lower()

            # speakText(f"{MyText}")
            return MyText
        except:
            return False
        
    