from time import sleep
from backend.input_voice import InputCommand
from backend.speak import SpeakVoice
from backend.worker import ThreadManager


class Brain:
    def __init__(self):
        self.input_command = InputCommand()
        self.speak = SpeakVoice()
        self.speak.speak("Virtual Assistant activated.")
        self.thread_manager = ThreadManager()
        self.thread_manager.register_event("voice_listening", self.input_command.listen_command)

    def disable_listen_command(self):
        self.thread_manager.deactivate_event("voice_listening")
        self.input_command.stop_listening()

    def enable_listen_command(self):
        self.thread_manager.trigger_event("voice_listening")
        self.input_command.start_listening()

    def input_manual_command(self, command):
        self.input_command.manual_command(command)



