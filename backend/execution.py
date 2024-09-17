import subprocess
import webbrowser
import os

def terminal_ejecutions(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error ejecting command: {e.stderr}"

def open_browser(url):
    try:
        chrome_path = '/usr/bin/google-chrome'  # Default path in many Linux distributions

        subprocess.run([chrome_path, url])

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