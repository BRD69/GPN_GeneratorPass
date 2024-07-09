from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super(UiMainWindow, self).__init__()
        self.app = app

        self._setupUi()

        self._load_data()

        self._connect_event()

    def _setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(350, 500)
        self.setMinimumSize(QtCore.QSize(350, 500))
        self.setMaximumSize(QtCore.QSize(350, 500))
        self.setBaseSize(QtCore.QSize(350, 500))
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Generator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Generator.setGeometry(QtCore.QRect(85, 155, 161, 32))
        self.btn_Generator.setStyleSheet("QPushButton{\n"
                                         "    border: 1px solid rgb(167, 167, 167);\n"
                                         "    background: rgb(242, 242, 242);\n"
                                         "    font-size: 14px;\n"
                                         "    border-radius: 3px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(200, 200, 200, 128);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgba(255, 255, 255, 128);\n"
                                         "}")
        self.btn_Generator.setObjectName("btn_Generator")
        self.text_Passwords = QtWidgets.QTextEdit(self.centralwidget)
        self.text_Passwords.setGeometry(QtCore.QRect(35, 200, 271, 256))
        self.text_Passwords.setStyleSheet("QTextEdit{\n"
                                          "    \n"
                                          "}")
        self.text_Passwords.setObjectName("text_Passwords")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 5, 311, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_Header = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layout_Header.setContentsMargins(0, 0, 0, 0)
        self.layout_Header.setSpacing(5)
        self.layout_Header.setObjectName("layout_Header")
        self.frame_LENGHT = QtWidgets.QFrame(self.layoutWidget)
        self.frame_LENGHT.setObjectName("frame_LENGHT")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_LENGHT)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_prefix_LENGHT = QtWidgets.QLabel(self.frame_LENGHT)
        self.lbl_prefix_LENGHT.setObjectName("lbl_prefix_LENGHT")
        self.horizontalLayout.addWidget(self.lbl_prefix_LENGHT)
        self.spb_LENGHT = QtWidgets.QSpinBox(self.frame_LENGHT)
        self.spb_LENGHT.setObjectName("spb_LENGHT")
        self.horizontalLayout.addWidget(self.spb_LENGHT)
        self.lbl_postfix_LENGHT = QtWidgets.QLabel(self.frame_LENGHT)
        self.lbl_postfix_LENGHT.setObjectName("lbl_postfix_LENGHT")
        self.horizontalLayout.addWidget(self.lbl_postfix_LENGHT)
        self.layout_Header.addWidget(self.frame_LENGHT)
        self.frame_COUNT = QtWidgets.QFrame(self.layoutWidget)
        self.frame_COUNT.setObjectName("frame_COUNT")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_COUNT)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_prefix_COUNT = QtWidgets.QLabel(self.frame_COUNT)
        self.lbl_prefix_COUNT.setObjectName("lbl_prefix_COUNT")
        self.horizontalLayout_2.addWidget(self.lbl_prefix_COUNT)
        self.spb_COUNT = QtWidgets.QSpinBox(self.frame_COUNT)
        self.spb_COUNT.setObjectName("spb_COUNT")
        self.horizontalLayout_2.addWidget(self.spb_COUNT)
        self.lbl_postfix_COUNT = QtWidgets.QLabel(self.frame_COUNT)
        self.lbl_postfix_COUNT.setObjectName("lbl_postfix_COUNT")
        self.horizontalLayout_2.addWidget(self.lbl_postfix_COUNT)
        self.layout_Header.addWidget(self.frame_COUNT)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 80, 311, 62))
        self.widget.setObjectName("widget")
        self.layout_CB = QtWidgets.QVBoxLayout(self.widget)
        self.layout_CB.setContentsMargins(0, 0, 0, 0)
        self.layout_CB.setObjectName("layout_CB")
        self.cb_LatinChar = QtWidgets.QCheckBox(self.widget)
        self.cb_LatinChar.setObjectName("cb_LatinChar")
        self.layout_CB.addWidget(self.cb_LatinChar)
        self.cb_Numbers = QtWidgets.QCheckBox(self.widget)
        self.cb_Numbers.setObjectName("cb_Numbers")
        self.layout_CB.addWidget(self.cb_Numbers)
        self.cb_SpecialSymbol = QtWidgets.QCheckBox(self.widget)
        self.cb_SpecialSymbol.setObjectName("cb_SpecialSymbol")
        self.layout_CB.addWidget(self.cb_SpecialSymbol)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self._retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Генератор паролей"))
        self.btn_Generator.setText(_translate("MainWindow", "Сгенерировать"))
        self.lbl_prefix_LENGHT.setText(_translate("MainWindow", "Длина пароля"))
        self.lbl_postfix_LENGHT.setText(_translate("MainWindow", "символов"))
        self.lbl_prefix_COUNT.setText(_translate("MainWindow", "Количество"))
        self.lbl_postfix_COUNT.setText(_translate("MainWindow", "паролей"))
        self.cb_LatinChar.setText(_translate("MainWindow", "Латинские буквы (AaBbCc...)"))
        self.cb_Numbers.setText(_translate("MainWindow", "Цифры (0123...)"))
        self.cb_SpecialSymbol.setText(_translate("MainWindow", "Специальные символы (!@#$&*(){}[]_-+=~?)"))

    def _load_data(self):
        self.spb_COUNT.setValue(self.app.symbol_pass.get_count_pass())
        self.spb_LENGHT.setValue(self.app.length_pass)
        self.cb_LatinChar.setChecked(True)

    def _connect_event(self):
        self.btn_Generator.clicked.connect(self._generate_event)

    def _generate_event(self):
        self.text_Passwords.setText('')
        self.app.symbol_pass.set_count_pass(self.spb_COUNT.text())

        length_pass = int(self.spb_LENGHT.text())
        symbols_char = self.cb_LatinChar.isChecked()
        symbols_num = self.cb_Numbers.isChecked()
        symbols_spec = self.cb_SpecialSymbol.isChecked()
        if not symbols_char and  not symbols_num and not symbols_spec:
            self.statusbar.showMessage('Выберите вариант пароля', 3000)
            self.cb_LatinChar.setChecked(True)
            return None
        passwords = self.app.symbol_pass.get_passwords(length_pass, symbols_char, symbols_num, symbols_spec)
        self.text_Passwords.setText('\n'.join(passwords))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = UiMainWindow(None)
    ui.show()
    sys.exit(app.exec_())
