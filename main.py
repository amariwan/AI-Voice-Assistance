import datetime
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import webbrowser
import pyautogui
import wikipedia
import os
import psutil
import wolframalpha
from time import sleep
import logging
import platform

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# User-specific data placeholders
USER_NAME = os.getenv("USER_NAME", "user")
USER_EMAIL = os.getenv("USER_EMAIL", "your_email")
USER_PASSWORD = os.getenv("USER_PASSWORD", "your_password")
WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID", "your_wolfram_app_id")
WEATHER_URL = "https://weather.com/weather/today/l/26.62,87.36?par=google&temp=c"
USER_AGENT = os.getenv("USER_AGENT", "your_user_agent")

def speak(audio):
    """Speaks out the given audio text."""
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def click():
    """Simulates a mouse click."""
    pyautogui.click()

def get_username():
    """Gets the username of the current user."""
    usernames = psutil.users()
    for user in usernames:
        speak(f"Sir, this computer is signed in as {user.name}.")

def take_screenshot():
    """Takes a screenshot and saves it to the Desktop."""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "screenshot.png")
    pyautogui.screenshot(desktop_path)
    speak(f"Screenshot saved to {desktop_path}")

def get_battery_status():
    """Gets the current battery status."""
    battery = psutil.sensors_battery()
    if battery:
        battery_percentage = battery.percent
        is_plugged = battery.power_plugged
        speak(f"Sir, it is {battery_percentage} percent.")
        if is_plugged:
            speak("and It is charging.")
        elif battery_percentage <= 95:
            speak("Sir, plug in the charger.")
    else:
        speak("Could not retrieve battery status.")

def shut_down():
    """Shuts down the computer."""
    speak("Initializing shutdown protocol.")
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    else:
        os.system("sudo shutdown now")

def restart():
    """Restarts the computer."""
    speak("Restarting your computer.")
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    else:
        os.system("sudo shutdown -r now")

def sleep_mode():
    """Puts the computer into sleep mode."""
    speak("Initializing sleep mode.")
    if platform.system() == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        os.system("pmset sleepnow")

def get_weather():
    """Fetches and speaks out the current weather details."""
    speak("Checking the details for weather...")
    headers = {"User-Agent": USER_AGENT}
    try:
        page = requests.get(WEATHER_URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        temperature = soup.find(class_="CurrentConditions--tempValue--3KcTQ")
        description = soup.find(class_="CurrentConditions--phraseValue--2xXSr")

        if temperature and description:
            temp = temperature.get_text()
            desc = description.get_text()
            speak(f"Sir, the temperature is {temp} Celsius and it is {desc} outside.")
        else:
            speak("Could not retrieve weather information.")
    except requests.RequestException as e:
        logging.error("Weather request failed: %s", e)
        speak("Failed to retrieve weather information.")

def check_messages():
    """Checks Facebook messages."""
    speak("Checking for messages...")
    try:
        client = Client(USER_EMAIL, USER_PASSWORD, user_agent=USER_AGENT)
        if client.isLoggedIn():
            threads = client.fetchUnread()
            if threads:
                speak(f"Sir, you have {len(threads)} new message(s).")
                for thread in threads:
                    info = client.fetchThreadInfo(thread.uid)[thread.uid]
                    speak(f"Message from {info.name}")
                    messages = client.fetchThreadMessages(thread.uid, limit=1)
                    for message in messages:
                        speak(f"Message: {message.text}")
            else:
                speak("Sir, you have no new messages.")
        else:
            speak("Failed to log in to Facebook.")
    except Exception as e:
        logging.error("Failed to check messages: %s", e)
        speak("Failed to check messages.")

def get_time():
    """Speaks out the current time."""
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    speak(f"Sir, the current time is {current_time}.")

def get_date():
    """Speaks out the current date."""
    now = datetime.datetime.now()
    speak(f"Sir, the current date is {now.strftime('%B %d, %Y')}.")

def google_search(query):
    """Performs a Google search."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query} on Google.")

def youtube_search(query):
    """Performs a YouTube search."""
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query} on YouTube.")

def calculate(expression):
    """Calculates the given expression using WolframAlpha."""
    client = wolframalpha.Client(WOLFRAM_APP_ID)
    try:
        res = client.query(expression)
        answer = next(res.results).text
        speak(f"The answer is {answer}.")
    except Exception as e:
        logging.error("Calculation failed: %s", e)
        speak("Failed to compute the answer.")

def recognize_command():
    """Recognizes voice commands."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"Recognized: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
    except sr.RequestError as e:
        logging.error("Recognition error: %s", e)
        speak("Sorry, I'm having trouble understanding you.")
    return ""

def handle_command(query):
    """Handles the recognized command."""
    if 'jarvis' in query:
        speak("Yes, Sir")
    elif 'date' in query:
        get_date()
    elif 'time' in query:
        get_time()
    elif 'thank you' in query:
        speak('No problem, Sir.')
    elif 'google' in query:
        speak('What do you want to search?')
        search_query = recognize_command()
        google_search(search_query)
    elif 'youtube' in query:
        speak('What do you want to search?')
        search_query = recognize_command()
        youtube_search(search_query)
    elif 'facebook' in query:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif 'gmail' in query:
        webbrowser.open("https://mail.google.com/")
        speak("Opening Gmail.")
    elif 'maps' in query:
        webbrowser.open("https://www.google.com/maps")
        speak("Opening Google Maps.")
    elif 'calculate' in query:
        speak('Tell me the expression.')
        expression = recognize_command()
        calculate(expression)
    elif 'weather' in query:
        get_weather()
    elif 'screenshot' in query:
        take_screenshot()
    elif 'wikipedia' in query:
        search_query = query.replace("wikipedia", "")
        results = wikipedia.summary(search_query, sentences=2)
        speak(f"According to Wikipedia, {results}")
    elif 'close window' in query:
        pyautogui.hotkey('alt', 'f4')
        speak('Closed the current window.')
    elif 'battery' in query:
        get_battery_status()
    elif 'shutdown' in query:
        shut_down()
    elif 'restart' in query:
        restart()
    elif 'sleep' in query:
        sleep_mode()
    elif 'message' in query:
        check_messages()
    elif 'username' in query:
        get_username()
    elif 'click' in query:
        click()
    else:
        speak("I did not understand that command.")

def greeting():
    """Gives a greeting message."""
    speak('Welcome back, Sir.')
    get_time()
    get_date()

if __name__ == '__main__':
    greeting()
    get_weather()
    speak("Getting battery information...")
    get_battery_status()
    while True:
        command_query = recognize_command()
        if command_query:
            handle_command(command_query)
