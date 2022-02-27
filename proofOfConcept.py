# ----------------------------------------------------------------IMPORT LIBRARIES---------------------------------------------------------------------------------#

# import the required libraries
import pandas as pd
import string
import random
# import termcolor
import os
import logging

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# --------------------------------------------------------------------LOGGING SETUP--------------------------------------------------------------------------------#

# create a unique logger
# ensures that the root logger isn't being used by multiple libraries & logs aren't getting combined/mixed up
# if the proofOfConcept file is imported to another file as a module, it will use the saLogger instead of __main__
saLogger = logging.getLogger(__name__)
saLogger.setLevel(logging.INFO)

# add the log formatting to the HANDLER, not the logger itself (much tidier!)
formatter = logging.Formatter('%(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('sa.log')
file_handler.setFormatter(formatter)

saLogger.addHandler(file_handler)

# --------------------------------------------------------------SETTING EMOTION VALUES-----------------------------------------------------------------------------#

# MUST be kept in so the colours display correctly in the console
# os.system('color')

# load the files containing various positive & negative words
poss = pd.read_csv('datasets/pos_sentiment.csv')
negs = pd.read_csv('datasets/neg_sentiment.csv')
poss.columns = ["text"]
negs.columns = ["text"]

# set a 'positive' or 'negative' label into each line of text data

# ORIGINAL COLOURED CONSOLE OUTPUT USING TERMCOLOR - this will instead be handled in the GUI, so termcolor.colored is removed to keep the logging output tidy
# ^^^
#data=([(pos['text'], termcolor.colored("positive", "green")) for index, pos in poss.iterrows()]+
#    [(neg['text'], termcolor.colored("negative", "red")) for index, neg in negs.iterrows()])

data=([(pos['text'], "positive") for index, pos in poss.iterrows()]+
    [(neg['text'], "negative") for index, neg in negs.iterrows()])


# test that it works by printing it
# print(data[0:3])

# ----------------------------------------------------------TOKENIZING/STEMMING/LEMMATIZATION----------------------------------------------------------------------#

# set up the translator to remove punctuation
translator = str.maketrans('', '', string.punctuation)

# set up the lemmatizer for lemmatization
lemmatizer = WordNetLemmatizer()

# create a blank array that will be used to store the data without its punctuation
no_punctuation=[]

# first, remove punctuation from the data & store it in the blank array
for words in data:
	no_punctuation.append(words[0].translate(translator)) 

# next, tokenize the punctuation-less data & remove any stop words within it
tokens=set(word.lower() for words in no_punctuation for word in word_tokenize(words[0]))
no_stopwords = [word for word in tokens if not word in stopwords.words()]

# create a blank array that will be used to store the lemmatized data
final_data=[]

# lemmatize the data to reduce each word to its stem
for words in no_stopwords:
	final_data.append(lemmatizer.lemmatize(words[0]))	

# finally, create the necessary datasets using the prepared data
train = [({word: (word in word_tokenize(x[0])) 
            for word in final_data}, x[1]) for x in data]

# test that it works by printing it
# print(train[0])


# ------------------------------------------------------TRAINING/TESTING/EVALUATING THE ALGORITHM-----------------------------------------------------------------#

# shuffle the data and split it into a new testing dataset
random.shuffle(train)
# len(train)
# 55
train_x=train[0:50]
test_x=train[51:55] 

# need to create 3 datasets (test_x, train_x & evaluate_x; with the final data, each dataset will have 30 items)

# define an NLTK Naive Bayes model and train it with the train_x data
model = nltk.NaiveBayesClassifier.train(train_x)

# show the most informative features
# model.show_most_informative_features()

# now, check the model's prediction accuracy with test_x data
acc=nltk.classify.accuracy(model, test_x)
saLogger.info("Accuracy: %s" % (acc))

# predict the new test data with the trained model
tests=['poor', 'good', 'great', 'waste of time']

# -------------------------------------------------------------------------OUTPUT-------------------------------------------------------------------------------#

for test in tests:
	t_features = {word: (word in word_tokenize(test.lower())) for word in tokens}
	saLogger.info("%s : %s" % (test, model.classify(t_features)))

# the saLogger can now be used to print any errors that may occur in the code (double check logic & add try/except statements where necessary!)