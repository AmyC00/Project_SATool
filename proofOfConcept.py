# load the required libraries
import pandas as pd
import nltk
nltk.download('punkt')
import random
from nltk.tokenize import word_tokenize
# import termcolor
import os
import logging

logging.basicConfig(filename='sa.log', level=logging.INFO, format='%(levelname)s:%(message)s')

# MUST be kept in so the colours display correctly in the console
os.system('color')

# load the files containing various positive & negative words
poss = pd.read_csv('datasets/pos_sentiment.csv')
negs = pd.read_csv('datasets/neg_sentiment.csv')
poss.columns = ["text"]
negs.columns = ["text"]

# set a 'positive' or 'negative' label into each line of text data

# ORIGINAL COLOURED CONSOLE OUTPUT USING TERMCOLOR - will instead be handled in GUI, so termcolor.colored is removed to keep the logging file tidy
# ^^^
#data=([(pos['text'], termcolor.colored("positive", "green")) for index, pos in poss.iterrows()]+
#    [(neg['text'], termcolor.colored("negative", "red")) for index, neg in negs.iterrows()])

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
logging.info("Accuracy: %s" % (acc))

# predict the new test data with the trained model
tests=['poor', 'good', 'great', 'waste of time']

for test in tests:
	t_features = {word: (word in word_tokenize(test.lower())) for word in tokens}
	logging.info("%s : %s" % (test, model.classify(t_features)))