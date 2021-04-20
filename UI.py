from PyQt5.QtWidgets import QMainWindow, QFrame, QGridLayout
from PyQt5.QtGui import QIcon
from funcs import *
import logging as lg

lg.basicConfig(filename='calc.log',
               level=lg.INFO,
               format='%(levelname)s : %(asctime)s : %(message)s',
               filemode='w')

final = ''


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()

        self.root = QFrame(self)
        self.setCentralWidget(self.root)
        self.lay_main = QGridLayout(self.root)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('calc_icon.jpg'))
        self.setStyleSheet('background-color: white')
        # self.setWindowFlags(Qt.FramelessWindowHint)

        create_buttons(self)
        self.widgets_add()
        self.update_screen('Basic Calculator')

        self.show()

    def widgets_add(self):
        self.lay_main.addWidget(self.output_screen, 0, 0, 2, 4)
        self.lay_main.addWidget(self.n7, 3, 0)
        self.lay_main.addWidget(self.n8, 3, 1)
        self.lay_main.addWidget(self.n9, 3, 2)
        self.lay_main.addWidget(self.n4, 4, 0)
        self.lay_main.addWidget(self.n5, 4, 1)
        self.lay_main.addWidget(self.n6, 4, 2)
        self.lay_main.addWidget(self.n1, 5, 0)
        self.lay_main.addWidget(self.n2, 5, 1)
        self.lay_main.addWidget(self.n3, 5, 2)
        self.lay_main.addWidget(self.n0, 6, 0)
        self.lay_main.addWidget(self.add, 3, 3)
        self.lay_main.addWidget(self.subtract, 4, 3)
        self.lay_main.addWidget(self.multiply, 5, 3)
        self.lay_main.addWidget(self.divide, 6, 3)
        self.lay_main.addWidget(self.power, 6, 2)
        self.lay_main.addWidget(self.enter, 7, 3)
        self.lay_main.addWidget(self.clear, 7, 0)
        self.lay_main.addWidget(self.all_clear, 7, 1)

    def update_screen(self, obj):
        self.output_screen.setText(obj)

    def push_0(self):
        number = 0
        state = 'number'
        self.output_modify(number, state)

    def push_1(self):
        number = 1
        state = 'number'
        self.output_modify(number, state)

    def push_2(self):
        number = 2
        state = 'number'
        self.output_modify(number, state)

    def push_3(self):
        number = 3
        state = 'number'
        self.output_modify(number, state)

    def push_4(self):
        number = 4
        state = 'number'
        self.output_modify(number, state)

    def push_5(self):
        number = 5
        state = 'number'
        self.output_modify(number, state)

    def push_6(self):
        number = 6
        state = 'number'
        self.output_modify(number, state)

    def push_7(self):
        number = 7
        state = 'number'
        self.output_modify(number, state)

    def push_8(self):
        number = 8
        state = 'number'
        self.output_modify(number, state)

    def push_9(self):
        number = 9
        state = 'number'
        self.output_modify(number, state)

    def push_add(self):
        number = ' + '
        state = 'symbol'
        self.output_modify(number, state)

    def push_subtract(self):
        number = ' - '
        state = 'symbol'
        self.output_modify(number, state)

    def push_multiply(self):
        number = ' * '
        state = 'symbol'
        self.output_modify(number, state)

    def push_divide(self):
        number = ' / '
        state = 'symbol'
        self.output_modify(number, state)

    def push_power(self):
        number = ' ^ '
        state = 'symbol'
        self.output_modify(number, state)

    def output_modify(self, number, state):
        global final, output
        if state == 'number':
            final += str(number)
        else:
            final += number

        output = final.split(sep=' ')
        self.update_screen(f'{final}')
        # print(final)
        # print(output)

    def add_func(self):
        global output
        output = np.array(output)

        ind = np.where(output == '+')
        ind = ind[0]
        # print(ind)

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
        # print(ind)

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
        # print(ind)

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
        # print(ind)

        for x in ind:
            if len(output) > x + 1:
                result_out = str(float(output[x - 1]) / float(output[x + 1]))
                output = np.delete(output, x - 1)
                output = np.delete(output, x - 1)

                output = list(output)
                output[x - 1] = result_out

    def power_func(self):
        global output
        output = np.array(output)

        ind = np.where(output == '^')
        ind = ind[0]
        # print(ind)

        for x in ind:
            if len(output) > x + 1:
                result_out = str(float(output[x - 1]) ** float(output[x + 1]))
                output = np.delete(output, x - 1)
                output = np.delete(output, x - 1)

                output = list(output)
                output[x - 1] = result_out

    def push_enter(self):
        global output, final
        while '^' in output:
            self.power_func()

        while '*' in output:
            self.multiply_func()

        while '/' in output:
            self.divide_func()

        while '+' in output:
            self.add_func()

        while '-' in output:
            self.subtract_func()

        # print(str(output[0]))
        self.update_screen(f'{final} = {str(output[0])}')

    def push_all_clear(self):
        global final
        self.update_screen('')
        final = ''

    def push_clear(self):
        self.update_screen(f'{final}')

