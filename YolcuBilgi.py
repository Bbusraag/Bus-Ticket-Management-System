

from PyQt5 import QtCore, QtGui, QtWidgets
from Ödeme import ode
import sqlite3
class Yolcu(object):
    def load(self):

        conn = sqlite3.connect('Data.db')
        content = 'SELECT * FROM YOLCU'
        result = conn.execute(content)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colm_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colm_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def B(self):
        self.new10 = QtWidgets.QMainWindow()
        self.ui = ode()
        self.ui.setupUi(self.new10)
        self.new10.show()

    def add(self):

        name = self.textEdit_9.toPlainText()
        surname = self.textEdit_11.toPlainText()
        birth = self.textEdit_7.toPlainText()
        phone = self.textEdit_8.toPlainText()
        email = self.textEdit_12.toPlainText()
        tc = self.textEdit_10.toPlainText()
        msgbox=QtWidgets.QMessageBox()
        conn = sqlite3.connect('Data.db')
        conn.execute(''' INSERT INTO YOLCU(NAME,SURNAME,BIRTHDATE,PHONE,EMAIL,TC) VALUES(?, ?,?,?,?,?)''', (name, surname, birth, phone, email, tc))
        conn.commit()
        msgbox.setInformativeText('PASSENGER INFORMATION HAS BEEN SAVED')
        self.load()
        msgbox.exec()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(911, 570)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textEdit_6 = QtWidgets.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(210, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setStyleSheet("color: rgb(0, 85, 255);\n"
"\n"
"")
        self.textEdit_6.setObjectName("textEdit_6")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 420, 511, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(11, 103, 200);")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(780, 500, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fotoğraf/icons8-right-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.B)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 500, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fotoğraf/icons8-left-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_7 = QtWidgets.QTextEdit(Form)
        self.textEdit_7.setGeometry(QtCore.QRect(40, 340, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(Form)
        self.textEdit_8.setGeometry(QtCore.QRect(280, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(Form)
        self.textEdit_9.setGeometry(QtCore.QRect(50, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(Form)
        self.textEdit_10.setGeometry(QtCore.QRect(280, 340, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(Form)
        self.textEdit_11.setGeometry(QtCore.QRect(50, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(Form)
        self.textEdit_12.setGeometry(QtCore.QRect(280, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_12.setObjectName("textEdit_12")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(200, 110, 81, 41))
        self.frame.setStyleSheet("image: url(:/newPrefix/fotoğraf/icons8-user-male-60.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(580, 170, 256, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(580, 400, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 97, 200);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.add)
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(720, 400, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 97, 200);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.load)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">                              PASSENDER INFORMATION</span></p></body></html>"))
        self.textEdit_6.setPlaceholderText(_translate("Form", "                     YOLCU BİLGİLERİ"))
        self.checkBox.setText(_translate("Form", "If You Want To Buy Your E-Ticket On Behalf Of Corporate Company Please Click Here"))
        self.textEdit_7.setPlaceholderText(_translate("Form", "BIRTH DATE"))
        self.textEdit_8.setPlaceholderText(_translate("Form", "PHONE NUMBER"))
        self.textEdit_9.setPlaceholderText(_translate("Form", "NAME"))
        self.textEdit_10.setPlaceholderText(_translate("Form", "T.C NO"))
        self.textEdit_11.setPlaceholderText(_translate("Form", "SURNAME"))
        self.textEdit_12.setPlaceholderText(_translate("Form", "E-POSTA"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "SURNAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "BIRTH DATE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "PHONE NUMBER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "E-POSTA"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "TC NO"))
        self.pushButton_9.setText(_translate("Form", "ADD PASSENGER"))
        self.pushButton_10.setText(_translate("Form", "DISPLAY PASSENGER"))

import test2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Yolcu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

