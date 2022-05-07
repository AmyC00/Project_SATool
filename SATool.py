# import the required libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from resultsWindow import Ui_resultsWindow
import pandas as pd
import string
import random
import os
os.system('color')
import logging
from sty import bg, ef, fg, rs
import sys

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

# -----------------------------------------------------------------LOADING SCREEN---------------------------------------------------------------------------#

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Analysing...")

        self.label_animation = QLabel(self)

        self.movie = QMovie('loading.gif')
        self.label_animation.setAlignment(Qt.AlignCenter)
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)

        self.startAnimation()
        timer.singleShot(300, self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

# ----------------------------------------------------------------------HOME WINDOW--------------------------------------------------------------------------------#

class Ui_homeWindow(object):
    
    def setupUi(self, homeWindow):
        homeWindow.setObjectName("homeWindow")
        homeWindow.resize(800, 618)
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home_InfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.home_InfoLabel.setGeometry(QtCore.QRect(120, 20, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.home_InfoLabel.setFont(font)
        self.home_InfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.home_InfoLabel.setObjectName("home_InfoLabel")
        self.home_TextToAnalyse = QtWidgets.QTextEdit(self.centralwidget)
        self.home_TextToAnalyse.setGeometry(QtCore.QRect(60, 90, 681, 371))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.home_TextToAnalyse.setFont(font)
        self.home_TextToAnalyse.setObjectName("home_TextToAnalyse")
        self.home_AnalyseTextBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.analyseData())
        self.home_AnalyseTextBtn.setGeometry(QtCore.QRect(320, 480, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home_AnalyseTextBtn.setFont(font)
        self.home_AnalyseTextBtn.setObjectName("home_AnalyseTextBtn")
        self.home_OpenFileBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openFile())
        self.home_OpenFileBtn.setGeometry(QtCore.QRect(320, 530, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home_OpenFileBtn.setFont(font)
        self.home_OpenFileBtn.setObjectName("home_OpenFileBtn")
        self.home_InfoLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.home_InfoLabel_2.setGeometry(QtCore.QRect(120, 50, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_InfoLabel_2.setFont(font)
        self.home_InfoLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.home_InfoLabel_2.setObjectName("home_InfoLabel_2")
        homeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        homeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homeWindow)
        self.statusbar.setObjectName("statusbar")
        homeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(homeWindow)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

    def retranslateUi(self, homeWindow):
        _translate = QtCore.QCoreApplication.translate
        homeWindow.setWindowTitle(_translate("homeWindow", "Home"))
        self.home_InfoLabel.setText(_translate("homeWindow", "Enter the text you want to analyse below:"))
        self.home_AnalyseTextBtn.setToolTip(_translate("homeWindow", "Analyse the text entered into the text box."))
        self.home_AnalyseTextBtn.setText(_translate("homeWindow", "Analyse text"))
        self.home_OpenFileBtn.setToolTip(_translate("homeWindow", "Open a text file to analyse its contents."))
        self.home_OpenFileBtn.setText(_translate("homeWindow", "Open a file"))
        self.home_InfoLabel_2.setText(_translate("homeWindow", "NOTE: each sentence must be on its own line."))

    def showEmptyTextFieldWarning(self):
        msg = QMessageBox()
        msg.setWindowTitle("No text entered for analysis")
        msg.setText("Please enter some text into the text box and try again.")
        msg.setIcon(QMessageBox.Warning)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()

    def openFile(self):
        fileName = QFileDialog.getOpenFileName(None, "Open a file", "", "Text files (*.txt);;All files (*)" )

        # output filename to screen
        if fileName[0]:
            f = open(fileName[0], 'r')

            with f:
                data = f.read()
                self.home_TextToAnalyse.setText(data)

            # self.home_TextToAnalyse.setText(fileName[0])
            # saLogger.info("Chosen file: " +fileName[0])


    # analyse the text the user has entered
    def analyseData(self):
        
        textToAnalyse = self.home_TextToAnalyse.toPlainText();
        # saLogger.info("Text being analysed: " +textToAnalyse);
        # saLogger.info(type(textToAnalyse))

        if(textToAnalyse == ""):
            # if there is no text in the text box, tell this to the user
            # there MUST be text present for the analysis to be carried out
            self.showEmptyTextFieldWarning()
            saLogger.warning("WARNING - no text has been entered for analysis.")
        else:
            # continue as normal
            self.loading_screen = LoadingScreen()

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
            #   final_data.append(lemmatizer.lemmatize(words[0]))   

            # finally, create the necessary datasets using the prepared data
            train = [({word: (word in word_tokenize(x[0])) \
                        for word in no_stopwords}, x[1]) for x in data]
                        

            # test that it works by printing it
            # print(train[0])

            # ------------------------------------------------------TRAINING/TESTING/EVALUATING THE ALGORITHM----------------------------------------------------------------#

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
            # saLogger.info("Accuracy: %s" % (acc))

            # -------------------------------------------------------------------------OUTPUT-------------------------------------------------------------------------------#

            # create an intensity analyser so that polarity scores can be calculated
            sid = SentimentIntensityAnalyzer()

            # analyse text input by the user
            # here, split each sentence entered by the user and put it into an array (split at each new line)

            sentimentData = textToAnalyse.split('\n')
            # saLogger.info(sentimentData)

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

            # declare an instance of the results window
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_resultsWindow()
            self.ui.setupUi(self.window)

            # re-initialize index to zero so it can be used to display colours for the items in the list box
            index = 0

            # pass data to the results window
            for f in finalData:
                if(isinstance(f, str)):
                    self.ui.results_AnalysisResults.addItem(f)
                    index = index + 1
                elif(isinstance(f, float)):
                    item = self.ui.results_AnalysisResults.item(index-1)
                    if(f >= -1 and f <= -0.7):
                        item.setBackground(QtGui.QColor(211, 0, 0))
                        item.setForeground(QtGui.QColor("white"))
                    elif(f >= -0.7 and f <= -0.3):
                        item.setBackground(QtGui.QColor(255, 71, 71))
                        item.setForeground(QtGui.QColor("white"))
                    elif(f >= -0.3 and f <= 0.3):
                        item.setBackground(QtGui.QColor(255, 214, 32))
                    elif(f >= 0.3 and f <= 0.7):
                        item.setBackground(QtGui.QColor(93, 228, 78))
                    elif(f >= 0.7 and f <= 1.0):
                        item.setBackground(QtGui.QColor(33, 142, 21))
                        item.setForeground(QtGui.QColor("white"))
            # show the results window
            self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())