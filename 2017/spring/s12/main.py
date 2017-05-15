#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QLabel
# from PyQt5.QtCore import QCoreApplication
x = input('write your height :')
y = input('write your weight :')

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        for i in range(1, int(x)+1):
            for j in range(1, int(y)+1):
                newlabel = QPushButton()
                newlabel.setStyleSheet('background-color: green')
                newlabel.clicked.connect(self.im_clicked)
                layout.addWidget(newlabel, i, j)

        self.layout = layout
        self.setLayout(layout)
        self.setGeometry(30, 40, 400, 400)
        self.setWindowTitle('Quit button')
        self.show()

    def im_clicked(self):
        sender = self.sender()
        sender.setStyleSheet('background-color: yellow')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
    time.sleep(2)
