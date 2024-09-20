from time import sleep
from backend.input_voice import InputCommand

def brain():
    input_command = InputCommand()
    input_command.speak("Virtual Assistant activated. Type 'exit' to close.")
    sleep(2)
    while True:
        command = input_command.listen_command()
        if not input_command.execute_command(command):
            break

if __name__ == "__main__":
    brain()