# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:26:26 2022

@author: Amy

"""

# load the required libraries
import pandas as pd
import nltk
import random
from nltk.tokenize import word_tokenize
import termcolor
import os
import PySimpleGUI as sg


# load the files containing various positive & negative words
poss = pd.read_csv('datasets/pos_sentiment.csv')
negs = pd.read_csv('datasets/neg_sentiment.csv')
poss.columns = ["text"]
negs.columns = ["text"]

# set a 'positive' or 'negative' label into each line of text data
data=([(pos['text'], "positive") for index, pos in poss.iterrows()]+
    [(neg['text'], "negative") for index, neg in negs.iterrows()])

# test that it works by printing it
# print(data[0:3])

# tokenize the words in text data & create the training data
tokens=set(word.lower() for words in data for word in word_tokenize(words[0]))
train = [({word: (word in word_tokenize(x[0])) \
            for word in tokens}, x[1]) for x in data]

# test that it works by printing it
# print(train[0])

# shuffle the data and split it into a new testing dataset
random.shuffle(train)
# len(train)
# 55
train_x=train[0:50]
test_x=train[51:55]

# define an NLTK Naive Bayes model and train it with the train_x data
model = nltk.NaiveBayesClassifier.train(train_x)

# show the most informative features
# model.show_most_informative_features()

# now, check the model's prediction accuracy with test_x data
acc=nltk.classify.accuracy(model, test_x)
# print("Accuracy:", acc)

# predict the new test data with the trained model
tests=['poor', 'good', 'great', 'waste of time']

for test in tests:
	t_features = {word: (word in word_tokenize(test.lower())) for word in tokens}

layout =  [[sg.Text(test)] +[sg.Text(model.classify(t_features))] for test in tests]
layout += [[sg.Text("Estimated accuracy: "), sg.Text(acc)]]
layout += [[sg.Button('OK')]]


# then, create the window and pass in your custom layout

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
    