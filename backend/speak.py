import threading
import os

class SpeakVoice:

    def __init__(self):
        # self.engine = pyttsx3.init()
        self.lock = threading.Lock()



    def start_speak(self, text):
        os.system(f'echo "{text}" | festival --tts')

    def speak(self, message):
        speak_thread = threading.Thread(target=self.start_speak, args=(message,))
        speak_thread.start()