import speech_recognition as sr
import webbrowser
import datetime


def speak(text):
    """Speaks the given text using the system's text-to-speech functionality."""
    engine = sr.Recognizer()
    with sr.Microphone() as source:
        engine.adjust_for_ambient_noise(source)  # Handle background noise
        audio = engine.listen(source)
    try:
        text = engine.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def get_audio():
    """Listens for user input and returns the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Recognized: " + text)
        return text.lower()  # Convert to lowercase for easier comparison
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None


def assistant(text):
    """Processes user commands and performs corresponding actions."""
    if text == "hello":
        speak("Hello! How can I help you today?")
    elif text == "what time is it":
        now = datetime.datetime.now()
        speak("It is " + now.strftime("%H:%M:%S"))
    elif text == "what is the date":
        today = datetime.date.today()
        speak("Today's date is " + today.strftime("%B %d, %Y"))
    elif "search for" in text:
        search_query = text.split("search for")[1].strip()
        speak("Searching the web for " + search_query)
        webbrowser.open("https://www.google.com/search?q=" + search_query)
    else:
        speak("Sorry, I can't assist you with that yet. How about I search the web for it?")
        search_query = text.strip()
        webbrowser.open("https://www.google.com/search?q=" + search_query)


print("Assistant is listening...")
while True:
    text = get_audio()
    if text:
        assistant(text)
