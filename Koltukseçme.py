

from PyQt5 import QtCore, QtGui, QtWidgets
from GidişSeferi import Sefer
import sqlite3
class Koltuk(object):
    def add(self):

        color = self.textEdit_2.toPlainText()
        date = self.textEdit_3.toPlainText()
        msgbox=QtWidgets.QMessageBox()
        conn = sqlite3.connect('Data.db')
        conn.execute(''' INSERT INTO NIKE(GENDER,SEAT) VALUES(?, ?)''', (color, date))
        conn.commit()
        msgbox.setInformativeText('your seat has been confirmed')
        self.load()
        msgbox.exec()
    def load(self):

        conn = sqlite3.connect('Data.db')
        content = 'SELECT * FROM NIKE'
        result = conn.execute(content)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colm_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colm_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def S(self):
        self.new6 = QtWidgets.QMainWindow()
        self.ui = Sefer()
        self.ui.setupUi(self.new6)
        self.new6.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 600)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 520, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fotoğraf/icons8-left-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 540, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fotoğraf/icons8-right-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.S)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(70, 20, 601, 481))
        self.frame.setStyleSheet("QFrame{\n"
"border:5px solid rgb(0, 85, 255);\n"
"border-radius:100px;\n"
"}\n"
"QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 180, 75, 23))
        self.pushButton_3.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 370, 75, 23))
        self.pushButton_4.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 310, 75, 23))
        self.pushButton_6.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.pushButton_7.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 180, 75, 23))
        self.pushButton_8.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 420, 75, 23))
        self.pushButton_10.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(410, 420, 75, 23))
        self.pushButton_11.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(410, 370, 75, 23))
        self.pushButton_12.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(410, 280, 75, 23))
        self.pushButton_13.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(410, 330, 75, 23))
        self.pushButton_14.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(410, 230, 75, 23))
        self.pushButton_15.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(410, 180, 75, 23))
        self.pushButton_16.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(150, 360, 75, 23))
        self.pushButton_17.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(150, 420, 75, 23))
        self.pushButton_18.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(150, 310, 75, 23))
        self.pushButton_19.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.pushButton_20.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame)
        self.pushButton_21.setGeometry(QtCore.QRect(490, 230, 75, 23))
        self.pushButton_21.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame)
        self.pushButton_22.setGeometry(QtCore.QRect(490, 280, 75, 23))
        self.pushButton_22.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame)
        self.pushButton_23.setGeometry(QtCore.QRect(490, 330, 75, 23))
        self.pushButton_23.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame)
        self.pushButton_24.setGeometry(QtCore.QRect(490, 370, 75, 23))
        self.pushButton_24.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame)
        self.pushButton_25.setGeometry(QtCore.QRect(490, 420, 75, 23))
        self.pushButton_25.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame)
        self.pushButton_26.setGeometry(QtCore.QRect(490, 180, 75, 23))
        self.pushButton_26.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame)
        self.pushButton_27.setGeometry(QtCore.QRect(50, 260, 75, 23))
        self.pushButton_27.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame)
        self.pushButton_28.setGeometry(QtCore.QRect(150, 220, 75, 23))
        self.pushButton_28.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 0, 255);\n"
"}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(230, 50, 120, 51))
        self.frame_3.setStyleSheet("image: url(:/newPrefix/fotoğraf/icons8-driver-40.png);\n"
"border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 90, 75, 51))
        self.pushButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("fotoğraf/icons8-steering-wheel-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(720, 200, 256, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(750, 50, 181, 31))
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
        self.textEdit_3.setGeometry(QtCore.QRect(750, 110, 181, 31))
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
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(740, 430, 75, 23))
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
        self.pushButton_29 = QtWidgets.QPushButton(Form)
        self.pushButton_29.setGeometry(QtCore.QRect(864, 430, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 97, 200);\n"
"}")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(self.load)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "1"))
        self.pushButton_4.setText(_translate("Form", "9"))
        self.pushButton_6.setText(_translate("Form", "5"))
        self.pushButton_7.setText(_translate("Form", "2"))
        self.pushButton_8.setText(_translate("Form", "13"))
        self.pushButton_10.setText(_translate("Form", "10"))
        self.pushButton_11.setText(_translate("Form", "12"))
        self.pushButton_12.setText(_translate("Form", "11"))
        self.pushButton_13.setText(_translate("Form", "8"))
        self.pushButton_14.setText(_translate("Form", "7"))
        self.pushButton_15.setText(_translate("Form", "4"))
        self.pushButton_16.setText(_translate("Form", "3"))
        self.pushButton_17.setText(_translate("Form", "21"))
        self.pushButton_18.setText(_translate("Form", "22"))
        self.pushButton_19.setText(_translate("Form", "17"))
        self.pushButton_20.setText(_translate("Form", "18"))
        self.pushButton_21.setText(_translate("Form", "16"))
        self.pushButton_22.setText(_translate("Form", "19"))
        self.pushButton_23.setText(_translate("Form", "20"))
        self.pushButton_24.setText(_translate("Form", "23"))
        self.pushButton_25.setText(_translate("Form", "24"))
        self.pushButton_26.setText(_translate("Form", "15"))
        self.pushButton_27.setText(_translate("Form", "6"))
        self.pushButton_28.setText(_translate("Form", "14"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "WHERE FROM"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "WHERE FROM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "DEPARTURE"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "ARRIVAL"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "PRICE"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "SEAT NO"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "GENDER"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "SEAT NO"))
        self.textEdit_3.setPlaceholderText(_translate("Form", "GENDER"))
        self.pushButton_9.setText(_translate("Form", "ADD SEAT"))
        self.pushButton_29.setText(_translate("Form", "DİSPLAY SEAT"))

import test2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Koltuk()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

