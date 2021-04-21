from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import numpy as np


def create_buttons(self):
    self.n0 = QPushButton('0')
    self.n0.setFont(QFont('Times', 15))
    self.n0.clicked.connect(self.push_0)
    self.n0.setStyleSheet('background-color: black;''color: white')

    self.n1 = QPushButton('1')
    self.n1.setFont(QFont('Times', 15))
    self.n1.clicked.connect(self.push_1)
    self.n1.setStyleSheet('background-color: black;''color: white')

    self.n2 = QPushButton('2')
    self.n2.setFont(QFont('Times', 15))
    self.n2.clicked.connect(self.push_2)
    self.n2.setStyleSheet('background-color: black;''color: white')

    self.n3 = QPushButton('3')
    self.n3.setFont(QFont('Times', 15))
    self.n3.clicked.connect(self.push_3)
    self.n3.setStyleSheet('background-color: black;''color: white')

    self.n4 = QPushButton('4')
    self.n4.setFont(QFont('Times', 15))
    self.n4.clicked.connect(self.push_4)
    self.n4.setStyleSheet('background-color: black;''color: white')

    self.n5 = QPushButton('5')
    self.n5.setFont(QFont('Times', 15))
    self.n5.clicked.connect(self.push_5)
    self.n5.setStyleSheet('background-color: black;''color: white')

    self.n6 = QPushButton('6')
    self.n6.setFont(QFont('Times', 15))
    self.n6.clicked.connect(self.push_6)
    self.n6.setStyleSheet('background-color: black;''color: white')

    self.n7 = QPushButton('7')
    self.n7.setFont(QFont('Times', 15))
    self.n7.clicked.connect(self.push_7)
    self.n7.setStyleSheet('background-color: black;''color: white')

    self.n8 = QPushButton('8')
    self.n8.setFont(QFont('Times', 15))
    self.n8.clicked.connect(self.push_8)
    self.n8.setStyleSheet('background-color: black;''color: white')

    self.n9 = QPushButton('9')
    self.n9.setFont(QFont('Times', 15))
    self.n9.clicked.connect(self.push_9)
    self.n9.setStyleSheet('background-color: black;''color: white')

    self.add = QPushButton('+')
    self.add.setFont(QFont('Times', 15))
    self.add.clicked.connect(self.push_add)
    self.add.setStyleSheet('background-color: black;''color: white')

    self.subtract = QPushButton('-')
    self.subtract.setFont(QFont('Times', 15))
    self.subtract.clicked.connect(self.push_subtract)
    self.subtract.setStyleSheet('background-color: black;''color: white')

    self.multiply = QPushButton('*')
    self.multiply.setFont(QFont('Times', 15))
    self.multiply.clicked.connect(self.push_multiply)
    self.multiply.setStyleSheet('background-color: black;''color: white')

    self.divide = QPushButton('/')
    self.divide.setFont(QFont('Times', 15))
    self.divide.clicked.connect(self.push_divide)
    self.divide.setStyleSheet('background-color: black;''color: white')

    self.power = QPushButton('^')
    self.power.setFont(QFont('Times', 15))
    self.power.clicked.connect(self.push_power)
    self.power.setStyleSheet('background-color: black;''color: white')

    self.enter = QPushButton('Enter')
    self.enter.setFont(QFont('Times', 15))
    self.enter.clicked.connect(self.push_enter)
    self.enter.setStyleSheet('background-color: black;''color: white')

    self.output_screen = QLabel()
    self.output_screen.setFont(QFont('Times', 25))
    self.output_screen.setAlignment(Qt.AlignCenter)
    self.output_screen.setStyleSheet('border: 5px solid black;''background-color: white;''color: black')

    self.clear = QPushButton('Clear')
    self.clear.setFont(QFont('Times', 15))
    self.clear.clicked.connect(self.push_clear)
    self.clear.setStyleSheet('background-color: black;''color: white')

    self.all_clear = QPushButton('All Clear')
    self.all_clear.setFont(QFont('Times', 15))
    self.all_clear.clicked.connect(self.push_all_clear)
    self.all_clear.setStyleSheet('background-color: black;''color: white')

    self.left = QPushButton('(')
    self.left.setFont(QFont('Times', 15))
    self.left.clicked.connect(self.push_left)
    self.left.setStyleSheet('background-color: black;''color: white')

    self.right = QPushButton(')')
    self.right.setFont(QFont('Times', 15))
    self.right.clicked.connect(self.push_right)
    self.right.setStyleSheet('background-color: black;''color: white')


