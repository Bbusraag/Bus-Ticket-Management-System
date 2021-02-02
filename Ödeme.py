

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class ode(object):

    def add(self):

        method = self.textEdit.toPlainText()
        card = self.textEdit_2.toPlainText()
        secure = self.textEdit_5.toPlainText()
        name = self.textEdit_3.toPlainText()
        date = self.textEdit_4.toPlainText()
        msgbox = QtWidgets.QMessageBox()
        conn = sqlite3.connect('Data.db')
        msgbox.setInformativeText('YOUR TICKET HAS BEEN CONFIRMED')
        conn.execute('''INSERT INTO KART(METHOD,NO,SECURITY,NAME,DATE) VALUES(?,?,?,?,?)''', (method, card, secure, name , date))
        conn.commit()
        self.load()
        msgbox.exec()

    def load(self):

        conn = sqlite3.connect('Data.db')
        content = 'SELECT * FROM KART'
        result = conn.execute(content)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colm_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colm_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()




    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1017, 598)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(240, 320, 261, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(0, 85, 255);")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(630, 410, 121, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: rgb(170, 170, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(360, 30, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(260, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 300, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(260, 240, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setStyleSheet("QTextEdit{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_5.setObjectName("textEdit_5")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 191, 91))
        self.frame.setStyleSheet("image: url(:/newPrefix/fotoğraf/images.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(630, 160, 301, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 410, 151, 51))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: rgb(170, 170, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.load)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 360, 161, 111))
        self.frame_2.setStyleSheet("image: url(:/newPrefix/fotoğraf/credit-card-icon-flat-style-illustration-vector-web-79711478.jpg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 550, 75, 23))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fotoğraf/icons8-left-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(940, 552, 75, 31))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fotoğraf/icons8-right-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "I read the sales contract, I approve"))
        self.pushButton.setText(_translate("Form", "COMPLETE PAYMENT"))
        self.label_9.setText(_translate("Form", "                 PAYMENT INFORMATION"))
        self.textEdit.setPlaceholderText(_translate("Form", "PAYMENT METHOD"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "CARD NO"))
        self.textEdit_3.setPlaceholderText(_translate("Form", "NAME"))
        self.textEdit_4.setPlaceholderText(_translate("Form", "EXPIRATION DATE"))
        self.textEdit_5.setPlaceholderText(_translate("Form", "SECURITY NO"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "METHOD"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "CARD NO"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "SECURITY NO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "EXPERTION DATE"))
        self.pushButton_2.setText(_translate("Form", "SHOW CARD INFORMATION"))

import test2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ode()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

