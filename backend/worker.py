import threading
import time

class ThreadManager:
    def __init__(self):
        # Dictionary to store events and threads
        self.events = {}
        self.threads = {}

    def register_event(self, event_name, function, *args):
        """
        Registers an event with its corresponding thread.
        :param event_name: Name of the event (str)
        :param function: Function to be executed by the thread
        :param args: Optional arguments for the function
        """

        event = threading.Event()
        # Define the thread associated with the event
        thread = threading.Thread(target=self._run_thread, args=(event, function, *args), daemon=True)

        # Store the event and thread in their respective dictionaries
        self.events[event_name] = event
        self.threads[event_name] = thread

        # Start the thread
        thread.start()

    def _run_thread(self, event, function, *args):
        """
        Executes the thread when the event is triggered.
        :param event: Event to control the thread
        :param function: Function to be executed by the thread
        :param args: Arguments for the function
        """
        while True:
            if event.is_set():
                function(*args)  # Execute the function associated with the event
                # event.clear()  # Pause the event after execution
            time.sleep(4)  # Short pause to avoid unnecessary CPU usage

    def trigger_event(self, event_name):
        """
        Triggers the event, allowing the corresponding thread to execute its function.
        :param event_name: Name of the event to trigger (str)
        """
        if event_name in self.events:
            self.events[event_name].set()
        else:
            print(f"Event '{event_name}' not registered.")

    def deactivate_event(self, event_name):
        """
        Deactivates the event, stopping the function from executing in the thread.
        :param event_name: Name of the event to deactivate (str)
        """
        if event_name in self.events:
            self.events[event_name].clear()
        else:
            print(f"Event '{event_name}' not registered.")

    def stop_thread(self, event_name):
        """
        Stops a thread completely.
        :param event_name: Name of the thread to stop (str)
        """
        if event_name in self.threads:
            self.threads[event_name].join(timeout=1)
            print(f"Thread '{event_name}' stopped.")
        else:
            print(f"Thread '{event_name}' not registered.")

    def is_event_active(self, event):
        """
        Verificar si el evento está activado
        :return: True si el evento está activado, False si está desactivado
        """
        return event.is_set()