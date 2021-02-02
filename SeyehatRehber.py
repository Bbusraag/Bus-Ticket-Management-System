

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QObject, QPointF, QPropertyAnimation, pyqtProperty

class seyehat(object):



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 534)
        Form.setStyleSheet("background-color: rgb(25, 115, 200);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 201, 551))
        self.frame.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"    \n"
"}\n"
"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(85, 170, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fotoğraf/Screenshot_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.PANDEMIC))
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fotoğraf/icons8-reply-arrow-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 390, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    color: rgb(85, 170, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("fotoğraf/Screenshot_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.TICKET))
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 250, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    color: rgb(85, 170, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("fotoğraf/Screenshot_5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.SAFE))
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 80, 751, 461))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.PANDEMIC = QtWidgets.QWidget()
        self.PANDEMIC.setObjectName("PANDEMIC")
        self.frame_3 = QtWidgets.QFrame(self.PANDEMIC)
        self.frame_3.setGeometry(QtCore.QRect(-20, -1, 771, 471))
        self.frame_3.setStyleSheet("image: url(:/newPrefix/fotoğraf/Screenshot_7.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stackedWidget.addWidget(self.PANDEMIC)
        self.SAFE = QtWidgets.QWidget()
        self.SAFE.setObjectName("SAFE")
        self.frame_4 = QtWidgets.QFrame(self.SAFE)
        self.frame_4.setGeometry(QtCore.QRect(10, 0, 721, 461))
        self.frame_4.setStyleSheet("image: url(:/newPrefix/fotoğraf/Screenshot_8.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.stackedWidget.addWidget(self.SAFE)
        self.TICKET = QtWidgets.QWidget()
        self.TICKET.setObjectName("TICKET")
        self.frame_5 = QtWidgets.QFrame(self.TICKET)
        self.frame_5.setGeometry(QtCore.QRect(10, -40, 721, 561))
        self.frame_5.setStyleSheet("image: url(:/newPrefix/fotoğraf/Screenshot_11.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.stackedWidget.addWidget(self.TICKET)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(190, -20, 731, 131))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"image: url(:/newPrefix/fotoğraf/Screenshot_6.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PANDEMİC RULES"))
        self.pushButton_8.setText(_translate("Form", "TICKET RULES"))
        self.pushButton_9.setText(_translate("Form", "SAFE TRAVEL"))

import test2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = seyehat()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

