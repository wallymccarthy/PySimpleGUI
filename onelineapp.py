import PySimpleGUI as sg

print(sg.Window('',[[sg.Input(),sg.Button('OK'),sg.Button('Cancel')]]).read())
