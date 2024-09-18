from execution import terminal_ejecutions, open_app, open_browser

def input_process(process):
    if process == 'one':
        print("Iniciando el VPN de EDUNEXT...")
        terminal_ejecutions('openvpn Documents/EDUNEXT/jorge_f.ovpn')
        open_app('todoist')
        open_app('spotify')
        open_browser('Default','https://calendar.google.com/calendar/u/0/r')
        open_browser('Default', 'https://3.basecamp.com/3966315/projects')
    else:
        print(f"No tengo habilitado el proceso '{process}'. Por favor, intente con otro.")