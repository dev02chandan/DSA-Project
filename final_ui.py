# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def button1click(self):
        print("Chall raha hai")
    def button2click(self):
        print("Chall raha hai returns")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 566)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enter = QtWidgets.QLabel(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(66, 200, 231, 21))
        self.enter.setStyleSheet("font: 14pt \"NSimSun\";")
        self.enter.setObjectName("enter")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 190, 101, 41))
        self.pushButton.setStyleSheet("background-color: rgb(64, 147, 255);\n"
"font: 12pt \"NSimSun\";\n"
"border-radius: 10px;\n"
"box-shadow: 1px 2px 22px 0px rgb(89,87,87,0.85);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button1click)
        self.enter_2 = QtWidgets.QLabel(self.centralwidget)
        self.enter_2.setGeometry(QtCore.QRect(66, 260, 251, 21))
        self.enter_2.setStyleSheet("font: 14pt \"NSimSun\";")
        self.enter_2.setObjectName("enter_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 250, 101, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(64, 147, 255);\n"
"font: 12pt \"NSimSun\";\n"
"border-radius: 10px;\n"
"box-shadow: 1px 2px 22px 0px rgb(89,87,87,0.85);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.button2click)
        self.enter_3 = QtWidgets.QLabel(self.centralwidget)
        self.enter_3.setGeometry(QtCore.QRect(66, 320, 101, 21))
        self.enter_3.setStyleSheet("font: 14pt \"NSimSun\";")
        self.enter_3.setObjectName("enter_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(186, 320, 251, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 21))
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
        self.enter.setText(_translate("MainWindow", "Enter File to Compress:"))
        self.pushButton.setText(_translate("MainWindow", "Select File"))
        self.enter_2.setText(_translate("MainWindow", "Enter File to Decompress:"))
        self.pushButton_2.setText(_translate("MainWindow", "Select File"))
        self.enter_3.setText(_translate("MainWindow", "Download:"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
