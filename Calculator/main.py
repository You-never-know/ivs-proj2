import sys
from PyQt5.QtWidgets import QApplication
from calculator import SetupWindow

app_object = QApplication(sys.argv)
calc_object = SetupWindow()

sys.exit(app_object.exec_())  #exits when executing done