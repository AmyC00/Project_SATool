from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication, QWidget, QLabel
import sys
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

# -----------------------------------------------------------------LOADING SCREEN---------------------------------------------------------------------------#

class Ui_resultsWindow(QMainWindow):
    def setupUi(self, resultsWindow):
        resultsWindow.setObjectName("resultsWindow")
        resultsWindow.resize(800, 618)
        self.centralwidget = QtWidgets.QWidget(resultsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.results_ResultsBreakdown = QtWidgets.QLabel(self.centralwidget)
        self.results_ResultsBreakdown.setGeometry(QtCore.QRect(10, 25, 311, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_ResultsBreakdown.setFont(font)
        self.results_ResultsBreakdown.setAlignment(QtCore.Qt.AlignCenter)
        self.results_ResultsBreakdown.setWordWrap(True)
        self.results_ResultsBreakdown.setObjectName("results_ResultsBreakdown")

        # save the analysis data
        self.results_SaveBtn = QtWidgets.QPushButton(self.centralwidget)
        # self.results_SaveBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.saveFile())
        self.results_SaveBtn.setGeometry(QtCore.QRect(100, 490, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_SaveBtn.setFont(font)
        self.results_SaveBtn.setObjectName("results_SaveBtn")

        # exit the program without saving
        self.results_StartOverBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.quit())
        self.results_StartOverBtn.setGeometry(QtCore.QRect(100, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_StartOverBtn.setFont(font)
        self.results_StartOverBtn.setObjectName("results_StartOverBtn")

        # list widget to display the results of the sentiment analysis
        self.results_AnalysisResults = QtWidgets.QListWidget(self.centralwidget)
        self.results_AnalysisResults.setGeometry(QtCore.QRect(330, 10, 451, 551))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.results_AnalysisResults.setFont(font)
        self.results_AnalysisResults.setObjectName("results_AnalysisResults")

        resultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        resultsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resultsWindow)
        self.statusbar.setObjectName("statusbar")
        resultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(resultsWindow)
        QtCore.QMetaObject.connectSlotsByName(resultsWindow)

    def retranslateUi(self, resultsWindow):
        _translate = QtCore.QCoreApplication.translate
        resultsWindow.setWindowTitle(_translate("resultsWindow", "Analysis results"))
        self.results_ResultsBreakdown.setText(_translate("resultsWindow", "Click on a sentence to show its emotion here."))
        self.results_SaveBtn.setToolTip(_translate("resultsWindow", "Save the results of the sentiment analysis as a text file."))
        self.results_SaveBtn.setText(_translate("resultsWindow", "Save results"))
        self.results_SaveBtn.setShortcut(_translate("resultsWindow", "Ctrl+C"))
        self.results_StartOverBtn.setToolTip(_translate("resultsWindow", "Delete the results of the analysis & exit the program."))
        self.results_StartOverBtn.setText(_translate("resultsWindow", "Exit"))

    # save file code - unsure of how to pass data between windows to save it
    # def saveFile(self):
    #     size = self.results_AnalysisResults.count()
    #     analysisData = []
    #     i = 0

    #     while i <= size:
    #         self.results_AnalysisResults.setCurrentRow(i)
    #         analysisData.append(self.results_AnalysisResults.currentItem.text())

    #     file = QFileDialog.getSaveFileName(None, "Save file", "Analysis results.txt", "Text files (*.txt);;All files (*)")
                
    #     with open(file[0], 'w') as f:
    #         data = f.write(analysisData)

    # quit the program without saving analysis results
    def quit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Exit without saving")
        msg.setText("Are you sure you want to exit the program without saving analysis results?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()  # show the message box

    # outputs the value of the button to the console; good for logging!
    def popup_button(self, i):  # i = the button that was clicked
        if(i.text() == "&Yes"):
            saLogger.info("Exiting program")
            sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    resultsWindow = QtWidgets.QMainWindow()
    ui = Ui_resultsWindow()
    ui.setupUi(resultsWindow)
    resultsWindow.show()
    sys.exit(app.exec_())
