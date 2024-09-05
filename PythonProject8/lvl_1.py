# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lvl_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Level1Window(object):
    def setupUi(self, Level1Window):
        Level1Window.setObjectName("Level1Window")
        Level1Window.resize(1450, 1000)
        Level1Window.setStyleSheet("QMainWindow{\n"
"border-image: url(:/newPrefix/photo/fon_lvl.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Level1Window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 128, 119))
        self.pushButton.setMinimumSize(QtCore.QSize(128, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(128, 122))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-image: url(:/newPrefix/photo/home.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/newPrefix/photo/home2.png);\n"
"border: none;\n"
"border-ruds: 9px;}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 140, 189, 114))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-image: url(:/newPrefix/photo/back.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/newPrefix/photo/back2.png);\n"
"border: none;\n"
"border-ruds: 9px;}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1300, 20, 128, 119))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"\n"
"border: none;\n"
"    background-image: url(:/newPrefix/photo/zanovo.png);\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/newPrefix/photo/zanovo2.png);\n"
"border: none;\n"
"border-ruds: 9px;}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 50, 551, 61))
        self.label.setStyleSheet("background-image: url(:/newPrefix/photo/уровень.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 860, 338, 77))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/photo/счёт.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1000, 43, 61, 71))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/photo/lvl1.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 580, 321, 137))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/photo/Line 1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.circle_4 = QtWidgets.QPushButton(self.centralwidget)
        self.circle_4.setGeometry(QtCore.QRect(682, 580, 49, 52))
        self.circle_4.setStyleSheet("QPushButton{\n"
"background-image: url(:/newPrefix/photo/Ellipse 1.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/newPrefix/photo/Ellipse 2.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:disabled{\n"
"background-image: url(:/newPrefix/photo/Ellipse 2.png);\n"
"border: none;\n"
"border-ruds: 9px;}")
        self.circle_4.setText("")
        self.circle_4.setObjectName("circle_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(680, 580, 317, 137))
        self.label_5.setMinimumSize(QtCore.QSize(1, 0))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/photo/Line 2.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 280, 321, 435))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/photo/Line 3.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(679, 280, 318, 435))
        self.label_7.setStyleSheet("background-image: url(:/newPrefix/photo/Line 4.png);\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.circle_3 = QtWidgets.QPushButton(self.centralwidget)
        self.circle_3.setGeometry(QtCore.QRect(949, 666, 49, 52))
        self.circle_3.setStyleSheet("QPushButton{\n"
"background-image: url(:/newPrefix/photo/Ellipse 1.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/newPrefix/photo/Ellipse 2.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:disabled{\n"
"background-image: url(:/newPrefix/photo/Ellipse 2.png);\n"
"border: none;\n"
"border-ruds: 9px;}")
        self.circle_3.setText("")
        self.circle_3.setObjectName("circle_3")
        self.circle_1 = QtWidgets.QPushButton(self.centralwidget)
        self.circle_1.setGeometry(QtCore.QRect(681, 280, 49, 52))
        self.circle_1.setStyleSheet("QPushButton{\n"
"background-image: url(:/newPrefix/photo/Ellipse 1.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/newPrefix/photo/Ellipse 2.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:disabled{\n"
"background-image: url(:/newPrefix/photo/Ellipse 2.png);\n"
"border: none;\n"
"border-ruds: 9px;}")
        self.circle_1.setText("")
        self.circle_1.setObjectName("circle_1")
        self.circle_2 = QtWidgets.QPushButton(self.centralwidget)
        self.circle_2.setGeometry(QtCore.QRect(409, 667, 49, 52))
        self.circle_2.setStyleSheet("QPushButton{\n"
"background-image: url(:/newPrefix/photo/Ellipse 1.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/newPrefix/photo/Ellipse 1.png);\n"
"border: none;\n"
"border-ruds: 9px;}\n"
"\n"
"QPushButton:disabled{\n"
"background-image: url(:/newPrefix/photo/Ellipse 2.png);\n"
"border: none;\n"
"border-ruds: 9px;}")
        self.circle_2.setText("")
        self.circle_2.setObjectName("circle_2")
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.circle_4.raise_()
        self.circle_3.raise_()
        self.circle_1.raise_()
        self.circle_2.raise_()
        Level1Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Level1Window)
        QtCore.QMetaObject.connectSlotsByName(Level1Window)

    def retranslateUi(self, Level1Window):
        _translate = QtCore.QCoreApplication.translate
        Level1Window.setWindowTitle(_translate("Level1Window", "MainWindow"))
import photos
