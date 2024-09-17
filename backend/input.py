from execution import terminal_ejecutions, open_app, open_browser

def input_process(process):
    if process == 'edunext':
        terminal_ejecutions('sudo openvpn Documents/EDUNEXT/jorge_f.ovpn')
        open_app('todoist')
        open_app('spotify')
        open_browser('https://calendar.google.com/calendar/u/0/r')
        open_browser('https://3.basecamp.com/3966315/projects')