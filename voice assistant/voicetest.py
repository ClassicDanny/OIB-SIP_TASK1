import webbrowser
import speech_recognition as sr
import datetime
import pyttsx3


class VoiceAssistant:
    class RecognitionError(Exception):
        pass

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def speak_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_audio(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                return self.recognizer.recognize_google(audio).lower()
            except sr.WaitTimeoutError:
                raise self.RecognitionError("Listening timed out. Please try again.")
            except sr.UnknownValueError:
                raise self.RecognitionError("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                raise self.RecognitionError(f"Error occurred during request to Google Speech Recognition service: {e}")

    def assistance(self, text):
        if 'hello' in text:
            self.speak('Hello! How are you today? How can I help you?')
        elif 'time' in text:
            now = datetime.datetime.now()
            self.speak("It's " + now.strftime("%H:%M:%S"))
        elif 'date' in text:
            now = datetime.date.today()
            self.speak("Today's date is " + now.strftime("%B %d, %Y"))
        elif 'search' in text:
            search_query = text.split("search")[1].strip()
            self.speak("Searching for " + search_query)
            webbrowser.open("https://www.google.com/search?q=" + "+".join(search_query.split()))
        elif 'exit' in text:  # Exit condition
            self.speak("Exiting the program. Goodbye!")
            exit()


# Usage
if __name__ == "__main__":
    assistant = VoiceAssistant()
    print("Welcome! I am a voice assistant.")
    print("What would you like to do?")
    print("Listening for your command...")
    while True:
        try:
            text = assistant.get_audio()
            if text:
                assistant.assistance(text)
        except VoiceAssistant.RecognitionError as e:
            print(e)
