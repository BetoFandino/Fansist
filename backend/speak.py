import threading
import pyttsx3

class SpeakVoice:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.lock = threading.Lock()

    def start_speak(self, message):
        with self.lock:
            self.engine.say(message)
            self.engine.runAndWait()

    def speak(self, message):
        speak_thread = threading.Thread(target=self.start_speak, args=(message,))
        speak_thread.start()