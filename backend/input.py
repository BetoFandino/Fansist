from time import sleep

import speech_recognition as sr
from processing import input_process
import pyttsx3
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to convert text to speech
def speak(message):
    engine.say(message)
    engine.runAndWait()


# Function to listen for voice commands
def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("How can I help you?")
        audio = recognizer.listen(source)

        try:
            # Recognize the voice command
            command = recognizer.recognize_sphinx(audio)  # Change language if needed
            # recognizer.recognize_sphinx()
            print(f"Command heard: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("Sorry, I didn't understand the command.")
            speak("Sorry, I didn't understand.")
            return None
        except sr.RequestError as e:
            print("Couldn't connect to the voice recognition service.", e)
            speak("Sorry, there was an error.")
            return None


# Function to execute the command
def execute_command(command):
    if command == 'thanks':
        print("Bye!")
        speak("Bye, boy.")
        sleep(3)
        return False
    input_process(command)
    return True



# Main example

while True:
    command = listen_command()
    if command:
        if not execute_command(command):
            break