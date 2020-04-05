from PyQt5 import QtWidgets
from ui import Ui_Calculator
import math_lib as m


class SetupWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()  # calling the init methods of the base classes QMainWindow and Ui_Calculator
        self.setupUi(self)  # creates the designed UI
        self.show()         # shows the UI

        # btns
        self.pushButton_0.clicked.connect(self.number_btn_pressed)
        self.pushButton_1.clicked.connect(self.number_btn_pressed)
        self.pushButton_2.clicked.connect(self.number_btn_pressed)
        self.pushButton_3.clicked.connect(self.number_btn_pressed)
        self.pushButton_4.clicked.connect(self.number_btn_pressed)
        self.pushButton_5.clicked.connect(self.number_btn_pressed)
        self.pushButton_6.clicked.connect(self.number_btn_pressed)
        self.pushButton_7.clicked.connect(self.number_btn_pressed)
        self.pushButton_8.clicked.connect(self.number_btn_pressed)
        self.pushButton_9.clicked.connect(self.number_btn_pressed)

        self.pushButton_dot.clicked.connect(self.dot_pressed)

        self.pushButton_not.clicked.connect(self.not_pressed)
        self.pushButton_inv.clicked.connect(self.inv_pressed)
        self.pushButton_factorial.clicked.connect(self.factorial_pressed)

    def number_btn_pressed(self):
        btn = self.sender()

        result_label = format(float(self.result.text() + btn.text()), '.15g')  # float solves starting 0, format solves formatting and string displaying
        self.result.setText(result_label)

    def dot_pressed(self):
        if '.' in self.result.text():
            self.result.setText(self.result.text())
        else:
            self.result.setText(self.result.text() + '.')

    def not_pressed(self):
        result_label = format(m.neg(float(self.result.text())), '.15g')
        self.result.setText(result_label)

    def inv_pressed(self):
        if self.result.text() == "0":
            self.result.setText("Undefined")
        else:
            result_label = format(m.inverse(float(self.result.text())), '.15g')
            self.result.setText(result_label)

    def factorial_pressed(self):
        if '.' in self.result.text() or '-' in self.result.text():
            self.result.setText("Undefined")
        else:
            result_label = format(m.factorial(int(self.result.text())), '.15g')
            self.result.setText(result_label)
