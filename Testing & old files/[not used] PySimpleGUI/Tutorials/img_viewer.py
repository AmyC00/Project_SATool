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
sg.theme('GrayGrayGray')

# first, the window layout in 2 columns

# create a nested list of elements that represent a vertical column of the UI
# this will create a Browse button that you'll use to find a folder with images in it

# key = what you use to identify a specific element in your GUI
# the In() text control will be used later to access the contents of the element
# events can be enabled/disabled for each element with the enable_events parameter

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# right-hand column of elements
# for now, we will only show the name of the file that was chosen

# the following code creates 3 elements:
    # 1. one that tells the user to chooose an image to display
    # 2. one that displays the name of the selected file
    # 3. one to display the image
    
# note that the image element has a key so we can easily refer back to it later
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# define the layout of the window
# next, write the code that will control how the elements are laid out on the screen

# contains two Column() elements with a VSeparator() (vertical separator) between them
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

# add the layout to the window
window = sg.Window("Image Viewer", layout)

# time to write the event loop to display the window!

# the event here will be the key string of whichever element the user interacts with
# the values variable contains a Python dictionary that maps the element key to a value
    # i.e. if the user picks a folder, then "-FOLDER-" will map to the folder path
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    # folder name was filled in, make a list of files in the folder
    
    # this time, check the event against the "-FOLDER-" key, which refers to the In() element you created earlier
    # if the event exists, you know the user has chosen a folder, and you use os.listdir() to get a file listing
    # then, you filter through that list to get only the files that are PNGs or GIFs
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # get a list of the files in the folder
            file_list = os.listdir(folder)
        except:
            file_list = []
            
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
        
    # if the event = "-FILE LIST-", then you know the user has chosen a file in the listbox()
    # thus, you will want to update the Image() and Text() elements to show the selected filename on the right    
    
    elif event == "-FILE LIST-": # if a file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
    
# when the user clicks exit, close the window
window.close()