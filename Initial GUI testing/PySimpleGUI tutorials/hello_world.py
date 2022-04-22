# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:13:00 2022

@author: Amy

PySimpleGUI Introductory Tutorial
"PySimpleGUI: The Simple Way to Create a GUI With Python"
https://realpython.com/pysimplegui-python/

"""

# hello_world.py

import PySimpleGUI as sg

# title = gives the window a title
# layout = sets the window's layout (nothing here yet)
# margins = sets the window's margins
# read = returns any events that are triggered in the Window() as a string, as well as a values dictionary

sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()