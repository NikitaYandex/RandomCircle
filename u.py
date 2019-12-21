#!/usr/bin/python
# -*- coding: UTF - 8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
import sqlite3
import random

v = 0
mnog = 1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 653)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 110, 331, 41))
        self.pushButton.setStyleSheet("font-size: 20pt;\n"
                                      "background-color: rgb(211, 253, 255);\n"
                                      "color: rgb(9, 3, 84);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Раздавать газеты"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = True
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self, event):
        if self.flag:
            self.flag = False
            self.paint = QPainter()
            self.paint.begin(self)
            self.draw_E(event)
            self.paint.end()

    def draw_E(self, e):
        size = random.randint(50, 350)
        self.paint.setBrush(QColor(random.choice(['yellow', 'red', 'blue', 'green', 'pink', 'orange'])))
        self.paint.drawEllipse(0, 0, size, size)
