import PySimplegGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Nospied!')]],ag.Button('Šķeres')
[sg.Button('Neaizvērt')]
[sg.Button('Aizvērt')]

window = sg.Window('Spēle',layout)

while True:
    event, values = window.read()
    if event == 'Aizvērt':
        break

window.close()

