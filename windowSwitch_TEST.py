from PyQt5 import QtCore, QtGui, QtWidgets

# window1 = HomeWindow = Ui_homeWindow
# window2 = ResultsWindow = Ui_resultsWindow

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_homeWindow(object):
    def setupUi(self, resultsWindow=None):
        homeWindow.setObjectName("homeWindow")
        homeWindow.resize(800, 618)
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home_InfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.home_InfoLabel.setGeometry(QtCore.QRect(120, 30, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.home_InfoLabel.setFont(font)
        self.home_InfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.home_InfoLabel.setObjectName("home_InfoLabel")
        self.home_TextToAnalyse = QtWidgets.QTextEdit(self.centralwidget)
        self.home_TextToAnalyse.setGeometry(QtCore.QRect(60, 80, 681, 371))
        self.home_TextToAnalyse.setObjectName("home_TextToAnalyse")
        self.home_AnalyseTextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.home_AnalyseTextBtn.setGeometry(QtCore.QRect(320, 480, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home_AnalyseTextBtn.setFont(font)
        self.home_AnalyseTextBtn.setObjectName("home_AnalyseTextBtn")
        self.home_AnalyseTextBtn.clicked.connect(self.handleButton)
        self.home_OpenFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.home_AnalyseTextBtn.clicked.connect(self.handleButton)
        self.home_OpenFileBtn.setGeometry(QtCore.QRect(320, 530, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home_OpenFileBtn.setFont(font)
        self.home_OpenFileBtn.setObjectName("home_OpenFileBtn")
        homeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        homeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homeWindow)
        self.statusbar.setObjectName("statusbar")
        homeWindow.setStatusBar(self.statusbar)
        self._resultsWindow = resultsWindow

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

    def handleButton(self):
    	# self.hide()
    	if self._resultsWindow is None:
    		self._resultsWindow = Ui_resultsWindow(self)
    	self._resultsWindow.show()




# END OF HOME WINDOW 



class Ui_resultsWindow(object):
    def setupUi(self, homeWindow=None):
    	super(Ui_resultsWindow, self).__init__()
    	resultsWindow.setObjectName("resultsWindow")
    	resultsWindow.resize(800, 618)
    	self.centralwidget = QtWidgets.QWidget(resultsWindow)
    	self.centralwidget.setObjectName("centralwidget")
    	self.results_AnalysisResults = QtWidgets.QListView(self.centralwidget)
    	self.results_AnalysisResults.setGeometry(QtCore.QRect(330, 20, 451, 561))
    	self.results_AnalysisResults.setObjectName("results_AnalysisResults")
    	self.results_ResultsBreakdown = QtWidgets.QLabel(self.centralwidget)
    	self.results_ResultsBreakdown.setGeometry(QtCore.QRect(10, 25, 311, 451))
    	font = QtGui.QFont()
    	font.setPointSize(12)
    	self.results_ResultsBreakdown.setFont(font)
    	self.results_ResultsBreakdown.setAlignment(QtCore.Qt.AlignCenter)
    	self.results_ResultsBreakdown.setWordWrap(True)
    	self.results_ResultsBreakdown.setObjectName("results_ResultsBreakdown")
    	self.results_SaveBtn = QtWidgets.QPushButton(self.centralwidget)
    	self.results_SaveBtn.setGeometry(QtCore.QRect(100, 490, 141, 41))
    	font = QtGui.QFont()
    	font.setPointSize(12)
    	self.results_SaveBtn.setFont(font)
    	self.results_SaveBtn.setObjectName("results_SaveBtn")
    	self.results_StartOverBtn = QtWidgets.QPushButton(self.centralwidget)
    	self.results_StartOverBtn.setGeometry(QtCore.QRect(100, 540, 141, 41))
    	font = QtGui.QFont()
    	font.setPointSize(12)
    	self.results_StartOverBtn.setFont(font)
    	self.results_StartOverBtn.setObjectName("results_StartOverBtn")
    	self.results_StartOverBtn.clicked.connect(self.handleResultsButton)
    	self.results_StartOverBtn.clicked.connect(self.handleButton)
    	resultsWindow.setCentralWidget(self.centralwidget)
    	self.menubar = QtWidgets.QMenuBar(resultsWindow)
    	self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
    	self.menubar.setObjectName("menubar")
    	resultsWindow.setMenuBar(self.menubar)
    	self.statusbar = QtWidgets.QStatusBar(resultsWindow)
    	self.statusbar.setObjectName("statusbar")
    	resultsWindow.setStatusBar(self.statusbar)
    	self._homeWindow = Ui_homeWindow

    	self.retranslateUi(resultsWindow)
    	QtCore.QMetaObject.connectSlotsByName(resultsWindow)

    def retranslateUi(self, resultsWindow):
        _translate = QtCore.QCoreApplication.translate
        resultsWindow.setWindowTitle(_translate("resultsWindow", "Analysis results"))
        self.results_ResultsBreakdown.setText(_translate("resultsWindow", "Click on a sentence in the list to show a breakdown of its emotion here."))
        self.results_SaveBtn.setToolTip(_translate("resultsWindow", "Save the results of the sentiment analysis as a text file."))
        self.results_SaveBtn.setText(_translate("resultsWindow", "Save results"))
        self.results_SaveBtn.setShortcut(_translate("resultsWindow", "Ctrl+C"))
        self.results_StartOverBtn.setToolTip(_translate("resultsWindow", "Delete the results of the analysis & start over with a new piece of text."))
        self.results_StartOverBtn.setText(_translate("resultsWindow", "Start over"))

    def handleButton(self):
    	self.hide()
    	if self._homeWindow is None:
    		self._homeWindow = Ui_homeWindow(self)
    	self._homeWindow.show()


#	def handleButton(self):


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())