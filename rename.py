#!/usr/bin/env python3

'''Imports'''
import sys
import os
from PyQt5.QtWidgets import (
	QMainWindow,
	QWidget,
	QPushButton,
	QApplication,
	QFileDialog,
	QLineEdit,
	QGridLayout,
	QLabel)
from PyQt5.QtGui import QIcon

'''Widget'''
class Widget(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'Rename'
		self.initUI()

	def initUI(self):
		self.filePath = ''

		'''Find Label'''
		findLabel = QLabel('Find', self)
		findLabel.move(20,20)

		'''Find Input'''
		self.textboxFind = QLineEdit(self)
		self.textboxFind.setFixedWidth(280)
		self.textboxFind.move(100,18)

		'''Replace Label'''
		replaceLabel = QLabel('Replace', self)
		replaceLabel.move(20,60)

		'''Replace Input'''
		self.textboxReplace = QLineEdit(self)
		self.textboxReplace.setFixedWidth(280)
		self.textboxReplace.move(100,58)

		'''Readonly Directory Output'''
		self.textboxSelectedDirectory = QLineEdit('No Directory Selected', self)
		self.textboxSelectedDirectory.setReadOnly(True)
		self.textboxSelectedDirectory.move(20,92)
		self.textboxSelectedDirectory.setFixedWidth(360)

		'''Readonly Status'''
		self.textboxStatus = QLineEdit('', self)
		self.textboxStatus.setReadOnly(True)
		self.textboxStatus.move(20,114)
		self.textboxStatus.setFixedWidth(360)
		
		'''
		Buttons
		'''
		self.getDirectoryButton = QPushButton('&Select directory', self)
		self.getDirectoryButton.move(20,140)
		self.getDirectoryButton.setToolTip('Select the directory you want rrrename to crawl though. This action is <strong>not</strong> recursive.')
		self.getDirectoryButton.clicked.connect(self.openFile)

		renameFileButton = QPushButton('&rrrename', self)
		renameFileButton.setProperty('mandatoryField', True);
		renameFileButton.move(250,140)
		renameFileButton.setToolTip('This will find and replace the files inside the directory')
		renameFileButton.clicked.connect(self.renameFile)

		'''
		Show
		'''
		# self.setLayout(grid)

	'''
	Open File and Select
	'''
	def openFile(self):
		options = QFileDialog.Options()
		self.filePath = QFileDialog.getExistingDirectory(self, 'Select directory')
		if self.filePath:
			self.textboxSelectedDirectory.setText('...' + self.filePath[-36:])
			self.getDirectoryButton.setText('Change Directory')

	'''
	Rename File
	'''
	def renameFile(self):
		findString = self.textboxFind.text()
		replaceString = self.textboxReplace.text()
		for file in os.listdir(self.filePath):
			fullPath = (os.path.join(self.filePath, file))
			print(fullPath,findString, replaceString)
			os.rename(fullPath, fullPath.replace(findString, replaceString))

		statusText = 'Reanmed ' + str(len(os.listdir(self.filePath)) + ' items')
		self.textboxStatus.setText(statusText)

'''Main Window'''
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		centralWidget = Widget()          
		self.setCentralWidget(centralWidget)
		self.setGeometry(100, 100, 400, 180)
		self.setStyleSheet(open('static/style.qss', 'r').read())
		self.setWindowIcon(QIcon('static/rename.png'))
		self.setWindowTitle('rrrename | Batch Renaming Tool')
		self.filePath = ''

'''Render and Execute'''
def main():
	app = QApplication(sys.argv)
	ex = Widget()
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()