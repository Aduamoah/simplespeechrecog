import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text to speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def recognize_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("User:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))
            return ""

# Main loop
while True:
    command = recognize_command()

    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        now = datetime.datetime.now()
        current_date = now.strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What would you like me to search for?")
        search_query = recognize_command()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
    elif "exit" in command:
        speak("Goodbye!")
        break
