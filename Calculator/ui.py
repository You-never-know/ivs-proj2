# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(240, 420)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_factorial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_factorial.setEnabled(True)
        self.pushButton_factorial.setGeometry(QtCore.QRect(0, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_factorial.setFont(font)
        self.pushButton_factorial.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_factorial.setObjectName("pushButton_factorial")
        self.pushButton_not = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_not.setEnabled(True)
        self.pushButton_not.setGeometry(QtCore.QRect(60, 60, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_not.setFont(font)
        self.pushButton_not.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_not.setObjectName("pushButton_not")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 240, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(0, 0, 240, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid rgb(220, 220, 220);\n"
"  background-color : white;\n"
"}\n"
"\n"
"")
        self.result.setObjectName("result")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 240, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 180, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 300, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 300, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setEnabled(True)
        self.pushButton_div.setGeometry(QtCore.QRect(180, 180, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: rgb(245, 252, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_power = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_power.setEnabled(True)
        self.pushButton_power.setGeometry(QtCore.QRect(60, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_power.setFont(font)
        self.pushButton_power.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_power.setObjectName("pushButton_power")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mul.setEnabled(True)
        self.pushButton_mul.setGeometry(QtCore.QRect(180, 240, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: rgb(245, 252, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setEnabled(True)
        self.pushButton_0.setGeometry(QtCore.QRect(60, 360, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_root = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_root.setEnabled(True)
        self.pushButton_root.setGeometry(QtCore.QRect(120, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_root.setFont(font)
        self.pushButton_root.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setEnabled(True)
        self.pushButton_del.setGeometry(QtCore.QRect(180, 60, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setEnabled(True)
        self.pushButton_dot.setGeometry(QtCore.QRect(0, 360, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 300, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sub.setEnabled(True)
        self.pushButton_sub.setGeometry(QtCore.QRect(180, 300, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: rgb(245, 252, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_inv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inv.setEnabled(True)
        self.pushButton_inv.setGeometry(QtCore.QRect(0, 60, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_inv.setFont(font)
        self.pushButton_inv.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_inv.setObjectName("pushButton_inv")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 180, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 180, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_mod = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mod.setEnabled(True)
        self.pushButton_mod.setGeometry(QtCore.QRect(180, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mod.setFont(font)
        self.pushButton_mod.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.pushButton_eq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eq.setEnabled(True)
        self.pushButton_eq.setGeometry(QtCore.QRect(120, 360, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 240, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setEnabled(True)
        self.pushButton_add.setGeometry(QtCore.QRect(180, 360, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(245, 245, 245);\n"
"   background-color: rgb(245, 252, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(245, 245, 245);\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_c = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c.setEnabled(True)
        self.pushButton_c.setGeometry(QtCore.QRect(120, 60, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setStyleSheet("QPushButton {\n"
"   border: 1px solid  rgb(242, 242, 242);\n"
"   background-color:  rgb(250, 250, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:   rgb(242, 242, 242);\n"
"}")
        self.pushButton_c.setObjectName("pushButton_c")
        Calculator.setCentralWidget(self.centralwidget)
        self.result.setBuddy(self.result)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.pushButton_factorial.setText(_translate("Calculator", "x!"))
        self.pushButton_not.setText(_translate("Calculator", "+/-"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.result.setText(_translate("Calculator", "0"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_div.setText(_translate("Calculator", "÷"))
        self.pushButton_power.setText(_translate("Calculator", "xⁿ"))
        self.pushButton_mul.setText(_translate("Calculator", "×"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_root.setText(_translate("Calculator", "ⁿ√x"))
        self.pushButton_del.setText(_translate("Calculator", "del"))
        self.pushButton_dot.setText(_translate("Calculator", "."))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_sub.setText(_translate("Calculator", "-"))
        self.pushButton_inv.setText(_translate("Calculator", "1/x"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_mod.setText(_translate("Calculator", "%"))
        self.pushButton_eq.setText(_translate("Calculator", "="))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_add.setText(_translate("Calculator", "+"))
        self.pushButton_c.setText(_translate("Calculator", "C"))
