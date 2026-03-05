# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Listening...")
#     recognizer.adjust_for_ambient_noise(source, duration=1)
#     audio = recognizer.listen(source)

# try:
#     print("Recognizing...")
#     text = recognizer.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))

#     def speak(text):
#         engine.say(text)
#         engine.runAndWait()
import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    else:
        print("Command not recognized")

if __name__ == "__main__":
    speak("Hello Umesh, Jarvis is online")

    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            print("You said:", word)

            if word.lower() == "jarvis":
                speak("Yes Umesh, how can I assist you?")

                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)

                command = r.recognize_google(audio)
                process_command(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results:", e)
