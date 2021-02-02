

from PyQt5 import QtCore, QtGui, QtWidgets
from Koltukseçme import Koltuk
import sqlite3

class Menu(object):



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

    def add(self):
        name = self.textEdit.toPlainText()
        color = self.textEdit_2.toPlainText()
        date = self.textEdit_3.toPlainText()
        conn = sqlite3.connect('Data.db')
        conn.execute(''' INSERT INTO NIKE(NAME,COLOR,DATE) VALUES(?, ?, ?)''', (name, color, date))
        conn.commit()
        self.load()



    def kaydet(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setInformativeText('your Informantıon has been saved')
        msgbox.exec_()
    def K(self):
        self.new5 = QtWidgets.QMainWindow()
        self.ui = Koltuk()
        self.ui.setupUi(self.new5)
        self.new5.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 603)
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 500, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 97, 200);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.kaydet)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(250, 270, 311, 191))
        self.calendarWidget.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(260, 210, 121, 22))
        font = QtGui.QFont()
        font.setItalic(True)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(0, 85, 255);\n"
"background-color: rgb(0,0,0);")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(440, 210, 121, 22))
        font = QtGui.QFont()
        font.setItalic(True)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("color: rgb(0, 85, 255);\n"
"background-color: rgb(0,0,0);")
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(460, 140, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(0, 85, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(280, 140, 111, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(830, 550, 75, 41))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fotoğraf/icons8-right-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.K)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 550, 75, 41))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fotoğraf/icons8-left-arrow-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 10, 301, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(640, 250, 256, 192))
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
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(690, 70, 181, 31))
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
        self.textEdit_2.setGeometry(QtCore.QRect(690, 130, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(690, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"    \n"
"    color: rgb(85, 170, 255);\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"    \n"
"    \n"
"border-bottom:1px solid #717072\n"
"}\n"
"")
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 470, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 97, 200);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 470, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 97, 200);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.load)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 131, 81))
        self.frame.setStyleSheet("image: url(:/newPrefix/fotoğraf/images.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.comboBox.setCurrentText(_translate("Form", "WHERE FROM"))
        self.comboBox.setItemText(0, _translate("Form", "WHERE FROM"))
        self.comboBox.setItemText(1, _translate("Form", "İSTANBUL"))
        self.comboBox.setItemText(2, _translate("Form", "KONYA"))
        self.comboBox.setItemText(3, _translate("Form", "BURSA"))
        self.comboBox.setItemText(4, _translate("Form", "ANKARA"))
        self.comboBox.setItemText(5, _translate("Form", "ESKİŞEHİR"))
        self.comboBox_2.setCurrentText(_translate("Form", "WHERE"))
        self.comboBox_2.setItemText(0, _translate("Form", "WHERE"))
        self.comboBox_2.setItemText(1, _translate("Form", "ANKARA"))
        self.comboBox_2.setItemText(2, _translate("Form", "BURSA"))
        self.comboBox_2.setItemText(3, _translate("Form", "İSTANBUL"))
        self.comboBox_2.setItemText(4, _translate("Form", "İZMİR"))
        self.comboBox_2.setItemText(5, _translate("Form", "KOCAELİ"))
        self.radioButton.setText(_translate("Form", "ROUND TRIP"))
        self.radioButton_2.setText(_translate("Form", "ONE DIRECTION"))
        self.label.setText(_translate("Form", "      TRIP   INFORMATION"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "WHERE FROM"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "WHERE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "DEPARTURE "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "ARRİVEL"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "PRICE"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "SEAT NO"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "GENDER"))
        self.textEdit.setPlaceholderText(_translate("Form", " WHERE FROM"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "WHERE"))
        self.textEdit_3.setPlaceholderText(_translate("Form", "DATE"))
        self.pushButton_2.setText(_translate("Form", " ADD INFORMATION"))
        self.pushButton_5.setText(_translate("Form", "DİSPLAY INFORMATION"))


import test2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

