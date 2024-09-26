import threading
from time import sleep

import speech_recognition as sr
from backend.processing import Process
from backend.speak import SpeakVoice



class InputCommand:

    def __init__(self):
        self.current_command = None
        self.speak = SpeakVoice().speak
        self.active = True

    # Function to listen for voice commands
    def listen_command(self):
        recognizer = sr.Recognizer()
        self.speak("¿Como te puedo ayudar?")
        while self.active:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

                try:
                    # Recognize the voice command
                    command = recognizer.recognize_sphinx(audio)  # Change language if needed
                    # recognizer.recognize_sphinx()
                    print(f"Command heard: {command}")
                    process = Process(command.lower())
                    status_process = process.start()
                    if status_process:
                        self.speak(f"Proceso {command.lower()} ejecutado exitosamente.")
                except sr.UnknownValueError:
                    print("Sorry, I didn't understand the command.")
                    self.speak("Lo siento, no te entendi.")

                except sr.RequestError as e:
                    print("Couldn't connect to the voice recognition service.", e)
                    self.speak("Lo siento, hubo un error.")


    def start_listening(self):
        self.active = True  # Cambia a estado activo

    def stop_listening(self):
        self.active = False  # Cambia a estado inactivo

    # Function to execute the command
    def manual_command(self, command):
        process = Process(command.lower())
        # process.init()
        status_process = process.start()
        if status_process:
            self.speak(f"Proceso {command.lower()} ejecutado exitosamente.")

