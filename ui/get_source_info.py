# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_website-file_info.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, source):
        self.source = source
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.homeLine = QtWidgets.QLineEdit(Form)
        self.homeLine.setObjectName("homeLine")
        self.verticalLayout.addWidget(self.homeLine)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.topicLine = QtWidgets.QLineEdit(Form)
        self.topicLine.setObjectName("topicLine")
        self.verticalLayout.addWidget(self.topicLine)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.articleLine = QtWidgets.QLineEdit(Form)
        self.articleLine.setObjectName("articleLine")
        self.verticalLayout.addWidget(self.articleLine)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(142, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.getBut = QtWidgets.QPushButton(Form)
        self.getBut.setObjectName("getBut")
        self.gridLayout.addWidget(self.getBut, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(142, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.getBut.clicked.connect(self._return)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.topicLine.setPlaceholderText(_translate("Form", "topic (category title)"))
        self.articleLine.setPlaceholderText(_translate("Form", "article (new title)"))
        self.getBut.setText(_translate("Form", "Okey"))

        if self.source == "PDF":
            self.homeLine.setPlaceholderText(_translate("Form", "PDF Path"))
            self.topicLine.setDisabled(True)
            self.articleLine.setDisabled(True)
        else:
            self.homeLine.setPlaceholderText(_translate("Form", "Website home page"))

    def _return(self):
        if self.source == "PDF":
            return self.homeLine.text()
        else:
            return [self.homeLine.text(), self.topicLine.text(), self.articleLine.text()]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
