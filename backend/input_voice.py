from time import sleep

import speech_recognition as sr
from backend.processing import input_process
import pyttsx3
import os


class InputCommand:

    def __init__(self):
        self.current_command = None
        self.engine = pyttsx3.init()


    def speak(self, message):
        self.engine.say(message)
        self.engine.runAndWait()


    # Function to listen for voice commands
    def listen_command(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            self.speak("How can I help you?")
            audio = recognizer.listen(source)

            try:
                # Recognize the voice command
                command = recognizer.recognize_sphinx(audio)  # Change language if needed
                # recognizer.recognize_sphinx()
                print(f"Command heard: {command}")
                return command.lower()

            except sr.UnknownValueError:
                print("Sorry, I didn't understand the command.")
                self.speak("Sorry, I didn't understand.")
                return None
            except sr.RequestError as e:
                print("Couldn't connect to the voice recognition service.", e)
                self.speak("Sorry, there was an error.")
                return None


    # Function to execute the command
    def execute_command(self, command):
        if command == 'thanks':
            print("Bye!")
            self.speak("Bye, boy.")
            sleep(3)
            return False
        input_process(command)
        return True
