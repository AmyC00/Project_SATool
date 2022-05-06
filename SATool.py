from PyQt5 import QtCore, QtGui, QtWidgets
import logging

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

# ----------------------------------------------------------------------HOME WINDOW--------------------------------------------------------------------------------#

class Ui_homeWindow(object):
    def setupUi(self, homeWindow):
        super(Ui_homeWindow, self).__init__()
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
        self.home_AnalyseTextBtn.clicked.connect(self.analyseData)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home_AnalyseTextBtn.setFont(font)
        self.home_AnalyseTextBtn.setObjectName("home_AnalyseTextBtn")
        self.home_OpenFileBtn = QtWidgets.QPushButton(self.centralwidget)
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

    def analyseData(self):
        textToAnalyse = self.home_TextToAnalyse.toPlainText();
        saLogger.info("Text being analysed: " +textToAnalyse);
        saLogger.info(type(textToAnalyse))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())


# def sentimentAnalysis()