from PyQt5.QtWidgets import QMainWindow, QFrame, QGridLayout
from funcs import *
import logging as lg

lg.basicConfig(filename='calc.log',
               level=lg.INFO,
               format='%(levelname)s : %(asctime)s : %(message)s',
               filemode='w')


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()

        self.root = QFrame(self)
        self.setCentralWidget(self.root)
        self.lay_main = QGridLayout(self.root)

        create_buttons(self)

        self.widgets_add()
        update_screen(self)

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
        self.lay_main.addWidget(self.enter, 7, 3)

