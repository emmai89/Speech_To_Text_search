import speech_recognition as sr
import keyboard
import time
import webbrowser

def audioToText():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    print("checking.....")

        # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language='en-AUS')
        print("Google Speech Recognition thinks you said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return text

def textToAction(text):
    # chose what function is wanted
    sections = text.split()

    if sections[0] == "open" :
        webbrowser.open('http://' +sections[1] +'.com', new=2)
        # opens up google and performs the search
    elif sections[0] == "images" and sections[1] == "of" :
        print("images")
    else :
        webbrowser.open('http://google.com', new=2)
        time.sleep(5)
        keyboard.write(text, 0.05)
        keyboard.press_and_release('enter')
