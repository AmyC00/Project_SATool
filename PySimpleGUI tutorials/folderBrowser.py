# choose a folder using windows explorer & output the path to the console

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:14:37 2022

@author: L00147036
"""

import PySimpleGUI as sg
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose a folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")]]


## building window
window = sg.Window('My folder browser', layout, size=(600,150))
    
while True:
    event, values = window.read()
    print(values["-IN2-"])
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])