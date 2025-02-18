import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import pyjokes
import pyautogui
import time
import random
from colorama import init, Fore
import sys

# Colorama initialize
init(autoreset=True)

# Initialize pyttsx3 engine only once
siri = pyttsx3.init()

# Set the speech rate (lower value means slower speech)
rate = siri.getProperty('rate')
siri.setProperty('rate', rate - 50)  # Slow down the speech speed

# Set voice (optional, can be changed based on the available voices on your system)
voices = siri.getProperty('voices')
siri.setProperty('voice', voices[1].id)  # Set to female voice (0 for male, 1 for female)

# Function to make the assistant talk
def talk(text):
    try:
        if text:  # Check if text is not empty
            siri.say(text)
            siri.runAndWait()
    except Exception as e:
        print(f"Error in speaking: {e}")

# Speech recognition function
listener = sr.Recognizer()

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print(Fore.GREEN + 'Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '')
    except Exception as e:
        print(f"Error in listening: {e}")
    return command

# Hacking Animation Function
def hacking_animation():
    hacking_texts = [
        "Accessing mainframe...",
        "Bypassing security...",
        "Decrypting passwords...",
        "Extracting sensitive data...",
        "Uploading trojan virus...",
        "Compiling payload...",
        "Connection established...",
        "Root access granted..."
    ]

    print(Fore.GREEN + "=" * 50)
    print(Fore.GREEN + "     ASSISTANT MODE ACTIVATED     ")
    print(Fore.GREEN + "=" * 50)
    
    for text in hacking_texts:
        sys.stdout.write(Fore.GREEN + f"\n[+] {text}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.5, 1.5))

    print(Fore.GREEN + "\n\n[✓] PROCESS COMPLETE!")
    time.sleep(1)
    print(Fore.GREEN + "\n[✓] System Secure. Launching Siri AI...\n")
    time.sleep(2)

# Run the hacking animation at the start
hacking_animation()

# Run the AI assistant
def run_siri():
    command = take_command()

    if 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time_now)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'stop music' in command:
        talk('Stopping the music.')
        time.sleep(2)  # Wait for YouTube to fully load
        pyautogui.hotkey('ctrl', 'w')  # Close YouTube tab

    elif 'tell me about' in command:
        look_for = command.replace("tell me about", '')
        info = wikipedia.summary(look_for, 1)
        talk(info)
        print(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke()) 

    elif 'date' in command:
        talk('Sorry, I am in another relationship.')

    elif 'search' in command:
        query = command.replace('search', '')
        talk('Searching in Google...')
        pywhatkit.search(query)

    elif 'stop' in command:
        talk('Goodbye!')
        return False  # Exit the program

    else:
        talk("How can I help you!")

    return True  # Continue listening

# Main program loop
talk("Hello sir, I am Siri.")
while True:
    if not run_siri():  
        break  # Exit loop when "stop" is said
