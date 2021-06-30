import os  # pip install os
import googletrans  # pip install googletrans
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3
import pywhatkit  # pip install pywhatkit
import datetime  # pip install datetime
import wikipedia as wk  # pip install
import pyjokes  # pip install pyjokes
from googletrans import Translator
import weather  # pip install weather

listener = sr.Recognizer()
engine = pyttsx3.init()
start = True


def change_voice(n):        # Engine Speech Voice Alteration
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[n].id)


def talk(text):             # Engine Speech Function Definition
    trans = Translator()
    detected = trans.detect(text)
    lang_code = detected.lang
    engine.setProperty('languages', lang_code)

    engine.say(text)
    engine.runAndWait()


def greet():            # Defining the greet command
    x = datetime.datetime.now()
    hour = x.strftime("%H")
    hour = int(hour)
    if hour >= 4 and hour < 12:
        print('Good Morning...Sir')
        talk('Good Morning...Sir')
    elif hour >= 12 and hour <= 17:
        print('Good Afternoon...Sir')
        talk('Good Afternoon...Sir')
    elif hour >= 17 and hour < 24:
        print('Good Evening...Sir')
        talk('Good Evening...Sir')
    elif hour >= 0 and hour < 4:
        print('Good Evening...Sir')
        talk('Good Evening...Sir')


def take_command():             # Taking user's command via Speech

    with sr.Microphone() as source:
        print("Listening...")
        try:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('jarvis', '')

            print(command)
        except:             # Raising exception when engine does not hear anything specifically.
            command = "none"

    return command


def translate_lan(text, a):
    d = googletrans.LANGUAGES
    for key, value in d.items():
        if a == value:
            lang_code = key
    translator = Translator()
    ans = translator.translate(text, lang_code)
    return ans.text


def run_jarvis():
    global start
    command = take_command()

    if "hello" in command:
        talk("Hello there.")
        print("Hello there.")

    elif 'how are you' in command:
        talk('I am always smart and clever')
        print('I am always smart and clever')

    elif 'play' in command:
        song = command.replace('play', '')
        if 'me' in song:
            song = song.replace('me', 'you')
        else:
            pass

        talk('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('It is' + time + 'right now')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'translate' in command:
        command = command.replace('translate', '')
        L = list(command.split(" "))
        for i in range(len(L)):
            if L[i] == 'to' or L[i] == 'into':
                idx = i
        L_text = L[:i-1]
        L_lang = L[i:]
        text = ' '.join(L_text)
        lang = ' '.join(L_lang)
        answer = translate_lan(text, lang)
        print(answer)
        talk(answer)

    elif 'convert' in command:
        command = command.replace('convert', '')
        L = list(command.split(" "))
        for i in L:
            if L[i] == 'to' or L[i] == 'into':
                idx = i
        L_text = L[:i]
        L_lang = L[i+1:]
        text = ' '.join(L_text)
        lang = ' '.join(L_lang)
        answer = translate_lan(text, lang)
        print(answer)
        talk(answer)

    elif 'date' in command:
        if 'me' in command:
            if 'with' in command:
                talk('Sorry, I have a headache')
        elif 'today' in command:
            date = datetime.datetime.now().strftime(' %d: %B: %Y')
            print(date)
            talk(date)
        elif 'yesterday' in command:
            day = int(datetime.datetime.now().strftime('%d'))-1
            month_year = datetime.datetime.now().strftime('%B: %Y')
            date = str(day)+': '+month_year
            print(date)
            talk(date)
        elif 'tomorrow' in command:
            day = int(datetime.datetime.now().strftime('%d'))+1
            month_year = datetime.datetime.now().strftime('%B: %Y')
            date = str(day)+': '+month_year
            print(date)
            talk(date)

    elif 'who' in command:
        try:
            if 'is' in command:
                person = command.replace('who is', '')
                info = wk.summary(person, 1)
                print(info)
                talk(info)
            elif 'was' in command:
                person = command.replace('who was', '')
                info = wk.summary(person, 1)
                print(info)
                talk(info)
        except:
            print("Sorry..But I don't know about this person yet")
            talk("Sorry..But I don't know about this person yet")

    elif 'weather' in command:
        talk("These are some temperature details for you: ")
        weather.run()

    elif 'search' in command:
        line = command.replace('search', 'searching')
        if 'me' in line:
            line = line.replace('me', 'you')
            command = command.replace('me', '')
        info = wk.summary(command, 1)
        print(info)
        talk(info)

        talk(line)
        command = command.replace('search', '')
        pywhatkit.search(command)

    elif 'open' in command:
        command = command.replace('open', '')
        try:
            say = 'Opening'+command
            talk(say)
            print('Opening', command.upper())
            os.system(command)
            os.startfile()
        except:
            talk("Sorry...No programs found as such")
            print("Sorry...No programs found as such")

    elif 'stop' in command:

        talk("Okay...I will take your leave then")
        print("Okay...I will take your leave then")
        start = False

    elif command == "none":
        print("Sorry..Didn't hear that...Could you repeat again")
        talk("Sorry..Didn't hear that...Could you repeat again")

    else:
        if 'jarvis' in command:
            command = command.replace('jarvis', '')
            talk("These are some results.")
        pywhatkit.search(command)
