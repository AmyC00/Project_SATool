from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_homeWindow(QtWidgets.QMainWindow):
#     def __init__(self, ResultsWindow=None):
#         super(Ui_homeWindow, self).__init__()
#         self.setGeometry(500, 100, 500, 500)
#         self.setWindowTitle("Window 1")
#         self.button = QtWidgets.QPushButton('Go to Window 2', self)
#         # self.button.clicked.connect(self.handleButton)
#         self.setCentralWidget(self.button)
#         self._ResultsWindow = ResultsWindow

class Ui_homeWindow(object):
  def setupUi(self, homeWindow):
      super(Ui_homeWindow, self).__init__()
      homeWindow.setObjectName("homeWindow")
      homeWindow.resize(500, 500)
      self.centralwidget = QtWidgets.QWidget(homeWindow)
      self.centralwidget.setObjectName("centralwidget")
      homeWindow.setCentralWidget(self.centralwidget)

      self.homeButton = QtWidgets.QPushButton(self.centralwidget)
      self.homeButton.setGeometry(QtCore.QRect(0, 0, 500, 500))
      font = QtGui.QFont()
      font.setPointSize(12)
      self.homeButton.setFont(font)
      self.homeButton.setObjectName("homeButton")
      # self.homeButton.clicked.connect(self.handleButton)

      self.retranslateUi(homeWindow)
      QtCore.QMetaObject.connectSlotsByName(homeWindow)

  def retranslateUi(self, homeWindow):
      _translate = QtCore.QCoreApplication.translate
      homeWindow.setWindowTitle(_translate("homeWindow", "Home"))
      self.homeButton.setText(_translate("homeWindow", "Go to Window 2"))

  # def handleButton(self):
  #     self.hide()
  #     if self._ResultsWindow is None:
  #         self._ResultsWindow = Ui_resultsWindow(self)
  #     self._ResultsWindow.show()

# class Ui_resultsWindow(object):
#   def setupUi(self, resultsWindow):
#       super(Ui_resultsWindow, self).__init__()
#       resultsWindow.setObjectName("resultsWindow")
#       resultsWindow.resize(500, 500)
#       self.centralwidget = QtWidgets.QWidget(resultsWindow)
#       self.centralwidget.setObjectName("centralwidget")
#       resultsWindow.setCentralWidget(self.centralwidget)

#       self.resultsButton = QtWidgets.QPushButton(self.centralwidget)
#       self.resultsButton.setGeometry(QtCore.QRect(0, 0, 500, 500))
#       font = QtGui.QFont()
#       font.setPointSize(12)
#       self.resultsButton.setFont(font)
#       self.resultsButton.setObjectName("resultsButton")
#       self.resultsButton.clicked.connect(self.handleButton)

#       self.retranslateUi(resultsWindow)
#       QtCore.QMetaObject.connectSlotsByName(resultsWindow)

#   def retranslateUi(self, resultsWindow):
#       _translate = QtCore.QCoreApplication.translate
#       resultsWindow.setWindowTitle(_translate("resultsWindow", "Results"))
#       self.resultsButton.setText(_translate("resultsWindow", "Go to Window 1"))

#   def handleButton(self):
#       self.hide()
#       if self._HomeWindow is None:
#           self._HomeWindow = Ui_homeWindow(self)
#       self._HomeWindow.show()

# class Ui_resultsWindow(QtWidgets.QMainWindow):
#   def __init__(self, HomeWindow=None):
#       super(Ui_resultsWindow, self).__init__()
#       self.setGeometry(500, 100, 500, 500)
#       self.setWindowTitle("Window 2")
#       self.button = QtWidgets.QPushButton('Go to Window 1', self)
#       self.button.clicked.connect(self.handleButton)
#       self.setCentralWidget(self.button)
#       self._HomeWindow = HomeWindow

#   def handleButton(self):
#       self.hide()
#       if self._HomeWindow is None:
#           self._HomeWindow = HomeWindow(self)
#       self._HomeWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())