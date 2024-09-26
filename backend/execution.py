import subprocess
import webbrowser
import os
from dotenv import load_dotenv

load_dotenv()

def terminal_executions(command):
    try:
        password = os.getenv('SUDO_PASSWORD')

        # Abre un terminal en el directorio /home/user y ejecuta el comando
        subprocess.run(
            ['gnome-terminal', '--working-directory=/home/jorge', '--', 'bash', '-c', f'echo {password} | sudo -S {command}; exec bash'])
    except subprocess.CalledProcessError as e:
        return f"Error ejecting command: {e.stderr}"

def open_browser(profile_name, url):
    try:
        chrome_path = '/usr/bin/google-chrome'  # Default path in many Linux distributions

        subprocess.run([chrome_path,f"--profile-directory={profile_name}", url])

    except FileNotFoundError:
        print("Google Chrome not found. Trying with the default browser.")
        webbrowser.open(url)

def open_app(app):
    try:
        subprocess.Popen([f"{app}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{app} opened successfully in the background.")

    except FileNotFoundError:
        print(f"{app} is not installed or not found in the system PATH.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to open {app}: {e}")

