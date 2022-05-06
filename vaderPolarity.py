import pandas
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sty import bg, ef, fg, rs
import os
os.system('color')

sid = SentimentIntensityAnalyzer()

# a = "This was the best movie I've ever seen, amazing!"
# b = "This was awful, I never want to see it again."
# c = "This was fine, a bit boring."

# extract JUST the compound polarity value from a list of strings (overall level of positive/negative sentiment)
sentimentData = ["This was the best movie I've ever seen, amazing!", "This was awful, I never want to see it again.", "This was fine, a bit boring."]

# aPolarityScores = str(sid.polarity_scores(a))
# bPolarityScores = str(sid.polarity_scores(b))
# cPolarityScores = str(sid.polarity_scores(c))

polarityScores = []
polarity = []

for s in sentimentData:
  polarityScores.append(str(sid.polarity_scores(s)))

# extract the compound score
# aSentiment = (aPolarityScores.partition("compound': ")[2]).strip("}")
# bSentiment = (bPolarityScores.partition("compound': ")[2]).strip("}")
# cSentiment = (cPolarityScores.partition("compound': ")[2]).strip("}")

for s in polarityScores:
  polarity.append((s.partition("compound': ")[2]).strip("}"))

# PSEUDOCODE
# for each item in the sentimentList
# 	if the polarity value is between -1 and -0.7
# 		very negative [red]
# 	else if the polarity value is between -0.7 and -0.3
#		negative [lighter red]
# 	else if the polarity value is between -0.3 and 0.3
#		neutral [yellow/gold]
# 	else if the polarity value is between 0.3 and 0.7
#		positive [lighter green]
#	else if the polarity value is between 0.7 and 1
# 		very positive [darker green]

# for s in sentiment:
#   if(float(s) >= -1 and float(s) <= -0.7):
#   	print(fg(211, 0, 0) +s +": very negative" + fg.rs)
#   elif(float(s) >= -0.7 and float(s) <= -0.3):
#   	print(fg(255, 71, 71) +s +": negative" + fg.rs)
#   elif(float(s) >= -0.3 and float(s) <= 0.3):
#   	print(fg(255, 214, 32) +s +": neutral" + fg.rs)
#   elif(float(s) >= 0.3 and float(s) <= 0.7):
#   	print(fg(93, 228, 78) +s +": positive" + fg.rs)
#   elif(float(s) >= 0.7 and float(s) <= 1.0):
#   	print(fg(33, 142, 21) +s +": very positive" + fg.rs)

# data = []

for s in polarity:
  if(float(s) >= -1 and float(s) <= -0.7):
    print(fg(211, 0, 0) +s +": very negative" + fg.rs)
  elif(float(s) >= -0.7 and float(s) <= -0.3):
    print(fg(255, 71, 71) +s +": negative" + fg.rs)
  elif(float(s) >= -0.3 and float(s) <= 0.3):
    print(fg(255, 214, 32) +s +": neutral" + fg.rs)
  elif(float(s) >= 0.3 and float(s) <= 0.7):
    print(fg(93, 228, 78) +s +": positive" + fg.rs)
  elif(float(s) >= 0.7 and float(s) <= 1.0):
    print(fg(33, 142, 21) +s +": very positive" + fg.rs)

# print("polarity of statement a: " +aSentiment)
# print("polarity of statement b: " +bSentiment)
# print("polarity of statement c: " +cSentiment)

# for d in data:
#   print(d)