

from PyQt5 import QtCore, QtGui, QtWidgets
from AnaSayfa import An
from PyQt5.QtCore import QObject, QPointF, QPropertyAnimation, pyqtProperty

import sqlite3

class Fo(object):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(865, 556)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(160, 100, 471, 391))
        self.frame.setStyleSheet("border: 5px solid ;\n"
"border-color: rgb(20, 92, 200);\n"
"border-radius:35px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 110, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"    color: rgb(8, 117, 200);\n"
"border-bottom:1px solid #717072\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 180, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color: rgb(8, 117, 200);\n"
"border-bottom:1px solid #717072\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 230, 81, 51))
        font = QtGui.QFont()
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(8, 117, 200);\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(8, 117, 200);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 110, 41, 31))
        self.frame_3.setStyleSheet("image: url(:/newPrefix/fotoğraf/icons8-lock-24.png);\n"
"border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(20, 170, 51, 41))
        self.frame_4.setStyleSheet("image: url(:/newPrefix/fotoğraf/icons8-key-24.png);\n"
"border:none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(340, 30, 101, 101))
        self.frame_2.setStyleSheet("border-color: rgb(16, 120, 200);\n"
"image: url(:/newPrefix/fotoğraf/icons8-bus-50.png);\n"
"background-color: rgb(20, 89, 200);\n"
"border-radius:50px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "USERNAME"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "PASSWORD"))
        self.pushButton_2.setText(_translate("Form", "Register"))
        self.pushButton.setText(_translate("Form", "Log In"))

    def login(self):

        connexion = sqlite3.connect('Data.db')
        print(connexion)
        print('conn done')
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        connexion = sqlite3.connect('Data.db')
        print(connexion)

        result = connexion.execute('''SELECT * FROM PROFIL WHERE USERNAME =? AND PASSWORD=?''', (username, password))
        if(len(result.fetchall())) > 0:
            print('user found')
            self.new1=QtWidgets.QMainWindow()
            self.ui=An()
            self.ui.setupUi(self.new1)
            self.new1.show()
        else:
            self.lineEdit.clear()
            self.lineEdit_2.clear()


import test2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Fo()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

