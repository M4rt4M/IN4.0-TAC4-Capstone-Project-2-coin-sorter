# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoinSorterMenu(object):
    def setupUi(self, CoinSorterMenu):
        CoinSorterMenu.setObjectName("CoinSorterMenu")
        CoinSorterMenu.resize(703, 607)
        self.pushButton = QtWidgets.QPushButton(CoinSorterMenu)
        self.pushButton.setGeometry(QtCore.QRect(10, 360, 161, 71))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("font: 12pt \"Calibri\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(CoinSorterMenu)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 450, 201, 71))
        self.pushButton_2.setStyleSheet("font: 12pt \"Calibri\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(CoinSorterMenu)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 360, 171, 71))
        self.pushButton_3.setStyleSheet("font: 12pt \"Calibri\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(CoinSorterMenu)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 360, 161, 71))
        self.pushButton_4.setStyleSheet("font: 12pt \"Calibri\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(CoinSorterMenu)
        self.pushButton_5.setGeometry(QtCore.QRect(530, 360, 161, 71))
        self.pushButton_5.setStyleSheet("font: 12pt \"Calibri\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(CoinSorterMenu)
        self.label.setGeometry(QtCore.QRect(160, 30, 371, 81))
        self.label.setStyleSheet("border-style:outset;\n"
"border-width:2px;\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"font: 26pt \"Calibri\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CoinSorterMenu)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 241, 191))
        self.label_2.setStyleSheet("border-style:outset;\n"
"border-width:2px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("coins.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(CoinSorterMenu)
        QtCore.QMetaObject.connectSlotsByName(CoinSorterMenu)

    def retranslateUi(self, CoinSorterMenu):
        _translate = QtCore.QCoreApplication.translate
        CoinSorterMenu.setWindowTitle(_translate("CoinSorterMenu", "Form"))
        self.pushButton.setText(_translate("CoinSorterMenu", "Coin Sorter Calculator"))
        self.pushButton_2.setText(_translate("CoinSorterMenu", "See Program Configuration"))
        self.pushButton_3.setText(_translate("CoinSorterMenu", "Multiple Coin Calculator"))
        self.pushButton_4.setText(_translate("CoinSorterMenu", "See Coin List"))
        self.pushButton_5.setText(_translate("CoinSorterMenu", "Set Details"))
        self.label.setText(_translate("CoinSorterMenu", "Coin Sorter - Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CoinSorterMenu = QtWidgets.QWidget()
    ui = Ui_CoinSorterMenu()
    ui.setupUi(CoinSorterMenu)
    CoinSorterMenu.show()
    sys.exit(app.exec_())