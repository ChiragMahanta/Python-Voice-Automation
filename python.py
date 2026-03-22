import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibary
import requests
import os
from dotenv import load_dotenv

# Initialize
r = sr.Recognizer()
engine = pyttsx3.init()

load_dotenv()


newsapi = os.getenv("NEWS_API_KEY")

# ---------------- SPEAK ----------------
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# ---------------- COMMAND HANDLER ----------------
def process_command(c):
    c = c.lower()

    # ---------- OPEN WEBSITES ----------
    if "open google" in c:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")

    # ---------- GOOGLE SEARCH ----------
    elif "search google for" in c:
        query = c.replace("search google for", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # ---------- PLAY MUSIC ----------
    elif "play music" in c:
        song = c.replace("play music", "").strip()

        link = musicLibary.music.get(song)

        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found in library")

    # ---------- NEWS ----------
    elif "news" in c:
        try:
            r_news = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
            )

            if r_news.status_code == 200:
                data = r_news.json()
                articles = data["articles"][:5]

                for article in articles:
                    speak(article["title"])
            else:
                speak("Could not fetch news")

        except:
            speak("Error getting news")

    # ---------- SYSTEM CONTROL ----------
    elif "shutdown" in c:
        os.system("shutdown /s /t 5")

    elif "restart" in c:
        os.system("shutdown /r /t 5")

    elif "lock" in c:
        os.system("rundll32.exe user32.dll,LockWorkStation")

    else:
        speak("Command not recognized")


# ---------------- MAIN LOOP ----------------
if __name__ == "__main__":
    speak("Hello Umesh, Jarvis is online")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            word = r.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Yes, how can I help you?")

                with sr.Microphone() as source:
                    print("Listening for command...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)

                command = r.recognize_google(audio)
                print("Command:", command)

                process_command(command)

        except sr.UnknownValueError:
            print("Could not understand")

        except sr.RequestError as e:
            print("API error:", e)

        except Exception as e:
            print("Error:", e)