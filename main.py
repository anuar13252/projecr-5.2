import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_Solve.clicked.connect(self.solve)
        self.btn_Clear.clicked.connect(self.clear)

    def clear(self):
        self.lineEdit_Text.clear()
        self.lineEdit_Words.clear()

    def solve(self):
        l = []
        text = self.lineEdit_Text.toPlainText()
        text = text.split()
        for i in range(len(text)):
            if text[i][0] == 'а' and text[i][-1] == 'я':
                l.append(text[i])
            else:
                continue
        self.lineEdit_Words.insertPlainText(' '.join(map(str, l)))

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()