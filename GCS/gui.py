# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_MainWindow(object):
    def csvtoxlsx(self):
        df = pd.read_csv('telemetrylive.csv')
        df.to_excel('telemetrylive.xlsx', index=None, header=True) 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(252, 253, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 571, 81))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 290, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(209, 255, 226);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self. csvtoxlsx)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "csv2xlsxConverter"))
        self.label.setText(_translate("MainWindow", ".csv to .xlsx CONVERTER"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
