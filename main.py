import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import wolframalpha

engine = pyttsx3.init()

r = sr.Recognizer()

mic = sr.Microphone()


def voice_parameter(i, j):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[i].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + j)

def firstoutput():
    voice_parameter(7, 10)
    engine.say('Hello, My name is Mike')
    engine.say('how may I help you?')
    engine.runAndWait()


def record():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('speak')
        audio = r.listen(source)
        return audio


def convert(audio):
    try:
        input1 = r.recognize_google(audio)
    except:
        print('Sorry I am unable to understand what you said.')
        input1 = ''
    return input1


def process(input1):
    if 'how are you' in input1:
        output1 = 'I am doing great. How are you doing?'
    elif 'are you a human' in input1:
        output1 = '''No!. I am a voice assistant created by Sir.Virat Kota and Sir.Siddharth. 
        I was created for helping humans.'''
    elif 'who are you' in input1:
        output1 = 'I am a voice assistant created by Virat Kota. I was created for helping humans.'
    elif '' == input1:
        output1 = 'I did not catch that'
    elif 'who are your creators' in input1 or 'who is your creator' in input1:
        output1 = '''Virat Kota have created me to help humans.'''
    elif 'what is your name' in input1:
        output1 = 'My name is Mike.'
    elif 'what is the time' in input1:
        output1 = datetime.datetime.now().strftime('%H:%M')
    elif 'google' in input1:
        input2 = 'https://www.google.com/search?q=' + input1
        webbrowser.open_new_tab(input2)
        output1 = 'searching in google for \"' + input1 + '\"'
    elif 'play a song' in input1:
        webbrowser.open_new_tab('https://open.spotify.com/playlist/4Qld8MoiinGP3X6hKhEyic')
        ouput1 = 'Opening Spotify'
        return ouput1
    elif 'open' in input1:
        input2 = input1.replace('open ', '')
        input3 = input2.replace(' ', '')
        input4 = 'https://www.' + input3 + '.com'
        webbrowser.open_new_tab(input4)
        output1 = input2 + " is now open "
    elif 'Wikipedia' in input1 or 'wikipedia' in input1:
        try:
            engine.say('Searching Wikipedia...')
            input1 = input1.replace('wikipedia', '')
            results = wikipedia.summary(input1, sentences=3)
            output1 = 'According to wikipedia ' + results
        except:
            output1 = 'Asked query not found in wikipedia'
    else:
        try:
            try:
                app_id = 'H44595-LV966663J2'
                client = wolframalpha.Client(app_id)
                res = client.query(input1)
                output1 = next(res.results).text
            except:
                results = wikipedia.summary(input1, sentences=3)

                output1 = 'According to wikipedia ' + results
        except:
            try:
                input2 = 'https://www.google.com/search?q=' + input1
                webbrowser.open_new_tab(input2)
                output1 = 'searching in google for \"' + input1 + '\"'
            except:
                pass
    return output1


def edit(output1):
    if len(output1) > 500:
        output1 = output1[:500] + '...'
    output1 = output1.replace('(', ' ')
    output1 = output1.replace(')', ' ')
    output1 = output1.replace(';', ' ')
    output1 = output1.replace('\'', ' ')
    return output1



def voiceoutput():
    voice_parameter(7, 10)
    audio = record()
    input1 = convert(audio)
    output1 = process(input1)
    output1 = edit(output1)
    return output1


