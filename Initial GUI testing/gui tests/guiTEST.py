# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:26:26 2022

@author: Amy

PySimpleGUI Introductory Tutorial
"PySimpleGUI: The Simple Way to Create a GUI With Python"
https://realpython.com/pysimplegui-python/

"""



# img_viewer.py

# import PySimpleGUI & Python's OS module
import PySimpleGUI as sg
import os.path

# set the window's theme
# (all themes can be previewed by using sg.theme_previewer())
# sg.theme('GrayGrayGray')

# first, the window layout in 2 columns

# create a nested list of elements that represent a vertical column of the UI

# key = what you use to identify a specific element in your GUI
# events can be enabled/disabled for each element with the enable_events parameter

# right-hand column of elements
# show all the text that has been analysed by the algorithm

word_list_column = [
    [
        sg.Text("Click an individual line of text to see the breakdown of its emotion levels:")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(60, 20), key="-LIST OF TEXT-")
    ],
]

# left-hand column of elements
# show the text that was chosen

# the following code creates 3 elements:
    # 1. one that tells the user to chooose an image to display
    # 2. one that displays the name of the selected file
    # 3. one to display the image
    
# note that the text being output has a key so we can easily refer back to it later
info_viewer_column = [
    [sg.Text("Choose a line of text on the right to begin.")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
]

# define the layout of the window

# next, write the code that will control how the elements are laid out on the screen

# contains two Column() elements with a VSeparator() (vertical separator) between them
layout = [
    [
        sg.Column(info_viewer_column),
        sg.VSeperator(),
        sg.Column(word_list_column),
    ]
]

# add the layout to the window
window = sg.Window("Emotion Viewer", layout)

# time to write the event loop to display the window!

# the event here will be the key string of whichever element the user interacts with
# the values variable contains a Python dictionary that maps the element key to a value
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    # window["-LIST OF TEXT-"].update(fnames)
    window["-LIST OF TEXT-"].update(-- ANALYSED WORDS GO HERE --)
        
    # if the event = "-LIST OF TEXT-", then you know the user has chosen a file in the listbox()
    # thus, you will want to update the Image() and Text() elements to show the selected filename on the right    
    
    if event == "-LIST OF TEXT-": # if a file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-LIST OF TEXT-"][0]
            )
            window["-TOUT-"].update(filename)
            # window["-IMAGE-"].update(filename=filename)
        except:
            pass
    
# when the user clicks exit, close the window
window.close()