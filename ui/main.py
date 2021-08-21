# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
import new_database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, category):
        self.db = new_database.db(category)
        self.nextPage = lambda: self.set_url(1)
        self.backpage = lambda: self.set_url(-1)
        self.dontSaveFunc = lambda: self.set_url(0)
        self.data = [None] * 4

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.webView = QWebEngineView(self.centralwidget) #----------------------
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(800, 400))
        # self.webView.setUrl(QtCore.QUrl("https://music.youtube.com/"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.backBut = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBut.sizePolicy().hasHeightForWidth())
        self.backBut.setSizePolicy(sizePolicy)
        self.backBut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backBut.setStyleSheet("border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"")
        self.backBut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBut.setIcon(icon)
        self.backBut.setIconSize(QtCore.QSize(64, 64))
        self.backBut.setCheckable(False)
        self.backBut.setObjectName("backBut")
        self.horizontalLayout.addWidget(self.backBut)
        spacerItem2 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.deleteBut = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteBut.sizePolicy().hasHeightForWidth())
        self.deleteBut.setSizePolicy(sizePolicy)
        self.deleteBut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deleteBut.setStyleSheet("border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"")
        self.deleteBut.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteBut.setIcon(icon1)
        self.deleteBut.setIconSize(QtCore.QSize(64, 64))
        self.deleteBut.setCheckable(False)
        self.deleteBut.setObjectName("deleteBut")
        self.horizontalLayout.addWidget(self.deleteBut)
        spacerItem3 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.nextBut = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBut.sizePolicy().hasHeightForWidth())
        self.nextBut.setSizePolicy(sizePolicy)
        self.nextBut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nextBut.setStyleSheet("border: none;\n"
"    background-color: transparent;\n"
"    outline: none;\n"
"")
        self.nextBut.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextBut.setIcon(icon2)
        self.nextBut.setIconSize(QtCore.QSize(64, 64))
        self.nextBut.setCheckable(False)
        self.nextBut.setObjectName("nextBut")
        self.horizontalLayout.addWidget(self.nextBut)
        spacerItem4 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.nextPage()
        self.control()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Translate", "Translate"))
# from PyQt5 import QtWebKitWidgets

    def set_url(self, c):
        if c == 1:
            self.data = self.db.readDB(False, self.data[1])
        elif c == -1:
            self.data = self.db.readDB(True, self.data[1])
        elif c == 0:
            self.data = self.db.remove_from_db(self.data[1])
            self.set_url(1)

        print("main :", self.data)
        self.webView.setUrl(QtCore.QUrl('https://translate.google.com/?sl=en&tl=tr&text='+str(self.data[1])+'&op=translate'))

    def control(self):
        self.nextBut.clicked.connect(self.nextPage)

        self.backBut.clicked.connect(self.backpage)

        self.deleteBut.clicked.connect(self.dontSaveFunc)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "database table name(saved category name + _1 or _2)")
    MainWindow.show()
    sys.exit(app.exec_())
