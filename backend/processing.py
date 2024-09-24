from backend.database import DatabaseManager
from backend.execution import terminal_executions, open_app, open_browser
from backend.speak import SpeakVoice

speak = SpeakVoice().speak


class Process:
    def __init__(self, process):
        self.process = process
        self.database = DatabaseManager()
        self.database.create_table()

    def init(self):
        action = [{
        'name': 'terminal_execution',
        'command': 'openvpn Documents/EDUNEXT/jorge_f.ovpn',
    },
    {
        'name': 'open_browser',
        'profile_name': 'Default',
        'url': 'https://calendar.google.com/calendar/u/0/r',
    },
    {
        'name': 'open_app',
        'app': 'todoist',
    },{
        'name': 'open_app',
        'app': 'spotify',
    },{
        'name': 'open_browser',
        'profile_name': 'Default',
        'url': 'https://3.basecamp.com/3966315/projects',
    }
    ]
        print('guardado data test')
        self.database.insert_process('one', action)

    def get(self):
        return self.database.get_process(self.process)

    def start(self):
        process_name, process = self.get()
        if not process: return None
        for procesing in process:
            if procesing['name'] == 'terminal_execution':
                terminal_executions(procesing['command'])
            elif procesing['name'] == 'open_browser':
                open_browser(procesing['profile_name'], procesing['url'])
            elif procesing['name'] == 'open_app':
                open_app(procesing['app'])
        return True

