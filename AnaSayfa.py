

from PyQt5 import QtCore, QtGui, QtWidgets
from AnaMenüü import Menu
from SeyehatRehber import seyehat
from PyQt5.QtCore import QObject, QPointF, QPropertyAnimation, pyqtProperty
import sys

class An(object):
    def AnaMenu(self):
            self.new2 = QtWidgets.QMainWindow()
            self.ui = Menu()
            self.ui.setupUi(self.new2)
            self.new2.show()

    def Save(self):
            msgbox = QtWidgets.QMessageBox()
            msgbox.setInformativeText('your Informantıon has been saved')
            msgbox.exec_()
    def Travel(self):
            self.new3 = QtWidgets.QMainWindow()
            self.ui =seyehat ()
            self.ui.setupUi(self.new3)
            self.new3.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1093, 539)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 610, 331, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 290, 291, 20))
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
"    color: rgb(8, 117, 200);\n"
"border-bottom:1px solid #717072\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 360, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"    color: rgb(8, 117, 200);\n"
"border-bottom:1px solid #717072\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(420, 360, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"    color: rgb(8, 117, 200);\n"
"border-bottom:1px solid #717072\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 120, 331, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(450, 430, 191, 20))
        self.checkBox.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 290, 291, 20))
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
"    \n"
"    color: rgb(0, 85, 255);\n"
"border-bottom:1px solid #717072\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 430, 191, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(760, 200, 281, 161))
        self.frame.setStyleSheet("image: url(:/newPrefix/fotoğraf/images.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 480, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 97, 200);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Save)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 20, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(8, 27, 200);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fotoğraf/icons8-right-arrow-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.AnaMenu)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 20, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(8, 27, 200);\n"
"}")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(790, 20, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(8, 27, 200);\n"
"}")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Travel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "GÖNDER"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "SURNAME"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "E-POSTA"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "PHONE"))
        self.label.setText(_translate("Form", "Take advantage of MegaBus opportunities"))
        self.checkBox.setText(_translate("Form", "Sms ile bilgilendir"))
        self.lineEdit.setPlaceholderText(_translate("Form", "NAME"))
        self.checkBox_2.setText(_translate("Form", "E-posta ile bilgilendir"))
        self.pushButton.setText(_translate("Form", "SAVE"))
        self.pushButton_3.setText(_translate("Form", "Voyage"))
        self.pushButton_4.setText(_translate("Form", "MENU"))
        self.pushButton_5.setText(_translate("Form", "TRAVEL GUİDE"))


import test3

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = An()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

