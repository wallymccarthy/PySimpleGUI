import PySimpleGUI as sg

chat_col = sg.Column([
[sg.Multiline(no_scrollbar = True, size = (40,5), key = '-TEXTBOX-')]
])
control_col = sg.Column([
[sg.Button('Send', key = '-SEND-')]
])

layout = [
    [chat_col],
    [control_col]
    ]

window = sg.Window('Chat with Professor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
