import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import re


engine = pyttsx3.init()
GOOGLE_API_KEY = "AIzaSyDLaih5sXlFlbJdGBeCrwLXt0d4GPD5YA8"
genai.configure(api_key=GOOGLE_API_KEY)

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('pitch', 160)     # Percentage (can go up to 200)
engine.setProperty('rate', 160)     # Speed percent (can go up to 200)
engine.setProperty('rate', 160)    # Speed percent (can go over 100)
engine.setProperty('volume', 1)

# try:
#     for model in genai.list_models():
#         print(model)
# except Exception as e:

#      print(f"Error: {e}")


def filter_please_explain(text):
    pattern = r'\bplease explain\b'
    if re.search(pattern, text, re.IGNORECASE):
        return True
    else:
        return False
    

def speecer(text, engine):
  # Volume 0-1
    engine.say(text)
    engine.runAndWait()

def take_command():

    """
    Take command from user and return it.

    Returns:
        str: Command taken from user.
    """
 
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query


def translate_and_speak(text):
    """
    Translate given text and speak it using text-to-speech.

    Args:
        text (str): Text to be translated and spoken.
    """
    translator = Translator()
    translated = translator.translate(text, dest='si')
    print(f"Translated text: {translated.text}")

    tts = gTTS(text=translated.text, lang='si')
    tts.save("output.mp3")

    os.system("start output.mp3")


command = ""
speecer("Hello, I am yasra", engine)



while command != "stop":
    command = take_command()

    if command == "stop":
        text = "Ok sumal I leave for you now"
        speecer(text, engine)
        break

    elif command == "None":
        continue

 


    elif command  == "hello" or command == "hello yasra" or command == "hello Astra" or command == "hello Yatra":
        text = "Hello, sumal how can I help you?"

    elif command == "what is your name":
        text = "I am your virtual assistant."
    
    elif command == "how are you":
        text = "I am fine, thank you and how are you?"
    
    elif command == "how old are you":
        text = "I am 1 years old."

    elif command == "what can you do":
        text = "I can talk with you"

    elif filter_please_explain(command):
        try:
            req =command
            model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
            response = model.generate_content(req+"Explain (20 <words <100)") 
            text = str(response.text)
        except Exception as e:
            print(f"Error: {e}")

    else:

        try:
            req =command
            model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
            response = model.generate_content(req + "give me short answer") 
            text = str(response.text)
        except Exception as e:
            print(f"Error: {e}")

    print(text)
    speecer(text, engine)
    


