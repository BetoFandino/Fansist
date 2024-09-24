import sqlite3
import json


class DatabaseManager:
    def __init__(self, db_name="processes.db"):
        # Connect to or create the database
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        # Create the table if it doesn't exist
        self.create_table()

    def create_table(self):
        """
        Creates a table called 'processes' to store information about processes.
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS processes (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               process_name TEXT NOT NULL,
                               action LIST NOT NULL)''')
        self.connection.commit()

    def insert_process(self, process_name, action_list):
        """
        Inserts a new process into the table.
        :param process_name: The name of the process (e.g., 'open_browser')
        :param action_list: A list of dictionaries, where each dictionary contains a command and its arguments.
                            For example: [{"name": "open_app", "app": "Todoist"}, {"name": "open_browser",
                            "url": "https://google.com"}]
        """
        action_json = json.dumps(action_list)
        self.cursor.execute("INSERT INTO processes (process_name, action) VALUES (?, ?)", (process_name, action_json))
        self.connection.commit()

    def get_all_processes(self):
        """
        Retrieves all processes from the table.
        """
        self.cursor.execute("SELECT * FROM processes")
        return self.cursor.fetchall()

    def get_process(self, process_name):
        """
        Retrieves a command based on its name and converts the action from JSON back to a Python list of dictionaries.
        :param process_name: The name of the command to search for
        :return: A tuple with command_name and action (as a list of dictionaries) if found, else None
        """
        self.cursor.execute("SELECT * FROM processes WHERE process_name = ?", (process_name,))
        result = self.cursor.fetchone()
        if result:
            process_name = result[1]
            action_list = json.loads(result[2])  # Convert the JSON back to a list of dictionaries
            return process_name, action_list
        return process_name, None

    def update_process(self, process_id, new_action_list):
        """
        Updates the action of an existing command in the table.
        :param process_id: The ID of the command to update
        :param new_action_list: The new list of actions to assign to the command
        """
        new_action_json = json.dumps(new_action_list)  # Convert the new action list to JSON format
        self.cursor.execute("UPDATE commands SET action = ? WHERE id = ?", (new_action_json, process_id))
        self.connection.commit()

    def delete_process(self, process_id):
        """
        Deletes a process from the table.
        :param process_id: The ID of the process to delete
        """
        self.cursor.execute("DELETE FROM processes WHERE id = ?", (process_id,))
        self.connection.commit()

    def close(self):
        """
        Closes the connection to the database.
        """
        self.connection.close()
