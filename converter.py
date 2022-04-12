import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True,), sg.Spin(['item 1','item 2'])],
    [sg.Button('Button', key = '-BUTTON1-')],
    [sg.Input()],
    [sg.Text('More Text'), sg.Button('Test Button', key = '-BUTTON2-')]
]

window = sg.Window('Converter',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        print('button pressed')

    if event == '-BUTTON2-':
        print('button pressed')

window.close()
