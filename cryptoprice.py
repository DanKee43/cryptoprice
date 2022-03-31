
import sys
import ctypes
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
import requests
import json
import random

def application():
    app = QApplication(sys.argv)
    mywindow = QMainWindow()

    mywindow.setWindowTitle("CryptoPrice")
    window_w = 750
    window_h = 500
    mywindow.setFixedSize(window_w, window_h)
    mywindow.setGeometry(300, 300, window_w, window_h)

    myappid = 'mycompany.myproduct.subproduct.version'                                                  # для логотипа
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    mylayout = QHBoxLayout()

    app.setWindowIcon(QtGui.QIcon("pyqtlogo.png"))                                                       # Логотип
    mywindow.setWindowIcon(QtGui.QIcon("pyqtlogo.png"))

    mywindow.setLayout(mylayout)
    label = PyQt5.QtWidgets.QLabel(mywindow)



    response = requests.get("https://api.coinbase.com/v2/prices/btc-USD/spot")
    data = response.json()
    currency = data["data"]["base"]
    price = data["data"]["amount"]
    print(response.text)
    text = QLabel(mywindow)
    text.setFixedSize(128, 128)
    text.setText(str(f"Валюта: {currency}\nЦена: {price}"))
    text.move(100, 100)
    text.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
    text.setStyleSheet("background-image : url(eth.png); border-color: black")


#################################


    Current = ""
    def changebtc():
        Current = "btc"
        print(Current)
    def changeeth():
        Current = "eth"
        print(Current)


    buttBtc = QPushButton(mywindow)
    buttBtc.setText("BTC")
    buttBtc.setFixedSize(50,50)
    buttBtc.move(400, 100) 
    buttBtc.clicked.connect(changebtc)

    buttEth = QPushButton(mywindow)
    buttEth.setText("ETH")
    buttEth.setFixedSize(50, 50)
    buttEth.move(460, 100)
    buttEth.clicked.connect(changeeth)

    text = QLabel(mywindow)
    text.setFixedSize(128, 128)
    text.setText(str(f"Валюта: {currency}\nЦена: {price}"))
    text.move(100, 100)
    text.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
    text.setStyleSheet(f"background-image : url(btc.png);")

    def buttonadd():
        zalups = ("hui", "pizda", "zhopa")
        ochko = random.randint(0, 2)
        hui = zalups[ochko]
        print(hui)
        #response = requests.get("https://api.coinbase.com/v2/prices/Btc-USD/spot")
        #data = response.json()
        #currency = data["data"]["base"]
        #price = data["data"]["amount"]
        print(response.text)
        text.setText(hui)




    button = QPushButton(mywindow)
    button.setText("Добавить криптовалюту")
    button.setFixedSize(150, 75)
    button.move(500, 250)
    button.adjustSize()
    button.clicked.connect(buttonadd)

    mywindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()