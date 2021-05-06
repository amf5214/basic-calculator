from PyQt5.QtWidgets import QSystemTrayIcon, QMainWindow, QFrame, QGridLayout, QAction, QMessageBox, QMenu
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
        # Creates the frame

        self.root = QFrame(self)
        self.setCentralWidget(self.root)

        # Creates the main layout
        self.lay_main = QGridLayout(self.root)

        # formats the window properties
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('calc_icon.png'))
        self.setStyleSheet('background-color: black;''color: white')
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # primary application operations
        create_buttons(self)
        self.widgets_add()

        # sets the default text of the output screen
        self.update_screen('Basic Calculator')

        # Creates a menu bar at the top of the window
        self.menu = self.menuBar()

        # # Creates the help button and adds it to the menu
        help_btn = QAction(QIcon('qm_4.png'), 'Help', self)
        help_btn.setShortcut('Ctrl+H')
        help_btn.setStatusTip('Help')
        help_btn.triggered.connect(self.help_menu)

        self.menu.addAction(help_btn)


        tray_icon = QSystemTrayIcon(QIcon('qm_4.png'), self)
        tray_icon.setToolTip('Need help with your calculator?')
        tray_icon.activated.connect(self.help_menu)
        tray_icon.show()

        # Shows the window
        self.show()

    def widgets_add(self):
        """
        Adds the widgets to the grid layout
        """
        self.lay_main.addWidget(self.output_screen, 0, 0, 3, 4)
        self.lay_main.addWidget(self.n7, 5, 0)
        self.lay_main.addWidget(self.n8, 5, 1)
        self.lay_main.addWidget(self.n9, 5, 2)
        self.lay_main.addWidget(self.n4, 6, 0)
        self.lay_main.addWidget(self.n5, 6, 1)
        self.lay_main.addWidget(self.n6, 6, 2)
        self.lay_main.addWidget(self.n1, 7, 0)
        self.lay_main.addWidget(self.n2, 7, 1)
        self.lay_main.addWidget(self.n3, 7, 2)
        self.lay_main.addWidget(self.n0, 8, 0)
        self.lay_main.addWidget(self.add, 7, 3)
        self.lay_main.addWidget(self.subtract, 6, 3)
        self.lay_main.addWidget(self.multiply, 5, 3)
        self.lay_main.addWidget(self.divide, 4, 3)
        self.lay_main.addWidget(self.power, 4, 0)
        self.lay_main.addWidget(self.enter, 8, 3)
        self.lay_main.addWidget(self.clear, 9, 1)
        self.lay_main.addWidget(self.all_clear, 9, 0)
        self.lay_main.addWidget(self.left, 4, 1)
        self.lay_main.addWidget(self.right, 4, 2)
        self.lay_main.addWidget(self.decimal, 8, 1)
        self.lay_main.addWidget(self.negative, 8, 2)

    def help_menu(self):
        """
        Creates a popup window to explain the functionality of the app
        """

        QMessageBox.about(self, 'Help', """This is a basic calculator that has built-in order of operations. \n
The order of operations is parentheses, exponents, multiplication, division, addition, and then subtraction. \n
This calculator does not support nested parentheses, so use of them will cause a failure""")

    def update_screen(self, obj):
        """
        Updates the text in the output screen
        """

        self.output_screen.setText(obj)

    def push_0(self):
        """
        On push of 0 this will add it to the string -> final
        """

        number = 0
        state = 'number'
        self.output_modify(number, state)

    def push_1(self):
        """
        On push of 1 this will add it to the string -> final
        """

        number = 1
        state = 'number'
        self.output_modify(number, state)

    def push_2(self):
        """
        On push of 2 this will add it to the string -> final
        """

        number = 2
        state = 'number'
        self.output_modify(number, state)

    def push_3(self):
        """
         On push of 3 this will add it to the string -> final
        """

        number = 3
        state = 'number'
        self.output_modify(number, state)

    def push_4(self):
        """
        On push of 4 this will add it to the string -> final
        """

        number = 4
        state = 'number'
        self.output_modify(number, state)

    def push_5(self):
        """
        On push of 5 this will add it to the string -> final
        """

        number = 5
        state = 'number'
        self.output_modify(number, state)

    def push_6(self):
        """
        On push of 6 this will add it to the string -> final
        """

        number = 6
        state = 'number'
        self.output_modify(number, state)

    def push_7(self):
        """
        On push of 7 this will add it to the string -> final
        """

        number = 7
        state = 'number'
        self.output_modify(number, state)

    def push_8(self):
        """
        On push of 8 this will add it to the string -> final
        """

        number = 8
        state = 'number'
        self.output_modify(number, state)

    def push_9(self):
        """
        On push of 9 this will add it to the string -> final
        """

        number = 9
        state = 'number'
        self.output_modify(number, state)

    def push_add(self):
        """
        On push of + this will add it to the string -> final
        """

        number = ' + '
        state = 'symbol'
        self.output_modify(number, state)

    def push_decimal(self):
        """
        On push of . this will add it to the string -> final
        """

        number = '.'
        state = 'symbol'
        self.output_modify(number, state)

    def push_subtract(self):
        """
        On push of - this will add it to the string -> final
        """

        number = ' - '
        state = 'symbol'
        self.output_modify(number, state)

    def push_multiply(self):
        """
        On push of * this will add it to the string -> final
        """

        number = ' * '
        state = 'symbol'
        self.output_modify(number, state)

    def push_divide(self):
        """
        On push of / this will add it to the string -> final
        """

        number = ' / '
        state = 'symbol'
        self.output_modify(number, state)

    def push_power(self):
        """
        On push of ^ this will add it to the string -> final
        """

        number = ' ^ '
        state = 'symbol'
        self.output_modify(number, state)

    def push_left(self):
        """
        On push of ( this will add it to the string -> final
        """

        number = '( '
        state = 'symbol'
        self.output_modify(number, state)

    def push_right(self):
        """
        On push of ) this will add it to the string -> final
        """

        number = ' )'
        state = 'symbol'
        self.output_modify(number, state)

    def push_negative(self):
        """
        On push of - this will add it to the string -> final
        """

        number = '-'
        state = 'symbol'
        self.output_modify(number, state)

    def output_modify(self, number, state):
        """
        This function takes an input and adds it to the final string and then updates the output list
        the state input determines what is added to the final string
            if state == 'number': then the input will be an integer
            else: the input will be a str with needed spaces
        """

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
        """
        finds addition symbol in output, adds the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

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
        """
        finds subtraction symbol in output, subtracts the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

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
        """
        finds multiplication symbol in output, multiplies the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

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
        """
        finds division symbol in output, divides the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

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
        """
        finds exponent symbol in output, raises the left number to the power of the right number
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

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

    def power_func_check(self):
        """
        finds exponent symbol in array_2, raises the left number to the power of the right number
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

        global array_2
        array_2 = np.array(array_2)

        ind = np.where(array_2 == '^')
        ind = ind[0]
        # print(ind)

        for x in ind:
            if len(array_2) > x + 1:
                result_out = str(float(array_2[x - 1]) ** float(array_2[x + 1]))
                array_2 = np.delete(array_2, x - 1)
                array_2 = np.delete(array_2, x - 1)

                array_2 = list(array_2)
                array_2[x - 1] = result_out

    def multiply_func_check(self):
        """
        finds multiplication symbol in array_2, multiplies the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

        global array_2
        array_2 = np.array(array_2)

        ind = np.where(array_2 == '*')
        ind = ind[0]
        # print(ind)

        for x in ind:
            if len(array_2) > x + 1:
                result_out = str(float(array_2[x - 1]) * float(array_2[x + 1]))
                array_2 = np.delete(array_2, x - 1)
                array_2 = np.delete(array_2, x - 1)

                array_2 = list(array_2)
                array_2[x - 1] = result_out

    def division_func_check(self):
        """
        finds division symbol in array_2, divides the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

        global array_2
        array_2 = np.array(array_2)

        ind = np.where(array_2 == '/')
        ind = ind[0]
        # print(ind)

        for x in ind:
            if len(array_2) > x + 1:
                result_out = str(float(array_2[x - 1]) / float(array_2[x + 1]))
                array_2 = np.delete(array_2, x - 1)
                array_2 = np.delete(array_2, x - 1)

                array_2 = list(array_2)
                array_2[x - 1] = result_out

    def add_func_check(self):
        """
        finds addition symbol in array_2, adds the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

        global array_2
        array_2 = np.array(array_2)

        ind = np.where(array_2 == '+')
        ind = ind[0]
        # print(ind)

        for x in ind:
            if len(array_2) > x + 1:
                result_out = str(float(array_2[x - 1]) + float(array_2[x + 1]))
                array_2 = np.delete(array_2, x - 1)
                array_2 = np.delete(array_2, x - 1)

                array_2 = list(array_2)
                array_2[x - 1] = result_out

    def subtract_func_check(self):
        """
        finds subtraction symbol in array_2, subtracts the numbers on each side of it
        and then removes both numbers and the symbol.
        Then it puts the result in the output list where the first number was
        """

        global array_2
        array_2 = np.array(array_2)

        ind = np.where(array_2 == '-')
        ind = ind[0]
        # print(ind)

        for x in ind:
            if len(array_2) > x + 1:
                result_out = str(float(array_2[x - 1]) - float(array_2[x + 1]))
                array_2 = np.delete(array_2, x - 1)
                array_2 = np.delete(array_2, x - 1)

                array_2 = list(array_2)
                array_2[x - 1] = result_out

    def parenthesis_function(self):
        """
        finds parentheses in output, performs operations inside of them
        and then removes both parentheses and the contents of them.
        Then it puts the result in the output list where the first parenthesis was
        """

        global output, final, array_2
        while '(' in output and ')' in output:
            output_arr = np.array(output)

            ind_st_1 = np.where(output_arr == '(')
            ind_st = ind_st_1[0]

            ind_sp_1 = np.where(output_arr == ')')
            ind_sp = ind_sp_1[0]

            array_2 = output_arr[ind_st[0]:ind_sp[0] + 1]
            ind3 = np.where(array_2 == '(')
            ind3_i = ind3[0]

            ind4 = np.where(array_2 == ')')
            ind4_i = ind4[0]

            array_2 = np.delete(array_2, [ind3_i, ind4_i])
            array_2 = list(array_2)

            while '^' in array_2:
                self.power_func_check()

            while '*' in array_2:
                self.multiply_func_check()

            while '/' in array_2:
                self.division_func_check()

            while '+' in array_2:
                self.add_func_check()

            while '-' in array_2:
                self.subtract_func_check()

            var = list(range(ind_st[0] + 1, ind_sp[0] + 1))
            output_arr = np.delete(output_arr, var)
            output = list(output_arr)
            output[ind_st[0]] = float(array_2[0])

    def push_enter(self):
        """
        Primary control loop that is activated by pressing the enter button
        performs all operations and runs the update_screen function to update the output screen with the output
        """

        global output, final, array_2
        while '(' in output and ')' in output:
            self.parenthesis_function()
            while '(' in output and ')' in output:
                self.parenthesis_function()

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
        """
        Clears all text from the output screen and resets the final string to empty string
        """

        global final
        self.update_screen('')
        final = ''

    def push_clear(self):
        """
        Clears all text from the output screen
        """

        self.update_screen(f'{final}')

