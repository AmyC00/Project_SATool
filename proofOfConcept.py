# ----------------------------------------------------------------IMPORT LIBRARIES---------------------------------------------------------------------------------#

# import the required libraries
import pandas as pd
import string
import random
import os
os.system('color')
import logging
from sty import bg, ef, fg, rs

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('wordnet')
nltk.download('omw-1.4')

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

# -------------------------------------------------------------------------IMPORTING DATA---------------------------------------------------------------------------#

# load the files containing various positive & negative words
poss = pd.read_csv('datasets/pos_sentiment.csv')
negs = pd.read_csv('datasets/neg_sentiment.csv')
poss.columns = ["text"] # positive sentiment data
negs.columns = ["text"] # negative sentiment data

# combine them all into one dataset
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
tokens = set(word.lower() for words in data for word in word_tokenize(words[0]))
no_stopwords = [word for word in tokens if not word in stopwords.words()]


# NOTE: lemmatization is causing the analysis results to come back wrong, indicating that all values are positive (shown in screenshots within dissertation)
# commented out for now to prevent this from happening

# # create a blank array that will be used to store the lemmatized data
# final_data=[]

# # lemmatize the data to reduce each word to its stem
# for words in no_stopwords:
# 	final_data.append(lemmatizer.lemmatize(words[0]))	

# finally, create the necessary datasets using the prepared data
train = [({word: (word in word_tokenize(x[0])) \
			for word in no_stopwords}, x[1]) for x in data]
			

# test that it works by printing it
# print(train[0])

# ------------------------------------------------------TRAINING/TESTING/EVALUATING THE ALGORITHM-----------------------------------------------------------------#

# shuffle the data and split it into a new testing dataset
random.shuffle(train)
# len(train)
# 55
train_x=train[0:50]
test_x=train[51:55] 

# define an NLTK Naive Bayes model and train it with the train_x data
model = nltk.NaiveBayesClassifier.train(train_x)

# now, check the model's prediction accuracy with test_x data
acc=nltk.classify.accuracy(model, test_x)
saLogger.info("Accuracy: %s" % (acc))

# -------------------------------------------------------------------------OUTPUT-------------------------------------------------------------------------------#

# create an intensity analyser so that polarity scores can be calculated
sid = SentimentIntensityAnalyzer()

# analyse text input by the user
sentimentData=['great', 'terrible', 'excellent', 'awesome', 'bad']

polarityScores = [] # full vader polarity data
polarity = [] # individual compound polarity scores

for s in sentimentData:
  polarityScores.append(str(sid.polarity_scores(s)))

for s in polarityScores:
  polarity.append((s.partition("compound': ")[2]).strip("}"))

finalData = [] # array of the text being analysed (sentimentData), and - for each item in the list - its compound vader polarity score (polarity)

index = 0

for p in polarity:
	for s in sentimentData:
		finalData.append(sentimentData[index])
		break
	finalData.append(float(p))
	index = index + 1

# print("original output: ")
# for test in sentimentData:
# 	t_features = {word: (word in word_tokenize(test.lower())) for word in tokens}
# 	print("%s : %s" % (test, model.classify(t_features)))

def polarityColour(f):
  if(f >= -1 and f <= -0.7):
    print(fg(211, 0, 0) +"very negative" + fg.rs)
  elif(f >= -0.7 and f <= -0.3):
    print(fg(255, 71, 71) +"negative" + fg.rs)
  elif(f >= -0.3 and f <= 0.3):
    print(fg(255, 214, 32) +"neutral" + fg.rs)
  elif(f >= 0.3 and f <= 0.7):
    print(fg(93, 228, 78) +"positive" + fg.rs)
  elif(f >= 0.7 and f <= 1.0):
    print(fg(33, 142, 21) +"very positive" + fg.rs)

for f in finalData:
	if(isinstance(f, str)):
		print(f)
	elif(isinstance(f, float)):
		polarityColour(f)
		print()





# print()
# print("polarity output: ")
# for p in polarity:
#   if(float(p) >= -1 and float(p) <= -0.7):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(211, 0, 0) +model.classify(t_features) + fg.rs +": very positive")
#   elif(float(p) >= -0.7 and float(p) <= -0.3):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(255, 71, 71) +model.classify(t_features) + fg.rs +": positive")
#   elif(float(p) >= -0.3 and float(p) <= 0.3):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(255, 214, 32) +model.classify(t_features) + fg.rs +": neutral")
#   elif(float(p) >= 0.3 and float(p) <= 0.7):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(93, 228, 78) +model.classify(t_features) + fg.rs +": negative")
#   elif(float(p) >= 0.7 and float(p) <= 1.0):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(33, 142, 21) +model.classify(t_features) + fg.rs +": very negative")

# ORIGINAL POLARITY COLOUR CODING CODE

# create an intensity analyser so that polarity scores can be calculated
# sid = SentimentIntensityAnalyzer()

# polarityScores = []

# for t in userInput:
#   polarityScores.append(str(sid.polarity_scores(t)))

# sentiment = []

# for s in polarityScores:
#   sentiment.append((s.partition("compound': ")[2]).strip("}"))

# # data = []

# for s in sentiment:
#   if(float(s) >= -1 and float(s) <= -0.7):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(211, 0, 0) +model.classify(t_features) + fg.rs +": very positive")
#   elif(float(s) >= -0.7 and float(s) <= -0.3):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(255, 71, 71) +model.classify(t_features) + fg.rs +": positive")
#   elif(float(s) >= -0.3 and float(s) <= 0.3):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(255, 214, 32) +model.classify(t_features) + fg.rs +": neutral")
#   elif(float(s) >= 0.3 and float(s) <= 0.7):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(93, 228, 78) +model.classify(t_features) + fg.rs +": negative")
#   elif(float(s) >= 0.7 and float(s) <= 1.0):
#   	t_features = {word: (word in word_tokenize(s.lower())) for word in tokens}
#   	print(fg(33, 142, 21) +model.classify(t_features) + fg.rs +": very negative")