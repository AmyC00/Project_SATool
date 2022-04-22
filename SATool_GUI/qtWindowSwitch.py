from PyQt5 import QtWidgets


class Window1(QtWidgets.QMainWindow):
	def __init__(self, window2=None):
		super(Window1, self).__init__()
		self.setGeometry(500, 100, 500, 500)
		self.setWindowTitle("Window 1")
		self.button = QtWidgets.QPushButton('Go to Window 2', self)
		self.button.clicked.connect(self.handleButton)
		self.setCentralWidget(self.button)
		self._window2 = window2

	def handleButton(self):
		self.hide()
		if self._window2 is None:
			self._window2 = Window2(self)
		self._window2.show()

class Window2(QtWidgets.QMainWindow):
	def __init__(self, window1=None):
		super(Window2, self).__init__()
		self.setGeometry(500, 100, 500, 500)
		self.setWindowTitle("Window 2")
		self.button = QtWidgets.QPushButton('Go to Window 1', self)
		self.button.clicked.connect(self.handleButton)
		self.setCentralWidget(self.button)
		self._window1 = window1

	def handleButton(self):
		self.hide()
		if self._window1 is None:
			self._window1 = Window1(self)
		self._window1.show()

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = Window1()
	window.show()
	sys.exit(app.exec_())	