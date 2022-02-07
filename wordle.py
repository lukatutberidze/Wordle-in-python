from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import random
import data as dt

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(507, 763)
                font = QtGui.QFont()
                font.setPointSize(20)
                MainWindow.setFont(font)
                MainWindow.setStyleSheet("background-color: rgb(18, 18, 18);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(160, 20, 201, 71))
                font = QtGui.QFont()
                font.setFamily("Trebuchet MS")
                font.setPointSize(36)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(255, 255, 255);")
                self.label.setObjectName("label")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(10, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton.setObjectName("pushButton")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(60, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_3.setGeometry(QtCore.QRect(110, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_3.setFont(font)
                self.pushButton_3.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(160, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_4.setFont(font)
                self.pushButton_4.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_5.setGeometry(QtCore.QRect(210, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_5.setFont(font)
                self.pushButton_5.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_5.setObjectName("pushButton_5")
                self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_6.setGeometry(QtCore.QRect(260, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_6.setFont(font)
                self.pushButton_6.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_6.setObjectName("pushButton_6")
                self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_7.setGeometry(QtCore.QRect(310, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_7.setFont(font)
                self.pushButton_7.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_7.setObjectName("pushButton_7")
                self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_8.setGeometry(QtCore.QRect(360, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_8.setFont(font)
                self.pushButton_8.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_8.setObjectName("pushButton_8")
                self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_9.setGeometry(QtCore.QRect(410, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_9.setFont(font)
                self.pushButton_9.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_9.setObjectName("pushButton_9")
                self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_10.setGeometry(QtCore.QRect(460, 510, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_10.setFont(font)
                self.pushButton_10.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_10.setObjectName("pushButton_10")
                self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_11.setGeometry(QtCore.QRect(30, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_11.setFont(font)
                self.pushButton_11.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_11.setObjectName("pushButton_11")
                self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_12.setGeometry(QtCore.QRect(80, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_12.setFont(font)
                self.pushButton_12.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_12.setObjectName("pushButton_12")
                self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_13.setGeometry(QtCore.QRect(130, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_13.setFont(font)
                self.pushButton_13.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_13.setObjectName("pushButton_13")
                self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_14.setGeometry(QtCore.QRect(180, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_14.setFont(font)
                self.pushButton_14.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_14.setObjectName("pushButton_14")
                self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_15.setGeometry(QtCore.QRect(230, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_15.setFont(font)
                self.pushButton_15.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_15.setObjectName("pushButton_15")
                self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_16.setGeometry(QtCore.QRect(280, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_16.setFont(font)
                self.pushButton_16.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_16.setObjectName("pushButton_16")
                self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_17.setGeometry(QtCore.QRect(330, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_17.setFont(font)
                self.pushButton_17.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_17.setObjectName("pushButton_17")
                self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_18.setGeometry(QtCore.QRect(380, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_18.setFont(font)
                self.pushButton_18.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_18.setObjectName("pushButton_18")
                self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_19.setGeometry(QtCore.QRect(430, 580, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_19.setFont(font)
                self.pushButton_19.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_19.setObjectName("pushButton_19")
                self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_20.setGeometry(QtCore.QRect(10, 650, 61, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_20.setFont(font)
                self.pushButton_20.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_20.setObjectName("pushButton_20")
                self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_21.setGeometry(QtCore.QRect(80, 650, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_21.setFont(font)
                self.pushButton_21.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_21.setObjectName("pushButton_21")
                self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_22.setGeometry(QtCore.QRect(130, 650, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_22.setFont(font)
                self.pushButton_22.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_22.setObjectName("pushButton_22")
                self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_23.setGeometry(QtCore.QRect(180, 650, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_23.setFont(font)
                self.pushButton_23.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_23.setObjectName("pushButton_23")
                self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_24.setGeometry(QtCore.QRect(230, 650, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_24.setFont(font)
                self.pushButton_24.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_24.setObjectName("pushButton_24")
                self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_25.setGeometry(QtCore.QRect(280, 650, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_25.setFont(font)
                self.pushButton_25.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_25.setObjectName("pushButton_25")
                self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_26.setGeometry(QtCore.QRect(330, 650, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_26.setFont(font)
                self.pushButton_26.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_26.setObjectName("pushButton_26")
                self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_27.setGeometry(QtCore.QRect(380, 650, 41, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_27.setFont(font)
                self.pushButton_27.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_27.setObjectName("pushButton_27")
                self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_28.setGeometry(QtCore.QRect(430, 650, 71, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic UI")
                font.setPointSize(12)
                self.pushButton_28.setFont(font)
                self.pushButton_28.setStyleSheet("background-color: rgb(131, 131, 131);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:\"10 px\"")
                self.pushButton_28.setObjectName("pushButton_28")
                self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser.setGeometry(QtCore.QRect(90, 120, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser.setFont(font)
                self.textBrowser.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser.setObjectName("textBrowser")
                self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_2.setGeometry(QtCore.QRect(160, 120, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_2.setFont(font)
                self.textBrowser_2.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_2.setObjectName("textBrowser_2")
                self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_3.setGeometry(QtCore.QRect(230, 120, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_3.setFont(font)
                self.textBrowser_3.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_3.setObjectName("textBrowser_3")
                self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_4.setGeometry(QtCore.QRect(300, 120, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_4.setFont(font)
                self.textBrowser_4.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_4.setObjectName("textBrowser_4")
                self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_5.setGeometry(QtCore.QRect(370, 120, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_5.setFont(font)
                self.textBrowser_5.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_5.setObjectName("textBrowser_5")
                self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_6.setGeometry(QtCore.QRect(90, 190, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_6.setFont(font)
                self.textBrowser_6.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_6.setObjectName("textBrowser_6")
                self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_7.setGeometry(QtCore.QRect(160, 190, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_7.setFont(font)
                self.textBrowser_7.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_7.setObjectName("textBrowser_7")
                self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_8.setGeometry(QtCore.QRect(230, 190, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_8.setFont(font)
                self.textBrowser_8.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_8.setObjectName("textBrowser_8")
                self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_9.setGeometry(QtCore.QRect(300, 190, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_9.setFont(font)
                self.textBrowser_9.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_9.setObjectName("textBrowser_9")
                self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_10.setGeometry(QtCore.QRect(370, 190, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_10.setFont(font)
                self.textBrowser_10.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_10.setObjectName("textBrowser_10")
                self.textBrowser_11 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_11.setGeometry(QtCore.QRect(90, 260, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_11.setFont(font)
                self.textBrowser_11.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_11.setObjectName("textBrowser_11")
                self.textBrowser_12 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_12.setGeometry(QtCore.QRect(160, 260, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_12.setFont(font)
                self.textBrowser_12.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_12.setObjectName("textBrowser_12")
                self.textBrowser_13 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_13.setGeometry(QtCore.QRect(230, 260, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_13.setFont(font)
                self.textBrowser_13.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_13.setObjectName("textBrowser_13")
                self.textBrowser_14 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_14.setGeometry(QtCore.QRect(300, 260, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_14.setFont(font)
                self.textBrowser_14.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_14.setObjectName("textBrowser_14")
                self.textBrowser_15 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_15.setGeometry(QtCore.QRect(370, 260, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_15.setFont(font)
                self.textBrowser_15.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_15.setObjectName("textBrowser_15")
                self.textBrowser_16 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_16.setGeometry(QtCore.QRect(90, 330, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_16.setFont(font)
                self.textBrowser_16.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_16.setObjectName("textBrowser_16")
                self.textBrowser_17 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_17.setGeometry(QtCore.QRect(160, 330, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_17.setFont(font)
                self.textBrowser_17.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_17.setObjectName("textBrowser_17")
                self.textBrowser_18 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_18.setGeometry(QtCore.QRect(230, 330, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_18.setFont(font)
                self.textBrowser_18.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_18.setObjectName("textBrowser_18")
                self.textBrowser_19 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_19.setGeometry(QtCore.QRect(300, 330, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_19.setFont(font)
                self.textBrowser_19.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_19.setObjectName("textBrowser_19")
                self.textBrowser_20 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_20.setGeometry(QtCore.QRect(370, 330, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_20.setFont(font)
                self.textBrowser_20.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_20.setObjectName("textBrowser_20")
                self.textBrowser_21 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_21.setGeometry(QtCore.QRect(90, 400, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_21.setFont(font)
                self.textBrowser_21.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_21.setObjectName("textBrowser_21")
                self.textBrowser_22 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_22.setGeometry(QtCore.QRect(160, 400, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_22.setFont(font)
                self.textBrowser_22.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_22.setObjectName("textBrowser_22")
                self.textBrowser_23 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_23.setGeometry(QtCore.QRect(230, 400, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_23.setFont(font)
                self.textBrowser_23.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_23.setObjectName("textBrowser_23")
                self.textBrowser_24 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_24.setGeometry(QtCore.QRect(300, 400, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_24.setFont(font)
                self.textBrowser_24.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_24.setObjectName("textBrowser_24")
                self.textBrowser_25 = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser_25.setGeometry(QtCore.QRect(370, 400, 61, 61))
                font = QtGui.QFont()
                font.setPointSize(26)
                self.textBrowser_25.setFont(font)
                self.textBrowser_25.setStyleSheet("background-color: rgb(80, 80, 80);")
                self.textBrowser_25.setObjectName("textBrowser_25")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.setup()

        def setup(self):
                self.word=random.choice(dt.ls).upper()
                print (self.word)
                self.able=0
                self.cells=[self.textBrowser,self.textBrowser_2, self.textBrowser_3,  self.textBrowser_4,  self.textBrowser_5,  self.textBrowser_6,  self.textBrowser_7,  self.textBrowser_8,  self.textBrowser_9,  self.textBrowser_10,  self.textBrowser_11,  self.textBrowser_12,  self.textBrowser_13,  self.textBrowser_14,  self.textBrowser_15,  self.textBrowser_16,  self.textBrowser_17,  self.textBrowser_18,  self.textBrowser_19,  self.textBrowser_20,  self.textBrowser_21,  self.textBrowser_22,  self.textBrowser_23,  self.textBrowser_24,  self.textBrowser_25,]
                self.pushButton.clicked.connect(lambda x:self.fill(self.pushButton))
                self.pushButton_2.clicked.connect(lambda x:self.fill(self.pushButton_2))
                self.pushButton_3.clicked.connect(lambda x:self.fill(self.pushButton_3))
                self.pushButton_4.clicked.connect(lambda x:self.fill(self.pushButton_4))
                self.pushButton_5.clicked.connect(lambda x:self.fill(self.pushButton_5))
                self.pushButton_6.clicked.connect(lambda x:self.fill(self.pushButton_6))
                self.pushButton_7.clicked.connect(lambda x:self.fill(self.pushButton_7))
                self.pushButton_8.clicked.connect(lambda x:self.fill(self.pushButton_8))
                self.pushButton_9.clicked.connect(lambda x:self.fill(self.pushButton_9))
                self.pushButton_10.clicked.connect(lambda x:self.fill(self.pushButton_10))
                self.pushButton_11.clicked.connect(lambda x:self.fill(self.pushButton_11))
                self.pushButton_12.clicked.connect(lambda x:self.fill(self.pushButton_12))
                self.pushButton_13.clicked.connect(lambda x:self.fill(self.pushButton_13))
                self.pushButton_14.clicked.connect(lambda x:self.fill(self.pushButton_14))
                self.pushButton_15.clicked.connect(lambda x:self.fill(self.pushButton_15))
                self.pushButton_16.clicked.connect(lambda x:self.fill(self.pushButton_16))
                self.pushButton_17.clicked.connect(lambda x:self.fill(self.pushButton_17))
                self.pushButton_18.clicked.connect(lambda x:self.fill(self.pushButton_18))
                self.pushButton_19.clicked.connect(lambda x:self.fill(self.pushButton_19))
                self.pushButton_21.clicked.connect(lambda x:self.fill(self.pushButton_21))
                self.pushButton_22.clicked.connect(lambda x:self.fill(self.pushButton_22))
                self.pushButton_23.clicked.connect(lambda x:self.fill(self.pushButton_23))
                self.pushButton_24.clicked.connect(lambda x:self.fill(self.pushButton_24))
                self.pushButton_25.clicked.connect(lambda x:self.fill(self.pushButton_25))
                self.pushButton_26.clicked.connect(lambda x:self.fill(self.pushButton_26))
                self.pushButton_27.clicked.connect(lambda x:self.fill(self.pushButton_27))
                self.pushButton_28.clicked.connect(self.delt)
                self.pushButton_20.clicked.connect(self.check)

        def fill(self,x):
                for i in range(25):
                        if self.cells[i].toPlainText()=='':
                                if i%5==0 and self.able!=i:
                                        break
                                self.cells[i].setText(f' {x.text()}')
                                break 
        def delt(self):
                for i in range(25):
                        if self.cells[i].toPlainText()=='':
                                if i==self.able:
                                        break
                                self.cells[i-1].setText(f'')
                        
        def check(self):
                st=''
                for i in range(self.able,self.able+5):

                        try:
                                st+=self.cells[i].toPlainText()[1]
                        except:
                                return None
                for i in range(5):
                        if st[i]==self.word[i]:
                                self.cells[self.able+i].setStyleSheet('background-color:green')
                        elif st[i] in self.word:
                                self.cells[self.able+i].setStyleSheet('background-color:yellow')
                        else:
                                self.cells[self.able+i].setStyleSheet('background-color:red')
                self.able+=5
                if st==self.word:
                        self.successlog('Congratulations! you won!')
                        self.restart()
                elif self.able==25:
                        self.successlog(f'You lost! the correct word was {self.word.lower()}')
                        self.restart()

        def successlog(self,message):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(message)
                msgBox.setWindowTitle("Game over")
                msgBox.addButton('Try again', QMessageBox.YesRole)
                returnValue = msgBox.exec()

        def restart(self):
                self.word=random.choice(dt.ls).upper()
                self.able=0
                print (self.word)
                for i in self.cells:
                        i.setText('')
                        i.setStyleSheet("background-color: rgb(80, 80, 80);")

                

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", " WORDLE"))
                self.pushButton.setText(_translate("MainWindow", "Q"))
                self.pushButton_2.setText(_translate("MainWindow", "W"))
                self.pushButton_3.setText(_translate("MainWindow", "E"))
                self.pushButton_4.setText(_translate("MainWindow", "R"))
                self.pushButton_5.setText(_translate("MainWindow", "T"))
                self.pushButton_6.setText(_translate("MainWindow", "Y"))
                self.pushButton_7.setText(_translate("MainWindow", "U"))
                self.pushButton_8.setText(_translate("MainWindow", "I"))
                self.pushButton_9.setText(_translate("MainWindow", "O"))
                self.pushButton_10.setText(_translate("MainWindow", "P"))
                self.pushButton_11.setText(_translate("MainWindow", "A"))
                self.pushButton_12.setText(_translate("MainWindow", "S"))
                self.pushButton_13.setText(_translate("MainWindow", "D"))
                self.pushButton_14.setText(_translate("MainWindow", "F"))
                self.pushButton_15.setText(_translate("MainWindow", "G"))
                self.pushButton_16.setText(_translate("MainWindow", "H"))
                self.pushButton_17.setText(_translate("MainWindow", "J"))
                self.pushButton_18.setText(_translate("MainWindow", "K"))
                self.pushButton_19.setText(_translate("MainWindow", "L"))
                self.pushButton_20.setText(_translate("MainWindow", "Enter"))
                self.pushButton_21.setText(_translate("MainWindow", "Z"))
                self.pushButton_22.setText(_translate("MainWindow", "X"))
                self.pushButton_23.setText(_translate("MainWindow", "C"))
                self.pushButton_24.setText(_translate("MainWindow", "V"))
                self.pushButton_25.setText(_translate("MainWindow", "B"))
                self.pushButton_26.setText(_translate("MainWindow", "N"))
                self.pushButton_27.setText(_translate("MainWindow", "M"))
                self.pushButton_28.setText(_translate("MainWindow", "Delete"))
                self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_19.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_22.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_23.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textBrowser_25.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
