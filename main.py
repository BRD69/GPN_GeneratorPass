import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

from form_main import UiMainWindow


class SymbolsPassword:
    def __init__(self, count_pass=3):
        self.count_pass = count_pass
        self.symbols_num = '0123456789'
        self.symbols_char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        self.symbols_spec = '!@#$&*(){}[]_-+=~?'
        self.symbols_pass = ''

    def get_count_pass(self):
        return self.count_pass

    def set_count_pass(self, count_pass):
        self.count_pass = int(count_pass)

    def get_passwords(self, length_pass, is_char=True, is_num=False, is_special=False):
        passwords = []
        self.symbols_pass = ''

        if is_char:
            self.symbols_pass += self.symbols_char
        if is_num:
            self.symbols_pass += self.symbols_num
        if is_special:
            self.symbols_pass += self.symbols_spec

        for n in range(self.count_pass):
            password = ''
            for i in range(length_pass):
                password += random.choice(self.symbols_pass)
            passwords.append(password)

        return passwords


class AppPasswordGenerator(QMainWindow):
    def __init__(self):
        super(AppPasswordGenerator, self).__init__()

        self.symbol_pass = SymbolsPassword()
        self.length_pass = 12

        self.ui = UiMainWindow(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.ico"))
    window = AppPasswordGenerator()
    window.ui.show()

    sys.exit(app.exec_())
