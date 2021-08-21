from PyQt5 import QtCore, QtWidgets, QtGui
import re
import database
from PyQt5.QtWebEngineWidgets import *


class Ui_Form(object):


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.trainLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainLabel.sizePolicy().hasHeightForWidth())
        self.trainLabel.setSizePolicy(sizePolicy)
        self.trainLabel.setStyleSheet("")
        self.trainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trainLabel.setObjectName("trainLabel")
        self.horizontalLayout_2.addWidget(self.trainLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.trainBut = QtWidgets.QPushButton(Form)
        self.trainBut.setObjectName("trainBut")
        self.horizontalLayout_2.addWidget(self.trainBut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.learnBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.learnBox.sizePolicy().hasHeightForWidth())
        self.learnBox.setSizePolicy(sizePolicy)
        self.learnBox.setObjectName("learnBox")
        self.horizontalLayout.addWidget(self.learnBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.learnBut = QtWidgets.QPushButton(Form)
        self.learnBut.setObjectName("learnBut")
        self.horizontalLayout.addWidget(self.learnBut)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.db = database.db()
        self.comboBox()

        self.trainBut.clicked.connect(self.get_train)
        self.learnBut.clicked.connect(self.learn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Language Learn Project"))
        self.trainLabel.setText(_translate("Form", "Train the model"))
        self.trainBut.setText(_translate("Form", "Train"))
        self.learnBut.setText(_translate("Form", "Learn"))

    def comboBox(self):
        data = self.db.table_list()
        if not data:
            return

        for i in data:
            a = re.sub('_1$', '(one word)', i[0])
            a = re.sub('_2$', '(two word)', a)
            self.learnBox.addItem(a)

    def get_train(self):
        from train_screen_new import Ui_Form

        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def learn(self):
        from main import Ui_MainWindow
        category = self.learnBox.currentText()

        category = re.sub('\(one word\)$', '_1', category)
        category = re.sub('\(two word\)$', '_2', category)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, category)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
