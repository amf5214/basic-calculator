from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont
import numpy as np

final = ''
output = []


def create_buttons(self):
    self.n0 = QPushButton('0')
    self.n0.setFont(QFont('Times', 15))
    self.n0.clicked.connect(push_0)

    self.n1 = QPushButton('1')
    self.n1.setFont(QFont('Times', 15))
    self.n1.clicked.connect(push_1)

    self.n2 = QPushButton('2')
    self.n2.setFont(QFont('Times', 15))
    self.n2.clicked.connect(push_2)

    self.n3 = QPushButton('3')
    self.n3.setFont(QFont('Times', 15))
    self.n3.clicked.connect(push_3)

    self.n4 = QPushButton('4')
    self.n4.setFont(QFont('Times', 15))
    self.n4.clicked.connect(push_4)

    self.n5 = QPushButton('5')
    self.n5.setFont(QFont('Times', 15))
    self.n5.clicked.connect(push_5)

    self.n6 = QPushButton('6')
    self.n6.setFont(QFont('Times', 15))
    self.n6.clicked.connect(push_6)

    self.n7 = QPushButton('7')
    self.n7.setFont(QFont('Times', 15))
    self.n7.clicked.connect(push_7)

    self.n8 = QPushButton('8')
    self.n8.setFont(QFont('Times', 15))
    self.n8.clicked.connect(push_8)

    self.n9 = QPushButton('9')
    self.n9.setFont(QFont('Times', 15))
    self.n9.clicked.connect(push_9)

    self.add = QPushButton('+')
    self.add.setFont(QFont('Times', 15))
    self.add.clicked.connect(push_add)

    self.subtract = QPushButton('-')
    self.subtract.setFont(QFont('Times', 15))
    self.subtract.clicked.connect(push_subtract)

    self.multiply = QPushButton('*')
    self.multiply.setFont(QFont('Times', 15))
    self.multiply.clicked.connect(push_multiply)

    self.divide = QPushButton('/')
    self.divide.setFont(QFont('Times', 15))
    self.divide.clicked.connect(push_divide)

    self.enter = QPushButton('Enter')
    self.enter.setFont(QFont('Times', 15))
    self.enter.clicked.connect(push_enter)

    self.output_screen = QLabel()
    self.output_screen.setFont(QFont('Times', 25))


def push_0(self):
    number = 0
    state = 'number'
    output_modify(self, number, state)


def push_1(self):
    number = 1
    state = 'number'
    output_modify(self, number, state)


def push_2(self):
    number = 2
    state = 'number'
    output_modify(self, number, state)


def push_3(self):
    number = 3
    state = 'number'
    output_modify(self, number, state)


def push_4(self):
    number = 4
    state = 'number'
    output_modify(self, number, state)


def push_5(self):
    number = 5
    state = 'number'
    output_modify(self, number, state)


def push_6(self):
    number = 6
    state = 'number'
    output_modify(self, number, state)


def push_7(self):
    number = 7
    state = 'number'
    output_modify(self, number, state)


def push_8(self):
    number = 8
    state = 'number'
    output_modify(self, number, state)


def push_9(self):
    number = 9
    state = 'number'
    output_modify(self, number, state)


def push_add(self):
    number = ' + '
    state = 'symbol'
    output_modify(self, number, state)


def push_subtract(self):
    number = ' - '
    state = 'symbol'
    output_modify(self, number, state)


def push_multiply(self):
    number = ' * '
    state = 'symbol'
    output_modify(self, number, state)


def push_divide(self):
    number = ' / '
    state = 'symbol'
    output_modify(self, number, state)


def output_modify(self, number, state):
    global final, output
    if state == 'number':
        final += str(number)
    else:
        final += number

    output = final.split(sep=' ')
    print(final)
    print(output)


def add_func(self):
    global output
    output = np.array(output)

    ind = np.where(output == '+')
    ind = ind[0]
    print(ind)

    for x in ind:
        if len(output) > x + 1:
            result_out = str(float(output[x - 1]) + float(output[x + 1]))
            output = np.delete(output, x - 1)
            output = np.delete(output, x - 1)

            output = list(output)
            output[x - 1] = result_out


def subtract_func(self):
    global output
    output = np.array(output)

    ind = np.where(output == '-')
    ind = ind[0]
    print(ind)

    for x in ind:
        if len(output) > x + 1:
            result_out = str(float(output[x - 1]) - float(output[x + 1]))
            output = np.delete(output, x - 1)
            output = np.delete(output, x - 1)

            output = list(output)
            output[x - 1] = result_out


def multiply_func(self):
    global output
    output = np.array(output)

    ind = np.where(output == '*')
    ind = ind[0]
    print(ind)

    for x in ind:
        if len(output) > x + 1:
            result_out = str(float(output[x - 1]) * float(output[x + 1]))
            output = np.delete(output, x - 1)
            output = np.delete(output, x - 1)

            output = list(output)
            output[x - 1] = result_out


def divide_func(self):
    global output
    output = np.array(output)

    ind = np.where(output == '/')
    ind = ind[0]
    print(ind)

    for x in ind:
        if len(output) > x + 1:
            result_out = str(float(output[x - 1]) / float(output[x + 1]))
            output = np.delete(output, x - 1)
            output = np.delete(output, x - 1)

            output = list(output)
            output[x - 1] = result_out


def push_enter(self):
    global output
    while '*' in output:
        multiply_func(self)

    while '/' in output:
        divide_func(self)

    while '+' in output:
        add_func(self)

    while '-' in output:
        subtract_func(self)


def update_screen(self):
    global output
    text = ''
    for x in output:
        text += str(x)
    self.output_screen.setText(text)




