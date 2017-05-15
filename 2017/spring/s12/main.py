#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout
# from PyQt5.QtCore import QCoreApplication
x = input('Enter the height of table: ')
y = input('Enter the width of table: ')


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create a grid layout
        layout = QGridLayout()

        # Add all of the buttons to the grid layout
        for i in range(1, int(x) + 1):
            for j in range(1, int(y) + 1):
                newlabel = QPushButton()
                # Change the color to green
                newlabel.setStyleSheet('background-color: green')
                # Set the action when the button was clicked to im_clicked
                newlabel.clicked.connect(self.im_clicked)
                layout.addWidget(newlabel, i, j)

        self.layout = layout
        self.setLayout(layout)
        # Initial Size of the screen
        self.setGeometry(30, 40, 400, 400)
        self.setWindowTitle('Quit button')
        self.show()

    def im_clicked(self):
        sender = self.sender()
        # Change the color to yellow
        sender.setStyleSheet('background-color: yellow')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
