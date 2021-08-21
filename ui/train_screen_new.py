from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor

import setText
import link_mapping

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.getFrom = QtWidgets.QComboBox(Form)
        self.getFrom.setObjectName("getFrom")
        self.getFrom.addItem("")
        self.getFrom.addItem("")
        self.horizontalLayout.addWidget(self.getFrom)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.categoryLine = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryLine.sizePolicy().hasHeightForWidth())
        self.categoryLine.setSizePolicy(sizePolicy)
        self.categoryLine.setObjectName("categoryLine")
        self.horizontalLayout_2.addWidget(self.categoryLine)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.startBut = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBut.sizePolicy().hasHeightForWidth())
        self.startBut.setSizePolicy(sizePolicy)
        self.startBut.setObjectName("startBut")
        self.horizontalLayout_2.addWidget(self.startBut)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(17, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.homeLine = QtWidgets.QLineEdit(Form)
        self.homeLine.setObjectName("homeLine")
        self.verticalLayout.addWidget(self.homeLine)
        spacerItem4 = QtWidgets.QSpacerItem(17, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.topicLine = QtWidgets.QLineEdit(Form)
        self.topicLine.setObjectName("topicLine")
        self.horizontalLayout_3.addWidget(self.topicLine)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.articleLine = QtWidgets.QLineEdit(Form)
        self.articleLine.setObjectName("articleLine")
        self.horizontalLayout_3.addWidget(self.articleLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(17, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        self.savedWords = QtWidgets.QTextEdit(Form)
        self.savedWords.setReadOnly(True)
        self.savedWords.setObjectName("savedWords")
        self.gridLayout.addWidget(self.savedWords, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.getFrom.activated[str].connect(self.redesign) #combo box event
        self.startBut.clicked.connect(self.start)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Train"))
        self.label.setText(_translate("Form", "Learn From"))
        self.getFrom.setItemText(0, _translate("Form", "PDF"))
        self.getFrom.setItemText(1, _translate("Form", "WEBSITE"))
        self.categoryLine.setPlaceholderText(_translate("Form", "Category"))
        self.startBut.setText(_translate("Form", "Start"))
        self.redesign()
        self.topicLine.setPlaceholderText(_translate("Form", "Topic (url category headline)"))
        self.articleLine.setPlaceholderText(_translate("Form", "Article (url news headline)"))
        # self.savedWords.setPlaceholderText(_translate("Form", "saved words"))

    def redesign(self):
        _translate = QtCore.QCoreApplication.translate
        source = self.getFrom.currentText()
        if source == "PDF":
            self.homeLine.setPlaceholderText(_translate("Form", "PDF Path"))
            self.topicLine.setEnabled(False)
            self.articleLine.setEnabled(False)
        else:
            self.homeLine.setPlaceholderText(_translate("Form", "Website home page"))
            self.topicLine.setEnabled(True)
            self.articleLine.setEnabled(True)

    def start(self):
        source = self.getFrom.currentText()
        if source == "PDF":
            path = self.homeLine.text()
            setText.run("pdf", self.categoryLine.text(), path)
        else:
            home = self.homeLine.text()
            topic = self.topicLine.text()
            article = self.articleLine.text()

            self.savedWords.append("Url search working")
            self.savedWords.repaint()

            urls = link_mapping.run(home, topic, article)
            self.savedWords.append("Url's found")
            self.savedWords.repaint()

            category = self.categoryLine.text()
            print(urls)
            for i, url in enumerate(urls):
                print(url.upper())
                self.savedWords.append(str(i) + "-) Working on:" + str(url))
                self.savedWords.repaint()
                print(i)
                setText.run("website", category, url)

        self.savedWords.append("COMPLETED")
