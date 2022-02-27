# choose a file using windows explorer & print its filepath to the console

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:11:20 2022

@author: L00147036
"""

import PySimpleGUI as sg
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]

## building window
window = sg.Window('File browser', layout, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])