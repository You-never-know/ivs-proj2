from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_Calculator
import math_lib as m


## Implementation of functions to GUI
# @param QtWidgets.QMainWindow PyQt plugin for GUI
# @param Ui_Calculator python implementation of calculator's UI
class SetupWindow(QtWidgets.QMainWindow, Ui_Calculator):
    x1 = None
    x2 = None
    x2_type = False

    ## Inicialization of GUI and connecting clicked buttons
    # Sets the window size to 260 × 455
    # Assigns ico.png as GUI window icon
    def __init__(self):
        super().__init__()  # calling the init methods of the base classes QMainWindow and Ui_Calculator
        self.setupUi(self)  # creates the designed UI
        self.show()  # shows the UI
        self.setFixedSize(260, 455)
        self.setWindowIcon(QIcon('ico.png'))

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

        self.pushButton_c.clicked.connect(self.c_pressed)
        self.pushButton_del.clicked.connect(self.del_pressed)

        self.pushButton_not.clicked.connect(self.not_pressed)
        self.pushButton_inv.clicked.connect(self.inv_pressed)
        self.pushButton_factorial.clicked.connect(self.factorial_pressed)

        self.pushButton_add.clicked.connect(self.operation_bin_pressed)
        self.pushButton_sub.clicked.connect(self.operation_bin_pressed)
        self.pushButton_mul.clicked.connect(self.operation_bin_pressed)
        self.pushButton_div.clicked.connect(self.operation_bin_pressed)
        self.pushButton_mod.clicked.connect(self.operation_bin_pressed)
        self.pushButton_root.clicked.connect(self.operation_bin_pressed)
        self.pushButton_power.clicked.connect(self.operation_bin_pressed)

        self.pushButton_add.setCheckable(True)
        self.pushButton_sub.setCheckable(True)
        self.pushButton_mul.setCheckable(True)
        self.pushButton_div.setCheckable(True)
        self.pushButton_mod.setCheckable(True)
        self.pushButton_root.setCheckable(True)
        self.pushButton_power.setCheckable(True)

        self.pushButton_eq.clicked.connect(self.eq_pressed)

    ## Definition for clicked decimal buttons
    def number_btn_pressed(self):
        btn = self.sender()

        if ((self.pushButton_add.isChecked() or
             self.pushButton_sub.isChecked() or
             self.pushButton_mul.isChecked() or
             self.pushButton_div.isChecked() or
             self.pushButton_mod.isChecked() or
             self.pushButton_root.isChecked() or
             self.pushButton_power.isChecked()) and (not self.x2_type)):
            # float solves starting 0, format solves formatting and string displaying
            result_label = format(float(btn.text()), '.15g')
            self.x2_type = True
        else:
            if ('.' in self.result.text()) and (btn.text() == "0"):
                result_label = self.result.text() + btn.text()

            else:
                result_label = format(float(self.result.text() + btn.text()), '.15g')
        self.result.setText(result_label)

    ## Definition for dot button clicked
    def dot_pressed(self):
        if '.' in self.result.text():
            self.result.setText(self.result.text())
        else:
            self.result.setText(self.result.text() + '.')

    ## Definition for clear button clicked
    # Operations reset - setChecked(False)
    def c_pressed(self):
        self.result.setText("0")
        self.pushButton_add.setChecked(False)
        self.pushButton_sub.setChecked(False)
        self.pushButton_mul.setChecked(False)
        self.pushButton_div.setChecked(False)
        self.pushButton_mod.setChecked(False)
        self.pushButton_root.setChecked(False)
        self.pushButton_power.setChecked(False)

    ## Definition for delete button clicked
    # Erases the last character
    def del_pressed(self):
        result_label = (self.result.text())
        if len(result_label) > 0:
            result_label = result_label[0:-1]
        else:
            result_label = ""
        self.result.setText(result_label)

    ## Definition for negation button pressed
    def not_pressed(self):
        result_label = format(m.neg(float(self.result.text())), '.15g')
        self.result.setText(result_label)

    ## Definition for inversion button pressed
    def inv_pressed(self):
        if m.inverse(float(self.result.text())) is None:
            self.result.setText("Undefined")
        else:
            result_label = format(m.inverse(float(self.result.text())), '.15g')
            self.result.setText(result_label)

    ## Definition for factorial button pressed
    def factorial_pressed(self):
        if '.' in self.result.text() or m.factorial(int(self.result.text())) is None:
            self.result.setText("Undefined")
        else:
            result_label = format(m.factorial(int(self.result.text())), '.15g')
            self.result.setText(result_label)

    ## Definition for all operations where two operands are used: addition, substraction, multiplication, division, modulo, root, exponencial to set the operation checked
    # get x1 - first operand
    def operation_bin_pressed(self):
        btn = self.sender()
        self.x1 = float(self.result.text())

        btn.setChecked(True)

    ## Definition for result of all operations where two operands are used when equals pressed
    # get x2 - second operand
    def eq_pressed(self):
        x2 = float(self.result.text())

        if self.pushButton_add.isChecked():
            result_label = format(m.addition(self.x1, x2), '.15g')
            self.pushButton_add.setChecked(False)

        elif self.pushButton_sub.isChecked():
            result_label = format(m.substraction(self.x1, x2), '.15g')
            self.pushButton_sub.setChecked(False)

        elif self.pushButton_mul.isChecked():
            result_label = format(m.multiplication(self.x1, x2), '.15g')
            self.pushButton_mul.setChecked(False)

        elif self.pushButton_div.isChecked():
            if m.division(self.x1, x2) is None:
                result_label = "Undefined"
            else:
                result_label = format(m.division(self.x1, x2), '.15g')
            self.pushButton_div.setChecked(False)

        elif self.pushButton_mod.isChecked():
            if m.modulo(self.x1, x2) is None:
                result_label = "Undefined"
            else:
                result_label = format(m.modulo(self.x1, x2), '.15g')
            self.pushButton_mod.setChecked(False)

        elif self.pushButton_root.isChecked():
            if m.root(self.x1, x2) is None:
                result_label = "Undefined"
            else:
                result_label = format(m.root(self.x1, x2), '.15g')
            self.pushButton_root.setChecked(False)

        elif self.pushButton_power.isChecked():
            if m.exponencial(self.x1, x2) is None:
                result_label = "Undefined"
            else:
                result_label = format(m.exponencial(self.x1, x2), '.15g')
            self.pushButton_power.setChecked(False)
        else:
            result_label = self.result.text()
        self.result.setText(result_label)
        self.x2_type = False
