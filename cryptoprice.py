
import sys
import ctypes
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QSlider, QCheckBox, QMainWindow, QLabel
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap


myappid = 'mycompany.myproduct.subproduct.version'                                                  # для логотипа
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication(sys.argv)
mywindow = QMainWindow()
mylayout = QHBoxLayout()

app.setWindowIcon(QtGui.QIcon("pyqtlogo.png"))                                                       # Логотип
mywindow.setWindowIcon(QtGui.QIcon("pyqtlogo.png"))

mywindow.setLayout(mylayout)

window_w = 750
window_h = 500
mywindow.setFixedSize(window_w, window_h)
mywindow.setWindowTitle("CryptoPrice")

label = PyQt5.QtWidgets.QLabel(mywindow)
label.setStyleSheet("color: blue")


mywindow.show()

if __name__ == "__main__":
    sys.exit(app.exec_())

