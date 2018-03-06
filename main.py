#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from rename import Widget, MainWindow

'''Render and Execute'''
def main():
	app = QApplication(['Name'])
	ex = Widget()
	mw = MainWindow()
	mw.show()
	app.setWindowIcon(QIcon('static/rename.png'))
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()