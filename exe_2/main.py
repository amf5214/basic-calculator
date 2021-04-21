from PyQt5.QtWidgets import QApplication
import sys
from UI import *


def run():
    calc = QApplication(sys.argv)
    window = Calc()
    sys.exit(calc.exec_())


if __name__ == '__main__':
    run()
