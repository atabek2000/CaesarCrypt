from PyQt5 import QtCore, QtGui, QtWidgets
import math as m

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 501)
        MainWindow.setFixedSize(500, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 200, 50))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.main_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(200, 20, 280, 50))
        self.main_text.setObjectName("main_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 75, 200, 50))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.key.setEnabled(True)
        self.key.setGeometry(QtCore.QRect(200, 75, 280, 50))
        self.key.setObjectName("key")
        self.shipher_button = QtWidgets.QPushButton(self.centralwidget)
        self.shipher_button.setGeometry(QtCore.QRect(200, 130, 75, 23))
        self.shipher_button.setObjectName("shipher_button")
        self.deshipher_button = QtWidgets.QPushButton(self.centralwidget)
        self.deshipher_button.setGeometry(QtCore.QRect(200, 160, 83, 23))
        self.deshipher_button.setObjectName("deshipher_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 190, 200, 50))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.second_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.second_text.setGeometry(QtCore.QRect(200, 190, 280, 50))
        self.second_text.setObjectName("second_text")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(10, 250, 470, 50))
        self.label_error.setText("")
        self.label_error.setStyleSheet("QLabel { color : red; }")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.shipher_button.clicked.connect(self.encrypt)
        self.deshipher_button.clicked.connect(self.decrypt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Исходный текст:"))
        self.label_2.setText(_translate("MainWindow", "Ключ:"))
        self.shipher_button.setText(_translate("MainWindow", "Шифровать"))
        self.deshipher_button.setText(_translate("MainWindow", "Расшифровать"))
        self.label_3.setText(_translate("MainWindow", "Обработанный текст:"))

    def encrypt(self):
        try:
            self.label_error.setText('')
            st = []
            key = abs(int(self.key.toPlainText()))
            for i in self.main_text.toPlainText():
                st.append(self.encryptCaesar(i, key))
            self.second_text.setPlainText(''.join(st))
        except:
            self.label_error.setText('Ошибка: '+str(sys.exc_info()[1]))

    def decrypt(self):
        try:
            self.label_error.setText('')
            key = abs(int(self.key.toPlainText()))
            st = []
            for i in self.main_text.toPlainText():
                st.append(self.decryptCaesar(i, key))
            self.second_text.setPlainText(''.join(st))

        except:
            self.label_error.setText('Ошибка: ' + str(sys.exc_info()[1]))

    def encryptCaesar(self, ch, key):
        if ord(ch) >= 65 and ord(ch) <= 90 and ord(ch)+key%26 > 90:
            return chr(ord(ch)+key%26-26)
        elif ord(ch) >= 97 and ord(ch) <= 122 and ord(ch)+key%26 > 122:
            return chr(ord(ch)+key%26-26)
        elif ord(ch) >= 1072 and ord(ch) <= 1103 and ord(ch)+key%32 > 1103:
            return chr(ord(ch)+key%32-32)
        elif ord(ch) >= 1040 and ord(ch) <= 1071 and ord(ch)+key%32 > 1071:
            return chr(ord(ch)+key%32-32)
        elif (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
            return chr(ord(ch) + key%26)
        elif (ord(ch) >= 1072 and ord(ch) <= 1103) or (ord(ch) >= 1040 and ord(ch) <= 1071):
            return chr(ord(ch)+key%32)
        else:
            return ch

    def decryptCaesar(self, ch, key):
        if ord(ch) >= 65 and ord(ch) <= 90 and ord(ch) - key % 26 < 65:
            return chr(ord(ch) - key % 26 + 26)
        elif ord(ch) >= 97 and ord(ch) <= 122 and ord(ch) - key % 26 < 97:
            return chr(ord(ch) - key % 26 + 26)
        elif ord(ch) >= 1072 and ord(ch) <= 1103 and ord(ch) - key % 32 < 1072:
            return chr(ord(ch) - key % 32 + 32)
        elif ord(ch) >= 1040 and ord(ch) <= 1071 and ord(ch) - key % 32 < 1040:
            return chr(ord(ch) - key % 32 + 32)
        elif (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
            return chr(ord(ch) - key % 26)
        elif (ord(ch) >= 1072 and ord(ch) <= 1103) or (ord(ch) >= 1040 and ord(ch) <= 1071):
            return chr(ord(ch) - key % 32)
        else:
            return ch


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

