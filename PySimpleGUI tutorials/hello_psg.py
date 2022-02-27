# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:20:47 2022

@author: Amy

PySimpleGUI Introductory Tutorial
"PySimpleGUI: The Simple Way to Create a GUI With Python"
https://realpython.com/pysimplegui-python/

"""

# hello_psg.py

# PySimpleGUI uses nested Python lists to lay out its elements

import PySimpleGUI as sg

# in this case, you add a Text() element and a Button() element
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# then, you create the window and pass in your custom layout

# create the window
window = sg.Window("Demo", layout)

# any GUI needs to run inside a loop & wait for the user to do something
# once the user does something, those events are processed by the event loop (i.e. clicking OK = breaking out of the loop & closing the window)
# infinite loops are a good thing here!

# create an event loop
while True:
    event, values = window.read()
    # end the program if the user closes the window OR presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    
window.close()