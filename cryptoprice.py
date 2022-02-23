
import sys
import ctypes
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
import requests
import json

def application():
    app = QApplication(sys.argv)
    mywindow = QMainWindow()
    mywindow.setWindowTitle("CryptoPrice")
    window_w = 750
    window_h = 500
    mywindow.setFixedSize(window_w, window_h)
    mywindow.setGeometry(300,300, window_w, window_h)

    myappid = 'mycompany.myproduct.subproduct.version'                                                  # для логотипа
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    mylayout = QHBoxLayout()

    app.setWindowIcon(QtGui.QIcon("pyqtlogo.png"))                                                       # Логотип
    mywindow.setWindowIcon(QtGui.QIcon("pyqtlogo.png"))

    mywindow.setLayout(mylayout)
    label = PyQt5.QtWidgets.QLabel(mywindow)

    response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    data = response.json()
    currency = data["data"]["base"]
    price = data["data"]["amount"]
    print(price)

    print(response.text)

    text = QLabel(mywindow)
    text.setFixedSize(200,200)
    text.setText(str(f"Валюта: {currency}\n Цена: {price}"))
    text.move(100,100)
    text.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))


    button = QPushButton(mywindow)
    button.setText("Добавить криптовалюту")
    button.setFixedSize(150,75)
    button.move(300, 250)
    button.adjustSize()




    mywindow.show()
    sys.exit(app.exec_())




def Button():
    print("hui")


if __name__ == "__main__":
    application()